package com.illuzor.thegame {
	import com.illuzor.thegame.world.elements.Portal;
	import com.illuzor.thegame.world.elements.PortalV;
	import com.illuzor.thegame.world.Hero;
	/**
	 * ...
	 * @author illuzor // illuzor.com // illuzor@gmail.com
	 */
	public class GameMan {
		
		public static var hero:Hero;
		public static var portal1:Portal;
		public static var portal2:PortalV;
		
		public static function teleport():void {
			hero.x = portal2.x + portal2.width/2;
			hero.y = portal2.y+2;
		}
		
	}
}