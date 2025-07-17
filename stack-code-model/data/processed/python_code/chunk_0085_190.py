package services.command.items.arrangementCodes
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.items.ItemsDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.items.arrangementCodes.GetArrangementsEvent;
	
	import mx.collections.ArrayCollection;

	public class GetArrangementsCommand extends BaseCommand
	{
		/**
		 *  @override 
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = GetArrangementsEvent(event);
			var delegate:ItemsDelegate = new ItemsDelegate(this);
			
			delegate.getArrangementsList(_event as GetArrangementsEvent);
			
			super.execute(event);
		}
		/**
		 *  @override 
		 */
		override public function result(data:Object):void
		{
			model.transactionModule.arrangementCodesList = new ArrayCollection(data as Array);
			
			super.result(data);
		}
	}
}