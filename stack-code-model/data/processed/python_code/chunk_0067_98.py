package services.command.miscellaneous.nationalities
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.miscellaneous.nationalities.NationalityDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.miscellaneous.nationalities.DeleteNationalityEvent;
	import services.vo.GlobalStorage;

	public class DeleteNationalityCommand extends BaseCommand
	{	
		override public function execute(event:CairngormEvent):void
		{
			_event = DeleteNationalityEvent( event );
			var delegate:NationalityDelegate = new NationalityDelegate( this );			
			delegate.deleteNationality(_event as DeleteNationalityEvent);
			super.execute( event );
		}
		
		override public function result(data:Object):void
		{
			for (var i:int = 0; i < GlobalStorage.nationality.length; i++)
				if (GlobalStorage.nationality.getItemAt(i).lId == (_event as DeleteNationalityEvent).listNationalities.getItemAt((_event as DeleteNationalityEvent).index).lId)
				{
					var tempLength:int = GlobalStorage.nationality.length;
					(_event as DeleteNationalityEvent).listNationalities.removeItemAt((_event as DeleteNationalityEvent).index);
					if (GlobalStorage.nationality.length == tempLength) // GlobalStorage.language and deleteEvt.listLanguage don't connect
					GlobalStorage.nationality.removeItemAt(i);
					break;
				}			
			super.result( data );
		}
		
	}
}