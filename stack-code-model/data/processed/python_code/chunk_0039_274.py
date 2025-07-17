/**
 * Created by ricardo_neves at bytesfromouterspace.com on 28/02/2015.
 */
package com.bytesfromouterspace.stockbrokers.event {
    import flash.events.Event;

    public class StockShareEvent extends Event {

        public static const STOCK_SHARE_SELL:String = "sellStockShare";
        public static const STOCK_SHARE_BUY:String = "buyStockShare";
        public static const STOCK_SHARE_CHANGED:String = "stockShareChanged";

        public function StockShareEvent(type:String, bubbles:Boolean = false, cancelable:Boolean = false) {
            super(type, bubbles, cancelable);

        }

        public override function clone():Event {
            return new StockShareEvent(type, bubbles, cancelable);
        }

        public override function toString():String {
            return formatToString("StockShareEvent", "type", "bubbles", "cancelable", "eventPhase");
        }

    }
}