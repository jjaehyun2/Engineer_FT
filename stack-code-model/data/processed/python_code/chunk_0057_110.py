package com.game.unit
{
	import com.calculation.Vector2D;
	import com.game.buddle.CoingetEffect;
	import com.game.building.Coin;
	import com.game.building.prod.Producter1;
	
	/**
	 * 可以采集资源的飞机 
	 */	
	public class PlaneResource extends Plane
	{
		
		public var hasResource:Boolean = false;
		private var allCoin:Vector.<Coin> = UnitManager.getInstance().coins;
		private var targetCoin:Coin;
		private var coinValue:int;
		private var savePoint:Vector2D;
		private const BackRange:Number = 20;
		private const FarRange:Number = 400;
		private var rangeFlag:Boolean = false;
		private var rangeGet:Boolean = false;
		private var rangeGetCount:int = 0;
		public function PlaneResource(pro:Producter1,rangeFlag:Boolean,teamId:int=1)
		{
			super(teamId);
			this.rangeFlag = rangeFlag;
			savePoint = new Vector2D(pro.x,pro.y);
		}
		
		override protected function findTarget():void{
			if(!hasResource){
				if(targetCoin==null && allCoin.length==0){
					super.findTarget();
				}else if(targetCoin==null){
					targetCoin = allCoin.pop();
					targetVec = new Vector2D(targetCoin.x,targetCoin.y);
					
					if(targetVec.distSQ(position) > FarRange * FarRange){
						arriveAngle = Math.random()*Math.PI/4-Math.PI/8;
						var offset:Vector2D = new Vector2D();
						offset.length = resRange * 0.8;
						var tv:Vector2D = new Vector2D(targetCoin.x,targetCoin.y);
						var sub:Vector2D = position.subtract(tv);
						offset.angle = sub.angle + arriveAngle;
						arrivePoint = tv.add(offset);
					}else{
						arrivePoint = position.clone();
					}
				}
			}
		}
		
		override public function rateRender(tick:int):void{
			super.rateRender(tick);
			renderEffect(tick);
		}
		
		override protected function move():void{
			if(hasResource){
				arrive(savePoint);
			}
			else if(targetCoin || target){
				arrive(arrivePoint);
			}else{
				seek(this.position.add(new Vector2D(maxSpeed,0)));
			}
		}
		
		override public function update():void{
			super.update();
			
			if(rangeGet){
				if(rangeGetCount < 0){
					var dx:Number = this.x - targetCoin.x;
					var dy:Number = this.y - targetCoin.y;
					
					if(position.distSQ(new Vector2D(targetCoin.x,targetCoin.y)) > BackRange*BackRange){
						var angle:Number = Math.atan2(dy,dx);
						var tx:Number = Math.cos(angle) * 1;
						var ty:Number = Math.sin(angle) * 1;
						targetCoin.x += tx;
						targetCoin.y += ty;
						coinEffect.updateImage();
					}else{
						rangeGet = false;
						coinEffect.stop();
						coinPick();
					}
				}else{
					rangeGetCount--;
				}
				
			}
			else if(hasResource){
				if(Math.abs(this.x - savePoint.x) < BackRange
					|| Math.abs(this.y - savePoint.y) < BackRange
				)
				{
					if(position.distSQ(savePoint) < BackRange * BackRange){
						hasResource = false;
						UnitManager.getInstance().moneyAdd(coinValue);
					}
				}
			}
			else if(targetCoin){ 
				if(Math.abs(this.x - targetCoin.x) < resRange
					|| Math.abs(this.y - targetCoin.y) < resRange)
				{
					if(position.distSQ(targetVec) < resRange * resRange){
						if(rangeFlag){
							rangeGet = true;
							rangeGetCount = 20;
							coinEffect.setTarget(targetCoin);
							coinEffect.x = this.x;
							coinEffect.y = this.y;
							coinEffect.updateImage();
							coinEffect.start();
						}
						else{
							coinPick();
						}
					}
				}
			}
		}
		
		protected function coinPick():void{
			hasResource = true;
			coinValue = targetCoin.value;
			targetCoin.removeFromParent();
			targetCoin = null;
		}
		
		protected function get resRange():Number{
			if(rangeFlag){
				return FarRange;
			}else{
				return BackRange;
			}
		}
		
		override protected function shoot():void{
			if(targetCoin || hasResource){
				
			}else{
				super.shoot();
			}
		}
		
		override public function remove():void{
			if(hasResource){
				var coin:Coin = new Coin(coinValue);
				coin.x = this.x;
				coin.y = this.y;
				allCoin.push(coin);
				this.parent.addChild(coin);
			}
			
			else if(targetCoin){
				allCoin.push(targetCoin);
			}
			
			if(_ce){
				_ce.removeFromParent();
			}
			
			super.remove();
		}
		
		protected var _ce:CoingetEffect;
		protected function get coinEffect():CoingetEffect{
			if(_ce == null){
				_ce = new CoingetEffect();
				parent.addChild(_ce);
			}
			return _ce;
		}
		protected function renderEffect(tick:int):void{
			if(_ce!=null){
				_ce.x = this.x;
				_ce.y = this.y;
				_ce.renderTick(tick);
			}
		}
	}
}