/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.straightouttaspace.Objects.Players.AI
{
	import flash.events.TimerEvent;
	import flash.geom.Point;
	
	import de.p3337.straightouttaspace.Objects.Players.Opponent;
	import de.p3337.straightouttaspace.Objects.Spaceships.OpponentSpaceship;
	import de.p3337.straightouttaspace.Objects.Spaceships.Spaceship;
	import de.p3337.straightouttaspace.Objects.Spaceships.SpaceshipFactory;
	import de.p3337.straightouttaspace.Utils.SizeEnum;
	import de.p3337.straightouttaspace.Utils.VectorCalculationHelper;

	/**
	 * This is a simple attack strategy:
	 * Opponents will shoot only once after they appeared at a distance of about 
	 * 400 px to the players spaceship.
	 * Their start position is set randomly. The number of opponent spaceships 
	 * for every attack is fixed for the first 25 waves, after that this will be 
	 * set randomly.
	 */
	public class SimpleAttackStrategy extends AttackStrategy
	{
		private var attackRows:Vector.<Object>;
		private var distanceToPlayer:Number;
		
		public function SimpleAttackStrategy(parent:Opponent, attackInterval:uint)
		{
			super(parent, attackInterval);
			
			// first 25 fixed waves to increase difficulty increasingly
			attackRows = new Vector.<Object>;
			attackRows.push(
				{s:1, m:0, l:0},
				{s:2, m:0, l:0},
				{s:3, m:0, l:0},
				{s:4, m:0, l:0},
				{s:5, m:0, l:0}, //  5
				{s:1, m:1, l:0},
				{s:2, m:1, l:0},
				{s:3, m:1, l:0},
				{s:5, m:0, l:0},
				{s:1, m:2, l:0}, // 10
				{s:2, m:2, l:0},
				{s:0, m:3, l:0},
				{s:1, m:0, l:1},
				{s:2, m:0, l:1},
				{s:0, m:1, l:1}, // 15
				{s:1, m:0, l:2},
				{s:2, m:0, l:2},
				{s:0, m:1, l:2},
				{s:0, m:2, l:2},
				{s:0, m:0, l:3}, // 20
				{s:1, m:1, l:2},
				{s:2, m:1, l:2},
				{s:0, m:1, l:3},
				{s:1, m:1, l:3},
				{s:2, m:1, l:3}  // 25
			);
			
			this.distanceToPlayer = 400;
		}
		
		/**
		 * @inheritDoc
		 */
		override protected function onAttackTimer(e:TimerEvent):void
		{
			sendNewSpaceshipWave();
		}
		
		/**
		 * @inheritDoc
		 */
		override public function update(ship:OpponentSpaceship):void
		{
			// fire if distance is under a certain trashhold
			if(!ship.hasFired)
			{
				var pos1:Point = ship.position.clone();
				pos1.x -= ship.texture.width;
				pos1.y -= ship.texture.height;
				
				var pos2:Point = parent.parent.player.spaceshipVector[0].position.clone();
				pos2.x -= parent.parent.player.spaceshipVector[0].texture.width;
				pos2.y -= parent.parent.player.spaceshipVector[0].texture.height;
				
				if(VectorCalculationHelper.calcDistanzBetween2Points(pos1, pos2) <= this.distanceToPlayer)
				{
					ship.fire();
				}
			}
		}
		
		/**
		 * @inheritDoc
		 */
		override public function fire(ship:OpponentSpaceship):void
		{
			// create new weapon / bullets
			var position:Point = ship.position.clone();
			position.y += ship.dimensions.height / 2;
			parent.weaponVector.push(
				parent.weaponFactory.createRedLaser(position, ship.weaponPower)
			);
		}
		
		/**
		 * @inheritDoc
		 */
		override public function move(ship:OpponentSpaceship):void
		{
			ship.position.y += ship.velocity;
		}
		
		/**
		 * Creates a new wave of opponent spaceships.
		 * The first 25 waves are determained by this.attackRows.  
		 */
		override public function sendNewSpaceshipWave():void
		{
			var attackRow:Object;
			if(this.attackRows.length > 0) {
			 attackRow = this.attackRows.shift();
			} else {
				attackRow = {
					s: Math.round(Math.random() * 2) + 2,
					m: Math.round(Math.random() * 3),
					l: Math.round(Math.random() * 5)
				}
			}
			
			var ship:OpponentSpaceship;
			var shipVector:Vector.<Spaceship> = parent.spaceshipVector;
			var shipFactory:SpaceshipFactory = parent.parent.spaceshipFactory;

			while (--attackRow.s > -1)
			{
				ship = shipFactory.createOpponentSpaceship(
					getRandomStartPosition(),
					SizeEnum.SMALL
				) as OpponentSpaceship;
				ship.velocity = getRandomSpaceshipVelocity(SizeEnum.SMALL);
				shipVector.push(ship);	
			}
			
			while (--attackRow.m > -1)
			{
				ship = shipFactory.createOpponentSpaceship(
					getRandomStartPosition(),
					SizeEnum.MEDIUM
				) as OpponentSpaceship;
				ship.velocity = getRandomSpaceshipVelocity(SizeEnum.MEDIUM);
				shipVector.push(ship);	
			}
			
			while (--attackRow.l > -1)
			{
				ship = shipFactory.createOpponentSpaceship(
					getRandomStartPosition(),
					SizeEnum.LARGE
				) as OpponentSpaceship;
				ship.velocity = getRandomSpaceshipVelocity(SizeEnum.LARGE);
				shipVector.push(ship);	
			}
		}
		
		private function getRandomStartPosition():Point
		{
			return new Point(
				Math.random() * (parent.stage.stageWidth - 200) + 100,
				Math.random() * -200 - 50
			);
		}
		
		private function getRandomSpaceshipVelocity(size:SizeEnum):Number
		{
			var velocity:Number = 1.0;
			switch(size)
			{
				case SizeEnum.SMALL: velocity += (Math.random() + 0.3) * 2.0; break;
				case SizeEnum.MEDIUM: velocity += (Math.random() + 0.2) * 1.4; break;
				case SizeEnum.LARGE: velocity += (Math.random() + 0.1) * 1.1; break;
			}
			return velocity;
		}
	}
}