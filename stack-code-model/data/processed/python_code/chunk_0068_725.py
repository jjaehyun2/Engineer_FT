package com.appfw.ctrl.boots
{
	import com.appfw.ActionConst;
	import com.appfw.ctrl.cmds.action.LoginCmd;
	
	import org.puremvc.as3.interfaces.IFacade;
	import org.puremvc.as3.patterns.facade.Facade;

	public class BootCmd
	{
		private static var _instance:BootCmd;
		
		public function BootCmd()
		{
		}
		
		public static function get instance():BootCmd
		{
			return _instance ||= new BootCmd();
		}
		
		protected function get facade():IFacade
		{
			return Facade.getInstance();
		}
		
		public function init():void
		{
			// 初始化通信接口
			facade.registerCommand(ActionConst.LOGIN, LoginCmd);
		}
	}
}