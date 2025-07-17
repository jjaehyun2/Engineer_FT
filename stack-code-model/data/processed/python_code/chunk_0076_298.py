package widgets.SearchEnhanced.supportClasses
{
	import mx.core.ClassFactory;
	
	import spark.components.DataGroup;
	
	public class SearchLayerDataGroup extends DataGroup
	{
		public function SearchLayerDataGroup()
		{
			super();
			this.itemRenderer = new ClassFactory(widgets.SearchEnhanced.supportClasses.SearchLayerItemRenderer);
		}
	}
}