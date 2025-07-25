package kabam.rotmg.account.web.services {
import kabam.lib.tasks.BaseTask;
import kabam.rotmg.account.core.Account;
import kabam.rotmg.account.core.services.ChangePasswordTask;
import kabam.rotmg.account.web.model.ChangePasswordData;
import kabam.rotmg.appengine.api.AppEngineClient;

public class WebChangePasswordTask extends BaseTask implements ChangePasswordTask {


    public function WebChangePasswordTask() {
        super();
    }
    [Inject]
    public var account:Account;
    [Inject]
    public var data:ChangePasswordData;
    [Inject]
    public var client:AppEngineClient;

    override protected function startTask():void {
        this.client.complete.addOnce(this.onComplete);
        this.client.sendRequest("/account/changePassword", this.makeDataPacket());
    }

    private function onComplete(_arg_1:Boolean, _arg_2:*):void {
        _arg_1 && this.onChangeDone();
        completeTask(_arg_1, _arg_2);
    }

    private function makeDataPacket():Object {
        var _local1:* = {};
        _local1.guid = this.account.getUserId();
        _local1.password = this.data.currentPassword;
        _local1.newPassword = this.data.newPassword;
        return _local1;
    }

    private function onChangeDone():void {
        this.account.updateUser(this.account.getUserId(), this.data.newPassword, this.account.getToken(), this.account.getSecret());
        completeTask(true);
    }
}
}