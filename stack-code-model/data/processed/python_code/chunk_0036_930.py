package services.command.reports
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.reports.GetReportDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.reports.GetItemTreeEvent;
	
	import mx.collections.ArrayCollection;

	public class GetItemTreeCommand extends BaseCommand
	{
		private var delegate:GetReportDelegate;
		
		override public function execute(event:CairngormEvent):void
		{
			_event = GetItemTreeEvent( event );
			delegate = new GetReportDelegate( this );
			delegate.getItemTree( _event as GetItemTreeEvent );
			super.execute(event);			
			
		}
		
		override public function result(data:Object):void
		{
			model.reportsModule.itemTree = data as Array; 
			super.result(data);
		}		
	}
}