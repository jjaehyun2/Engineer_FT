package services.command.BDC
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.BDC.BDCDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.BDC.TotalLogoutEvent;

	public class TotalLogoutCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = TotalLogoutEvent(event);
			var delegate:BDCDelegate= new BDCDelegate(this);
			delegate.totalLogout(_event as TotalLogoutEvent);
			
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