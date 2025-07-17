package worlds {
	
	import actors.Background;
	import actors.Player;
	import game.Credits;
	import hud.AnimatedMessage;
	import net.flashpunk.graphics.Image;
	import net.flashpunk.Sfx;
	import net.flashpunk.tweens.misc.VarTween;
	import net.flashpunk.World;
	import net.flashpunk.FP;
	import game.Constants;
	import net.flashpunk.utils.Input;
	import net.flashpunk.utils.Key;
	import game.LevelData;
	import game.Assets;
	
	public class MenuWorld extends World {
		
		public static var music:Sfx;
		
		protected var menuPlayer:Player;
		protected var background:Background;
		protected var title:AnimatedMessage;
		protected var start:AnimatedMessage;
		protected var creditsButton:AnimatedMessage;
		protected var creditsData:Credits;
		protected var credits:AnimatedMessage;
		protected var fade:Image;
		protected var fadeTween:VarTween;
		
		public function MenuWorld():void {
			super();
			
			menuPlayer = new Player(50, 50);
			menuPlayer.vy = -6;
			
			background = new Background();
			title = new AnimatedMessage(FP.halfWidth, 60, "speed trail", 44, 0x32CD32, 0x2F4F4F, Constants.NONE_ANIMATION);
			start = new AnimatedMessage(FP.halfWidth, 390, "press x to start", 24, 0x00BFFF, 0x2F4F4F, Constants.NONE_ANIMATION);
			creditsButton = new AnimatedMessage(FP.halfWidth, 440, "press c to view credits", 24, 0xF0FFF0, 0x2F4F4F, Constants.NONE_ANIMATION);
			
			creditsData = new Credits();
			credits = new AnimatedMessage(FP.halfWidth, FP.halfHeight - 55, creditsData.toString(), 16, 0xFFFF00, 0x000000, Constants.NONE_ANIMATION);
			credits.visible = false;
			
			fade = Image.createRect(FP.width, FP.height, 0x000000);
			fade.alpha = 0;
			fade.scrollX = fade.scrollY = 0;
			fadeTween = new VarTween(startGame);
		}
		
		override public function begin():void {
			super.begin();
			
			add(background);
			add(title);
			add(start);
			add(creditsButton);
			add(credits);
			add(menuPlayer);
			addGraphic(fade);
			addTween(fadeTween);
		}
		
		public function startGame():void {
			music = new Sfx(Assets.MUSIC);
			music.loop();
			FP.world = new GameWorld(LevelData.getCurrentLevel());
		}
		
		override public function update():void {
			super.update();
			
			menuPlayer.move();
			camera.x = menuPlayer.x - FP.screen.width * 0.5;
			camera.y = menuPlayer.y - FP.screen.height * 0.5;
			
			if (Input.pressed(Key.X)) {
				var choice:Sfx = new Sfx(Assets.CHOICE);
				choice.play();
				fadeTween.tween(fade, "alpha", 1, 1.8);
			}
			
			if (Input.pressed(Key.C)) {
				background.visible = !background.visible;
				title.visible = !title.visible;
				menuPlayer.visible = !menuPlayer.visible;
				credits.visible = !credits.visible;
			}
		}
		
	}

}