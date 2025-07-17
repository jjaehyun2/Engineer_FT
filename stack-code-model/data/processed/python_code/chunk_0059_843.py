package services.command.checkOut
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.checkOut.CheckOutDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.checkOut.AttachPackageToAccountEvent;

	public class AttachPackageToAccountCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = AttachPackageToAccountEvent(event);
			var delegate:CheckOutDelegate = new CheckOutDelegate(this);
			delegate.attachPackagesToAccount(_event as AttachPackageToAccountEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			super.result(data);
		}
	}
}