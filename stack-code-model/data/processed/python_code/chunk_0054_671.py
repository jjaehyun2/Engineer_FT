package drawer.views {
	import application.AssetsLoader;
	import application.utils.DeviceInfo;
	import application.utils.MyCanvas;
	import application.utils.StaticGUI;
	import feathers.controls.Check;
	import feathers.controls.Label;
	import feathers.controls.LayoutGroup;
	import feathers.controls.ScrollContainer;
	import feathers.controls.text.TextFieldTextRenderer;
	import feathers.core.ITextRenderer;
	import feathers.layout.FlowLayout;
	import feathers.layout.ILayout;
	import feathers.layout.VerticalAlign;
	import feathers.layout.VerticalLayout;
	import feathers.skins.IStyleProvider;
	import feathers.skins.ImageSkin;
	import feathers.controls.Button;
	import starling.display.Image;
	import starling.display.Quad;
	import starling.text.TextFormat;
	import starling.textures.TextureSmoothing;
	
	import starling.events.Event;
	
	public class DrawerView extends ScrollContainer {
		
		public static const CHANGE_DOCK_MODE_TO_NONE:String = "changeDockModeToNone";
		public static const CHANGE_DOCK_MODE_TO_BOTH:String = "changeDockModeToBoth";
		
		public function DrawerView() {
			super();
			
		}
		
		private var _titleLabel:Label;
		private var _dockCheck:Check;
		
		private var btnStyle1:TextFormat;
		private var btnStyle2:TextFormat;
		private var labelStyle1:TextFormat;
		private var labelStyle2:TextFormat;
		private var lariStyle:TextFormat;
		private var line:MyCanvas;
		private var titleLabel:Label;
		private var fillBalanceBtn:Button;
		private var menuList:Vector.<Button>;
		
		
		override protected function initialize():void {
			//never forget to call super.initialize()
			super.initialize();
			
			
			var layout:VerticalLayout = new VerticalLayout();
			//layout.horizontalAlign = HorizontalAlign.CENTER;
			//layout.verticalAlign = VerticalAlign.MIDDLE;
			
			layout.paddingTop = Settings._getIntByDPI(107);
			layout.paddingLeft = Settings._getIntByDPI(45);
			layout.gap = Settings._getIntByDPI(50);
			
			this.layout = layout;
			
			
			btnStyle1 = new TextFormat;
			btnStyle1.font = '_bpgArialRegular';
			btnStyle1.size = Settings._getIntByDPI(30);
			btnStyle1.color = 0xffffff;
			
			btnStyle2 = new TextFormat;
			btnStyle2.font = '_bpgArialRegular';
			btnStyle2.size = Settings._getIntByDPI(20);
			btnStyle2.color = 0xffffff;
			
			labelStyle1 = new TextFormat;
			labelStyle1.font = '_bpgArialRegular';
			labelStyle1.size = Settings._getIntByDPI(20);
			labelStyle1.color = 0xa6a7a8;
			
			labelStyle2 = new TextFormat;
			labelStyle2.font = '_bpgArialRegular';
			labelStyle2.size = Settings._getIntByDPI(50);
			labelStyle2.color = 0xffffff;
			
			lariStyle = new TextFormat;
			lariStyle.font = '_lariSymbol';
			lariStyle.size = Settings._getIntByDPI(30);
			lariStyle.color = 0xffffff;
			
			var btn:Button;
			
			
			var menuGroup:LayoutGroup = new LayoutGroup();
			var menuGroupLayout:VerticalLayout = new VerticalLayout();
			menuGroupLayout.gap = Settings._getIntByDPI(0);
			menuGroupLayout.paddingLeft = Settings._getIntByDPI(-15);
			menuGroup.layout = menuGroupLayout;
			this.addChild( menuGroup );
			
			menuList = new Vector.<Button>;
			
			for (var i:uint; i < 6; i++ ) {
				
				btn = StaticGUI._addBtnSkin(menuGroup, Settings._mui['drawer_menu_item_' + i][Settings._lang],  btnStyle1, null);
				btn.addEventListener(Event.TRIGGERED, menuHandler);
				menuList.push(btn);
			}
			
			
			line = new MyCanvas;
			addChild(line);
			line.lineStyle(2, 0x66696a);
			line.lineTo(0, 0);
			line.lineTo(Settings._getIntByDPI(400), 0);
			
			
			var sectorTwoGroup:LayoutGroup = new LayoutGroup();
			var sectorTwoGroupLayout:VerticalLayout = new VerticalLayout();
			sectorTwoGroupLayout.gap = Settings._getIntByDPI(30);
			sectorTwoGroup.layout = sectorTwoGroupLayout;
			this.addChild( sectorTwoGroup );
			
			var label1Group:LayoutGroup = new LayoutGroup();
			var label1GroupLayout:VerticalLayout = new VerticalLayout();
			label1GroupLayout.gap = 5;
			label1Group.layout = label1GroupLayout;
			sectorTwoGroup.addChild( label1Group );
			
			titleLabel = StaticGUI._addLabel(label1Group, Settings._mui['drawer_title_1'][Settings._lang], labelStyle1);
			titleLabel = StaticGUI._addLabel(label1Group, 'ზვიად Ziziguri დიდი царица', btnStyle1);
			
			
			var label2Group:LayoutGroup = new LayoutGroup();
			label2Group.width = Settings._getIntByDPI(350);
			var label2GroupLayout:FlowLayout = new FlowLayout();
			//label2GroupLayout.rowVerticalAlign = VerticalAlign.BOTTOM;
			label2GroupLayout.firstHorizontalGap = Settings._getIntByDPI(350);
			label2GroupLayout.gap = 5;
			label2Group.layout = label2GroupLayout;
			sectorTwoGroup.addChild(label2Group);
			
			titleLabel = StaticGUI._addLabel(label2Group, Settings._mui['drawer_title_2'][Settings._lang], labelStyle1);
			titleLabel = StaticGUI._addLabel(label2Group, '33.54', labelStyle2);
			

			var lariSimGroup:LayoutGroup = new LayoutGroup();
			var lariSimGroupLayout:VerticalLayout = new VerticalLayout();
			lariSimGroupLayout.paddingTop = Settings._getIntByDPI(23);
			
			lariSimGroup.layout = lariSimGroupLayout;
			label2Group.addChild(lariSimGroup);
			
			//titleLabel = StaticGUI._addLabel(lariSimGroup, 's', lariStyle);
			var lariImg:Image = new Image(AssetsLoader._asset.getTexture("lari_simb.png"));
			//lariImg.textureSmoothing = TextureSmoothing.TRILINEAR;
			lariImg.width = Settings._getIntByDPI(22);
			lariImg.scaleY = lariImg.scaleX;
			lariSimGroup.addChild(lariImg);
			
			
			var fillSkin:ImageSkin = new ImageSkin(AssetsLoader._asset.getTexture("drawer_fill_balance_btn.png"));
			fillSkin.scale9Grid = StaticGUI._getScale9GridRect(fillSkin.width, fillSkin.height);
			
			fillBalanceBtn = StaticGUI._addBtnSkin(sectorTwoGroup, Settings._mui['drawer_balance_btn'][Settings._lang], btnStyle2, fillSkin);
			fillBalanceBtn.width = Settings._getIntByDPI(265);
			fillBalanceBtn.height = Settings._getIntByDPI(68)
			
			line = new MyCanvas;
			addChild(line);
			line.lineStyle(2, 0x66696a);
			line.lineTo(0, 0);
			line.lineTo(Settings._getIntByDPI(400), 0);
			
			this.height = stage.stageHeight - Settings._getIntByDPI(100);
			
			
		}
		
		private function menuHandler(e:Event):void {
			
		}
		
		override public function dispose():void {
			
			for (var i:uint; i < menuList.length; i++ ) {
				
				menuList[i].removeEventListener(Event.TRIGGERED, menuHandler);
				
			}
			menuList = null;
			this.removeChildren();
			super.dispose();
			
		}
		
		private function addBtnSkin(cont:*, fStyle:TextFormat, bSkin:ImageSkin ,btn:Button):Button {
			btn.fontStyles = fStyle;
			
			btn.labelFactory = function():ITextRenderer {
				var renderer:TextFieldTextRenderer = new TextFieldTextRenderer();
				renderer.embedFonts = true;
				//renderer.textFormat = btnStyle
				return renderer;
			}
			btn.defaultSkin = bSkin;
			cont.addChild(btn);
			btn.validate();
			return btn;
		}
	}
}