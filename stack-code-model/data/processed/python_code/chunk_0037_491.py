/*
** Source code Copyright 2006, Andrew Rapo
** May be used in non-commercial and commercial applications
** as long as the author is credited
*/

package org.rapo.games.astro {
	
	public class MathTables{
		
		public static var sine:Array = new Array(360);     // sin table
		public static var cosine:Array = new Array(360);   // cosine table
		public static var PI:Number;
		public static var angleDivisions:Number = 32;
		
		static var tablesInitialized:Boolean = initTables();
		
		public function MathTables(){
		}
			
		public static function initTables():Boolean {
		
			PI = Math.PI;
			// loop through all angles and add to the arrays
	
			for (var temp_ang:Number = 360; temp_ang >= 0; temp_ang--) {
				sine[temp_ang] = Math.sin(PI*temp_ang/180.0);
				cosine[temp_ang] = Math.cos(PI*temp_ang/180.0);
			}
			
			return true;
		}
		
		public static function traceTables() {
					
			for (var temp_ang:Number = 360; temp_ang >= 0; temp_ang--) {
				//trace("Ang: " + temp_ang + ", Sin: " + sine[temp_ang] + ", Cos: " + cosine[temp_ang]);
			}
		}
		
		public static function setVelocity(angle_index:Number, speed:Number, velocity:Object):void {
			
			var angle:Number = 360 - Math.floor((angle_index - 1) * (360 / angleDivisions));
			velocity.y = (cosine[angle] * -1) * speed;
			velocity.x =   (sine[angle] * -1) * speed;
		}
	}
}