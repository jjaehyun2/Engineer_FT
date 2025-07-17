package controls.TermsAndConditions.events {
	import flash.events.Event;

	public class TermsAndConditionsAgreementEvent extends Event {
		public function TermsAndConditionsAgreementEvent(type:String, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
		}
		
        public static const TYPE_TERMSANDCONDITIONS_AGREEMENT:String = "termsAndConditionsAgreement";

        override public function clone():Event {
            return new TermsAndConditionsAgreementEvent(type);
        }
	}
}