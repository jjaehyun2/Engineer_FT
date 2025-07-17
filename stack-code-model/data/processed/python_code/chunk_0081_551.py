/**
 * Created by Akira on 02/03/2015.
 */
package com.bytesfromouterspace.stockbrokers.controller {

    import com.bytesfromouterspace.stockbrokers.event.KingpinEvent;
    import com.bytesfromouterspace.stockbrokers.event.ReputationStatusEvent;
    import com.bytesfromouterspace.stockbrokers.model.InvestorsModel;
    import com.bytesfromouterspace.stockbrokers.model.KingpinModel;

    public class InvestorsController {

        private var model:InvestorsModel;
        public var kingpinControllers:Vector.<KingpinController>;

        public function InvestorsController(model:InvestorsModel) {
            this.model = model;
            kingpinControllers = new Vector.<KingpinController>(model.kingpins.length, true);
            for(var i:int = 0; i < kingpinControllers.length; i++) {
                kingpinControllers[i] = new KingpinController(model.kingpins[i]);
                model.kingpins[i].addEventListener(KingpinEvent.LOAN_ACCEPT, onAcceptLoan);
                model.kingpins[i].addEventListener(KingpinEvent.LOAN_PAY, onPayLoan);
            }
        }

        private function onPayLoan(event:KingpinEvent):void {
            model.payLoan(event.target as KingpinModel);
        }

        private function onAcceptLoan(event:KingpinEvent):void {
            model.acceptedLoan(event.target as KingpinModel);
        }

        public function handleLevelChange(event:ReputationStatusEvent):void {
            for(var i:int = 0; i < kingpinControllers.length; i++) {
                kingpinControllers[i].onLevelChanged(event.level);
            }
        }

        public function getLoanedInterestRates():Number {
            return model.responsabilitiesRates * -1;
        }
    }
}