/**
 * Created by Akira on 02/03/2015.
 */
package com.bytesfromouterspace.stockbrokers.model {
    import com.bytesfromouterspace.stockbrokers.event.KingpinEvent;

    import flash.events.Event;

    [Event(name="change", type="com.bytesfromouterspace.stockbrokers.event.KingpinEvent")]
    [Event(name="loadAccept", type="com.bytesfromouterspace.stockbrokers.event.KingpinEvent")]
    [Event(name="loadPay", type="com.bytesfromouterspace.stockbrokers.event.KingpinEvent")]
    public class KingpinModel extends BaseModel{

        public var id:int;
        public var minLevel:int;
        public var rate:Number;
        private var _accepted:Boolean;
        public var amount:int;
        private var _enabled:Boolean;
        private var _paid:Boolean;


        public function KingpinModel(id:int, minLevel:int, rate:Number, amount:int) {
            super();
            this.id = id;
            this.minLevel = minLevel;
            this.rate = rate;
            this.amount = amount;
            _enabled = false;
            _accepted = false;
            _paid = false;
        }

        public function get accepted():Boolean {
            return _accepted;
        }

        public function set accepted(value:Boolean):void {
            _accepted = value;
            dispatchEvent(new KingpinEvent(KingpinEvent.CHANGE));
            if(value) {
                dispatchEvent(new KingpinEvent(KingpinEvent.LOAN_ACCEPT));
            }
        }

        public function get enabled():Boolean {
            return _enabled;
        }

        public function set enabled(value:Boolean):void {
            _enabled = value;
            dispatchEvent(new KingpinEvent(KingpinEvent.CHANGE));
        }

        public function get paid():Boolean {
            return _paid;
        }

        public function set paid(value:Boolean):void {
            _paid = value;
            dispatchEvent(new KingpinEvent(KingpinEvent.CHANGE));
            if(value) {
                dispatchEvent(new KingpinEvent(KingpinEvent.LOAN_PAY));
            }
        }

        public function requestLoanPay():void {
            dispatchEvent(new KingpinEvent(KingpinEvent.LOAN_PAY));
        }

        public function get interestRateValue():Number {
            if(_accepted && !_paid) {
                return amount * rate;
            }
            return 0;
        }

        public function get capitalDue():Number {
            if(_accepted && !_paid) {
                return amount * rate + amount;
            }
            return 0;
        }

    }
}