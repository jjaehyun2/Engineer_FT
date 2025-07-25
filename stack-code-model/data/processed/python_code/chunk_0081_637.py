package io.decagames.rotmg.pets.popup.info {
    import io.decagames.rotmg.ui.buttons.BaseButton;
    import io.decagames.rotmg.ui.buttons.SliceScalingButton;
    import io.decagames.rotmg.ui.popups.signals.ClosePopupSignal;
    import io.decagames.rotmg.ui.texture.TextureParser;
    
    import robotlegs.bender.bundles.mvcs.Mediator;
    
    public class PetInfoDialogMediator extends Mediator {
        
        
        public function PetInfoDialogMediator() {
            super();
        }
        
        [Inject]
        public var view: PetInfoDialog;
        [Inject]
        public var closePopupSignal: ClosePopupSignal;
        private var closeButton: SliceScalingButton;
        
        override public function initialize(): void {
            this.closeButton = new SliceScalingButton(TextureParser.instance.getSliceScalingBitmap("UI", "close_button"));
            this.closeButton.clickSignal.addOnce(this.onClose);
            this.view.header.addButton(this.closeButton, "right_button");
            this.addInfo();
        }
        
        override public function destroy(): void {
            this.closeButton.clickSignal.remove(this.onClose);
            this.closeButton.dispose();
        }
        
        private function addInfo(): void {
            this.view.addInfoItem(new PetInfoItem("Pets"));
            this.view.addInfoItem(new PetInfoItem("Feeding"));
            this.view.addInfoItem(new PetInfoItem("Fusing"));
            this.view.addInfoItem(new PetInfoItem("Upgrade"));
            this.view.addInfoItem(new PetInfoItem("Wardrobe"));
        }
        
        private function onClose(_arg_1: BaseButton): void {
            this.closePopupSignal.dispatch(this.view);
        }
    }
}