package com.appfw.ctrl.cmds
{
	import com.appfw.ctrl.boots.BootCmd;
	import com.appfw.ctrl.boots.BootModel;
	import com.appfw.ctrl.boots.BootViewMediator;
	
	import org.puremvc.as3.interfaces.INotification;
	import org.puremvc.as3.patterns.command.SimpleCommand;
	
	import starling.display.DisplayObjectContainer;
	
	public class StartupAppCmd extends SimpleCommand
	{
		public function StartupAppCmd()
		{
			super();
		}
		
		override public function execute( notification:INotification ) : void
		{
			trace("boot");
			BootCmd.instance.init();
			BootModel.instance.init();
			BootViewMediator.instance.init(notification.getBody() as DisplayObjectContainer);
		}
	}
}