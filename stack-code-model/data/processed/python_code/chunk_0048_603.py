/**
 * Created by Akira on 02/03/2015.
 */
package com.bytesfromouterspace.stockbrokers.event {
    import flash.events.Event;

    public class BonusEvent extends Event {

        public static const BONUS_EVENT:String = "bonusEvent";
        public var bonusCategory:uint;

        public function BonusEvent(bonusCategory:uint,  bubbles:Boolean = false, cancelable:Boolean = false) {
            super(BONUS_EVENT, bubbles, cancelable);
            this.bonusCategory = bonusCategory;
        }

        public override function clone():Event {
            return new BonusEvent(bonusCategory, bubbles, cancelable);
        }

        public override function toString():String {
            return formatToString("BonusEvent", "type", "bonusCategory", "bubbles", "cancelable", "eventPhase");
        }

    }
}