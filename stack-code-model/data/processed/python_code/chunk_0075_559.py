package services.command.BDC
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.BDC.BDCDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.BDC.CheckProfilesEvent;
	import services.events.BDC.UpdateRoomStatesEvent;

	public class UpdateRoomStatesCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = UpdateRoomStatesEvent(event);
			var delegate:BDCDelegate= new BDCDelegate(this);
			delegate.updateRoomStates(_event as UpdateRoomStatesEvent);
			
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