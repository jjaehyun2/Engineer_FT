package widgets.SearchEnhanced.supportClasses
{
	import mx.core.ClassFactory;
	
	import spark.components.DataGroup;
	
	// These events bubble up from the SearchResultItemRenderer
	[Event(name="searchResultLinkClick", type="flash.events.Event")]

	public class SearchResultLinkDataGroup extends DataGroup
	{
		public function SearchResultLinkDataGroup()
		{
			super();
			
			this.itemRenderer = new ClassFactory(SearchResultLinkItemRenderer);
		}
	}
}