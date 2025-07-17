package services.command.BDC
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.BDC.BDCDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.BDC.CheckProfilesEvent;

	public class CheckProfilesCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = CheckProfilesEvent(event);
			var delegate:BDCDelegate= new BDCDelegate(this);
			delegate.checkProfiles(_event as CheckProfilesEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			var profiles:Array = data as Array;
			model.BDCModule.listProfiles = profiles;
			super.result(data);
		}
	}
}