package com.ats.helpers {

    import flash.events.Event;

    public class NetworkEvent extends Event {

        public static const IP_ADDRESS_FOUND:String = "ipAddressFound";
        public static const IP_ADDRESS_NOT_FOUND:String = "ipAddressNotFound";

        public var ipAddress:String;

        public function NetworkEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false) {
            super(type, bubbles, cancelable);
        }
    }
}