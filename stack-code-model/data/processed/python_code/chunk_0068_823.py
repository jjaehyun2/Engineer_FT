package components {
	
	import application.AssetsLoader;
	import application.utils.StaticGUI;
	import feathers.controls.ButtonState;
	import feathers.controls.LayoutGroup;
	import feathers.controls.TabBar;
	import feathers.controls.ToggleButton;
	import feathers.controls.text.TextFieldTextRenderer;
	import feathers.core.ITextRenderer;
	import feathers.data.ListCollection;
	import feathers.layout.AnchorLayout;
	import feathers.layout.AnchorLayoutData;
	import feathers.layout.HorizontalAlign;
	import feathers.layout.VerticalAlign;
	import feathers.layout.VerticalLayout;
	import feathers.skins.ImageSkin;
	import flash.geom.Rectangle;
	import starling.display.Quad;
	import starling.events.Event;
	import starling.text.TextFormat;
	
	
	public class AddressMenuBlock extends LayoutGroup {
		
		private var tabStyle:TextFormat;
		private var tabSelectedStyle:TextFormat;
		private var tabDisabledStyle:TextFormat;
		
		private var tabBar:TabBar;
		
		private var menuArray:Array;
		
		public function AddressMenuBlock(menuArr:Array = null) {
			menuArray = menuArr
			super();
			//this.title = "Screen C";
		}
		
		override protected function initialize():void {
			
			var layout:AnchorLayout = new AnchorLayout();

			this.layout = layout;

			tabStyle = new TextFormat;
			tabStyle.font = '_bpgArialRegular';
			tabStyle.size = Settings._getIntByDPI(24);
			tabStyle.color = 0xb6b6b6;
			
			tabSelectedStyle = new TextFormat;
			tabSelectedStyle.font = '_bpgArialRegular';
			tabSelectedStyle.size = Settings._getIntByDPI(24);
			tabSelectedStyle.color = 0x575757;
			
			tabDisabledStyle = new TextFormat;
			tabDisabledStyle.font = '_bpgArialRegular';
			tabDisabledStyle.size = Settings._getIntByDPI(24);
			tabDisabledStyle.color = 0xabadad;

			
			var dataProvObj:Object;
			var dataProvArr:Array = new Array;
			
			for (var i:uint; i < menuArray.length; i++) {
				dataProvObj = new Object;
				dataProvObj.label = menuArray[i];
				dataProvArr.push(dataProvObj);
				
			}
			
			tabBar = new TabBar();
			
			tabBar.tabFactory = function():ToggleButton {
				
				
				var tab:ToggleButton = new ToggleButton();
				
				tab.labelFactory = function():ITextRenderer {
					var renderer:TextFieldTextRenderer = new TextFieldTextRenderer();
					renderer.embedFonts = true;
					return renderer;
				};
				tab.defaultSkin = new Quad(50, 50, 0xffffff);
				
				tab.fontStyles = tabStyle;
				tab.setFontStylesForState(ButtonState.DOWN_AND_SELECTED, tabSelectedStyle);
				tab.setFontStylesForState(ButtonState.HOVER_AND_SELECTED, tabSelectedStyle);
				tab.setFontStylesForState(ButtonState.UP_AND_SELECTED, tabSelectedStyle);
				tab.setFontStylesForState(ButtonState.DISABLED, tabDisabledStyle);
				
				return tab;
			}
			
			
			var selectionSkin:Quad = new Quad(int(stage.stageWidth / 2), Settings._getIntByDPI(3), 0x186c97);
			selectionSkin.y = Settings._getIntByDPI(86) - selectionSkin.height;
			tabBar.selectionSkin = selectionSkin;
			tabBar.dataProvider = new ListCollection(dataProvArr);
			
			tabBar.addEventListener(Event.CHANGE, tabBarHandler);
			tabBar.layoutData = new AnchorLayoutData(0, 0, 0, 0);
			tabBar.styleProvider = null;
			this.addChild(tabBar);
			tabBar.validate();
			this.width = stage.stageWidth
			this.height = Settings._getIntByDPI(86);
			tabBarHandler(null);
			
		}
		
		private function tabBarHandler(event:Event):void {
			//this._label.text = "selectedIndex: " + this._tabBar.selectedIndex.toString();
			this.dispatchEventWith(AppEvent.CHANGE, false, {selectedIndex:tabBar.selectedIndex } );
		}
		
		override public function dispose():void {
			
			//StaticGUI._safeRemoveChildren(this, true);
			if(tabBar){
				tabBar.removeEventListener(Event.CHANGE, tabBarHandler);
				tabBar.dispose();
			}
			tabDisabledStyle = null;
			tabSelectedStyle = null;
			tabStyle = null;
			menuArray = null;
			
			
			tabBar = null;
			super.dispose();
		}
	}
}