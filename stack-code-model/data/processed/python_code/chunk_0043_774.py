package com.game.unit
{
	import com.Track;
	import com.calculation.SteeredVehicle;
	import com.calculation.Vector2D;
	import com.component.hpbar.HpBar;
	import com.game.unit.core.Finder;
	import com.game.unit.core.Finder2;
	import com.game.unit.core.Properties;
	import com.game.unit.core.RateBehavior;
	
	import flash.geom.Point;
	
	import core.unit.behavior.IAffact;
	import core.unit.behavior.IUnit;
	
	import starling.display.DisplayObject;
	import starling.events.Event;
	
	public class Unit extends SteeredVehicle implements IUnit
	{
		private var _teamId:int=1
		protected var propertys:Properties;
		protected var rateBehavior:RateBehavior;
		protected var finder:Finder;
		private var _track:Track;
		
		protected var bar:HpBar;
		protected var mainDisplay:DisplayObject;
		
		public function Unit(teamId:int=1)
		{
			super();
			_teamId = teamId;
			createFinder();
			createRate();
			propertys = new Properties();
			drawBar();
			
			this.addEventListener(Event.REMOVED_FROM_STAGE,onRemove);
		}
		
		override public function set rotation(value:Number):void{
			mainDisplay.rotation = value + Math.PI/2;
		}
		
		override public function get rotation():Number{
			return mainDisplay.rotation - Math.PI/2;
		}
		
		protected function createFinder():void{
			finder = new Finder2(this);
		}
		
		protected function createRate():void{
			rateBehavior = new RateBehavior();
		}
		
		public function isEnermy(id:int):Boolean{
			return !(_teamId & id);
		}
		
		public function get teamId():int{
			return _teamId;
		}
		
		public function set teamId(value:int):void{
			_teamId = value;
		}
		
		override protected function draw():void
		{
//			display.graphics.clear();
//			if(_teamId==1){
//				display.graphics.beginFill(0xff0000);
//			}
//			if(_teamId==10){
//				display.graphics.beginFill(0x0000ff);
//			}
//			display.graphics.lineStyle(0);
//			display.graphics.moveTo(10, 0);
//			display.graphics.lineTo(-10, 5);
//			display.graphics.lineTo(-10, -5);
//			display.graphics.lineTo(10, 0);
//			display.graphics.endFill();
		}
		
		protected function drawBar():void{
			bar = new HpBar();
			bar.draw(30);
			bar.y = -15;
			addChild(bar);
		}
		
		public function set hp(value:int):void
		{
			propertys.hp = value;
			bar.percentFromProperty(propertys);
		}
		
		public function get hp():int
		{
			return propertys.hp;
		}
		
		public function set hpMax(value:int):void
		{
			propertys.hpMax = value;
			propertys.hp = value;
		}
		
		public function get hpMax():int
		{
			return propertys.hpMax;
		}
		
		public function get attack():int
		{
			return propertys.attack;
		}
		
		public function set attack(value:int):void
		{
			propertys.attack = value;
		}
		
		public function get isProtected():Boolean{
			return propertys.isProtected;
		}
		
		public function set isProtected(value:Boolean):void{
			propertys.isProtected = value;
		}
		
		public function renderTick(tick:int):void
		{
		}
		
		public function resetTick(tick:int=-1):void{
			rateBehavior.resetTick(tick);
		}
		
		public function remove():void{
			dispatchEventWith(Event.REMOVED);
			track.remove(this);
			UnitManager.getInstance().removePos(this);
			this.removeFromParent();
		}
		
		override public function set x(value:Number):void{
			super.x = value;
			finder.gridChangeFlag();
		}
		
		override public function set y(value:Number):void{
			super.y = value;
			finder.gridChangeFlag();
		}
		
		public function get track():Track
		{
			return UnitManager.getInstance().track;
		}
		
		public function coolDown():void
		{
			rateBehavior.coolDown();
		}
		
		public function isCool():Boolean
		{
			return rateBehavior.isCool();
		}
		
		public function set rate(value:int):void
		{
			rateBehavior.rate = value;
		}
		
		public function get rate():int
		{
			return rateBehavior.rate;
		}
		
		public function rateRender(tick:int):void{
			return rateBehavior.rateRender(tick);
		}
		
		public function get percent():Number{
			return rateBehavior.percent;
		}
		
		public function defence(iaffact:IAffact):void{
			this.hp -= iaffact.affactValue;
			if(hp<=0 && parent){
				remove();
			}
		}
		
		public function find(r:int=0):Vector.<IUnit>
		{
			return finder.find(r);
		}
		
		public function set range(value:int):void
		{
			finder.range = value;
		}
		
		public function get range():int
		{
			return finder.range;
		}
		
//		public function prefind():void
//		{
//			finder.prefind();
//		}
		
		public function gridPostion(range:int):Point
		{
			return finder.gridPostion(range);
		}
		
		public function gridChangeFlag():void{
			finder.gridChangeFlag();
		}
		
		protected function onRemove(e:Event):void
		{
			this.removeEventListener(Event.REMOVED_FROM_STAGE,onRemove);
		}
	}
}