package io.decagames.rotmg.social.popups {
   import io.decagames.rotmg.social.model.FriendRequestVO;
   import io.decagames.rotmg.social.signals.FriendActionSignal;
   import io.decagames.rotmg.ui.buttons.BaseButton;
   import io.decagames.rotmg.ui.buttons.SliceScalingButton;
   import io.decagames.rotmg.ui.popups.modal.error.ErrorModal;
   import io.decagames.rotmg.ui.popups.signals.ClosePopupSignal;
   import io.decagames.rotmg.ui.popups.signals.RemoveLockFade;
   import io.decagames.rotmg.ui.popups.signals.ShowLockFade;
   import io.decagames.rotmg.ui.popups.signals.ShowPopupSignal;
   import io.decagames.rotmg.ui.texture.TextureParser;
   import kabam.rotmg.text.view.stringBuilder.LineBuilder;
   import robotlegs.bender.bundles.mvcs.Mediator;
   
   public class InviteFriendPopupMediator extends Mediator {
       
      
      [Inject]
      public var view:InviteFriendPopup;
      
      [Inject]
      public var closePopupSignal:ClosePopupSignal;
      
      [Inject]
      public var showFade:ShowLockFade;
      
      [Inject]
      public var friendsAction:FriendActionSignal;
      
      [Inject]
      public var removeFade:RemoveLockFade;
      
      [Inject]
      public var showPopup:ShowPopupSignal;
      
      private var closeButton:SliceScalingButton;
      
      public function InviteFriendPopupMediator() {
         super();
      }
      
      override public function initialize() : void {
         this.closeButton = new SliceScalingButton(TextureParser.instance.getSliceScalingBitmap("UI","close_button"));
         this.closeButton.clickSignal.addOnce(this.onClose);
         this.view.sendButton.clickSignal.add(this.onSendButtonClick);
         this.view.header.addButton(this.closeButton,"right_button");
      }
      
      override public function destroy() : void {
         this.view.sendButton.clickSignal.remove(this.onSendButtonClick);
      }
      
      private function onClose(param1:BaseButton) : void {
         this.closePopupSignal.dispatch(this.view);
      }
      
      private function onSendButtonClick(param1:BaseButton) : void {
         this.showFade.dispatch();
         var _loc2_:FriendRequestVO = new FriendRequestVO("/requestFriend",this.view.search.text,this.onSearchCallback);
         this.friendsAction.dispatch(_loc2_);
      }
      
      private function onSearchCallback(param1:Boolean, param2:Object, param3:String) : void {
         if(param1) {
            this.removeFade.dispatch();
            this.closePopupSignal.dispatch(this.view);
         } else {
            this.showPopup.dispatch(new ErrorModal(350,"Friends List Error",LineBuilder.getLocalizedStringFromKey(String(param2))));
            this.removeFade.dispatch();
         }
      }
   }
}