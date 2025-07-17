package net.wooga.selectors.pseudoclasses {

	import net.wooga.selectors.selectoradapter.SelectorAdapter;

	public class LastChild extends NthLastChild {

		override public function isMatching(subject:SelectorAdapter):Boolean {
			super.setArguments([1]);
			return super.isMatching(subject);
		}

		override public function setArguments(arguments:Array):void {
			if (arguments.length != 0) {
				throw new ArgumentError("Wrong argument count");
			}
		}
	}
}