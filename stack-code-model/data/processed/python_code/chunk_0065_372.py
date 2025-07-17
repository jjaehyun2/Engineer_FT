package com.fw.controller.bootstraps
{
	import com.GameMainClass;
	import com.fw.MediatorConst;
	import com.fw.view.AppMediator;
	
	import org.puremvc.as3.interfaces.IFacade;
	import org.puremvc.as3.patterns.facade.Facade;
	
	import starling.display.DisplayObjectContainer;
	
	public class BootstrapViewMediator
	{
		public function BootstrapViewMediator()
		{
			super();
		}
		
		protected static function get facade():IFacade
		{
			return Facade.getInstance();
		}
		
		public static function initCmd(view:DisplayObjectContainer):void
		{
			//游戏主舞台
			facade.registerMediator(new AppMediator(view as GameMainClass));
			
			facade.sendNotification(MediatorConst.SHOW_MAIN_UI);
		}
	}
}