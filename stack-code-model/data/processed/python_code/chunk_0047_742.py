package components.renderers{
	import application.AssetsLoader;
	import application.utils.MyCanvas;
	import application.utils.StaticGUI;
	import components.MailBlock;
	import feathers.controls.Button;
	import feathers.controls.GroupedList;
	import feathers.controls.Label;
	import feathers.controls.LayoutGroup;
	import feathers.controls.List;
	import feathers.controls.renderers.IGroupedListItemRenderer;
	import feathers.controls.renderers.IListItemRenderer;
	import feathers.core.FeathersControl;
	import feathers.layout.AnchorLayout;
	import feathers.layout.AnchorLayoutData;
	import feathers.layout.HorizontalAlign;
	import feathers.layout.VerticalLayout;
	import feathers.utils.touch.TapToSelect;
	import feathers.utils.touch.TapToTrigger;
	import starling.display.Image;
	import starling.display.Quad;
	import starling.text.TextFormat;
	import starling.textures.TextureSmoothing;
	import starling.utils.Align;
	
	import starling.events.Event;
	
	public class MapAddressBlockListRenderer extends FeathersControl implements IListItemRenderer {
		public function MapAddressBlockListRenderer() {
			
			super();
			
			trigger = new TapToTrigger(this);
			select = new TapToSelect(this);

		}
		
		private var trigger:TapToTrigger;
		private var select:TapToSelect;
		
		
		protected var _state:String;
		
		protected var _index:int = -1;
		
		public function get index () : int {
			return this._index;
		};
		
		public function set index (value:int) : void {
			if (this._index == value) {
				return;
			}
			this._index = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}
		
		protected var _owner:List;
		
		public function get owner():List {
			return this._owner;
		}
		
		public function set owner(value:List):void {
			if (this._owner == value) {
				return;
			}
			this._owner = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}
		
		protected var _data:Object;
		
		public function get data():Object {
			return this._data;
		}
		
		public function set data(value:Object):void {
			if (this._data == value) {
				return;
			}
			this._data = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}
		
		protected var _factoryID:String;
		
		public function get factoryID():String {
			return this._factoryID;
		}
		
		public function set factoryID(value:String):void {
			this._factoryID = value;
		}
		
		protected var _isSelected:Boolean;
		
		public function get isSelected():Boolean {
			return this._isSelected;
		}
		
		public function set isSelected(value:Boolean):void {
			if (this._isSelected == value) {
				return;
			}
			this._isSelected = value;
			this.invalidate(INVALIDATION_FLAG_SELECTED);
			this.dispatchEventWith(Event.CHANGE);
		}
		
		protected var _padding:Number = 0;
		
		public function get padding():Number {
			return this._padding;
		}
		
		public function set padding(value:Number):void {
			if (this._padding == value) {
				return;
			}
			this._padding = value;
			this.invalidate(INVALIDATION_FLAG_LAYOUT);
		}
		
		
		protected var _conten:LayoutGroup;
		
		private var addressStyle:TextFormat;
		private var cityStyle:TextFormat;
		private var distStyle:TextFormat;
		
		private var line:MyCanvas;
		private var line2:MyCanvas;
		private var arrow:Image;
		
		protected var _labelAddress:Label;
		protected var _labelCity:Label;
		protected var _labelDistance:Label;
		
		override protected function initialize():void {
			
			super.initialize();
			
			addressStyle = new TextFormat;
			addressStyle.font = '_bpgArialRegular';
			addressStyle.size = Settings._getIntByDPI(24);
			addressStyle.color = 0x575757;
			
			cityStyle = new TextFormat;
			cityStyle.font = '_bpgArialRegular';
			cityStyle.size = Settings._getIntByDPI(24);
			cityStyle.color = 0x929394;
			
			distStyle = new TextFormat;
			distStyle.font = '_bpgArialRegular';
			distStyle.size = Settings._getIntByDPI(24);
			distStyle.horizontalAlign = HorizontalAlign.LEFT;
			distStyle.color = 0x186c97;
			
			if (!_conten) {
				
				var layout:AnchorLayout = new AnchorLayout();
				
				_conten = new LayoutGroup;
				_conten.backgroundSkin = new Quad(80, 80, 0xf3f5f7);
				_conten.height = Settings._getIntByDPI(150);
				_conten.width = stage.stageWidth;
				_conten.layout = layout;
				addChild(_conten);
			}
			
			var lineSize:uint = Settings._getIntByDPI(1);
			if (lineSize < 1) lineSize = 1;
			
			if (!line) {
				line = new MyCanvas;
				
				line.lineStyle(lineSize, 0xced6db);
				line.lineTo(0, 0);
				line.lineTo(stage.stageWidth, 0);
				line.endFill();
				line.y = int(_conten.height - line.height);
				_conten.addChild(line);
			}
			
			
			
			
			if (!arrow) {
				arrow = new Image(AssetsLoader._asset.getTexture("post_item_btn_arrow.png"));
				arrow.textureSmoothing = TextureSmoothing.TRILINEAR;
				arrow.width = Settings._getIntByDPI(11);
				arrow.x = stage.stageWidth - Settings._getIntByDPI(46);
				arrow.alignPivot(Align.LEFT, Align.CENTER);
				arrow.y = int(_conten.height) / 2;
				arrow.scaleY = arrow.scaleX;
				arrow.color = 0x4d4d4d;
				_conten.addChild(arrow);
			}
			
			if (!_labelAddress) {
				_labelAddress = StaticGUI._addLabel(_conten, "", addressStyle);
				_labelAddress.layoutData = new AnchorLayoutData(NaN, NaN, NaN, Settings._getIntByDPI(35), NaN, Settings._getIntByDPI( -15));
				
			}
			
			if (!_labelCity) {
				_labelCity = StaticGUI._addLabel(_conten, "", cityStyle);
				_labelCity.layoutData = new AnchorLayoutData(NaN, NaN, NaN, Settings._getIntByDPI(35), NaN, Settings._getIntByDPI( 15));
			}
			
			if (!_labelDistance) {
				_labelDistance = StaticGUI._addLabel(_conten, int(Math.random()*1588).toString()+" მ", distStyle);
				_labelDistance.layoutData = new AnchorLayoutData(NaN, Settings._getIntByDPI(135) - _labelDistance.width, NaN, NaN, NaN, Settings._getIntByDPI(0));
			}
			
			if (!line2) {
				line2 = new MyCanvas;
				
				line2.lineStyle(lineSize, 0xced6db);
				line2.lineTo(0, 0);
				line2.lineTo(0, Settings._getIntByDPI(23));
				line2.endFill();
				line2.y = int(_conten.height - line2.height) / 2;
				line2.x = stage.stageWidth - Settings._getIntByDPI(150);
				_conten.addChild(line2);
			}
			
		}
		
		override public function dispose():void {
			
			if (_labelAddress) StaticGUI._safeRemoveChildren(_labelAddress, true);
			if (_labelCity) StaticGUI._safeRemoveChildren(_labelCity, true);
			if (_labelDistance) StaticGUI._safeRemoveChildren(_labelDistance, true);
			
			if (line) line.dispose();
			if (line2) line2.dispose();
			
			super.dispose();
		}
		
		override protected function draw():void {
			var dataInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_DATA);
			
			if (dataInvalid) {
				this.commitData();
			}
			
			this.autoSizeIfNeeded();
			this.layoutChildren();
		}
		
		protected function autoSizeIfNeeded():Boolean {
			var needsWidth:Boolean = isNaN(this.explicitWidth);
			var needsHeight:Boolean = isNaN(this.explicitHeight);
			if (!needsWidth && !needsHeight) {
				return false;
			}
			
			this._conten.width = this.explicitWidth - 2 * this._padding;
			this._conten.height = this.explicitHeight - 2 * this._padding;
			this._conten.validate();
			
			var newWidth:Number = this.explicitWidth;
			if (needsWidth) {
				newWidth = this._conten.width + 2 * this._padding;
			}
			var newHeight:Number = this.explicitHeight;
			if (needsHeight) {
				newHeight = this._conten.height + 2 * this._padding;
			}
			
			return this.setSizeInternal(newWidth, newHeight, false);
		}
		
		protected function commitData():void {
			if (this._data) {
				
				_labelAddress.text = this._data.address;
				_labelCity.text = this._data.city;
				//this._label.text = this._data.label;
				
				/*_blockIitem._addDataState(this._data.status);
				_blockIitem.validate();*/
				
			} else {
				
			}
		}
		
		protected function layoutChildren():void {
			this._conten.x = this._padding;
			this._conten.y = this._padding;
			this._conten.width = this.actualWidth - 2 * this._padding;
			this._conten.height = this.actualHeight - 2 * this._padding;
		}
	}
}