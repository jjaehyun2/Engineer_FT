/**
 * Created by ricardo_neves at bytesfromouterspace.com on 28/02/2015.
 */
package com.bytesfromouterspace.stockbrokers.ui.events {
    import flash.events.Event;

    public class UIEvent extends Event {

        public static const UI_CHANGED:String = "uiChanged";

        public function UIEvent(type:String, bubbles:Boolean = false, cancelable:Boolean = false) {
            super(type, bubbles, cancelable);

        }

        public override function clone():Event {
            return new UIEvent(type, bubbles, cancelable);
        }

        public override function toString():String {
            return formatToString("UIEvent", "type", "bubbles", "cancelable", "eventPhase");
        }

    }
}