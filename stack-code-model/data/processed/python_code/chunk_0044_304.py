package services.command.inHouse
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.inHouse.InHouseDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.inHouse.GetMessageHistoryEvent;

	public class GetMessageHistoryCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = GetMessageHistoryEvent(event);
			var delegate:InHouseDelegate = new InHouseDelegate(this);
			delegate.getMessageHistory(_event as GetMessageHistoryEvent);
			
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