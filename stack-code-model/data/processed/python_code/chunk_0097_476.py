package SeedsOfDestruction
{
	import flash.display.BitmapData;
	import net.flashpunk.Entity;
	import net.flashpunk.FP;
	import net.flashpunk.graphics.Image;
	import net.flashpunk.graphics.Spritemap;
	import net.flashpunk.utils.Input;
	import net.flashpunk.utils.Key;
	
	/**
	 * ...
	 * @author Philip Ludington
	 */
	public class Win extends Entity 
	{		
		[Embed(source='/assets/WinScreen.png')]
		private var WIN_SCREEN:Class;
		
		[Embed(source='/assets/IntroScreen.png')]
		private var INTRO_SCREEN:Class;	
		
		[Embed(source='/assets/Space.png')]
		private var PLANT_LAUNCH:Class;		
		
		public var spriteMap:Spritemap;
		public var imageSpace:Image = new Image(PLANT_LAUNCH);
		
		public function Win() 
		{			
			trace("created");
			addGraphic(imageSpace);
			imageSpace.y = -389;
			
			// Make the Pink transparent
			var bitmapData:BitmapData = Global.MakeTransparent(INTRO_SCREEN);		
			spriteMap = new Spritemap(bitmapData, 232, 199);
			
			// Define the animations
			spriteMap.add("launch", [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12], 2, false);
			
			addGraphic(spriteMap);
			spriteMap.x = 152;
			spriteMap.y = 80;
			
			// Make the Pink transparent
			bitmapData = Global.MakeTransparent(WIN_SCREEN);
			var image:Image = new Image(bitmapData);		
			addGraphic(image);			
			
			layer = -100;
		}
		
		override public function added():void 
		{
			super.added();
			
			Play();
		}
		
		override public function update():void 
		{
			super.update();
			
			if (Input.mousePressed
			|| Input.pressed(Key.ANY))
			{
				var a:Seeds = (Seeds)(FP.world);
				a.Stop();
				FP.world = new Seeds();
			}
		}
		
		public function Play():void 
		{
			trace("added");
			
			spriteMap.play("launch");
		}
	}

}