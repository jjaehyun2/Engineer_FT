package widgets.AddShapefile
{
	import mx.core.ClassFactory;
	
	import spark.components.DataGroup;
	
	// these events bubble up from the SearchResultItemRenderer
	[Event(name="shapefileResultClick", type="flash.events.Event")]
	[Event(name="shapefileDelete", type="flash.events.Event")]
	
	public class ShapeFileResultDataGroup extends DataGroup
	{
		public function ShapeFileResultDataGroup()
		{
			super();
			this.itemRenderer = new ClassFactory(ShapeFileResultItemRenderer);
		}
	}
}