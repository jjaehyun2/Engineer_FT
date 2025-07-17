package services.command.miscellaneous.nationalities
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.miscellaneous.nationalities.NationalityDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.miscellaneous.nationalities.AddNationalitiesEvent;

	public class AddNationalitiesCommand extends BaseCommand
	{	
		override public function execute(event:CairngormEvent):void
		{
			_event = AddNationalitiesEvent( event );
			var delegate:NationalityDelegate = new NationalityDelegate( this );
			
			delegate.addNationality(_event as AddNationalitiesEvent);
			super.execute( event );
		}
		
		override public function result(data:Object):void
		{
			super.result( data );	
		}
		
	}
}