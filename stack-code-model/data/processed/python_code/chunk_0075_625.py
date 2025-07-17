package services.command.miscellaneous.nationalities
{
	import com.adobe.cairngorm.control.CairngormEvent;
	import services.business.miscellaneous.nationalities.NationalityDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.miscellaneous.nationalities.GetNationalityEvent;
	import services.vo.GlobalStorage;
	
	import mx.collections.ArrayCollection;
	import mx.controls.Alert;

	public class GetNationalityCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			_event = GetNationalityEvent( event );
			var delegate:NationalityDelegate = new NationalityDelegate( this );			
			delegate.getNationality( _event as GetNationalityEvent );
			super.execute( event);
		}
		
		override public function result(data:Object):void
		{
			GlobalStorage.nationality = new ArrayCollection( data as Array );
			super.result( data );
		}		
		
	}
}