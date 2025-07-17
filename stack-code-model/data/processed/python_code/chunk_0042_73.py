package com.game.unit.core
{
	import flash.geom.Point;
	
	import core.unit.behavior.IFindable;
	import core.unit.behavior.IUnit;
	
	/**
	 * 范围寻敌
	 */	
	public class Finder extends GridPos implements IFindable
	{
		protected var _range:int;
		protected var _ifindable:IFindable;
		protected var allUnit:Vector.<IUnit>;
		public function Finder(unit:IFindable)
		{
			allUnit = UnitManager.getInstance().list;
			_ifindable = unit;
			super(_ifindable);
		}
		
//		private function prefind():void{
//			var prefindUnit:Vector.<IUnit> = new Vector.<IUnit>;
//			for(var i:int=0;i<allUnit.length;i++){
//				var u:IUnit = allUnit[i];
//				var selfPoint:Point = gridPostion(_range);
//				var targetPoint:Point = u.gridPostion(_range);
//				if(Math.abs(selfPoint.x-targetPoint.x)<=1 && Math.abs(selfPoint.y-targetPoint.y)<=1){
//					prefindUnit.push(u);
//				}
//			}
//		}
		
		public function find(r:int=0):Vector.<IUnit>
		{
			if(r==0){
				r = _range; 
			}
			var prefindUnit:Vector.<IUnit> = new Vector.<IUnit>;
			for(var i:int=0;i<allUnit.length;i++){
				var u:IUnit = allUnit[i];
				var selfPoint:Point = gridPostion(r);
				var targetPoint:Point = u.gridPostion(r);
				if(Math.abs(selfPoint.x-targetPoint.x)<=1 && Math.abs(selfPoint.y-targetPoint.y)<=1){
					prefindUnit.push(u);
				}
			}
			
			var vec:Vector.<IUnit> = new Vector.<IUnit>;
			for each(var unit:IUnit in prefindUnit){
				if(typeFix(unit)){
					var dx:Number = Math.abs(_ifindable.x - unit.x);
					var dy:Number = Math.abs(_ifindable.y - unit.y);
					var len:Number = r/1.42
					if(dx < len && dy < len){
						vec.push(unit);
					}else if(r>Math.sqrt(dx*dx+dy*dy)){
						vec.push(unit);
					}
				}
			}
			return vec;
		}
		
		protected function typeFix(unit:IUnit):Boolean{
			return _ifindable.isEnermy(unit.teamId);
		}
		
		public function get range():int{
			return _range;
		}
		
		public function set range(value:int):void{
			_range = value;
		}
		
		public function isEnermy(id:int):Boolean
		{
			return _ifindable.isEnermy(id);
		}
		
		public function get teamId():int
		{
			return _ifindable.teamId;
		}
		
		public function set teamId(value:int):void
		{
			_ifindable.teamId = value;
		}
		
	}
}