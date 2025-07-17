package com.adrienheisch.spacewar.background
{
	import com.adrienheisch.spacewar.Main;
	import flash.display.Stage;
	
	/**
	 * ...
	 * @author Adrien Heisch
	 */
	public class BackgroundManager
	{
		
		protected static var stage:Stage;
		
		public static function init():void
		{
			stage = Main.instance.stage;
			
			stage.addChild(BackgroundContainer.instance);
			
			drawBackground();
		}
		
		protected static function drawBackground():void
		{
			var lStar:Star;
			for (var i:int = 99; i >= 0; i--)
			{
				BackgroundContainer.instance.addChild(lStar = new Star());
				lStar.x = stage.stageWidth * Math.random();
				lStar.y = stage.stageHeight * Math.random();
			}
		}
	
	}

}