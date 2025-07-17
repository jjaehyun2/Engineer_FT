/**
 * Created by ricardo_neves at bytesfromouterspace.com on 28/02/2015.
 */
package com.bytesfromouterspace.stockbrokers.event {
    import flash.events.Event;

    public class ReputationEvent extends Event {

        public static const REPUTATION_EVENT:String = "reputationEvent";

        public var repType:uint;
        public var repAmount:int;

        public function ReputationEvent(repType:uint, repAmount:int = 0, bubbles:Boolean = false, cancelable:Boolean = false) {
            super(REPUTATION_EVENT, bubbles, cancelable);
            this.repType = repType;
            this.repAmount = repAmount;
        }

        public override function clone():Event {
            return new ReputationEvent(repType, repAmount, bubbles, cancelable);
        }

        public override function toString():String {
            return formatToString("ReputationEvent", "repType", "repAmount", "type", "bubbles", "cancelable", "eventPhase");
        }

    }
}