package services.command.miscellaneous.langueges
{
	import com.adobe.cairngorm.control.CairngormEvent;
	import services.business.miscellaneous.langueges.LanguageDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.miscellaneous.langueges.DeleteLanguageEvent;
	import services.vo.GlobalStorage;

	public class DeleteLanguageCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			_event = DeleteLanguageEvent( event );
			var delegate:LanguageDelegate = new LanguageDelegate( this );
			delegate.deleteLanguage(_event as DeleteLanguageEvent);
			super.execute( event );
		}
		
		override public function result(data:Object):void
		{
			for (var i:int = 0; i < GlobalStorage.language.length; i++)
				if (GlobalStorage.language.getItemAt(i).lId == (_event as DeleteLanguageEvent).listLanguage.getItemAt((_event as DeleteLanguageEvent).index).lId)
				{					
					var tempLength:int = GlobalStorage.language.length;
					(_event as DeleteLanguageEvent).listLanguage.removeItemAt((_event as DeleteLanguageEvent).index);
					if (GlobalStorage.language.length == tempLength) // GlobalStorage.language and deleteEvt.listLanguage don't connect
					GlobalStorage.language.removeItemAt(i);
					break;
				}
			super.result( data );							
		}
		
	}
}