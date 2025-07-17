package
{
	import flash.display.BitmapData;
	
	import net.flashpunk.FP;
	import net.flashpunk.World;
	import net.flashpunk.graphics.Image;
	import net.flashpunk.graphics.Text;
	import net.flashpunk.utils.Input;
	
	public class TitleWorld extends World
	{
		private var generator:MazeGenerator;
		private var generateTick:Number;
		
		private var firstTime:Boolean;
		private var playerWin:Boolean;
		
		public function TitleWorld(generator:MazeGenerator, firstTime:Boolean = false)
		{
			this.generator = generator;
			generateTick = 0;
			
			this.firstTime = firstTime;
			
			playerWin = (generator.getLevel() == 6);
			generator.setLevel(1);
		}
		
		override public function begin():void
		{
			Text.size = 48;
			var titleText:Text = new Text("MAZE ESCAPE");
			titleText.x = FP.screen.width / 2 - titleText.width / 2;
			titleText.y = FP.screen.height / 2 - 70;
			
			var titleTextBox:Image = new Image(new BitmapData(titleText.width + 20, titleText.height + 10, false, 0xFF000000));
			titleTextBox.x = titleText.x - 10;
			titleTextBox.y = titleText.y - 5;
			
			Text.size = 20;
			var playText:Text = new Text("click to try escape from lava");
			playText.x = FP.screen.width / 2 - playText.width / 2;
			playText.y = FP.screen.height / 2 - playText.height / 2;
			
			var playTextBox:Image = new Image(new BitmapData(playText.width + 20, playText.height + 10, false, 0xFF000000));
			playTextBox.x = playText.x - 10;
			playTextBox.y = playText.y - 5;

			if (!firstTime)
			{
				Text.size = 24;
				var infoText:Text = new Text(playerWin ? "A WINRAR IS YOU!" : "GAME OVER");
				infoText.x = FP.screen.width / 2 - infoText.width / 2;
				infoText.y = FP.screen.height / 2 + 100;
				
				var infoTextBox:Image = new Image(new BitmapData(infoText.width + 20, infoText.height + 10, false, 0xFF000000));
				infoTextBox.x = infoText.x - 10;
				infoTextBox.y = infoText.y - 5;
				
				addGraphic(infoText, 0);
				addGraphic(infoTextBox, 1);
			}
			
			addGraphic(titleText, 0);
			addGraphic(titleTextBox, 1);
			
			addGraphic(playText, 0);
			addGraphic(playTextBox, 1);
			
			addGraphic(generator.getMaze(), 2);
		}
		
		override public function update():void
		{
			generateTick += FP.elapsed;
			
			if (generateTick >= .02)
			{
				generateTick -= .02;
				
				if (!generator.generateMazeStep())
					if (!generator.propogateLavaStep())
						generator.reset();
			}
			
			if (Input.mousePressed)
				FP.world = new MazeWorld(generator);
		}
	}
}