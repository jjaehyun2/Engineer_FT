/*
 * Class: AssembleMenuBar
 * @author Ryan C. Knaggs
 * @since 1.0
 * @date 09/18/2009
 * @description: Designed to build the categories
 * for the main menu bar
 */

package views
{
	import flash.events.MouseEvent;
	
	import libs.vo.GlobalsVO;
	
	import models.Menu_Model;
	
	import mx.containers.HBox;
	
	import mxml.*;
	
	import utils.strings.Strings;
	
	
	
	public class CreateMenuBar_View
	{
		
		
		private var _menuBar:HBox;
		private var _callBack:Function;
		private var _model:Menu_Model;
		private var _css:Function;
		private var _categories:Array;							// List of category references
		
		private const MCR:String = "MenuController";
		private const MBC:String = "MenuBarContainer";
		private const MBH:String = "menuBarHeight";
		private const CSH:String = "categorySeparatorHeight";
		private const CSW:String = "categorySeparatorWidth";
		private const CSSC:String = "categorySeparatorScaleContent";
		private const CSMAR:String = "categorySeparatorMaintainAspectRatio";
		
		// BEGIN: Please do not change the code found within this comment block...
		public var callback_signal_addCategory:Function;
		// END!   Please do not change the code found within this comment block...

		/**
		 * Constructor 
		 * @param parent
		 */
		 		
		public function CreateMenuBar_View() {
		}
		
		
		
		
		/**
		 * Return reference of the requested
		 * category item 
		 * @param id
		 * @return CategoryItem instance 
		 */
		 		
		public function getCategoryRef(id:int):CategoryItem {
			return _categories[id];
		}
		
		
		
		
		
		public function getCategories():Array {
			return _categories;
		}
		
		
		
		
		/**
		 * Deselect all category items 
		 */
		 		
		public function deSelectAll():void {
			for(var i:Object in this._categories) {
				this._categories[i].onMouseOut();
			}
		}
		
		
		
		
		
		/**
		 * Loop throught the menu data from the
		 * menu model and get the main category
		 * information and build the
		 * main category for the menu bar.
		 */
		
		public function init(callBack:Function):void {
			
			this._callBack = callBack;
			var container:MenuBar = GlobalsVO.getGlobal(MBC);
			
			this._css = GlobalsVO.getCSSProperty;
			this._menuBar = container.menuBar;
			
			// ADMINTOOL: Clear all menus and sub-menus
			GlobalsVO.getGlobal(MCR).deleteAndRemoveAllMenuChildren();
			
			// Alias for data model
			_model = GlobalsVO.getGlobal(GlobalsVO.DATA_MODEL);

			// Define the menu bar height from the CSS style
			GlobalsVO.setMaxHeight(container.componentHeight = Number(_css(MBH)));
			
			// Apply the CSS style to the menu bar container
			GlobalsVO.setStyle(container);
			
			/* Get the category level information
			 * to build the menu categorys */
			var data:int=0;
			_categories = new Array();
			
			while(data < _model.menuData.data.length) {
				addCategorySeparator(_menuBar);
				_categories.push(addCategory(_model.menuData.data[data],data++));
			}
			
			addCategorySeparator(_menuBar);
		}
		
		
		
		
		
		/**
		 * Set and lock the category highlight 
		 * @param item
		 */
		 		
		public function setStaticCategory(item:int):void {
			
			/* This line of code exists because sometimes the 
			 * item can be out of range for the array 
			 * and this results in a null object and as 
			 * we know null objects do not respond well to messages */
			 
			if (item > -1) { 
				_categories[item].overRideSelect = true;
			}
		}
		
		
		
		
		
		
		/**
		 * Add a category to the menu bar
		 * @param - data:Object is the main category
		 * information for building the category item in the
		 * menubar.
		 */
		
		private function addCategory(data:Object,categoryId:int):CategoryItem {
			// Get the MainCategory class, this is an MXML file
			var ci:CategoryItem = new CategoryItem();
			ci.htmlText = unescape(data[_model.getMetaDataValue(GlobalsVO.META_LABEL)]);
			
			// Set the url
			
			var u:String = data[_model.metaData.hash.url];
			var hasUrl:Boolean = ( (u is String) && (u.length > 0) );
			ci.url = (hasUrl) ? _model.getUrl(data) : null;
			ci.target = data[_model.getMetaDataValue(GlobalsVO.META_TARGET)];
			ci.categoryPosition = categoryId;
			ci.currentData = data;
			this._menuBar.addChild(ci);
			
			// Apply the CSS style to the Category Item container
			GlobalsVO.setStyle(ci);
			
			// Setup the approprate listeners for the category behavior.
			ci.addEventListener(MouseEvent.CLICK,_callBack);
			ci.addEventListener(MouseEvent.MOUSE_OVER,_callBack);
			ci.addEventListener(MouseEvent.MOUSE_OUT,_callBack);
			
			// BEGIN: Please do not change the code found within this comment block...
			if (this.callback_signal_addCategory is Function) {
				try {
					this.callback_signal_addCategory(ci,_menuBar,_model);
				} catch (e:Error) {}
			}
			// END!   Please do not change the code found within this comment block...
			
			return ci;
		}
		
		
		
		
		
		
		/**
		 * Add a graphic separator between the
		 * category items 
		 * @param target - The container where to 
		 * place the graphic asset into
		 */
		 		
		private function addCategorySeparator(target:Object):void {
			var cis:CategoryItemSeparator = new CategoryItemSeparator();
			cis.componentHeight=Number(_css(CSH));
			cis.componentWidth=Number(_css(CSW));
			cis.scaleContent = Strings.strToBool(_css(CSSC));
			cis.maintainAspectRatio = Strings.strToBool(_css(CSMAR));
			target.addChild(cis);
		}
	}
}