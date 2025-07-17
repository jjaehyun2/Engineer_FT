package services.command.frontend
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.frontend.GetCityDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.frontend.GetCityEvent;
	import framework.module.CommonModule;
	import services.vo.common.CityVO;
	
	import mx.collections.ArrayCollection;
	/**
	 *  Command for get list of cities.
	 *  
	 *  @author Artemyev Dmitriy
	 *  @date 08.06.2009
	 */
	public class GetCityCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = GetCityEvent(event);
			var delegate:GetCityDelegate = new GetCityDelegate(this);
			delegate.getCities(_event as GetCityEvent);
		}
		/**
		 *  The handler to get result of the execution by remote call for
		 *  <code>getCities()</code>.
		 *  <p>This method is called by a service when the return value
		 *  has been received.</p>
		 *  <p><b>Note:</b>all received from server cities are cashed.</p>
		 *   
		 *  @param data:Object - result of the remote call.
		 */
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			_storage.cities = new ArrayCollection(data as Array);
			/// all cities will be cashed
			for each(var city:CityVO in _storage.cities)
			{
				CommonModule.addCity(city);
			}
			
			super.result(data);
		}
	}
}