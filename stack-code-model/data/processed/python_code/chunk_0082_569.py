package ageofai.map.geom {
	
	/**
	 * 	Simple integer point implementation
	 * 	
	 */
	public class IntPoint {
		public var x:int;
		public var y:int;
		
		function IntPoint(x:int=0, y:int=0) {
			this.x = x;
			this.y = y;
		}
		
		
		public function add(p:IntPoint):void {
			x += p.x;
			y += p.y;
		}
		
		public function addNew(p:IntPoint):IntPoint {
			return new IntPoint(x+p.x, y+p.y);
		}
		

		public function toString():String {
			return "IntPoint("+x+", "+y+")";
		}
		
		public function equals(other:IntPoint):Boolean {
			if (other == null) return false;
			
			return (this.x == other.x && this.y == other.y);
		}
	}
}