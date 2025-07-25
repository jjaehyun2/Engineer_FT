package io.decagames.rotmg.ui.popups.header {
    import flash.display.Sprite;
    
    import io.decagames.rotmg.ui.buttons.SliceScalingButton;
    import io.decagames.rotmg.ui.labels.UILabel;
    import io.decagames.rotmg.ui.sliceScaling.SliceScalingBitmap;
    import io.decagames.rotmg.ui.texture.TextureParser;
    
    public class PopupHeader extends Sprite {
        
        public static const LEFT_BUTTON: String = "left_button";
        
        public static const RIGHT_BUTTON: String = "right_button";
        
        public static var TYPE_FULL: String = "full";
        
        public static var TYPE_MODAL: String = "modal";
        
        public function PopupHeader(_arg_1: int, _arg_2: String) {
            super();
            this.headerWidth = _arg_1;
            this.headerType = _arg_2;
            if (_arg_2 == TYPE_FULL) {
                this.backgroundBitmap = TextureParser.instance.getSliceScalingBitmap("UI", "popup_header", _arg_1);
                addChild(this.backgroundBitmap);
            }
            this.buttonsContainers = new Vector.<Sprite>();
            this.buttons = new Vector.<SliceScalingButton>();
        }
        
        private var backgroundBitmap: SliceScalingBitmap;
        private var titleBackgroundBitmap: SliceScalingBitmap;
        private var buttonsContainers: Vector.<Sprite>;
        private var buttons: Vector.<SliceScalingButton>;
        private var headerWidth: int;
        private var headerType: String;
        
        private var _titleLabel: UILabel;
        
        public function get titleLabel(): UILabel {
            return this._titleLabel;
        }
        
        private var _coinsField: CoinsField;
        
        public function get coinsField(): CoinsField {
            return this._coinsField;
        }
        
        private var _fameField: FameField;
        
        public function get fameField(): FameField {
            return this._fameField;
        }
        
        public function setTitle(_arg_1: String, _arg_2: int, _arg_3: Function = null): void {
            if (!this.titleBackgroundBitmap) {
                if (this.headerType == TYPE_FULL) {
                    this.titleBackgroundBitmap = TextureParser.instance.getSliceScalingBitmap("UI", "popup_header_title", _arg_2);
                    addChild(this.titleBackgroundBitmap);
                    this.titleBackgroundBitmap.x = Math.round((this.headerWidth - _arg_2) / 2);
                    this.titleBackgroundBitmap.y = 29;
                } else {
                    this.titleBackgroundBitmap = TextureParser.instance.getSliceScalingBitmap("UI", "modal_header_title", _arg_2);
                    addChild(this.titleBackgroundBitmap);
                    this.titleBackgroundBitmap.x = Math.round((this.headerWidth - _arg_2) / 2);
                }
                this._titleLabel = new UILabel();
                if (_arg_3 != null) {
                    _arg_3(this._titleLabel);
                }
                this._titleLabel.text = _arg_1;
                addChild(this._titleLabel);
                this._titleLabel.x = this.titleBackgroundBitmap.x + (this.titleBackgroundBitmap.width - this._titleLabel.textWidth) / 2;
                if (this.headerType == TYPE_FULL) {
                    this._titleLabel.y = this.titleBackgroundBitmap.height - this._titleLabel.height / 2 - 3;
                } else {
                    this._titleLabel.y = this.titleBackgroundBitmap.y + (this.titleBackgroundBitmap.height - this._titleLabel.height) / 2;
                }
            }
        }
        
        public function addButton(_arg_1: SliceScalingButton, _arg_2: String): void {
            var _local3: * = null;
            var _local4: Sprite = new Sprite();
            if (this.headerType == TYPE_FULL) {
                _local3 = TextureParser.instance.getSliceScalingBitmap("UI", "popup_header_button_decor");
                _local4.addChild(_local3);
            }
            _local4.addChild(_arg_1);
            addChild(_local4);
            this.buttonsContainers.push(_local4);
            this.buttons.push(_arg_1);
            if (this.headerType == TYPE_FULL) {
                _local3.y = (this.backgroundBitmap.height - _local3.height) / 2;
                _arg_1.y = _local3.y + 8;
            } else {
                _arg_1.y = 5;
            }
            if (_arg_2 == "right_button") {
                if (this.headerType == TYPE_FULL) {
                    _local3.x = this.headerWidth - _local3.width;
                    _arg_1.x = _local3.x + 6;
                } else {
                    _arg_1.x = this.titleBackgroundBitmap.x + this.titleBackgroundBitmap.width - _arg_1.width - 3;
                }
            } else if (this.headerType == TYPE_FULL) {
                _local3.x = _local3.width;
                _local3.scaleX = -1;
                _arg_1.x = 16;
            } else {
                _arg_1.x = this.titleBackgroundBitmap.x + 3;
            }
        }
        
        public function showCoins(_arg_1: int): CoinsField {
            var _local2: * = null;
            this._coinsField = new CoinsField(_arg_1);
            this._coinsField.x = 44;
            addChild(this._coinsField);
            this.alignCurrency();
            var _local4: int = 0;
            var _local3: * = this.buttonsContainers;
            for each(_local2 in this.buttonsContainers) {
                addChild(_local2);
            }
            return this._coinsField;
        }
        
        public function showFame(_arg_1: int): FameField {
            this._fameField = new FameField(_arg_1);
            this._fameField.x = 44;
            addChild(this._fameField);
            this.alignCurrency();
            return this._fameField;
        }
        
        public function dispose(): void {
            var _local1: * = null;
            if (this.backgroundBitmap) {
                this.backgroundBitmap.dispose();
            }
            this.titleBackgroundBitmap.dispose();
            if (this._coinsField) {
                this._coinsField.dispose();
            }
            if (this._fameField) {
                this._fameField.dispose();
            }
            var _local3: int = 0;
            var _local2: * = this.buttons;
            for each(_local1 in this.buttons) {
                _local1.dispose();
            }
            this.buttonsContainers = null;
            this.buttons = null;
        }
        
        private function alignCurrency(): void {
            if (this._coinsField && this._fameField) {
                this._coinsField.y = 39;
                this._fameField.y = 63;
            } else if (this._coinsField) {
                this._coinsField.y = 51;
            } else if (this._fameField) {
                this._fameField.y = 51;
            }
        }
    }
}