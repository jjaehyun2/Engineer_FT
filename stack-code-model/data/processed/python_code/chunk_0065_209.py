package
{
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.external.ExternalInterface;
	
	import org.osmf.events.DisplayObjectEvent;
	import org.osmf.events.LoadEvent;
	import org.osmf.events.TimeEvent;
	import org.osmf.media.MediaPlayerSprite;
	import org.osmf.media.URLResource;
	import org.osmf.traits.LoadState;
	import org.osmf.utils.OSMFSettings;
	
	public class simplevideo extends Sprite
	{
		private var videoPlayer:MediaPlayerSprite;
		private var videoWidth:int;
		private var videoHeight:int;
		
		public function simplevideo()
		{
			stage.scaleMode = StageScaleMode.NO_SCALE;
			stage.align = StageAlign.TOP_LEFT;
			OSMFSettings.enableStageVideo = true;
			initializeExternalInterface();
		}
		
		private function initializeExternalInterface():void
		{
			if (ExternalInterface.available)
			{
				ExternalInterface.addCallback("init", onInit);
				ExternalInterface.addCallback("play", onPlay);
				ExternalInterface.addCallback("pause", onPause);
				ExternalInterface.addCallback("getCurrentTime", getCurrentTime);
				ExternalInterface.addCallback("setCurrentTime", setCurrentTime);
				ExternalInterface.addCallback("getDuration", getDuration);
				ExternalInterface.addCallback("getVolume", getVolume);
				ExternalInterface.addCallback("setVolume", setVolume);
			}
		}
		
		private function onInit(src:String):void
		{
			videoPlayer = new MediaPlayerSprite();
			videoPlayer.mediaPlayer.autoPlay = false;
			videoPlayer.mediaPlayer.addEventListener(LoadEvent.LOAD_STATE_CHANGE, onLoadStateChange);
			videoPlayer.mediaPlayer.addEventListener(TimeEvent.COMPLETE, onVideoEnded);
			videoPlayer.mediaPlayer.addEventListener(DisplayObjectEvent.MEDIA_SIZE_CHANGE, onVideoSizeChanged);
			stage.addEventListener(Event.RESIZE, onStageResize);
			videoPlayer.media = videoPlayer.mediaFactory.createMediaElement(new URLResource(src));
		}
		
		private function onLoadStateChange(event:LoadEvent):void {
			if (event.loadState == LoadState.READY)
			{
				addChild(videoPlayer);
				ExternalInterface.call("simpleVideoSwfReady");
			}
		}
		
		private function onVideoEnded(evt:TimeEvent):void
		{
			ExternalInterface.call("simpleVideoSwfEnded");
		}
		
		private function resize():void
		{
			var playerWidth:int = videoWidth;
			var playerHeight:int = videoHeight;
			var ratio:Number = videoWidth / videoHeight;
			
			if (ratio >= (stage.stageWidth / stage.stageHeight))
			{
				playerWidth = stage.stageWidth;
				playerHeight = stage.stageWidth * ratio;
			}
			else
			{
				playerWidth = stage.stageHeight * ratio;
				playerHeight = stage.stageHeight;
			}
			
			//need to handle it this way because videoPlayer.width and videoPlayer.height always return 0
			videoPlayer.width = playerWidth;
			videoPlayer.height = playerHeight;
			videoPlayer.x = (stage.stageWidth - playerWidth) / 2;
			videoPlayer.y = (stage.stageHeight - playerHeight) / 2;
			
		}
		
		private function onStageResize(evt:Event):void
		{
			resize();
		}
		
		private function onVideoSizeChanged(evt:DisplayObjectEvent):void
		{
			videoWidth = evt.newWidth;
			videoHeight = evt.newHeight;
			resize();
		}
		
		private function onPause():void
		{
			videoPlayer.mediaPlayer.pause();
		}
		
		private function onPlay():void
		{
			videoPlayer.mediaPlayer.play();
		}
		
		private function getCurrentTime():Number
		{
			return videoPlayer.mediaPlayer.currentTime;
		}
		
		private function setCurrentTime(time:Number):void
		{
			videoPlayer.mediaPlayer.seek(time);
		}
		
		private function getDuration():Number
		{
			return videoPlayer.mediaPlayer.duration;
		}
		
		private function getVolume():Number
		{
			return videoPlayer.mediaPlayer.volume;
		}
		
		private function setVolume(volume:Number):void
		{
			videoPlayer.mediaPlayer.volume = volume;
		}
	}
}