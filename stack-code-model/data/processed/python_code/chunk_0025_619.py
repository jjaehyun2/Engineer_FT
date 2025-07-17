package screens.posta {
	
	import application.utils.StaticGUI;
	import components.MailBlock;
	import components.MailMenuBlock;
	import components.renderers.MailBlockListRenderer;
	import feathers.controls.List;
	import feathers.controls.Screen;
	import feathers.controls.ScrollBarDisplayMode;
	import feathers.controls.ScrollPolicy;
	import feathers.controls.renderers.IListItemRenderer;
	import feathers.data.ListCollection;
	import feathers.layout.HorizontalAlign;
	import feathers.layout.VerticalAlign;
	import feathers.layout.VerticalLayout;
	import starling.display.DisplayObject;
	import starling.events.Event;
	
	
	public class ScreenAllMails extends Screen {
		

		private var menu:MailMenuBlock;
		private var list:List;
		private var mailList:ListCollection;
		
		public function ScreenAllMails() {
			super();
			//this.title = "Screen C";
		}
		
		override protected function initialize():void {
			
			super.initialize();
			
			
			var layout:VerticalLayout = new VerticalLayout();
			layout.horizontalAlign = HorizontalAlign.CENTER;
			layout.verticalAlign = VerticalAlign.TOP;
			layout.gap = Settings._getIntByDPI(15);
			layout.paddingTop = Settings._getIntByDPI(150);
			layout.paddingBottom = Settings._getIntByDPI(130);
			this.layout = layout;
			
			
			
			var listLayout:VerticalLayout = new VerticalLayout();
			listLayout.verticalAlign = VerticalAlign.TOP;
			listLayout.horizontalAlign = HorizontalAlign.CENTER;
			
			
			list = new List();
			list.horizontalScrollPolicy = ScrollPolicy.OFF;
			list.verticalScrollPolicy = ScrollPolicy.AUTO;
			list.scrollBarDisplayMode = ScrollBarDisplayMode.NONE;
			//list.clipContent = false;
			list.width = stage.stageWidth;
			list.backgroundSkin = null;
			list.height = stage.stageHeight - Settings._getIntByDPI(330);
			this.addChild(list);
			list.validate();
			list.layout = listLayout;
			
			list.dataProvider = null;
			list.snapScrollPositionsToPixels = true;
			
			
			
			list.setItemRendererFactoryWithID(MailBlock.CHECK_TOPAY_MAIL,      CHECK_TOPAY_MAIL_itemFactory);
			list.setItemRendererFactoryWithID(MailBlock.COMPLETED_MAIL,        COMPLETED_MAIL_itemFactory);
			list.setItemRendererFactoryWithID(MailBlock.ENTER_GOODS_MAIL,      ENTER_GOODS_MAIL_itemFactory);
			list.setItemRendererFactoryWithID(MailBlock.PAY_MAIL,              PAY_MAIL_itemFactory);
			list.setItemRendererFactoryWithID(MailBlock.PAYED_MAIL,            PAYED_MAIL_itemFactory);
			list.setItemRendererFactoryWithID(MailBlock.UNKNOWN_MAIL,          UNKNOWN_MAIL_itemFactory);
			
			
			list.factoryIDFunction = function( item:Object,  index:int ):String {
				
				return item.status;
			};
			
			
			mailList = new ListCollection;
			list.dataProvider = mailList;
			
			var menuArr:Array = String(Settings._mui['mails_allmails_menu'][Settings._lang]).split(',');
			menu = new MailMenuBlock(menuArr);
			
			menu.addEventListener(AppEvent.CHANGE, menuChangeHandler);
			
			addChildAt(menu, 0);
			menu.validate();
			
			this.width = stage.stageWidth;
			this.height = stage.stageHeight;
			
			//this.validate();
		}
		
		private function menuChangeHandler(e:Event):void {
			
			mailList.removeAll();
			
			switch(e.data.selectedIndex) {
				case 0:
					
					mailList.addItem( { status: MailBlock.PAY_MAIL  } );
					mailList.addItem( { status: MailBlock.COMPLETED_MAIL  } );
					mailList.addItem( { status: MailBlock.COMPLETED_MAIL  } );
					mailList.addItem( { status: MailBlock.COMPLETED_MAIL  } );
					mailList.addItem( { status: MailBlock.COMPLETED_MAIL  } );
					mailList.addItem( { status: MailBlock.COMPLETED_MAIL  } );
					mailList.addItem( { status: MailBlock.COMPLETED_MAIL  } );
					mailList.addItem( { status: MailBlock.COMPLETED_MAIL  } );
					mailList.addItem( { status: MailBlock.COMPLETED_MAIL  } );
					mailList.addItem( { status: MailBlock.COMPLETED_MAIL  } );
					mailList.addItem( { status: MailBlock.COMPLETED_MAIL  } );
					mailList.addItem( { status: MailBlock.COMPLETED_MAIL  } );
					mailList.addItem( { status: MailBlock.COMPLETED_MAIL  } );
					mailList.addItem( { status: MailBlock.COMPLETED_MAIL  } );
					mailList.addItem( { status: MailBlock.COMPLETED_MAIL  } );
					
					break;
					
					
				case 1:
					
					mailList.addItem( { status: MailBlock.PAY_MAIL  } );
					mailList.addItem( { status: MailBlock.PAYED_MAIL  } );
					
					break;
					
					
				case 2:
					
					mailList.addItem( { status: MailBlock.CHECK_TOPAY_MAIL  } );
					mailList.addItem( { status: MailBlock.UNKNOWN_MAIL  } );
					
					break;
			}
		}
		
		
		private function CHECK_TOPAY_MAIL_itemFactory():IListItemRenderer {
			return itemFactory(MailBlock.CHECK_TOPAY_MAIL);
		}
		
		private function COMPLETED_MAIL_itemFactory():IListItemRenderer {
			return itemFactory(MailBlock.COMPLETED_MAIL);	
		}
		
		private function ENTER_GOODS_MAIL_itemFactory():IListItemRenderer{
			return itemFactory(MailBlock.ENTER_GOODS_MAIL);	
		}
		
		private function PAY_MAIL_itemFactory():IListItemRenderer {
			return itemFactory(MailBlock.PAY_MAIL);	
		}
		
		private function PAYED_MAIL_itemFactory():IListItemRenderer {
			return itemFactory(MailBlock.PAYED_MAIL);	
		}
		
		private function UNKNOWN_MAIL_itemFactory():IListItemRenderer {
			return itemFactory(MailBlock.UNKNOWN_MAIL);	
		}
		
		private function itemFactory(st:String):IListItemRenderer {
			var renderer:MailBlockListRenderer = new MailBlockListRenderer(st);
			renderer.padding = Settings._getIntByDPI(5);
			return renderer;	
		}
		
		private function disposeItemAccessory(item:Object):void {
			DisplayObject(itemFactory(item.status)).dispose();
		}
		
		override public function dispose():void {
			
			if (list) {
				list.dataProvider.dispose(disposeItemAccessory);
				StaticGUI._safeRemoveChildren(list, true);
			}
			
			
			
			
			menu.removeEventListener(AppEvent.CHANGE, menuChangeHandler);
			menu.dispose();
			list = null;
			mailList = null
			menu = null;
			super.dispose();
		}
	}
}