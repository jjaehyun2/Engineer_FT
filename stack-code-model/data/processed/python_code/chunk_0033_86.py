package widgets.LayerSymbolFilter
{
	import mx.core.ClassFactory;
	
	import spark.components.DataGroup;
	
	[Event(name="filterOptionClick", type="flash.events.Event")]
	
	public class FilterOptionDataGroup extends DataGroup
	{
		public function FilterOptionDataGroup()
		{
			super();
			
			this.itemRenderer = new ClassFactory( FilterOptionItemRenderer );
		}
	}
}