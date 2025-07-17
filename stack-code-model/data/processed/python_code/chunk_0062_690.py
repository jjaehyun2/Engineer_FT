/**
 Copyright 2009 Ben Longoria
 
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

/**
 * TubeLoc
 *
 * @author Ben Longoria <enefekt@gmail.com>
 */
class TubeLoc {
	
	private static var PLAYING_STATE:Number = 1;
	private static var ON_STATE_CHANGE:String = "onStateChange";
	private static var ON_ERROR:String = "onError";
	private static var MOVIE_STATE_UPDATE:String = "onMovieStateUpdate";
	private static var MOVIE_PROGRESS:String = "onMovieProgress";
	private static var ON_YT_MOVIE_COMPLETE:String = "onYouTubeMovieComplete";
	private static var application:TubeLoc;

	private var _parent:MovieClip = _root;//simulating parent

	private var mainMovieClip:MovieClip;
	private var youtubeMovie:MovieClip;
	private var depth:Number = 5;
	private var youtubeLoader:MovieClipLoader;
	private var youtubeListener:Object;

	private var receivingConnection:LocalConnection;
	private var sendingConnection:LocalConnection;
	private var as3Id:String;//id for the AVM2 SWF
	private var as2Id:String;//id for the AVM1 SWF
	private var as3Listener:String;//method to be called in the AVM2 SWF
	private var youtubeId:String;//id of the youtube clip
	private var playerAPIUrl:String;//url of the chromeless player

	private var lastPlayerState:Number;
	private var lastVideoUrl:String;
	private var finalBytesLoadedEvent:Boolean = false;
	
	private var hasInit:Boolean = false;

	public var loadInterval:Number;

	/**
	 * @param	mainMovieClip_p	MovieClip to work with 
	 */
	function TubeLoc(mainMovieClip_p:MovieClip) {
		_parent._lockroot = true;
		init(mainMovieClip_p);
	}

	/**
	 * entry point to application
	 *
	 * @param (same as constructor)
	 */
	static function main(mainMovieClip_p:MovieClip) {
		application = new TubeLoc(mainMovieClip_p);
	}

	/**
	 * @param (same as constructor)
	 */
	private function init(mainMovieClip_p:MovieClip):Void {
		//set main movie clip
		mainMovieClip = mainMovieClip_p;

		//take care of Stage settings
		Stage.scaleMode = "noScale";
		Stage.align = "tl";

		//grab data from parent clip to use for LocalConnection instances
		as3Id = _parent.as3Id;
		as2Id = _parent.as2Id;
		as3Listener = _parent.as3Listener;
		playerAPIUrl = unescape(_parent.playerAPIUrl);


		//set up local connections
		receivingConnection = new LocalConnection();
		receivingConnection.allowDomain("*");
		receivingConnection.connect(as2Id);

		//set up callable methods from as3
		receivingConnection.destroy = TubeLoc.create(this, destroy);
		receivingConnection.pauseVideo = TubeLoc.create(this, pauseVideo);
		receivingConnection.playVideo = TubeLoc.create(this, playVideo);
		receivingConnection.stopVideo = TubeLoc.create(this, stopVideo);
		receivingConnection.loadVideoById = TubeLoc.create(this, loadVideoById);
		receivingConnection.cueVideoById = TubeLoc.create(this, cueVideoById);
		receivingConnection.setSize = TubeLoc.create(this, setSize);
		receivingConnection.clearVideo = TubeLoc.create(this, clearVideo);
		receivingConnection.mute = TubeLoc.create(this, mute);
		receivingConnection.unMute = TubeLoc.create(this, unMute);
		receivingConnection.setVolume = TubeLoc.create(this, setVolume);
		receivingConnection.seekTo = TubeLoc.create(this, seekTo);

		sendingConnection = new LocalConnection();

		//init ui
		initUI();
	}

	/**
	 * init the user interface
	 */
	private function initUI():Void {
		youtubeMovie = mainMovieClip.createEmptyMovieClip("youtubeMovie_mc" + as3Id, depth++);

		var tl:TubeLoc = this;
		youtubeListener = new Object();
		youtubeListener.onLoadInit = function() {
			tl.loadInterval = setInterval(tl, "checkPlayerLoaded", 100);
		}
		youtubeListener.onLoadError = function(target_p:MovieClip, errorCode_p:String, httpStatus_p:Number) {
			tl.dispatchPlayerLoadError();
		}

		youtubeLoader = new MovieClipLoader();
		youtubeLoader.addListener(youtubeListener);
		youtubeLoader.loadClip(playerAPIUrl, youtubeMovie);
	}

	/**
	 * @sends onError
	 */
	public function dispatchPlayerLoadError():Void {
		var event:Object = {
			eventName:ON_ERROR,
			value:301
		};
		sendingConnection.send(as3Id, as3Listener, event);
	}

