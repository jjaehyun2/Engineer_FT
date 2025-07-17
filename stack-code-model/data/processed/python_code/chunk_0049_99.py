package com.fw
{
	import com.fw.controller.StartupAppCmd;

	public class LostFacade extends AppFacade
	{
		private static var _instance:LostFacade;
		
		public function LostFacade()
		{
			super();
		}
		
		public static function get instance():LostFacade
		{
			if (_instance == null)
				_instance = new LostFacade();
			return _instance as LostFacade;
		}
		
		override protected function initializeController():void
		{
			super.initializeController();
			
			// 以下这句在继承之后要加的
			registerCommand(AppFacade.STARTUP_APPFACADE, StartupAppCmd);
		}
	}
}