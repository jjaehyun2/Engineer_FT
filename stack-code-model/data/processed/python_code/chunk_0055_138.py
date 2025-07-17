package controls.paypal.events {
	import flash.events.Event;

	public class DonationClickedEvent extends Event {
		public function DonationClickedEvent(type:String, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
		}
		
        public static const TYPE_DONATION_CLICKED:String = "donationClicked";

        override public function clone():Event {
            return new DonationClickedEvent(type);
        }
	}
}