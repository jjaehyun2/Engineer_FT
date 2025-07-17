package services.command.frontend
{
	import com.adobe.cairngorm.control.CairngormEvent;
	import com.adobe.cairngorm.control.CairngormEventDispatcher;
	
	import services.business.frontend.GetMiscCountryPageDelegate;
	import services.cairngorm.BaseCommand;
	import services.controller.AppController;
	import services.events.frontend.GetMiscCountryPageEvent;
	import services.events.frontend.GetRegionEvent;
	import services.vo.GlobalStorage;
	import services.vo.common.CountryVO;
	
	import mx.collections.ArrayCollection;
	/**
	 *  Command for get list of countries.
	 *  
	 *  @author Artemyev Dmitriy
	 * 	@update Potapov Viktor 
	 *  @date 08.06.2009
	 *  @date_of_update 10.08.2009
	 */
	public class GetMiscCountryPageCommand extends BaseCommand
	{
		
		
		/**
		 *  Interface method. 
		 *  <p>Execute for forwarding the event to the method
		 *  <code>getCountry()</code>.
		 *  
		 *  @param event:CairngormEvent
		 *  
		 *  @see services.events.frontend.GetCountryEvent
		 *  @see services.business.frontend.GetCountryDelegate
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = GetMiscCountryPageEvent( event );
			var delegate:GetMiscCountryPageDelegate = new GetMiscCountryPageDelegate(this);			
			delegate.getMiscCountryPage( _event as GetMiscCountryPageEvent );
			super.execute( event );
		}
		
		override public function result(data:Object):void
		{
			var countries:ArrayCollection = new ArrayCollection(data as Array);
			
			GlobalStorage.countries = countries;
			
			// cashe all city in the address storage
			for(var i:int = 0; i < countries.length; i++)
			{
				GlobalStorage.addressStorage.addCountry(data[i] as CountryVO);
			}
			
			if (countries.length != 0 && getCountryEvent.loadDefault)
			{
				var curCountryId:Number = (GlobalStorage.countries.getItemAt(0) as CountryVO).lId;
				//model.profilesModule.currentProfile.lCurrentCountryId = curCountryId;
				
				var evtRegion:GetRegionEvent = new GetRegionEvent(AppController.GET_REGION_EVENT);
				evtRegion.countryId = curCountryId;
				CairngormEventDispatcher.getInstance().dispatchEvent(evtRegion);
			}
			
			//GetRegionsList
			
			if (getCountryEvent.callBack is Function)
				getCountryEvent.callBack();
			
			super.result( data );
		}
	
	}
}