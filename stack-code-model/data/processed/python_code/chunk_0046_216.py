package com.appfw.view.mediator
{
	import com.GameMainClass;
	import com.appfw.MediatorConst;
	import com.appfw.ctrl.cmds.ui.ShowBattleWndCmd;
	import com.engine.utils.Map;
	import com.fw.AbstractMediator;
	import com.fw.mgr.TimerMgr;
	import com.fw.mgr.WndMgr;
	
	import starling.display.DisplayObjectContainer;
	
	public class AppMediator extends AbstractMediator
	{
		private static const NAME:String = "AppMediator";		
		private var _rootView:GameMainClass;
		
		public function AppMediator(viewComponent:DisplayObjectContainer)
		{
			super(NAME);
			this._rootView = viewComponent as GameMainClass;
			WndMgr.defaultWinParent = this._rootView;
			TimerMgr.systemTime = new Date().time;
		}
		
		override public function onRegister():void
		{
		}
		
		override public function onRemove():void
		{
		}
		
		override protected function listNotificationListeners(listeners:Map):void
		{
			super.listNotificationListeners(listeners);
			//			appFacade.registerCommand(MediatorConst.SHOW_MAIN_UI, ShowMainUICmd);
			appFacade.registerCommand(MediatorConst.SHOW_BATTLE, ShowBattleWndCmd);
		}
	}
}