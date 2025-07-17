package
{
	import com.heyi.player.core.StarlingMediaPlayer;
	import com.tudou.utils.Utils;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.ui.Multitouch;
	import flash.ui.MultitouchInputMode;
	import starling.display.Sprite;
	import starling.events.Event;
	import starling.events.NetStatusEvent;
	/**
	 * StarlingMediaPlayer 的使用样例
	 * 
	 * @author 8088
	 */
	public class StarlingPlayerSample extends Sprite 
	{
		
		public function StarlingPlayerSample() 
		{
			if (stage) onStage();
			else addEventListener(Event.ADDED_TO_STAGE, onStage);
		}
		
		protected function onStage(evt:Event = null):void
		{
			removeEventListener(Event.ADDED_TO_STAGE, onStage);
			
			initPlayer();
			
			//initMonitor();
			
		}
		
		private function initPlayer():void
		{
			var player:StarlingMediaPlayer = new StarlingMediaPlayer();
			//player.hardwareAccelerate = true;
			player.source = {
				url:"http://10.10.22.82/videos/test1.mp4",
				bufferTime: 1
			}
			player.addEventListener(NetStatusEvent.NET_STATUS, onNetStatus);
			player.start();
			addChild(player);
		}
		
		private function onNetStatus(evt:NetStatusEvent):void
		{
			trace("DEMO#####", Utils.serialize(evt.info))
		}
		
		private function deactivate(e:Event):void 
		{
			// make sure the app behaves well (or exits) when in background
			//NativeApplication.nativeApplication.exit();
		}
		
	}
	
}