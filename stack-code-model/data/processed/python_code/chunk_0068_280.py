package services.command.backend
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.backend.GetPageOfStartDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.backend.GetPageOfStartEvent;
	import services.vo.GlobalStorage;
	import services.vo.common.CountryVO;
	
	import mx.collections.ArrayCollection;

//TODO: can't find usages in the project
	public class GetPageOfStartCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			_event = GetPageOfStartEvent( event );
			var delegate:GetPageOfStartDelegate = new GetPageOfStartDelegate( this );
			 
			delegate.GetPageOfStart( _event as GetPageOfStartEvent );
			super.execute( event );
		}
		
 		override public function result(data:Object):void
		{
			var test:Array = data['COUNTRY_LIST'];// it's hack
			
			
		 	var countries:ArrayCollection = new ArrayCollection(data['COUNTRY_LIST'] as Array);
			
			
			//TODO: where can we find a countries fiels
			GlobalStorage.countries = countries;
			
			for(var i:int = 0; i < countries.length; i++)
			{
				GlobalStorage.addressStorage.addCountry((data['COUNTRY_LIST'] as Array)[i] as CountryVO);
			}
			
			model.roomSettingsModule.roomSettingsDP.removeAll();			
			model.roomSettingsModule.roomSettingsDP = new ArrayCollection(data['ROOM_SETTING_LIST'] as Array);			
			model.roomSettingsModule.maxRoomSettingsItems = model.roomSettingsModule.roomSettingsDP.length;
			
			 model.roomTypesModule.roomTypesDP.removeAll();
			 model.roomTypesModule.roomTypesDP = new ArrayCollection(data['ROOM_TYPE_LIST'] as Array);	
			 model.roomTypesModule.maxRoomTypesItems = model.roomTypesModule.roomTypesDP.length;
			
			 
			 GlobalStorage.language = new ArrayCollection( data['LANGUAGE_LIST'] as Array );
			
			 GlobalStorage.salutationAll = new ArrayCollection( data['SALUTATION_LIST'] as Array ); 
			
			 GlobalStorage.nationality = new ArrayCollection( data['NATIONALITY_LIST'] as Array ); 
			
			 GlobalStorage.vipTotal = new ArrayCollection(data['VIP_TOTAL_LIST'] as Array); 
			
			 GlobalStorage.mailings = new ArrayCollection(data['MAILING_LIST'] as Array);
			 
			 GlobalStorage.sourceCodes = new ArrayCollection(data['SOURCE_CODE_LIST'] as Array);
			 
			 GlobalStorage.marketCodes = new ArrayCollection(data['MARKET_CODE_LIST'] as Array);
			 
			 GlobalStorage.loyaltyPrograms = new ArrayCollection(data['LOYALTY_PROGRAM_LIST'] as Array);
			
			var items:Array = data['VAT_LIST'] as Array;
			model.vatModule.vatDP.removeAll();
			model.vatModule.maxVATItems = items.length;
			for(i = 0; i<items.length; i++)
			{
				model.vatModule.vatDP.addItem( items[i] );
			}
			super.result( data );
		}		
	}
}