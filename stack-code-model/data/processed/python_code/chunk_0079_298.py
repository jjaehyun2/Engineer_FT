package com.game.unit
{
	import com.game.unit.core.RateBehavior;
	
	import core.unit.behavior.IUnit;
	
	import starling.events.Event;
	import starling.events.EventDispatcher;

	public class PlaneMore extends Plane
	{
		private var planeList:Vector.<IUnit>;
		
		private var produce:Boolean = true;
		
		private var stopRate:RateBehavior = new RateBehavior();
		
		public function PlaneMore(teamId:int=1)
		{
			super(teamId);
			planeList = new Vector.<IUnit>;
			
			stopRate = new RateBehavior();
			stopRate.rate = 5000;
			
			maxSpeed = 1;
			mass = 50;
		}
		
		override protected function draw():void{
			super.draw();
			mainDisplay.scaleX = mainDisplay.scaleY = 0.3;
		}
		
		override protected function get imageString():String{
			return "JitPlane";
		}
		
		override public function rateRender(tick:int):void{
			if(produce){
				stopRate.rateRender(tick);
				if(stopRate.isCool()){
					super.rateRender(tick);
				}
			}
		}
		
		override protected function shoot():void{
			if(planeList.length<5 && isCool()){
				var currentPlane:Plane1 = new Plane1();
				BatteryDataFactory.SetObjectProperty(currentPlane,1);
				currentPlane.x = this.x;
				currentPlane.y = this.y;
				
				UnitManager.getInstance().sceneSprite.addChild(currentPlane);
				track.add(currentPlane);
				
				UnitManager.getInstance().addPos(currentPlane);
				planeList.push(currentPlane);
				currentPlane.addEventListener(Event.REMOVED,onRemovePlane);
				coolDown();
				
				if(planeList.length == 5){
					produce = false;
				}
			}
		}
		
		protected function onRemovePlane(event:Event):void
		{
			(event.currentTarget as EventDispatcher).removeEventListener(Event.REMOVED,onRemove);
			var index:int = planeList.indexOf(event.target as IUnit);
			if(index != -1){
				planeList.splice(index,1);
				
				if(planeList.length == 0){
					produce = true;
					stopRate.resetTick();
					stopRate.coolDown();
				}
			}
		}
		
		override public function remove():void{
			for each(var p:Plane in planeList){
				p.removeEventListeners(Event.REMOVED);
			}
			super.remove();
		}
	}
}