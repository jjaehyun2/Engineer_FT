package com.cupcake.game.graphics {
	
	import flash.display.MovieClip;	
	import flash.events.MouseEvent;
	
	public class MainMenu extends MovieClip{
		public function MainMenu(){
			init();
		}	
		
		private function init():void 
		{			
			//trace(playerVsComputerBtn);
			
			enableSpockLizard.addEventListener(MouseEvent.CLICK, onEnableSpockLizard);
			
			playerVsComputerBtn.addEventListener(MouseEvent.CLICK, onPlayerVsComputer);
			
			computerVsComputerBtn.addEventListener(MouseEvent.CLICK, onComputerVsComputer);
		}				
		
		private function onEnableSpockLizard(e:MouseEvent):void 
		{
			if (e.currentTarget.currentFrame == 1){
				e.currentTarget.gotoAndStop(2);
				
				Game.enableSpockLizardGame = true;	
			}
			else{
				e.currentTarget.gotoAndStop(1);
				
				Game.enableSpockLizardGame = false;	
			}			
		}
		
		private function onPlayerVsComputer(e:MouseEvent):void 
		{
			addChild(new Game(false));
		}
		
		private function onComputerVsComputer(e:MouseEvent):void 
		{
			addChild(new Game(true));
		}
	}	
}