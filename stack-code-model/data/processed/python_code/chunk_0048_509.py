package com.game.unit.core
{
	import core.unit.behavior.ITeamate;
	import core.unit.behavior.IUnit;
	
	import flash.display.DisplayObject;
	
	public class FinderNull extends Finder
	{
		public function FinderNull(unit:IUnit)
		{
			super(unit);
		}
		
		override public function find(r:int=0):Vector.<IUnit>{
			return null;
		}
	}
}