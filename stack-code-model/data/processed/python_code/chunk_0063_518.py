package kabam.rotmg.external.service {
import flash.external.ExternalInterface;

import kabam.rotmg.external.command.RequestPlayerCreditsSignal;

public class ExternalServiceHelper {

    public function ExternalServiceHelper() {
        super();
    }
    [Inject]
    public var requestPlayerCredits:RequestPlayerCreditsSignal;

    public function mapExternalCallbacks():void {
        if (ExternalInterface.available) {
            ExternalInterface.addCallback("updatePlayerCredits", this.updatePlayerCredits);
        }
    }

    private function updatePlayerCredits():void {
        this.requestPlayerCredits.dispatch();
    }
}
}