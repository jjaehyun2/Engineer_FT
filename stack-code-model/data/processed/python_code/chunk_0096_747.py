package com.game.building
{
	import com.game.buddle.Buddle;
	import com.game.buddle.BuddleArea;
	import com.game.buddle.BuddleFly;
	import com.game.buddle.BuddleJump;
	import com.game.buddle.BuddlePool;
	
	import core.unit.behavior.IAffact;
	import core.unit.behavior.IUnit;
	
	import starling.display.Image;
	
	public class BatteryNormal extends Building
	{
		public var buddle:int=0;
		public var drop:int=0;
		
		public function BatteryNormal(teamId:int=10)
		{
			super(teamId);
			
		}
		
		override protected function draw():void{
			var battery:Image = new Image(Game.asset.getTexture("battery"));
			battery.pivotX = battery.width>>1;
			battery.pivotY = battery.height>>1;
			battery.rotation = -Math.PI/2;
			addChild(battery);
			
			mainDisplay = battery;
		}
		
		override public function renderTick(tick:int):void{
			rateRender(tick);
			if(isCool()){
				var vec:Vector.<IUnit> = find();
				if(vec && vec.length>0){
					var index:int = vec.length * Math.random();
					var unit:IUnit = vec[index];
					var b:Buddle = createBuddle();
					b.target = unit;
					
					var dx:Number = unit.x - this.x;
					var dy:Number = unit.y - this.y;
					rotation = Math.atan2(dy,dx);
					
					coolDown();
				}
			}
		}
		
		override public function defence(iaffact:IAffact):void{
			if(this.hp>0){
				this.hp -= iaffact.affactValue;
				if(hp<=0){
					var coin:Coin = new Coin(drop);
					coin.x = this.x + int(Math.random() * 20) - 10;
					coin.y = this.y - int(Math.random() * 20) - 30;
					parent.addChild(coin);
					UnitManager.getInstance().coins.push(coin);
					remove();
				}
			}
		}
		
		protected function createBuddle():Buddle
		{
			var b:Buddle;
			switch(buddle){
				case 0:
					b = BuddlePool.getIns().getNew();
					break;
				case 1:
					b = new BuddleArea();
					break;
				case 2:
					b = new BuddleJump();
					break;
				case 3:
					b = new BuddleFly();
					break;
				default:
					b = BuddlePool.getIns().getNew();
			}
			b.affactValue = attack;
			b.x = this.x;
			b.y = this.y;
			parent.addChild(b);
			track.add(b);
			return b;
		}
	}
}