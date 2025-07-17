package services.command.BDC
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.BDC.BDCDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.BDC.CheckProfilesEvent;
	import services.events.BDC.CheckShiftsEvent;

	public class CheckShiftsCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = CheckShiftsEvent(event);
			var delegate:BDCDelegate= new BDCDelegate(this);
			delegate.checkShifts(_event as CheckShiftsEvent);
			
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