	/**
	 * @sends onMovieStateUpdate
	 */
	private function dispatchMovieUpdate():Void {
		var event:Object = {
			eventName:MOVIE_STATE_UPDATE,
			videoBytesLoaded:youtubeMovie.getVideoBytesLoaded(),
			videoBytesTotal:youtubeMovie.getVideoBytesTotal(),
			videoStartBytes:youtubeMovie.getVideoStartBytes(),
			muted:youtubeMovie.isMuted(),
			volume:youtubeMovie.getVolume(),
			playerState:youtubeMovie.getPlayerState(),
			currentTime:youtubeMovie.getCurrentTime(),
			duration:youtubeMovie.getDuration(),
			videoUrl:youtubeMovie.getVideoUrl(),
			videoEmbedCode:youtubeMovie.getVideoEmbedCode()
		};

		sendingConnection.send(as3Id, as3Listener, event);
	}
	
	/**
	 * @sends onMovieProgress
	 */
	private function dispatchMovieProgress():Void {
		var event:Object = {
			eventName:MOVIE_PROGRESS,
			currentTime:youtubeMovie.getCurrentTime()
		};
		sendingConnection.send(as3Id, as3Listener, event);
	}

	/**
	 * called on an interval to see if player is loaded, and then to dispatch update and progress events
	 */
	public function checkPlayerLoaded():Void {
		if(!hasInit && youtubeMovie.isPlayerLoaded()) {
			hasInit = true;
			dispatchCompleteEvent();
			youtubeMovie.addEventListener(ON_STATE_CHANGE, TubeLoc.create(this, onPlayerStateChange));
			youtubeMovie.addEventListener(ON_ERROR, TubeLoc.create(this, onPlayerError));
			dispatchMovieUpdate();
		} else if(hasInit) {
			if(lastPlayerState == PLAYING_STATE) {
				dispatchMovieProgress();
			}
			var newUrl:String = youtubeMovie.getVideoUrl();
			if(newUrl && newUrl != lastVideoUrl && youtubeMovie.getDuration() > 0) {
				lastVideoUrl = newUrl;
				dispatchMovieUpdate();
			}
		}
		if(youtubeMovie.getVideoBytesLoaded() != youtubeMovie.getVideoBytesTotal()) {
			finalBytesLoadedEvent = false;
			dispatchMovieUpdate();
		} else if(youtubeMovie.getVideoBytesLoaded() == youtubeMovie.getVideoBytesTotal() && !finalBytesLoadedEvent) {
			finalBytesLoadedEvent = true;
			dispatchMovieUpdate();
		}
	}

	private function dispatchCompleteEvent():Void {
		var event:Object = {
			eventName:ON_YT_MOVIE_COMPLETE
		};
		sendingConnection.send(as3Id, as3Listener, event);
	}

	public function onPlayerStateChange(newState_p:Number):Void {
		var event:Object = {
			eventName:ON_STATE_CHANGE,
			value:newState_p
		};
		sendingConnection.send(as3Id, as3Listener, event);
		lastPlayerState = newState_p;
	}

	public function onPlayerError(errorCode_p:Number):Void {
		var event:Object = {
			eventName:ON_ERROR,
			value:errorCode_p
		};
		sendingConnection.send(as3Id, as3Listener, event);
	}

	public function seekTo(dataObject_p:Object):Void {
		youtubeMovie.seekTo(dataObject_p.seconds, dataObject_p.allowSeekAhead);
	}

	public function setVolume(dataObject_p:Object):Void {
		youtubeMovie.setVolume(dataObject_p.volume);
	}

	public function unMute():Void {
		youtubeMovie.unMute();
	}

	public function mute():Void {
		youtubeMovie.mute();
	}

	public function clearVideo():Void {
		youtubeMovie.clearVideo();
	}

	public function setSize(dataObject_p:Object):Void {
		youtubeMovie.setSize(dataObject_p.width, dataObject_p.height);
	}

	public function loadVideoById(dataObject_p:Object):Void {
		youtubeId = dataObject_p.videoId;
		youtubeMovie.loadVideoById(youtubeId, dataObject_p.startSeconds);
	}

	public function cueVideoById(dataObject_p:Object):Void {
		youtubeId = dataObject_p.videoId;
		youtubeMovie.cueVideoById(youtubeId, dataObject_p.startSeconds);
	}

	public function stopVideo():Void {
		youtubeMovie.stopVideo();
	}

	public function playVideo():Void {
		youtubeMovie.playVideo();
	}

	public function pauseVideo():Void {
		youtubeMovie.pauseVideo();
	}

	public function destroy():Void {
		receivingConnection.close();
		sendingConnection.close();
		clearInterval(loadInterval);
		youtubeMovie.destroy();
	}
	
	/**
	 * This is Joey Lott's ascb Proxy.create function.
	 */
	public static function create(oTarget:Object, fFunction:Function):Function {
		
		var aParameters:Array = new Array();
		for(var i:Number = 2; i < arguments.length; i++) {
			aParameters[i - 2] = arguments[i];
		}
		
		var fProxy:Function = function():Void {
			var aActualParameters:Array = arguments.concat(aParameters);
			fFunction.apply(oTarget, aActualParameters);
		};
		
		return fProxy;
		
	}

};