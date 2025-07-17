/*
Copyright 2009 Google Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package controls.google {
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.events.MouseEvent;
	import flash.events.TimerEvent;
	import flash.net.URLLoader;
	import flash.net.URLRequest;
	import flash.net.URLVariables;
	import flash.system.Security;
	import flash.utils.Timer;
	
	import mx.collections.ArrayCollection;
	import mx.controls.SWFLoader;
	import mx.events.FlexEvent;
	import mx.events.ResizeEvent;
	
	import spark.components.Button;
	import spark.components.ComboBox;
	import spark.components.Group;
	import spark.components.TextInput;
	import spark.events.ListEvent;

	public class AS3Player extends Group {
		// Member variables.
		private var cueButton:Button;
		private var isQualityPopulated:Boolean;
		private var isWidescreen:Boolean;
		private var pauseButton:Button;
		private var playButton:Button;
		private var player:Object;
		private var playerLoader:SWFLoader;
		private var qualityComboBox:ComboBox;
		private var videoIdTextInput:TextInput;
		private var youtubeApiLoader:URLLoader;

		// CONSTANTS.
		private static const DEFAULT_VIDEO_ID:String="0QRO3gKj3qw";
		private static const PLAYER_URL:String="http://www.youtube.com/apiplayer?version=3";
		private static const SECURITY_DOMAIN:String="http://www.youtube.com";
		private static const YOUTUBE_API_PREFIX:String="http://gdata.youtube.com/feeds/api/videos/";
		private static const YOUTUBE_API_VERSION:String="2";
		private static const YOUTUBE_API_FORMAT:String="5";
		private static const WIDESCREEN_ASPECT_RATIO:String="widescreen";
		private static const QUALITY_TO_PLAYER_WIDTH:Object={small: 320, medium: 640, large: 854, hd720: 1280};
		private static const STATE_ENDED:Number=0;
		private static const STATE_PLAYING:Number=1;
		private static const STATE_PAUSED:Number=2;
		private static const STATE_CUED:Number=5;

		[Bindable]
		private var __videoID__:String;
		
		[Bindable]
		private var __autoplay__:Boolean = false;
		
		private var __timer__:Timer = new Timer(2500);
		private var __delayed__:Array = [];

		public function AS3Player():void {
			// Specifically allow the chromless player .swf access to our .swf.
			try {
				Security.allowDomain(SECURITY_DOMAIN);
			} catch (err:Error) {}

			setupPlayerLoader();
			setupYouTubeApiLoader();
			this.addEventListener(FlexEvent.CREATION_COMPLETE, 
				function (event:FlexEvent):void {
					if (__videoID__ == null) {
						setupUi();
					}
				}
			);
			this.addEventListener(ResizeEvent.RESIZE, 
				function (event:ResizeEvent):void {
					if (player) {
						trace('(RESIZE).1 --> width='+width+', height='+height+', oldWidth='+event.oldWidth+', oldHeight='+event.oldHeight);
						var newWidth:Number=width;
						var newHeight:Number;
						if (isWidescreen) {
							newHeight=newWidth * 9 / 16;
						} else {
							newHeight=newWidth * 3 / 4;
						}
						player.setSize(newWidth, newHeight);
						trace('(RESIZE).2 --> width='+width+', height='+height+', newWidth='+newWidth+', newHeight='+newHeight);
					}
				}
			);
			this.__timer__.addEventListener(TimerEvent.TIMER, 
				function (event:TimerEvent):void {
					var aFunc:Function = __delayed__.pop();
					if (aFunc is Function) {
						aFunc();
					}
				}
			);
			this.__timer__.start();
		}
		
		public function get videoID():String {
			return this.__videoID__;
		}
		
		public function set videoID(videoID:String):void {
			if (this.__videoID__ != videoID) {
				this.__videoID__ = videoID;
			}
		}

		public function get timer_delay():Number {
			return this.__timer__.delay;
		}
		
		public function set timer_delay(timer_delay:Number):void {
			if (this.__timer__.delay != timer_delay) {
				this.__timer__.delay = timer_delay;
				if (timer_delay > 0) {
					if (this.__autoplay__) {
						this.__timer__.stop();
						this.__timer__.reset();
						this.__timer__.start();
					}
				} else {
					this.__timer__.stop();
				}
			}
		}
		
		public function get autoplay():Boolean {
			return this.__autoplay__;
		}
		
		public function set autoplay(autoplay:Boolean):void {
			if (this.__autoplay__ != autoplay) {
				this.__autoplay__ = autoplay;
				if (!autoplay) {
					this.__timer__.stop();
				} else {
					this.__timer__.stop();
					this.__timer__.reset();
					this.__timer__.start();
				}
			}
		}
		
		private function setupUi():void {
			// Create a TextInput field for the YouTube video id, and pre-populate it.
			videoIdTextInput=new TextInput();
			videoIdTextInput.text=DEFAULT_VIDEO_ID;
			videoIdTextInput.width=100;
			videoIdTextInput.x=10;
			videoIdTextInput.y=10;
			addElement(videoIdTextInput);

			// Create a Button for cueing up the video whose id is specified.
			cueButton=new Button();
			cueButton.enabled=false;
			cueButton.label="Cue Video";
			cueButton.width=100;
			cueButton.x=120;
			cueButton.y=10;
			cueButton.addEventListener(MouseEvent.CLICK, cueButtonClickHandler);
			addElement(cueButton);

			// Create a ComboBox that will contain the list of available playback
			// qualities. Selecting from the ComboBox will change the playback quality
			// and resize the player. Note that playback qualities are only available
			// once a video has started playing, so the values in this ComboBox can't
			// be populated until then.
			qualityComboBox=new ComboBox();
			qualityComboBox.prompt="n/a";
			qualityComboBox.width=100;
			qualityComboBox.x=230;
			qualityComboBox.y=10;
			qualityComboBox.addEventListener('change', qualityComboBoxChangeHandler);
			addElement(qualityComboBox);

			// Create a Button for playing the cued video.
			playButton=new Button();
			playButton.enabled=false;
			playButton.label="Play";
			playButton.width=90;
			playButton.height=40;
			playButton.x=340;
			playButton.y=10;
			playButton.addEventListener(MouseEvent.CLICK, playButtonClickHandler);
			addElement(playButton);

			// Create a Button for pausing the cued video.
			pauseButton=new Button();
			pauseButton.enabled=false;
			pauseButton.label="Pause";
			pauseButton.width=90;
			pauseButton.height=30;
			pauseButton.x=450;
			pauseButton.y=10;
			pauseButton.addEventListener(MouseEvent.CLICK, pauseButtonClickHandler);
			addElement(pauseButton);
		}

		private function setupPlayerLoader():void {
			playerLoader=new SWFLoader();
			playerLoader.addEventListener(Event.INIT, playerLoaderInitHandler);
			playerLoader.load(PLAYER_URL);
		}

		private function playerLoaderInitHandler(event:Event):void {
			if (this.__videoID__) {
				playerLoader.x = 0;
				playerLoader.y = 0;
				playerLoader.width = this.width;
				playerLoader.height = this.height;
				trace("playerLoader.width="+playerLoader.width+', playerLoader.height='+playerLoader.height);
			}
			addElement(playerLoader);
			playerLoader.content.addEventListener("onReady", onPlayerReady);
			playerLoader.content.addEventListener("onError", onPlayerError);
			playerLoader.content.addEventListener("onStateChange", onPlayerStateChange);
			playerLoader.content.addEventListener("onPlaybackQualityChange", onVideoPlaybackQualityChange);
		}

		private function setupYouTubeApiLoader():void {
			youtubeApiLoader=new URLLoader();
			youtubeApiLoader.addEventListener(IOErrorEvent.IO_ERROR, youtubeApiLoaderErrorHandler);
			youtubeApiLoader.addEventListener(Event.COMPLETE, youtubeApiLoaderCompleteHandler);
		}

		private function youtubeApiLoaderCompleteHandler(event:Event):void {
			var atomData:String=youtubeApiLoader.data;

			// Parse the YouTube API XML response and get the value of the
			// aspectRatio element.
			var atomXml:XML=new XML(atomData);
			var aspectRatios:XMLList=atomXml..*::aspectRatio;

			isWidescreen=aspectRatios.toString() == WIDESCREEN_ASPECT_RATIO;

			isQualityPopulated=false;
			// Cue up the video once we know whether it's widescreen.
			// Alternatively, you could start playing instead of cueing with
			// player.loadVideoById(videoIdTextInput.text);
			player.cueVideoById((videoIdTextInput) ? videoIdTextInput.text : this.__videoID__);
		}

		private function qualityComboBoxChangeHandler(event:Event):void {
			var cmbo:ComboBox=ComboBox(event.target);
			var qualityLevel:String=cmbo.selectedItem[cmbo.labelField];
			player.setPlaybackQuality(qualityLevel);
		}

		private function loadVideoById(videoID:String):void {
			var request:URLRequest=new URLRequest(YOUTUBE_API_PREFIX + videoID);

			var urlVariables:URLVariables=new URLVariables();
			urlVariables.v=YOUTUBE_API_VERSION;
			urlVariables.format=YOUTUBE_API_FORMAT;
			request.data=urlVariables;

			try {
				youtubeApiLoader.load(request);
			} catch (error:SecurityError) {
				trace("A SecurityError occurred while loading", request.url);
			}
		}

		private function cueButtonClickHandler(event:MouseEvent):void {
			this.loadVideoById(videoIdTextInput.text);
		}

		private function playVideoHandler():void {
			player.playVideo();
		}
		
		public function play():void {
			this.playVideoHandler();
		}
		
		private function playButtonClickHandler(event:MouseEvent):void {
			this.playVideoHandler();
		}

		private function pauseVideoHandler():void {
			player.pauseVideo();
		}
		
		public function pause():void {
			this.pauseVideoHandler();
		}
		
		private function pauseButtonClickHandler(event:MouseEvent):void {
			this.pauseVideoHandler();
		}

		private function youtubeApiLoaderErrorHandler(event:IOErrorEvent):void {
			trace("Error making YouTube API request:", event);
		}

		private function onPlayerReady(event:Event):void {
			player=playerLoader.content;
			player.visible=false;

			if (cueButton) {
				cueButton.enabled=true;
			} else {
				this.loadVideoById(__videoID__);
				this.__delayed__.push(this.playVideoHandler);
			}
		}

		private function onPlayerError(event:Event):void {
			trace("Player error:", Object(event).data);
		}

		private function onPlayerStateChange(event:Event):void {
			trace("State is", Object(event).data);

			switch (Object(event).data) {
				case STATE_ENDED:
					if (playButton) {
						playButton.enabled=true;
					}
					if (pauseButton) {
						pauseButton.enabled=false;
					}
					break;

				case STATE_PLAYING:
					if (playButton) {
						playButton.enabled=false;
					}
					if (pauseButton) {
						pauseButton.enabled=true;
					}

					if (!isQualityPopulated) {
						populateQualityComboBox();
					}
					break;

				case STATE_PAUSED:
					if (playButton) {
						playButton.enabled=true;
					}
					if (pauseButton) {
						pauseButton.enabled=false;
					}
					break;

				case STATE_CUED:
					if (playButton) {
						playButton.enabled=true;
					}
					if (pauseButton) {
						pauseButton.enabled=false;
					}

					if (!this.__videoID__) {
					}
					resizePlayer("medium");
					break;
			}
		}

		private function onVideoPlaybackQualityChange(event:Event):void {
			trace("Current video quality:", Object(event).data);
			resizePlayer(Object(event).data);
		}

		private function resizePlayer(qualityLevel:String):void {
			var newWidth:Number=QUALITY_TO_PLAYER_WIDTH[qualityLevel] || 640;
			var newHeight:Number;

			if (isWidescreen) {
				// Widescreen videos (usually) fit into a 16:9 player.
				newHeight=newWidth * 9 / 16;
			} else {
				// Non-widescreen videos fit into a 4:3 player.
				newHeight=newWidth * 3 / 4;
			}

			//trace("isWidescreen is", isWidescreen, ". Size:", newWidth, newHeight);
			//player.setSize(newWidth, newHeight);

			// Center the resized player on the stage.
			try {
				//player.x=(stage.stageWidth - newWidth) / 2;
				//player.y=(stage.stageHeight - newHeight) / 2;
			} catch (err:Error) {
				//player.x=0;
				//player.y=0;
			}

			player.visible=true;
		}

		private function populateQualityComboBox():void {
			isQualityPopulated=false;

			if (qualityComboBox) {
				isQualityPopulated=true;
				var qualities:Array=player.getAvailableQualityLevels();
				qualityComboBox.dataProvider=new ArrayCollection(qualities);
				
				var currentQuality:String=player.getPlaybackQuality();
				qualityComboBox.selectedItem=currentQuality;
			}
		}
	}
}