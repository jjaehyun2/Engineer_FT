package controls.TermsAndConditions.events {
	import flash.events.Event;

	public class TermsAndConditionsNoAgreementEvent extends Event {
		public function TermsAndConditionsNoAgreementEvent(type:String, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
		}
		
        public static const TYPE_TERMSANDCONDITIONS_NO_AGREEMENT:String = "termsAndConditionsNoAgreement";

        override public function clone():Event {
            return new TermsAndConditionsNoAgreementEvent(type);
        }
	}
}