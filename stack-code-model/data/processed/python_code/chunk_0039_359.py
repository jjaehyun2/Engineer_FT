package kabam.rotmg.account.core.services {
   import com.company.util.MoreObjectUtil;
   import kabam.lib.tasks.BaseTask;
   import kabam.rotmg.account.core.Account;
   import kabam.rotmg.appengine.api.AppEngineClient;
   
   public class ListPowerUpStatsTask extends BaseTask {
       
      
      [Inject]
      public var account:Account;
      
      [Inject]
      public var client:AppEngineClient;
      
      private var requestData:Object;
      
      public function ListPowerUpStatsTask() {
         super();
      }
      
      override protected function startTask() : void {
         this.requestData = this.makeRequestData();
         this.sendRequest();
      }
      
      public function makeRequestData() : Object {
         var _loc1_:* = {};
         MoreObjectUtil.addToObject(_loc1_,this.account.getCredentials());
         MoreObjectUtil.addToObject(_loc1_,this.account.getCredentials());
         _loc1_.game_net_user_id = this.account.gameNetworkUserId();
         _loc1_.game_net = this.account.gameNetwork();
         _loc1_.play_platform = this.account.playPlatform();
         return _loc1_;
      }
      
      private function sendRequest() : void {
         this.client.complete.addOnce(this.onComplete);
         this.client.sendRequest("/account/listPowerUpStats",this.requestData);
      }
      
      private function onComplete(param1:Boolean, param2:*) : void {
         completeTask(true);
      }
   }
}