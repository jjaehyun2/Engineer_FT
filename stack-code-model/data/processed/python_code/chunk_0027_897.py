package  
{
	import net.flashpunk.Entity;
	import net.flashpunk.graphics.Image;
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Tomb extends Entity
	{
		[Embed(source = "Assets/Graphics/Items & Objects/m_headstone.png")]private const TOMB:Class;
		private var _image:Image;
		
		private var _shouldFall:Boolean = false;
		public function Tomb(player:Player, en:Entity) 
		{
			_image = new Image(TOMB);
			if (en == null)
			{
				x = player.x;
				y = player.y;
			}
			else if (en is Spike)
			{
				var spike:Spike = en as Spike;
				if (spike.anim.frame == 8)
				{
					x = player.x;
					y = spike.y;
					_image.angle = 0;
				}
				else if (spike.anim.frame == 7)
				{
					y = player.y;
					x = spike.x + 16;
					_image.angle = 270;
				}
				else if (spike.anim.frame == 6)
				{
					y = player.y + 16;
					x = spike.x;
					_image.angle = 90;
				}
				else if (spike.anim.frame == 4)
				{
					x = player.x + 16;
					y = spike.y + 16;
					_image.angle = 180;
				}
			}
			else if (en is Fireball)
			{
				x = player.x;
				y = int(en.y/16)*16;
			}
			else if (en is Skull)
			{
				x = player.x;
				y = en.y;
				//_shouldFall = true;
				//setHitbox(16, 16);
			}
				
			graphic = _image;
			
			type = "tomb";
			layer = 281
			
			
			MainMenu.flash.start(0xFF0000,.5,.6);
			MainMenu.quake.start(15, 0.5);
		}
		
		/*public override function update():void
		{
			if (_shouldFall)
			{
				y++;
				if (collide("level", x, y))
				{
					y--;
					_shouldFall = false;
				}
			}
		}*/
		
	}

}