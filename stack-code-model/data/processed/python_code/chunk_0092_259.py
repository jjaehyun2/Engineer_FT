package com.cupcake.game {
	
	import com.cupcake.game.graphics.MainMenu;
	import com.cupcake.game.test.CheckCombinations;
	import flash.display.MovieClip;	
	import flash.display.StageScaleMode;
	
	public class Main extends MovieClip{
		public function Main(){
			//initialize app interface			
			addChild(new MainMenu());
			
			stage.scaleMode = StageScaleMode.EXACT_FIT;
			
			
			//test
			//new CheckCombinations();
		}	
	}	
}