package flexmvcs.patterns.utils {

	public class Queue {
		protected var list:Array;
		
		public function Queue() {
			list = new Array();		
		}

		public function enqueue(item:Object):void {
			list.push(item);
		}
		
		public function dequeue():Object {
			return list.shift();
		}
		
		public function peek():Object {
			if(list.length > 0) {
				return list[0];
			}
			else {
				return null;
			}
		}
	}
}