package services.command.security
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.security.SecurityDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.security.AddSystemUserEvent;

	public class AddSystemUserCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			_event = AddSystemUserEvent( event );
			var delegate:SecurityDelegate = new SecurityDelegate( this );			
			delegate.addSystemUser(_event as AddSystemUserEvent);
			super.execute(event);
			
		}
		
		override public function result(data:Object):void
		{
			super.result(data);			
		}
		
		override public function fault(info:Object):void
		{
			super.fault(info);
		}
		
	}
}