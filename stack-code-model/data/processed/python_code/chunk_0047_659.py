package screens.map {
	
	import application.utils.StaticGUI;
	import components.AddressMenuBlock;
	import components.renderers.MapAddressBlockListRenderer;
	import feathers.controls.List;
	import feathers.controls.Screen;
	import feathers.controls.ScrollBarDisplayMode;
	import feathers.controls.ScrollPolicy;
	import feathers.controls.renderers.IListItemRenderer;
	import feathers.data.ListCollection;
	import feathers.layout.HorizontalAlign;
	import feathers.layout.VerticalAlign;
	import feathers.layout.VerticalLayout;
	import screens.ScreenID;
	import starling.display.DisplayObject;
	import starling.events.Event;
	
	
	public class ScreenMapAdressList extends Screen {
		
		private var menu:AddressMenuBlock;
		private var list:List;
		private var mailList:ListCollection;
		
		public function ScreenMapAdressList() {
			super();
			//this.title = "Screen C";
		}
		
		override protected function initialize():void {
			
			super.initialize();
			
			
			var layout:VerticalLayout = new VerticalLayout();
			layout.horizontalAlign = HorizontalAlign.CENTER;
			layout.verticalAlign = VerticalAlign.TOP;
			//layout.gap = Settings._getIntByDPI(5);
			//layout.paddingTop = Settings._getIntByDPI(5);
			
			this.layout = layout;
			
			
			
			var listLayout:VerticalLayout = new VerticalLayout();
			listLayout.verticalAlign = VerticalAlign.TOP;
			listLayout.horizontalAlign = HorizontalAlign.LEFT;
			
			
			list = new List();
			list.horizontalScrollPolicy = ScrollPolicy.OFF;
			list.verticalScrollPolicy = ScrollPolicy.AUTO;
			list.scrollBarDisplayMode = ScrollBarDisplayMode.NONE;
			//list.clipContent = false;
			list.width = stage.stageWidth;
			list.backgroundSkin = null;
			list.height = stage.stageHeight - Settings._getIntByDPI(305);
			this.addChild(list);
			list.validate();
			list.layout = listLayout;
			list.addEventListener(Event.CHANGE, listChangeHandler );
			list.dataProvider = null;
			list.snapScrollPositionsToPixels = true;
			
			
			list.itemRendererFactory = function():IListItemRenderer{
				var renderer:MapAddressBlockListRenderer = new MapAddressBlockListRenderer();
				//renderer.padding = 20;
				return renderer;
			}
			
			mailList = new ListCollection;
			list.dataProvider = mailList;
			
			var menuArr:Array = String(Settings._mui['map_address_menu'][Settings._lang]).split(',');
			menu = new AddressMenuBlock(menuArr);
			menu.addEventListener(AppEvent.CHANGE, menuChangeHandler);
			
			addChildAt(menu, 0);
			
			this.width = stage.stageWidth;
			this.height = stage.stageHeight;
			
			//this.validate();
		}
		
		private function listChangeHandler(e:Event):void {
			//dispatchEventWith(AppEvent.TOGGLE_TOP_MAP_DRAWER, true);
			Settings._splash._navigator.pushScreen(ScreenID.MAPS);
		}
		
		private function menuChangeHandler(e:Event):void {
			
			mailList.removeAll();
			list.scrollToPosition(0,0);
			
			switch(e.data.selectedIndex) {
				case 0:
					
					mailList.addItem( { address: 'დავით აღმაშენებლის გამზ. №44 ', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის გამზ. №44 ', city:'თბილისი'  } );
					mailList.addItem( { address: 'ქეთევან წამებულის გამზ. №84/86', city:'თბილისი'  } );
					mailList.addItem( { address: 'ქეთევან წამებულის გამზ. №84/86', city:'თბილისი'  } );
					mailList.addItem( { address: 'ი.ჭავჭავაძის გამზ. №21', city:'თბილისი'  } );
					mailList.addItem( { address: 'ი.ჭავჭავაძის გამზ. №21', city:'თბილისი'  } );
					mailList.addItem( { address: 'ვაჟა-ფშაველის გამზ. №67', city:'თბილისი'  } );
					mailList.addItem( { address: 'ვაჟა-ფშაველის გამზ. №67', city:'თბილისი'  } );
					mailList.addItem( { address: 'ვაჟა-ფშაველის გამზ. №67', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					
					break;
					
					
				case 1:
					
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					
					break;
					
					
				case 2:
					
					mailList.addItem( { address: 'დავით აღმაშენებლის ქ. №7', city:'თბილისი'  } );
					mailList.addItem( { address: 'ვაჟა-ფშაველის გამზ. №67', city:'თბილისი'  } );
					
					break;
			}
		}
		
		private function itemFactory(st:String):IListItemRenderer {
			var renderer:MapAddressBlockListRenderer = new MapAddressBlockListRenderer;
			return renderer;	
		}
		
		private function disposeItemAccessory(item:Object):void {
			DisplayObject(itemFactory(item.address)).dispose();
		}
		
		override public function dispose():void {
			
			if (list) {
				list.removeEventListener(Event.CHANGE, listChangeHandler);
				list.dataProvider.dispose(disposeItemAccessory);
				StaticGUI._safeRemoveChildren(list, true);
			}
			if (menu) {
				menu.removeEventListener(AppEvent.CHANGE, menuChangeHandler);
				menu.dispose();
			}
			list = null;
			mailList = null
			menu = null;
			super.dispose();
		}
	}
}