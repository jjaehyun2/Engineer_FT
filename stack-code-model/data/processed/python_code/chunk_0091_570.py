package components.renderers{
	import application.utils.StaticGUI;
	import components.MailBlock;
	import feathers.controls.GroupedList;
	import feathers.controls.Label;
	import feathers.controls.List;
	import feathers.controls.renderers.IGroupedListItemRenderer;
	import feathers.controls.renderers.IListItemRenderer;
	import feathers.core.FeathersControl;
	import feathers.layout.AnchorLayoutData;
	
	import starling.events.Event;
	
	public class MailBlockListRenderer extends FeathersControl implements IListItemRenderer {
		public function MailBlockListRenderer(st:String) {
			super();
			
			_state = st;
		}
		
		protected var _label:Label;
		protected var _blockIitem:MailBlock;
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
		
		override protected function initialize():void {
			
			super.initialize();
			
			if (!_blockIitem) {
				
				
				_blockIitem = new MailBlock(_state);
				this.width = stage.stageWidth - Settings._getIntByDPI(34);
				//_blockIitem.layoutData = new AnchorLayoutData(0, 0, 0, 0);
				this.addChild(this._blockIitem);
				_blockIitem.validate();

			}
		}
		
		override public function dispose():void {
			
			if (_blockIitem) _blockIitem = StaticGUI._safeRemoveChildren(_blockIitem, true);
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
			
			this._blockIitem.width = this.explicitWidth - 2 * this._padding;
			this._blockIitem.height = this.explicitHeight - 2 * this._padding;
			this._blockIitem.validate();
			
			var newWidth:Number = this.explicitWidth;
			if (needsWidth) {
				newWidth = this._blockIitem.width + 2 * this._padding;
			}
			var newHeight:Number = this.explicitHeight;
			if (needsHeight) {
				newHeight = this._blockIitem.height + 2 * this._padding;
			}
			
			return this.setSizeInternal(newWidth, newHeight, false);
		}
		
		protected function commitData():void {
			if (this._data) {
				//this._label.text = this._data.label;
				
				/*_blockIitem._addDataState(this._data.status);
				_blockIitem.validate();*/
				
			} else {
				
			}
		}
		
		protected function layoutChildren():void {
			this._blockIitem.x = this._padding;
			this._blockIitem.y = this._padding;
			this._blockIitem.width = this.actualWidth - 2 * this._padding;
			this._blockIitem.height = this.actualHeight - 2 * this._padding;
		}
	}
}