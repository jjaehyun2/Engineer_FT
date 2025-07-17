package com.fw.controller.bootstraps
{
	import com.fw.ActionConst;
	import com.fw.controller.cmds.action.LoginCommand;
	
	import org.puremvc.as3.interfaces.IFacade;
	import org.puremvc.as3.patterns.facade.Facade;
	
	public class BootstrapCmd
	{
		public function BootstrapCmd()
		{
			super();
		}
		
		protected static function get facade():IFacade
		{
			return Facade.getInstance();
		}
		
		public static function initCmd():void
		{
			// 初始化通信接口
			facade.registerCommand(ActionConst.LOGIN, LoginCommand);
		}
	}
}