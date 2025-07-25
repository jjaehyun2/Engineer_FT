package io.decagames.rotmg.shop.mysteryBox.contentPopup {
    import com.company.assembleegameclient.objects.ObjectLibrary;
    
    import flash.display.Bitmap;
    import flash.display.BitmapData;
    import flash.filters.DropShadowFilter;
    import flash.text.TextFormat;
    
    import io.decagames.rotmg.ui.gird.UIGridElement;
    import io.decagames.rotmg.ui.labels.UILabel;
    
    import kabam.rotmg.text.model.FontModel;
    
    public class UIItemContainer extends UIGridElement {
        
        
        public function UIItemContainer(_arg_1: int, _arg_2: uint, _arg_3: Number = 0, _arg_4: int = 40) {
            super();
            this._itemId = _arg_1;
            this.size = _arg_4;
            this.background = _arg_2;
            this.backgroundAlpha = _arg_3;
            this.graphics.clear();
            this.graphics.beginFill(_arg_2, _arg_3);
            this.graphics.drawRect(0, 0, _arg_4, _arg_4);
            this.graphics.endFill();
            var _local5: BitmapData = ObjectLibrary.getRedrawnTextureFromType(_arg_1, _arg_4 * 2, true, false);
            this._imageBitmap = new Bitmap(_local5);
            this._imageBitmap.x = -Math.round((this._imageBitmap.width - _arg_4) / 2);
            this._imageBitmap.y = -Math.round((this._imageBitmap.height - _arg_4) / 2);
            this.addChild(this._imageBitmap);
        }
        
        private var size: int;
        private var background: uint;
        private var backgroundAlpha: Number;
        
        override public function get width(): Number {
            return this.size;
        }
        
        override public function get height(): Number {
            return this.size;
        }
        
        private var _itemId: int;
        
        public function get itemId(): int {
            return this._itemId;
        }
        
        private var _imageBitmap: Bitmap;
        
        public function get imageBitmap(): Bitmap {
            return this._imageBitmap;
        }
        
        private var _quantity: int = 1;
        
        public function get quantity(): int {
            return this._quantity;
        }
        
        private var _showTooltip: Boolean;
        
        public function get showTooltip(): Boolean {
            return this._showTooltip;
        }
        
        public function set showTooltip(_arg_1: Boolean): void {
            this._showTooltip = _arg_1;
        }
        
        override public function dispose(): void {
            this._imageBitmap.bitmapData.dispose();
            super.dispose();
        }
        
        public function showQuantityLabel(_arg_1: int): void {
            var _local2: * = null;
            this._quantity = _arg_1;
            _local2 = new UILabel();
            var _local3: TextFormat = new TextFormat();
            _local3.color = 0xffffff;
            _local3.bold = true;
            _local3.font = FontModel.DEFAULT_FONT_NAME;
            _local3.size = this.size * 0.35;
            _local2.defaultTextFormat = _local3;
            _local2.text = _arg_1 + "x";
            _local2.y = this.size - _local2.textHeight - this.size * 0.1;
            _local2.x = this.size - _local2.textWidth - this.size * 0.1;
            _local2.filters = [new DropShadowFilter(1, 90, 0, 0.5, 4, 4)];
            addChild(_local2);
        }
        
        public function clone(): UIItemContainer {
            var _local1: UIItemContainer = new UIItemContainer(this._itemId, this.background, this.backgroundAlpha, this.size);
            if (this._quantity > 1) {
                _local1.showQuantityLabel(this._quantity);
            }
            return _local1;
        }
    }
}