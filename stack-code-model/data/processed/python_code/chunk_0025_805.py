package com.appfw
{
	import com.appfw.ctrl.cmds.StartupAppCmd;
	import com.fw.AppFacade;
	
	public class FpFacade extends AppFacade
	{
		private static var _instance:FpFacade;
		
		public function FpFacade()
		{
			super();
		}
		
		public static function get instance():FpFacade
		{
			return _instance ||= new FpFacade();
		}
		
		override protected function initializeController():void
		{
			super.initializeController();
			// 以下这句在继承之后要加的
			registerCommand(AppFacade.STARTUP_APPFACADE, StartupAppCmd);
		}
	}
}