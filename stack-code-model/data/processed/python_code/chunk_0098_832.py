package com.cupcake.game.logic.shapes {
	import com.cupcake.game.logic.HandShape;
	
	public class Lizard extends HandShape{
		
		
		public function Lizard(){
			
		}	
		
		override public function beats():Array 
		{
			return [Paper, Spock];
		}
	}	
}