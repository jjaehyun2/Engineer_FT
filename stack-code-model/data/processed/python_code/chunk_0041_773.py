package zombie.behaviors 
{
	import fplib.base.Behavior;
	import fplib.base.GameEntity;
	import fplib.math.Vector2D
	import net.flashpunk.FP;
	import net.flashpunk.graphics.Spritemap;
	import zombie.entities.NPC;
	import zombie.worlds.GameWorld;
	
	/**
	 * ...
	 * @author Diogo Muller
	 */
	public class ZombieBehavior extends Behavior
	{
		private var _target : GameEntity = null;
		private var _minDistance: Number = Math.random() * 90 + 10;
		public var minimumDistance : Number = 100;
		
		public function ZombieBehavior() 
		{
			
		}
		
		override public function update():void 
		{
			if ( ! _target )
			{
				_target = FP.world.nearestToEntity("player", parent) as GameEntity;
			}
			else if( parent.type == "enemy" )
			{			
				var desiredVelocity : Vector2D = Vector2D.subtract(parent.position, _target.position);
				var distance : Number = desiredVelocity.Size;
				
				if( distance < 100 )
				{
					desiredVelocity.normalize();
					desiredVelocity = Vector2D.multiply(desiredVelocity, FP.elapsed * 30);
					(parent.graphic as Spritemap).play("run");
					if (!(FP.world as GameWorld).IsEvil) {
						(parent as NPC).randomZombieNpcMessage();
					}
					else {
						(parent as NPC).randomHumanNpcMessage();
					}
				}
				else
				{
					desiredVelocity = Vector2D.ZERO;
					(parent.graphic as Spritemap).play("stand");
				}
				
				parent.position = Vector2D.add(parent.position, desiredVelocity);
			}
			else if ( parent.type == "npc" )
			{
				var desiredVelocitySeek : Vector2D = Vector2D.subtract(_target.position, parent.position);
				var distanceSeek : Number = desiredVelocitySeek.Size;

				desiredVelocitySeek.normalize();
				desiredVelocitySeek = Vector2D.multiply(desiredVelocitySeek, FP.elapsed * 45);
				(parent.graphic as Spritemap).play("run");
				
                if(distanceSeek > _minDistance)
                    parent.position = Vector2D.add(parent.position, desiredVelocitySeek);
			}
		}
		
	}

}