package services.command.miscellaneous.vat
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.miscellaneous.vat.VATDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.miscellaneous.vat.GetVATDataEvent;
	
	import mx.collections.ArrayCollection; 

	public class GetVATDataCommand extends BaseCommand
	{	 
		override public function execute(event:CairngormEvent):void
		{
			_event = GetVATDataEvent( event );
			var delegate:VATDelegate = new VATDelegate( this );			
			delegate.getVAT(_event as GetVATDataEvent);
			super.execute( event );
		}
		
		override public function result(data:Object):void
		{
			var items:Array = data as Array;
			model.vatModule.vatDP = new ArrayCollection();
			model.vatModule.maxVATItems = items.length;
			for(var i:int = 0;i<items.length;i++)
			{
				model.vatModule.vatDP.addItem( items[i] );
			} 
			
			super.result( data );
		}
	
	}
}