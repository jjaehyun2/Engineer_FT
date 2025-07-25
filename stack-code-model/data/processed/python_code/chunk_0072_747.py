package kabam.rotmg.account.core.services {
   import com.company.assembleegameclient.parameters.Parameters;
   import com.company.assembleegameclient.screens.CharacterSelectionAndNewsScreen;
   import com.company.util.MoreObjectUtil;
   import flash.events.MouseEvent;
   import flash.events.TimerEvent;
   import flash.utils.Timer;
   import io.decagames.rotmg.seasonalEvent.data.SeasonalEventModel;
   import io.decagames.rotmg.seasonalEvent.popups.SeasonalEventErrorPopup;
   import io.decagames.rotmg.ui.popups.signals.ClosePopupSignal;
   import io.decagames.rotmg.ui.popups.signals.ShowPopupSignal;
   import kabam.lib.tasks.BaseTask;
   import kabam.rotmg.account.core.Account;
   import kabam.rotmg.account.core.signals.CharListDataSignal;
   import kabam.rotmg.account.securityQuestions.data.SecurityQuestionsModel;
   import kabam.rotmg.account.web.WebAccount;
   import kabam.rotmg.account.web.view.MigrationDialog;
   import kabam.rotmg.account.web.view.WebLoginDialog;
   import kabam.rotmg.appengine.api.AppEngineClient;
   import kabam.rotmg.core.StaticInjectorContext;
   import kabam.rotmg.core.model.PlayerModel;
   import kabam.rotmg.core.signals.CharListLoadedSignal;
   import kabam.rotmg.core.signals.SetLoadingMessageSignal;
   import kabam.rotmg.core.signals.SetScreenWithValidDataSignal;
   import kabam.rotmg.dialogs.control.CloseDialogsSignal;
   import kabam.rotmg.dialogs.control.OpenDialogSignal;
   import robotlegs.bender.framework.api.ILogger;
   
   public class GetCharListTask extends BaseTask {
      
      private static const ONE_SECOND_IN_MS:int = 1000;
      
      private static const MAX_RETRIES:int = 7;

      
      [Inject]
      public var account:Account;
      
      [Inject]
      public var client:AppEngineClient;
      
      [Inject]
      public var setLoadingMessage:SetLoadingMessageSignal;
      
      [Inject]
      public var charListData:CharListDataSignal;
      
      [Inject]
      public var charListLoadedSignal:CharListLoadedSignal;
      
      [Inject]
      public var logger:ILogger;
      
      [Inject]
      public var openDialog:OpenDialogSignal;
      
      [Inject]
      public var securityQuestionsModel:SecurityQuestionsModel;
      
      private var requestData:Object;
      
      private var retryTimer:Timer;
      
      private var numRetries:int = 0;

      public function GetCharListTask() {
         super();
      }
      
      override protected function startTask() : void {
         this.logger.info("GetUserDataTask start");
         this.requestData = this.makeRequestData();
         this.sendRequest();
      }
      
      public function makeRequestData() : Object {
         var _loc1_:* = {};
         _loc1_.game_net_user_id = this.account.gameNetworkUserId();
         _loc1_.game_net = this.account.gameNetwork();
         _loc1_.play_platform = this.account.playPlatform();
         _loc1_.do_login = true;
         _loc1_.accessToken = this.account.getAccessToken();
         return _loc1_;
      }
      
      private function sendRequest() : void {
         this.client.complete.addOnce(this.onComplete);
         this.client.sendRequest("/char/list",this.requestData);
      }
      
      private function onComplete(param1:Boolean, param2:*) : void {
         completeTask(true);
         if(param1) {
            this.onListComplete(param2);
         } else {
            this.onTextError(param2);
         }
      }
      
      private function onListComplete(param1:String) : void {
         var _loc3_:* = null;
         var _loc2_:XML = new XML(param1);
         if("Account" in _loc2_) {
            this.account.creationDate = new Date(_loc2_.Account[0].CreationTimestamp * 1000);
            if("SecurityQuestions" in _loc2_.Account[0]) {
               this.securityQuestionsModel.showSecurityQuestionsOnStartup = !Parameters.data.skipPopups && !Parameters.ignoringSecurityQuestions && _loc2_.Account[0].SecurityQuestions[0].ShowSecurityQuestionsDialog[0] == "1";
               this.securityQuestionsModel.clearQuestionsList();
               for each(_loc3_ in _loc2_.Account[0].SecurityQuestions[0].SecurityQuestionsKeys[0].SecurityQuestionsKey) {
                  this.securityQuestionsModel.addSecurityQuestion(_loc3_.toString());
               }
            }
         }
         this.charListData.dispatch(_loc2_);
         this.charListLoadedSignal.dispatch();
         if(this.retryTimer != null) {
            this.stopRetryTimer();
         }
      }
      
      private function onTextError(param1:String) : void {
         if(this.numRetries < 7) {
            this.setLoadingMessage.dispatch("Loading.text");
         } else {
            this.setLoadingMessage.dispatch("error.loadError");
         }
         if (param1 == "Account credentials not valid") {
            this.clearAccountAndReloadCharacters();
         } else if(param1 == "Account is under maintenance") {
            this.setLoadingMessage.dispatch("This account has been banned");
            this.account.clear();
         } else {
            this.waitForASecondThenRetryRequest();
         }
      }
      
      private function clearAccountAndReloadCharacters() : void {
         this.logger.info("GetUserDataTask invalid credentials");
         this.account.clear();
         this.client.complete.addOnce(this.onComplete);
         this.requestData = this.makeRequestData();
         this.client.sendRequest("/char/list",this.requestData);
      }
      
      private function waitForASecondThenRetryRequest() : void {
         this.logger.info("GetUserDataTask error - retrying");
         this.retryTimer = new Timer(1000,1);
         this.retryTimer.addEventListener("timerComplete",this.onRetryTimer);
         this.retryTimer.start();
      }
      
      private function stopRetryTimer() : void {
         this.retryTimer.stop();
         this.retryTimer.removeEventListener("timerComplete",this.onRetryTimer);
         this.retryTimer = null;
      }

      private function onRetryTimer(param1:TimerEvent) : void {
         this.stopRetryTimer();
         if(this.numRetries < 7) {
            this.sendRequest();
            this.numRetries++;
         } else {
            this.clearAccountAndReloadCharacters();
            this.setLoadingMessage.dispatch("LoginError.tooManyFails");
         }
      }
   }
}