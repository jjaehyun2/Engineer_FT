/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.straightouttaspace.Objects.Weapons
{
	import flash.geom.Point;
	
	import de.p3337.straightouttaspace.Objects.DrawableObject;
	import de.p3337.straightouttaspace.Objects.Players.Player;
	import de.p3337.straightouttaspace.Objects.Players.PlayerObject;
	import de.p3337.straightouttaspace.Objects.Spaceships.Spaceship;
	import de.p3337.straightouttaspace.Sound.Jukebox;
	import de.p3337.straightouttaspace.Sound.SoundFileEnum;
	import de.p3337.straightouttaspace.Utils.CollisionCalculationHelper;
	import de.p3337.straightouttaspace.Utils.Dimensions;

	/**
	 * The Laser is a special weapon that will fire one single dangerous light
	 * beam.
	 */
	public class Laser extends Weapon
	{
		private var _direction:Point;
		private var _velocity:uint;
		
		public function Laser(parent:PlayerObject, position:Point, dimensions:Dimensions, power:uint)
		{
			super(parent, position, dimensions, power);
			
			this._direction = new Point();
			this._velocity =  10;
			
			if(parent is Player)
			{
				Jukebox.getInstance().play(SoundFileEnum.FIRE);
			}
		}
		
		/**
		 * @inheritDoc
		 */
		override public function update():void
		{
			position.x += this._velocity * this._direction.x;
			position.y += this._velocity * this._direction.y;
			
			if(position.y < -dimensions.height
				|| position.y > (parent.parent.parent.main.stage.stageHeight + dimensions.height)
				|| position.x < -dimensions.width
				|| position.x > (parent.parent.parent.main.stage.stageWidth + dimensions.width)
				|| checkSpaceshipCollision())
			{
				this.toBeDestroyed = true;
			}
		}
		
		private function checkSpaceshipCollision():Boolean
		{
			var collisionVector:Vector.<DrawableObject> = new Vector.<DrawableObject>();
			if(parent is Player) {
				var opponentSpaceships:Vector.<Spaceship> = parent.parent.opponent.spaceshipVector;
				for each(var opponentSpaceship:Spaceship in opponentSpaceships)
				{
					if(CollisionCalculationHelper.checkWeaponShipCollision(this, opponentSpaceship))
					{ 
						collisionVector.push(opponentSpaceship);
					}
				}
			}
			else
			{
				var playersSpaceship:Spaceship = parent.parent.player.spaceshipVector[0];
				if(CollisionCalculationHelper.checkWeaponShipCollision(this, playersSpaceship))
				{
					collisionVector.push(playersSpaceship);
				}
			}
			
			for each(var hardHitSpaceship:Spaceship in collisionVector)
			{
				hardHitSpaceship.shieldStrength -= this.power;
				if(hardHitSpaceship.shieldStrength <= 0)
				{
 					hardHitSpaceship.toBeDestroyed = true;
					
					if(parent is Player)
					{
						parent.score += hardHitSpaceship.points;
					}
				}
			}
			
			if(collisionVector.length > 0) return true;
			else return false;
		}

		public function get direction():Point
		{
			return _direction;
		}

		public function set direction(value:Point):void
		{
			_direction = value;
		}

		public function get velocity():uint
		{
			return _velocity;
		}

		public function set velocity(value:uint):void
		{
			_velocity = value;
		}
		
		/**
		 * @inheritDoc
		 */
		override public function destroy():void
		{
			super.destroy();
			this.direction = null;
		}
	}
}