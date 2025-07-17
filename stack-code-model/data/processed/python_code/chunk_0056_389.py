package com.game.buddle
{
	import com.Track;
	import com.calculation.SteeredVehicle;
	import com.calculation.Vector2D;
	import com.game.unit.MoveRate;
	
	import core.procedure.IProcedure;
	import core.unit.behavior.IAffact;
	import core.unit.behavior.IUnit;
	
	import starling.core.Starling;
	import starling.display.MovieClip;
	import starling.events.Event;
	
	public class Buddle extends SteeredVehicle implements IAffact,IProcedure
	{
		private var _target:IUnit;
		private var _affactValue:int;
		private var _isProtected:Boolean = false;
		
		protected var buddleString:String;
		protected var boomString:String;
		
		protected var moveRate:MoveRate;

		private var mc:MovieClip;

		private var boom:MovieClip;
		
		public function Buddle(buddleString:String="boom_purple",boomString:String="bz_purple")
		{
			this.buddleString = buddleString;
			this.boomString = boomString;
			super();
			
			moveRate = new MoveRate();
			
			draw();
			setProperty();
		}
		
		protected function setProperty():void{
			maxForce = maxSpeed = 50;
			mass = 1;
			maxSpeed = 5;
		}
		
		override public function set rotation(value:Number):void{
			super.rotation = value + Math.PI/2;
		}
		
		override protected function draw():void
		{
			mc = new MovieClip(Game.asset.getTextures(buddleString),8);
			mc.pivotX = mc.width >> 1;
			mc.pivotY = 2;
			mc.scaleX = mc.scaleY = 0.2;
			addChild(mc);
			Starling.juggler.add(mc);
			
			boom = new MovieClip(Game.asset.getTextures(boomString),24);
		}
		
		public function get affactValue():int
		{
			return _affactValue;
		}
		
		public function set affactValue(value:int):void
		{
			_affactValue = value;
		}
//		private var lifeCount:int = 50;
		public function renderTick(tick:int):void
		{
			moveTick(tick);
			update();
			
			if(isHit){
				boom.x = target.x;
				boom.y = target.y;
				boom.pivotX = boom.width>>1;
				boom.pivotY = boom.height>>1;
				boom.scaleX = boom.scaleY = 0.2;
				parent.addChild(boom);
				Starling.juggler.add(boom);
				
				boom.addEventListener(Event.COMPLETE,function():void{
					boom.removeEventListeners(Event.COMPLETE);
					boom.removeFromParent();
					Starling.juggler.remove(boom);
				});
				
				target.defence(this);
				remove();
			}
//			lifeCount--;
//			if(lifeCount == 0){
//				this.parent.removeChild(this);
//				track.remove(this);
//			}
		}
		
		protected function get isHit():Boolean{
			return Math.abs(this.x - target.x) <= Math.abs(velocity.x) && Math.abs(this.y - target.y) <= Math.abs(velocity.y);
		}
		
		protected function move():void{
			seek(new Vector2D(target.x,target.y));
		}
		
		private function moveTick(tick:int):void
		{
			moveRate.rateRender(tick);
			if(moveRate.isCool()){
				move();
				update();
				moveRate.coolDown();
			}
		}
		
		public function get track():Track
		{
			return UnitManager.getInstance().track;
		}
		
		public function get isProtected():Boolean
		{
			return _isProtected;
		}
		
		public function set isProtected(value:Boolean):void
		{
			_isProtected = value;
		}
		
		public function get target():IUnit
		{
			return _target;
		}
		
		public function set target(value:IUnit):void
		{
			_target = value;
		}
		
		public function remove():void{
			Starling.juggler.remove(mc);
			this.removeFromParent();
			track.remove(this);
			BuddlePool.getIns().restore(this);
		}
		
		public function reuse():void{
			Starling.juggler.add(mc);
		}
	}
}