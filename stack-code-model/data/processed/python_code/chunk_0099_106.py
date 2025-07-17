/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.straightouttaspace.Objects.Weapons
{
	import flash.geom.Point;
	
	import de.p3337.straightouttaspace.Objects.DrawableObject;
	import de.p3337.straightouttaspace.Objects.Players.PlayerObject;
	import de.p3337.straightouttaspace.Utils.Dimensions;

	/**
	 * Abstract class for implementing a weapon.
	 * 
	 * Every weapon will make a certain amount of damage which is represented by
	 * "power".
	 */
	public class Weapon extends DrawableObject
	{
		protected var _parent:PlayerObject;
		protected var power:uint
		
		public function Weapon(parent:PlayerObject, position:Point, dimensions:Dimensions, power:uint)
		{
			super(position, dimensions);
			
			this._parent = parent;
			this.power = power;
		}
		
		public function get parent():PlayerObject
		{
			return _parent;
		}
		
		/**
		 * @inheritDoc
		 */
		public function destroy():void
		{
			this._parent = null;
		}
	}
}