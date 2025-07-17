package com.game.unit
{
	import com.calculation.Vector2D;
	import com.game.buddle.Buddle;
	import com.game.buddle.BuddlePool;
	
	import flash.filters.GlowFilter;
	
	import core.unit.behavior.IUnit;
	
	import starling.display.Image;
	import starling.textures.Texture;

	public class Plane extends Unit
	{
//		public static const glowFilter:GlowFilter =  new GlowFilter(0x0000ff,1,2,2);
		protected var target:IUnit;
		protected var targetVec:Vector2D;
		protected var arriveAngle:Number;
		protected var arrivePoint:Vector2D;
		protected var findedVec:Vector.<IUnit>;
		
		protected var moveRate:MoveRate;
		
		public function Plane(teamId:int=1)
		{
			super(teamId);
			touchable = false;
			moveRate = new MoveRate();
			arriveThreshold = 200;
		}
		
		override protected function draw():void{
			var t:Texture = Game.asset.getTexture(imageString);
			var image:Image = new Image(t);
			image.pivotX = image.width>>1;
			image.pivotY = image.height>>1;
			image.scaleX = image.scaleY = 0.2;
			addChild(image);
			mainDisplay = image;
		}
		
		protected function get imageString():String{
			return "BluePlane";			
		}
		
		protected function get buddleString():String{
			return "boom_purple";
		}
		
		protected function get boomString():String{
			return "bz_purple";
		}
		
		protected function targetAvaiable():Boolean{
			return !target || target.hp<=0;
		}
		
		protected function findTarget():void{
			if(targetAvaiable()){
				var vec:Vector.<IUnit> = find(range * 2);
				target = vec.pop();
				if(target){
					targetVec = new Vector2D(target.x,target.y);
					
					if(targetVec.distSQ(position) > range * range){
						arriveAngle = Math.random()*Math.PI/4-Math.PI/8;
						var offset:Vector2D = new Vector2D();
						offset.length = range*0.9;
						var tv:Vector2D = new Vector2D(target.x,target.y);
						var sub:Vector2D = position.subtract(tv);
						offset.angle = sub.angle + arriveAngle;
						arrivePoint = tv.add(offset);
					}else{
						arrivePoint = position.clone();
					}
				}
			}
		}
		
		override public function renderTick(tick:int):void{
			findTarget();
			moveRate.rateRender(tick);
			if(moveRate.isCool()){
				move();
				update();
				moveRate.coolDown();
			}
			rateRender(tick);
			shoot();
			renderTickEnd();
		}
		
		protected function renderTickEnd():void{
			findedVec = null
		}
		
		protected function move():void{
			if(target){
				arrive(arrivePoint);
			}else{
				seek(this.position.add(new Vector2D(maxSpeed,0)));
			}
		}
		
		protected function shoot():void{
			if(isCool()){
//				filters = [glowFilter];
				if(armed){
					var unit:IUnit = findedVec[findedVec.length-1];
					var b:Buddle = createBuddle();
					b.target = unit;
					b.x = this.x;
					b.y = this.y;
					parent.addChild(b);
					track.add(b);
					
					coolDown();
//					filters = null;
				}
			}
		}
		
		protected function get armed():Boolean{
			if(findedVec==null){
				findedVec = find();
			}
			return findedVec.length>0;
		}
		
		protected function createBuddle():Buddle{
			var b:Buddle = BuddlePool.getIns().getNew();
//			var b:Buddle = new Buddle(buddleString,boomString);
			b.affactValue = attack;
			b.maxSpeed = 10;
			return b;
		}
		
		protected function surround(target:Vector2D,angle:Number):Vector2D{
			var offset:Vector2D = new Vector2D();
			if(isCool())
				offset.length = 0.8*range;
			else
				offset.length = range;
			var sub:Vector2D = position.subtract(target);
			offset.angle = sub.angle + angle;
			var endVector:Vector2D = target.add(offset);
			seek(endVector);
			return endVector;
		}
	}
}