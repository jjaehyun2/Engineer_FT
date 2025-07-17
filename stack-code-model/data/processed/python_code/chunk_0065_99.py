package flexmvcs.patterns.command {

	import flash.events.Event;
	
	public class CompositeResult {
		public var results:Array;
		public var failures:Array;
		public var successes:Array;
		
		public function CompositeResult() {
			results = new Array();
			failures = new Array();
			successes = new Array();
		}
		
		public function addFailure(failure:Event):void {
			failures.push(failure);
			results.push(failure);
		}
		
		public function addSuccess(success:Event):void {
			successes.push(success);
			results.push(success);
		}
		
		public function toString():String {
			return "[CompositeResult failures=" + failures.length + " successes=" + successes.length + "]";
		}
	}
}