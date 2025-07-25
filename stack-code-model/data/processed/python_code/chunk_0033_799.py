package io.decagames.rotmg.social.tasks {
import kabam.lib.tasks.BaseTask;
import kabam.rotmg.account.core.Account;
import kabam.rotmg.appengine.api.AppEngineClient;

public class GuildDataRequestTask extends BaseTask implements ISocialTask {

    public function GuildDataRequestTask() {
        super();
    }
    [Inject]
    public var client:AppEngineClient;
    [Inject]
    public var account:Account;

    private var _requestURL:String;

    public function get requestURL():String {
        return this._requestURL;
    }

    public function set requestURL(param1:String):void {
        this._requestURL = param1;
    }

    private var _xml:XML;

    public function get xml():XML {
        return this._xml;
    }

    public function set xml(param1:XML):void {
        this._xml = param1;
    }

    override protected function startTask():void {
        this.client.setMaxRetries(8);
        this.client.complete.addOnce(this.onComplete);
        var _loc1_:Object = {};
        _loc1_.accessToken = this.account.getAccessToken();
        _loc1_.targetName = "";
        _loc1_.accessToken = this.account.getAccessToken();
        _loc1_.game_net_user_id = this.account.gameNetworkUserId();
        _loc1_.game_net = this.account.gameNetwork();
        _loc1_.play_platform = this.account.playPlatform();
        this.client.sendRequest(this._requestURL, _loc1_);
    }

    private function onComplete(param1:Boolean, param2:*):void {
        if (param1) {
            this._xml = new XML(param2);
            completeTask(true);
        } else {
            completeTask(false, param2);
        }
    }
}
}