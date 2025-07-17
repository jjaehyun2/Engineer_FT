package controls.MediaPresentation.events {
	import flash.events.Event;
	import flash.geom.Point;
	
	import mx.collections.ArrayCollection;
	
	public class ChangedItemsCanvasDataProviderEvent extends Event {
		public function ChangedItemsCanvasDataProviderEvent(type:String, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
		}
		
		public static const TYPE_CHANGED_ITEMS_CANVAS_DATA_PROVIDER:String = "changedItemsCanvasDataProvider";
		
		override public function clone():Event {
			return new ChangedItemsCanvasDataProviderEvent(type);
		}
	}
}