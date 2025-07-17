package modules.gameCommon.view
{
	
	import common.event.EventCenter;
	
	import laya.events.Event;
	import laya.utils.Handler;
	import laya.utils.Tween;
	
	//import ui.gameCommon.ReplayControlViewUI;
	

	public class ReplayControlView
	{
		protected var _skin:*;
		
		public function ReplayControlView(skin:*)
		{
			_skin = skin;
			
			orignalY = _skin.replayBox.y;
			
			_skin.backBtn.on(Event.CLICK,this,onClick_backBtn);
			_skin.upBtn.on(Event.CLICK,this,onClick_upBtn);
			_skin.playBtn.on(Event.CLICK,this,onClick_playBtn);
			_skin.stopBtn.on(Event.CLICK,this,onClick_stopBtn);
			_skin.downBtn.on(Event.CLICK,this,onClick_downBtn);
			_skin.skipBtn.on(Event.CLICK,this,onClick_skipBtn);
			
			EventCenter.instance.on(EventCenter.REPLAY_over,this,onReplayOver);
			
			_skin.on(Event.CLICK,this,onClickSkin);
			_skin.replayBox.on(Event.CLICK,this,onClickReplayBox);
			
			reset();
			hide();
		}
		
		protected var state:uint = 0;
		
		protected function onClickSkin(e:Event):void
		{
			if(state == 1)
			{
				hideBtns();
			}
			else
			{
				showEff();
			}
			
		}
		
		protected function onClickReplayBox(e:Event):void
		{
			e.stopPropagation();
			Laya.timer.clear(this,hideBtns);
			HideEff();
		}
		
		
		/**屏蔽的暂时不做*/
		public function show():void
		{
			_skin.visible = true;
			_skin.replayBox.y = orignalY;
			
			Tween.clearAll(_skin.replayBox);
			state = 1;
			HideEff();
		}
		
		/**隐藏按钮动画*/
		public function HideEff():void
		{
			Laya.timer.once(8000,this,hideBtns);
		}
		
		protected function hideBtns():void
		{
			state = 0;
			Tween.to(_skin.replayBox,{y:orignalY+72},300);
		}
		
		/**显示按钮动画*/
		public function showEff():void
		{
			state = 1;
			Tween.to(_skin.replayBox,{y:orignalY},300,null,Handler.create(this,HideEff));
		}
		
		
		
		public function hide():void
		{
			_skin.visible = false;
		}
		
		protected function onClick_backBtn(e:Event):void
		{
			EventCenter.instance.event(EventCenter.REPLAY_back,null);
		}
		protected function onClick_upBtn(e:Event):void
		{
			onClick_stopBtn();
			EventCenter.instance.event(EventCenter.REPLAY_up,null);
		}
		protected function onClick_playBtn(e:Event=null):void
		{
			_skin.playBtn.visible = false;
			_skin.stopBtn.visible = true;
			
			EventCenter.instance.event(EventCenter.REPLAY_play,null);
		}
		protected function onClick_stopBtn(e:Event=null):void
		{
			_skin.playBtn.visible = true;
			_skin.stopBtn.visible = false;
			
			EventCenter.instance.event(EventCenter.REPLAY_pause,null);
		}
		
		protected function onClick_downBtn(e:Event):void
		{
			onClick_stopBtn();
			EventCenter.instance.event(EventCenter.REPLAY_down,null);
		}
		
		protected function onClick_skipBtn(e:Event):void
		{
			
			EventCenter.instance.event(EventCenter.REPLAY_skip,null);
		}
		
		protected function onReplayOver():void
		{
			_skin.upBtn.disabled = true;
			_skin.playBtn.disabled = true;
			_skin.stopBtn.disabled = true;
			_skin.downBtn.disabled = true;
			_skin.skipBtn.disabled = true;
		}
		
		protected var orignalY:Number = 472;
		
		
		public function moveCalculate():void
		{
			_skin.replayBox.y = 559;
		}
		
		public function reset():void
		{
			_skin.replayBox.y = orignalY;
			
			_skin.stopBtn.visible = true;
			_skin.playBtn.visible = false;
			
			_skin.upBtn.disabled = false;
			_skin.playBtn.disabled = false;
			_skin.stopBtn.disabled = false;
			_skin.downBtn.disabled = false;
			_skin.skipBtn.disabled = false;
			
			
			//临时加的，等功能实现后再去掉
			//_skin.skipBtn.visible = false;
			//_skin.upBtn.visible = false;
		}
		
		public function replayup_reset():void
		{
			_skin.replayBox.y = orignalY;
			
			_skin.stopBtn.visible = false;
			_skin.playBtn.visible = true;
			
			_skin.upBtn.disabled = false;
			_skin.playBtn.disabled = false;
			_skin.stopBtn.disabled = false;
			_skin.downBtn.disabled = false;
			_skin.skipBtn.disabled = false;
		}
	}
}