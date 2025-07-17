package services.command.BDC
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.BDC.BDCDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.BDC.CheckDepartureEvent;

	public class CheckDepartureCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = CheckDepartureEvent(event);
			var delegate:BDCDelegate= new BDCDelegate(this);
			delegate.checkDeparture(_event as CheckDepartureEvent);
			
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