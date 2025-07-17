/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.straightouttaspace.Utils
{
	import flash.geom.Point;
	import flash.geom.Rectangle;
	
	import de.p3337.straightouttaspace.Objects.Players.Player;
	import de.p3337.straightouttaspace.Objects.Spaceships.Spaceship;
	import de.p3337.straightouttaspace.Objects.Weapons.Weapon;

	/**
	 * This class provides static methods to calculate bitmap collisions between
	 * a weapon and a spaceship or between to spaceships.
	 */
	public class CollisionCalculationHelper
	{
		/**
		 * Checks if a weapon and a spaceship have collided.
		 * 
		 * @param weapon The weapon to check if it has hit a certain spaceship.
		 * @param ship The spaceship to check if it was hit by a certain weapon.
		 * @return True if a weapon has hit a spaceship.
		 */
		public static function checkWeaponShipCollision(weapon:Weapon, ship:Spaceship):Boolean
		{
			var isCollision:Boolean = false;
			
			var weaponOffsetX:Number = -weapon.dimensions.width / 2;
			var weaponOffsetY:Number = (-weapon.dimensions.height / 2) * (weapon.parent is Player? 1 : -1);
			var shipOffsetX:Number = -ship.dimensions.width / 2;
			var shipOffsetY:Number = -ship.dimensions.height /2
			
			var rect1:Rectangle = new Rectangle(
				weapon.position.x + weaponOffsetX,
				weapon.position.y + weaponOffsetY,
				weapon.dimensions.width,
				weapon.dimensions.height);
			
			var rect2:Rectangle = new Rectangle(
				ship.position.x + shipOffsetX,
				ship.position.y + shipOffsetY,
				ship.dimensions.width,
				ship.dimensions.height);
			
			// phase 1 : rectangle intersection
			var alphaTreshold:Number = 255;
			var intersection:Rectangle = rect1.intersection(rect2);
			if(intersection.width != 0 || intersection.height != 0)
			{	
				// Phase 2 Bitmap hitTest
				if(weapon.texture.bitmapData.hitTest(
					new Point(rect1.x, rect1.y),
					alphaTreshold,
					ship.texture.bitmapData,
					new Point(rect2.x, rect2.y),
					alphaTreshold))
				{
					isCollision = true;
				}
			}
			return isCollision;
		}
		
		/**
		 * Checks if two spaceships have collided.
		 * 
		 * @param ship1 The spaceship to check if it hits a certain spaceship.
		 * @param ship2 The spaceship to check if it was hit by a certain spaceship.
		 * @return True if the two spaceships have collided.
		 */
		public static function checkShipShipCollision(ship1:Spaceship, ship2:Spaceship):Boolean
		{
			var isCollision:Boolean = false;
			
			var ship1OffsetX:Number = -ship1.dimensions.width / 2;
			var ship1OffsetY:Number = -ship1.dimensions.height /2
			var ship2OffsetX:Number = -ship2.dimensions.width / 2;
			var ship2OffsetY:Number = -ship2.dimensions.height /2
			
			var rect1:Rectangle = new Rectangle(
				ship1.position.x + ship1OffsetX,
				ship1.position.y + ship1OffsetY,
				ship1.dimensions.width,
				ship1.dimensions.height);
			
			var rect2:Rectangle = new Rectangle(
				ship2.position.x + ship2OffsetX,
				ship2.position.y + ship2OffsetY,
				ship2.dimensions.width,
				ship2.dimensions.height);
			
			// phase 1 : rectangle intersection
			var alphaTreshold:Number = 255;
			var intersection:Rectangle = rect1.intersection(rect2);
			if(intersection.width != 0 || intersection.height != 0)
			{	
				// Phase 2 Bitmap hitTest
				if(ship1.texture.bitmapData.hitTest(
					new Point(rect1.x, rect1.y),
					alphaTreshold,
					ship2.texture.bitmapData,
					new Point(rect2.x, rect2.y),
					alphaTreshold))
				{
					isCollision = true;
				}
			}
			return isCollision;
		}
	}
}