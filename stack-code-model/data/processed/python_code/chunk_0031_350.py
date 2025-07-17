package SeedsOfDestruction
{
	import com.greensock.TweenMax;
	import flash.display.BitmapData;
	import net.flashpunk.Entity;
	import net.flashpunk.FP;
	import net.flashpunk.graphics.Backdrop;
	import net.flashpunk.graphics.Emitter;
	import net.flashpunk.graphics.Image;
	import net.flashpunk.graphics.ParticleType;
	import net.flashpunk.graphics.TiledImage;
	import net.flashpunk.Sfx;
	import net.flashpunk.utils.Draw;
	import net.flashpunk.utils.Ease;
	import net.flashpunk.utils.Input;
	import net.flashpunk.utils.Key;
	import Infrastructure.*;
	
	public class Seeds extends Room
	{
		[Embed(source = "/assets/sky.png")] public static const SPACE:Class;
		[Embed(source = "/assets/ground.png")] public static const GROUND:Class;
		[Embed(source = "/assets/puff.png")] public static const PUFF:Class;
		
		// Game Objects
		public var space:Backdrop = new Backdrop(SPACE, true, true);
		public var ground:TiledImage;
		public var puffs:Emitter;
		public var points:int = 0;
		public var hud:HUD = new HUD();
		public var player:Player;
		
		// The different screens
		private var lose:Lose = new Lose();
		private var win:Win = new Win();		
		private var titleScreen:TitleScreen = new TitleScreen();
		private var intro:IntroScreen = new IntroScreen();
		
		public function Seeds() 
		{
			FP.volume = .6;
			
			// Make the Pink transparent
			var bitmapData:BitmapData = Global.MakeTransparent(PUFF);
			puffs = new Emitter(bitmapData, 22, 22);
			
			bitmapData = Global.MakeTransparent(GROUND);
			ground = new TiledImage(bitmapData, FP.width, 20);
			
			addGraphic(space, 20);
			addGraphic(ground, 0, 0, FP.height - ground.height);
			
			// Create Player
			player = new Player(FP.halfWidth, FP.height - ground.height + 5);			
			add(player);
			player.active = false;
			
			// Add the Puff frames
			addGraphic(puffs, 20);
			
			// Create Puff variation #1
			var t2:ParticleType = puffs.newType("Puff1", [0, 1, 2, 3, 4]);
			t2.setMotion(20, 20, 0.4, 140, 65, 1.5, Ease.cubeOut);
			t2.setAlpha(1, 0, Ease.cubeIn);
			t2.setGravity(0.3, 0.2);
			
			// Create Puff variation #2
			t2 = puffs.newType("Puff2", [5, 6, 7, 8, 9]);
			t2.setMotion(20, 20, 0.4, 140, 65, 1.5, Ease.cubeOut);
			t2.setAlpha(1, 0, Ease.cubeIn);
			t2.setGravity(0.3, 0.2);
			
			// Create Puff variation #3
			t2 = puffs.newType("Puff3", [10, 11, 12, 13, 14]);
			t2.setMotion(20, 20, 0.4, 140, 65, 1.5, Ease.cubeOut);
			t2.setAlpha(1, 0, Ease.cubeIn);
			t2.setGravity(0.3, 0.2);
			
			// Create Puff variation #4
			t2 = puffs.newType("Puff4", [15, 16, 17, 18, 19]);
			t2.setMotion(20, 20, 0.4, 140, 65, 1.5, Ease.cubeOut);
			t2.setAlpha(1, 0, Ease.cubeIn);
			t2.setGravity(0.3, 0.2);
			
			// Setup the soil bar
			add(hud);
			
			add(titleScreen);
		}
		
		// Play the Intro Story
		public function Intro():void 
		{
			remove(titleScreen);
			
			add(intro);
			intro.Start();
		}
		
		// Stop the game
		public function Stop():void
		{
			// Deactive the player
			player.active = false;
			
			// Clear the playing field
			var badPlantList:Array = [];
			getClass( BadPlant, badPlantList );
			
			for each( var badPlant:BadPlant in badPlantList )
			{
				if ( badPlant != null )
				{
					remove( badPlant);
				}
			}
			
			var seedList:Array = [];
			getClass( Seed, seedList );
			
			for each( var seed:Seed in seedList )
			{
				if ( seed != null )
				{
					remove(seed);
				}
			}			
			
			// Make sure all the different possible screens are gone			
				if ( titleScreen != null )
				{
			remove(titleScreen);
			}
			
				if ( intro != null )
				{
			remove(intro);
			}
			
				if ( win != null )
				{
			remove(win);
			}
			
				if ( lose != null )
				{
			remove(lose);	
			}		
		}
		
		// Play the game
		public function Play():void
		{	
			Stop(); // This clears it all right out
			
			// Reset the score			
			hud.Restart();
			
			// Start
			player.active = true;
			TweenMax.delayedCall(1.5, spawnSeed);
		}
		
		public function PlayerWin():void
		{			
			// Deactive the player
			Stop();
			
			if ( win == null )
			{
				win = new Win();
			}
			trace("add");
			add(win);			
			win.Play();
		}
		public function spawnSeed():void
		{
			if ( player.active )
			{
				add(new Seed(25 + FP.rand(FP.width - 50), -25));
				TweenMax.delayedCall(1.0, spawnSeed);
			}
		}
		
		override public function update():void 
		{
			super.update();
			
			//if (points >= 10)
			//{
				//trace("Complete!");
				//active = false;
			//}
			
			if ( Input.pressed(Key.F2)
				&& Global.isDebugBuild())
			{
					FP.console.enable();
					Input.mouseCursor = MouseCursor.DEFAULT.ToString();
			}
		}
		
		override public function render():void 
		{
			super.render();
			
			Draw.circlePlus(mouseX, mouseY, 4, 0x33FF33, 1, false, 1);
			Draw.line(mouseX - 5, mouseY - 5, mouseX + 5, mouseY + 5, 0x33FF33);
			Draw.line(mouseX + 5, mouseY - 5, mouseX - 5, mouseY + 5, 0x33FF33);
		}
	}
}