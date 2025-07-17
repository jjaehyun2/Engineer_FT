package framework.views.events
{
	import flash.events.Event;
	
	import mx.collections.ArrayCollection;
	
	public class CategoryDataEvent extends Event
	{
		public static const GET_CATEGORIES_DATA:String = "CategoryDataEvent_getCategoriesData";
		public static const CATEGORIES_DATA_RETURN:String = "CategoryDataEvent_categoriesDataReturn";
		
		public var data:ArrayCollection;
		
		public function CategoryDataEvent(type:String, _data:ArrayCollection = null, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
			data = _data;
		}
		
		public override function clone():Event {
			return new CategoryDataEvent(type, data);
		}
	}
}