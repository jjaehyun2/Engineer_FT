package io.decagames.rotmg.pets.popup.info {
    import flash.display.Sprite;
    import flash.events.Event;
    
    import io.decagames.rotmg.ui.defaults.DefaultLabelFormat;
    import io.decagames.rotmg.ui.gird.UIGridElement;
    import io.decagames.rotmg.ui.labels.UILabel;
    import io.decagames.rotmg.ui.sliceScaling.SliceScalingBitmap;
    import io.decagames.rotmg.ui.texture.TextureParser;
    
    public class PetInfoItem extends UIGridElement {
        
        
        public function PetInfoItem(_arg_1: String) {
            super();
            this.titleText = _arg_1;
            this.init();
        }
        
        public var titleText: String;
        protected var hoverMask: Sprite;
        private var listBackground: SliceScalingBitmap;
        private var infoTitle: UILabel;
        
        public function get titel(): String {
            return this.titleText;
        }
        
        public function get background(): Sprite {
            return this.hoverMask;
        }
        
        private function init(): void {
            addEventListener("removedFromStage", this.onRemoved);
            this.listBackground = TextureParser.instance.getSliceScalingBitmap("UI", "listitem_content_background");
            addChild(this.listBackground);
            this.listBackground.height = 40;
            this.listBackground.width = 260;
            this.infoTitle = new UILabel();
            DefaultLabelFormat.petNameLabel(this.infoTitle, 0xffffff);
            addChild(this.infoTitle);
            this.infoTitle.text = this.titleText;
            this.infoTitle.y = 10;
            this.infoTitle.x = 15;
            this.hoverMask = new Sprite();
            this.hoverMask.graphics.beginFill(0xff0000, 0);
            this.hoverMask.graphics.drawRect(0, 0, this.listBackground.width, this.listBackground.height);
            this.hoverMask.graphics.endFill();
            addChild(this.hoverMask);
        }
        
        private function onRemoved(_arg_1: Event): void {
            removeEventListener("removedFromStage", this.onRemoved);
        }
    }
}