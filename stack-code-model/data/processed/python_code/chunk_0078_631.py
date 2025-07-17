package framework.view.components.address
{
	import flash.events.Event;
	
	import services.vo.common.RegionVO;
	
	import h2olib.control.ComboBoxEx;

	public class RegionComboBox extends ComboBoxEx
	{
		private var _regionId:Number = 0;
		
		public function RegionComboBox()
		{
			super();
		}
		
		/**
		 *  @private
		 */
		override public function set dataProvider(value:Object):void
		{
			super.dataProvider = value;
			if (_regionId == 0)
			{
				if (dataProvider.length > 0)
				{
					selectedItem = dataProvider.getItemAt(0);
					//regionId = (selectedItem as RegionVO).lId;
				}
				else 
				{
					regionId = 0;
					selectedIndex = -1;
					selectedItem = null;
				}
			}
			else
			{
				setItemByField("lId", _regionId);
			}
		}
		
		[Bindable(event="regionIdChanged")]
		public function get regionId():Number
		{
			return _regionId;
		}
		/**
		 *  @private
		 */
		public function set regionId(value:Number):void
		{
			_regionId = value;
			
			dispatchEvent(new Event("regionIdChanged"));
		}
	}
}