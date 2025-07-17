package  
{
	import net.flashpunk.Entity;
	import net.flashpunk.graphics.Spritemap;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class GreenOrb extends Entity 
	{
		[Embed(source = "Assets/Graphics/SpriteSheets/green_orb_SS.png")]private const ORB:Class;
		public var orb:Spritemap = new Spritemap(ORB, 25, 25);
		public function GreenOrb(X:int, Y:int ) 
		{
			super(X, Y);
			graphic = orb;
			orb.play();
			type = "YellowOrb";
			setHitbox(25, 25);
			layer = 8;
		}
		
		public override function update():void
		{
			orb.frame++;
		}
		
		public function takeOrb():void
		{
			type = "";
			x = 432;
			y = 4;
			graphic.scrollX = 0;
			graphic.scrollY = 0;
		}
		
	}

}