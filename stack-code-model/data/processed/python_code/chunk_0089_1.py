package dom.tidesdk.ui
{
	/**
	 * <p>An object representing a menu.</p>
	 * 
	 *   <p>A Menu object can be added to the current
	 * window of a TideSDK application. Menu objects can
	 * be made up of a number of MenuItems(see <a
	 * href="#!/api/Ti.UI.MenuItem" rel="Ti.UI.MenuItem"
	 * class="docClass">Ti.UI.MenuItem</a>). These menu
	 * items can be added to the menu object at anytime
	 * and TideSDK will ensure that all menu instances
	 * update immediately.</p>
	 * 
	 *   <p>Please take a look at the code example
	 * below:</p>
	 * 
	 *   <pre><code>    //Create the menu object        
	 * var menu = <a
	 * href="#!/api/Ti.UI-method-createMenu"
	 * rel="Ti.UI-method-createMenu"
	 * class="docClass">Ti.UI.createMenu</a>();     
	 * //Create menu items     var subMenu1 =
	 * menu.addItem('Menu1');     var subMenu2 =
	 * menu.addItem('Menu2');     var subMenu3 =
	 * menu.addItem('Menu3');      //Add menu to the
	 * current window     <a
	 * href="#!/api/Ti.UI-method-getCurrentWindow"
	 * rel="Ti.UI-method-getCurrentWindow"
	 * class="docClass">Ti.UI.getCurrentWindow</a>().setMenu(menu);
	 *      //Or alternatively you can use the snippet
	 * below     //to add the menu to the current window 
	 *    //Ti.UI.currentWindow.menu = menu;
	 * </code></pre>
	 */
	public class TMenu
	{
		//
		// METHODS
		//

		/**
		 * <p>Add a check item to this menu with the given
		 * attributes.</p>
		 * 
		 * @param label  The label for the new item 
		 * @param listener  An event listener callback for the item 
		 * 
		 * @return Ti.UI.MenuItem   
		 */
		public function addCheckItem(label:String, listener:Function=null):TMenuItem { return null; }

		/**
		 * <p>Add an item to this menu with the given
		 * attributes.</p>
		 * 
		 * @param label  The label for the new item 
		 * @param listener  An event listener callback for the item 
		 * @param iconURL  "The URL for this item's icon" 
		 * 
		 * @return Ti.UI.MenuItem   
		 */
		public function addItem(label:String, listener:Function=null, iconURL:String=null):TMenuItem { return null; }

		/**
		 * <p>Add a separator item to this menu.</p>
		 * 
		 * @return Ti.UI.MenuItem   
		 */
		public function addSeparatorItem():TMenuItem { return null; }

		/**
		 * <p>Append a MenuItem object to a menu.</p>
		 * 
		 * @param item  Append an item to this menu 
		 */
		public function appendItem(item:TMenuItem):void {}

		/**
		 * <p>Remove all items from this menu.</p>
		 */
		public function clear():void {}

		/**
		 * <p>Get an item from this menu at the given index.
		 * This method will throw an exception if the index
		 * is out of range.</p>
		 * 
		 * @param index  The index of the item to get 
		 * 
		 * @return Ti.UI.MenuItem   
		 */
		public function getItemAt(index:int):TMenuItem { return null; }

		/**
		 * <p>Get the length of this menu.</p>
		 * 
		 * @return Number   
		 */
		public function getLength():Number { return 0; }

		/**
		 * <p>Insert a menu item before the given index. This
		 * method will throw an exception if the index of out
		 * of range.</p>
		 * 
		 * @param item  The menu item to insert 
		 * @param index  The index for this menu item 
		 */
		public function insertItemAt(item:TMenuItem, index:int):void {}

		/**
		 * <p>Remove the item in this menu at the given
		 * index. This method will throw an exception if the
		 * index is out of range.</p>
		 * 
		 * @param index  The index of the item to remove 
		 */
		public function removeItemAt(index:int):void {}

		public function TMenu() {}
	}
}