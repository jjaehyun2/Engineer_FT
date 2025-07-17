package framework.events
{
	import flash.events.Event;
	
	public class UpdateCategoryEvent extends Event
	{
		public static const UPDATE_CATEGORY:String = "UpdateCategoryEvent_updateCategory";
		public var categoryId:uint;
		public var columnName:String;
		public var columnValue:*;
		
		public function UpdateCategoryEvent(type:String, _categoryId:uint, _cName:String, _cValue:*, bubbles:Boolean=false, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			
			categoryId = _categoryId;
			columnName = _cName;
			columnValue = _cValue;
		}
		
		public override function clone():Event {
			return new UpdateCategoryEvent(type, categoryId, columnName, columnValue);
		}
	}
}