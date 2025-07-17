package com.game.building.prod
{
	import com.component.menu.Selection;
	import com.game.building.Building;
	import com.game.unit.Plane;
	import com.game.unit.Plane1;
	import com.game.unit.PlaneResource;
	import com.game.unit.Unit;
	
	import core.procedure.IProcedure;
	import core.unit.behavior.IUnit;
	
	import starling.display.Canvas;
	import starling.display.Image;
	import starling.events.Event;
	import starling.events.EventDispatcher;
	
	public class Producter1 extends Building implements IProcedure
	{
		private var planeList:Vector.<IUnit>;

		protected var currentPlane:Unit;
		protected var maxCount:int;
		protected var tickCountArray:Array;
		protected var maxCountArray:Array;
//		protected var priceArray:Array;
		protected var _price:int = -1;
		
		public function Producter1()
		{
			planeList = new Vector.<IUnit>;
			setTickCount();
			setMaxCount();
			rate = tickCountArray[0];
			maxCount = maxCountArray[0];
		}
		
//		protected function setPrice():void{
//			priceArray = [120,150,180,210];
//		}
		
		protected function setTickCount():void{
//			tickCountArray = [3000,2800,2600,2400,2200];
			tickCountArray = [500,500,500,500,500];
		}
		
		protected function setMaxCount():void{
//			maxCountArray = [1,2,2,2,3];
			maxCountArray = [2,3,4,5,6];
		}
		
		override public function getSelection():Vector.<Selection>{
			var selections:Vector.<Selection> = new Vector.<Selection>;
			if(canUpgrade()){
				var upgradeSelection:Selection = new Selection();
//				upgradeSelection.text = "lv+(" + price+")";
				upgradeSelection.text = price.toString();
				upgradeSelection.icon = "upgrade";
				upgradeSelection.func = upgrade;
				selections.push(upgradeSelection);
			}
			
			var sell:Selection = new Selection();
			sell.text = sellPrice.toString();
			sell.icon = "sell";
			sell.func = onSell;
			selections.push(sell);
			
			return selections;
		}
		
		public function canUpgrade():Boolean{
			return buildingLevel<5;
		}
		
		override public function upgrade():Boolean{
			if(canUpgrade() && UnitManager.getInstance().moneyCost(price)){
				buildPrice += price;
				buildingLevel++;
				_price = -1;
				return true;
			}
			return false;
		}
		
		private function onSell():void
		{
			UnitManager.getInstance().moneyAdd(sellPrice);
			UnitManager.getInstance().removeBuild(this);
			remove();
		}
		
		override public function remove():void{
			dispatchEventWith(Event.REMOVED);
			track.remove(this);
			this.removeFromParent();
			
			for each(var p:Plane in planeList){
				p.removeEventListeners(Event.REMOVED);
			}
		}
		
		public function get price():int{
			if(_price == -1){
				_price = BatteryDataFactory.GetPrice(type,buildingLevel);
			}
			return _price;
		}
		
		public function get sellPrice():int{
			return buildPrice * 0.7;
		}
		
		private function get countRate():int{
			var value:int = tickCountArray[buildingLevel-1];
			return Research.getInstance().valueChange(Research.RESEARCH_4,value);
		}
		
		override public function set buildingLevel(value:int):void{
			super.buildingLevel = value;
			rate = countRate;
			maxCount = maxCountArray[buildingLevel-1];
		}
		
		override protected function draw():void{
			var imgName:String = Factory.SwitchUrl(type);
			var img:Image = new Image(Game.asset.getTexture(imgName));
			img.pivotX = img.width>>1;
			img.pivotY = img.height>>1;
			addChild(img);
//			var canvas:Canvas = new Canvas();
//			canvas.beginFill(color);
//			canvas.drawRectangle(-10,-10,20,20);
//			canvas.endFill();
//			addChild(canvas);
		}
		
		protected function get color():uint{
			return Factory.SwitchColor(type);
		}
		
		protected function get type():String{
			return Factory.P1;
		}
		
		override public function renderTick(tick:int):void
		{
//			if(!isStart) return;
			if(planeList.length<maxCount){
				if(isCool()){
					createPlane();
					BatteryDataFactory.SetObjectProperty(currentPlane,buildingLevel);
					
					currentPlane.x = this.x;
					currentPlane.y = this.y;
					
					UnitManager.getInstance().sceneSprite.addChild(currentPlane);
					track.add(currentPlane);
					
					UnitManager.getInstance().addPos(currentPlane);
					planeList.push(currentPlane);
					currentPlane.addEventListener(Event.REMOVED,removePlane);
					coolDown();
				}
			}
			rateRender(tick);
		}
		
		protected function createPlane():void{
			currentPlane = new Plane1();
//			currentPlane = new PlaneResource(this);
		}
		
		protected function removePlane(event:Event):void
		{
			(event.currentTarget as EventDispatcher).removeEventListener(Event.REMOVED,onRemove);
			var index:int = planeList.indexOf(event.target as IUnit);
			if(index != -1){
				planeList.splice(index,1);
			}
		}
	}
}