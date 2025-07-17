package widgets.LayerSymbolFilter
{
	import mx.core.ClassFactory;
	
	import spark.components.DataGroup;
	
	[Event(name="filterOptionChanged", type="flash.events.Event")]
	
	public class FilterGroupDataGroup extends DataGroup
	{
		public function FilterGroupDataGroup()
		{
			super();
			
			this.itemRenderer = new ClassFactory( FilterGroupItemRenderer );
		}
	}
}