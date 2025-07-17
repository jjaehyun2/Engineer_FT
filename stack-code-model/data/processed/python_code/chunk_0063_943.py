package com.maxpaynestory.arcadeshooter.core
{
	import com.greensock.*;
	import com.greensock.easing.*;
	import com.maxpaynestory.arcadeshooter.events.GameEvent;
	import com.maxpaynestory.arcadeshooter.interfaces.IPlayer;
	
	import flash.display.Sprite;
	import flash.events.Event;
	
	public class Player extends Sprite implements IPlayer
	{
		
		protected var speed:Number;
		protected var hideFactor:Number;
		public static const BOOST_PLAYER_SPEED:String="boostplayerspeed";
		
		public function Player()
		{
			super();
			speed = 4;
			hideFactor = 0.5;
			this.addEventListener(Event.ADDED_TO_STAGE,onPlaneAddedToStage);
			this.addEventListener(GameEvent.GIVE_PERKS_TO_PLAYER,onGettingPerks);
		}
		
		protected function onGettingPerks(event:GameEvent):void
		{
			var perksArray:Array = event.data as Array;
			
			for(var perksCounter:int=0; perksCounter < perksArray.length;perksCounter++){
				switch(perksArray[perksCounter]){
					case Player.BOOST_PLAYER_SPEED:
						speed += 5;
						break;
				}
			}
		}
		
		protected function onPlaneAddedToStage(event:Event):void
		{
			this.addChild(AssetsManager.getInstance().getPlaneImg());
			this.scaleY = 0.7;
			this.scaleX = 0.7;
		}
		
		public function spawn(xPos:Number, yPos:Number):void
		{
			this.y = stage.stageHeight + this.height + 10;
			this.x = stage.stageWidth/2;
			
			//// Use Greensock Tween library for player spawning
			TweenLite.to(this, 1, {
				y:stage.stageHeight - 90,
				onComplete:onCompleteTweeningSpawn
			});
		}
		
		private function onCompleteTweeningSpawn():void
		{
			this.dispatchEvent(new GameEvent(GameEvent.ENABLE_PLAYER_CONTROLS,{}));
		}
		
		public function die():void
		{
			this.parent.removeChild(this);
		}
		
		public function moveLeft():void
		{
			if(this.x > -(this.width * hideFactor)){
				this.x -= speed;
			}
		}
		
		public function moveRight():void
		{
			if(this.x < stage.stageWidth - this.width + (this.width * hideFactor)){
				this.x += speed;
			}
		}
		
		public function moveDown():void
		{
			if(this.y < stage.stageHeight - this.height + (this.height * hideFactor)){
				this.y += speed;
			}
		}
		
		public function moveUp():void
		{
			if(this.y > 0){
				this.y -= speed;
			}
		}
		
		public function fire():void
		{
			this.dispatchEvent(new GameEvent(GameEvent.PLAYER_FIRED,{}));
		}
	}
}