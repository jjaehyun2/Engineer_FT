package io.decagames.rotmg.pets.popup.hatching {
   import io.decagames.rotmg.ui.buttons.BaseButton;
   import io.decagames.rotmg.ui.buttons.SliceScalingButton;
   import io.decagames.rotmg.ui.popups.signals.ClosePopupSignal;
   import io.decagames.rotmg.ui.texture.TextureParser;
   import robotlegs.bender.bundles.mvcs.Mediator;
   
   public class PetHatchingDialogMediator extends Mediator {
       
      
      [Inject]
      public var view:PetHatchingDialog;
      
      [Inject]
      public var closePopupSignal:ClosePopupSignal;
      
      private var closeButton:SliceScalingButton;
      
      public function PetHatchingDialogMediator() {
         super();
      }
      
      override public function initialize() : void {
         this.closeButton = new SliceScalingButton(TextureParser.instance.getSliceScalingBitmap("UI","close_button"));
         this.closeButton.clickSignal.addOnce(this.onClose);
         this.view.header.addButton(this.closeButton,"right_button");
         this.view.okButton.clickSignal.addOnce(this.onClose);
      }
      
      override public function destroy() : void {
         this.closeButton.clickSignal.remove(this.onClose);
         this.closeButton.dispose();
         this.view.okButton.clickSignal.remove(this.onClose);
      }
      
      private function onClose(param1:BaseButton) : void {
         this.closePopupSignal.dispatch(this.view);
      }
   }
}