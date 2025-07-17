package {
	import flash.display.Sprite;
	import flash.events.Event;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	public class Main extends Sprite {
		
		public function Main():void {
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			
			
			var menu:MainMenu = new MainMenu("Menu title");
			addChild(menu);
			
			var item1:MenuItem = new MenuItem("Item 1");
			item1.addItem(new MenuItem("item 1/1"));
			item1.addItem(new MenuItem("item 1/2"));
			menu.addItem(item1);
			
			var item2:MenuItem = new MenuItem("Item 2");
			item2.addItem(new MenuItem("item 2/1"));
			item2.addItem(new MenuItem("item 2/2"));
			item2.addItem(new MenuItem("item 2/2"));
			menu.addItem(item2);
			
			menu.addItem(new MenuItem("Item 3"));
			menu.addItem(new MenuItem("Item 4"));
			menu.addItem(new MenuItem("Item 5"));
		}
		
	}
	
}