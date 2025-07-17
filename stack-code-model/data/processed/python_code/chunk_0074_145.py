package screens {
	import application.AssetsLoader;
	import feathers.controls.Screen;
	import feathers.controls.TabBar;
	import feathers.controls.ToggleButton;
	import feathers.data.ListCollection;
	import feathers.layout.AnchorLayout;
	import feathers.layout.AnchorLayoutData;
	import starling.display.Image;
	import starling.display.Quad;
	import starling.events.Event;
	
	
	public class TopFooter extends Screen {
		
		public function TopFooter() {
			super();
		}
		
		public var _tabBar:TabBar;
		private var clickedBoo:Boolean;
		
		override protected function initialize():void {
			//never forget to call super.initialize()
			super.initialize();
			
			
			Settings._topFooter = this;
			
			this.layout = new AnchorLayout();
			
			var dataProvArr:Array = new Array;
			var dataProvObj:Object;
			var defaultIco:Image;
			var defaultSelectedIco:Image;
			
			
			for (var i:uint; i < 5; i++) {
				
				dataProvObj = new Object;
				dataProvObj.label = '';
				defaultIco = new Image(AssetsLoader._asset.getTexture('footer_item_' + (i + 1) + '_normal.png'));
				defaultIco.height = Settings._getIntByDPI(54);
				defaultIco.scaleX = defaultIco.scaleY;
				
				defaultSelectedIco = new Image(AssetsLoader._asset.getTexture('footer_item_' + (i + 1) + '_selected.png'));
				defaultSelectedIco.height = Settings._getIntByDPI(54);
				defaultSelectedIco.scaleX = defaultSelectedIco.scaleY;
				dataProvObj.defaultIcon = defaultIco;
				dataProvObj.defaultSelectedIcon = defaultSelectedIco;
				dataProvArr.push(dataProvObj);
				
			}
			
			_tabBar = new TabBar();
			_tabBar.styleProvider = null;
			_tabBar.tabFactory = function():ToggleButton{
				var tab:ToggleButton = new ToggleButton();
				tab.defaultSkin = new Quad(50,50,0x273447);

				return tab;
			}
			
			_tabBar.height = Settings._getIntByDPI(103);
			_tabBar.dataProvider = new ListCollection(dataProvArr);
											
			_tabBar.addEventListener(Event.CHANGE, tabBarHandler);
			_tabBar.addEventListener(Event.TRIGGERED, tabBarClickHandler);
			_tabBar.layoutData = new AnchorLayoutData(NaN, 0, 0, 0);
			_tabBar.styleProvider = null;
			addChild(_tabBar);
			_tabBar.validate();
			height = Settings._getIntByDPI(103);
			width = stage.stageWidth;
			
		}
		
		private function tabBarClickHandler(e:Event):void {
			clickedBoo = true;

		}
		
		private function tabBarHandler(event:Event):void {
			//this._label.text = "selectedIndex: " + this._tabBar.selectedIndex.toString();
			//trace("selectedIndex: " + tabBar.selectedIndex.toString());
			
			
			if (clickedBoo) {
				clickedBoo = false;
				switch(_tabBar.selectedIndex) {
					
					case 0:
						
						Settings._splash._navigator.pushScreen(ScreenID.MAIN_MAILS);
						
						break;
					case 1:
						
						Settings._splash._navigator.pushScreen(ScreenID.ALL_MAILS);
						
						break;
					case 2:
						
						Settings._splash._navigator.pushScreen(ScreenID.DECLARE_MAIL);
						
						break
					case 3:
						
						Settings._splash._navigator.pushScreen(ScreenID.MAPS_ADDRESS);
						
						break;
				}
			}	
		}
	}
}