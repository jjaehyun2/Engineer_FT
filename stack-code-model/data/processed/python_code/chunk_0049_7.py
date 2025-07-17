package classes {
	
	import flash.display.MovieClip;
	//import classes.Pieces;
	
	public class Piece extends MovieClip{
		protected var vx:Number;
		protected var vy:Number;
		protected var type:String;
		protected var m:Number;
		protected var r:Number;
		protected var fric:Number;
		
		public function Piece(){
			fric = 0.01
		}
		public function set vX(newValue:Number):void{
			vx = newValue;
		}
		public function set vY(newValue:Number):void{
			vy = newValue;
		}
		public function set mass(newValue:Number):void{
			m = newValue;
		}
		public function set radius(newValue:Number):void{
			r = newValue;
		}
		public function get vX():Number{
			return vx;
		}
		public function get vY():Number{
			return vy;
		}
		public function get mass():Number{
			return m;
		}
		public function get radius():Number {
			return r;
		}
		public function get friction():Number {
			return fric;
		}
		public function get Type():String {
			return type;
		}
	}
}