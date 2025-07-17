package com.game.building
{
	import com.component.menu.Selection;
	import com.game.unit.Unit;
	
	import core.procedure.IMenu;
	
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;
	
	public class Building extends Unit implements IMenu
	{
		private var _buildingLevel:int=1;
		public var dx:int;
		public var dy:int;
		public var buildPrice:int;
		public function Building(teamId:int=1)
		{
			super(teamId);
			
			
//			addEventListener(MouseEvent.CLICK,onClick);
			addEventListener(TouchEvent.TOUCH,onTouch);
			
			touchGroup = true;
		}
		
		public function get buildingLevel():int
		{
			return _buildingLevel;
		}

		public function set buildingLevel(value:int):void
		{
			_buildingLevel = value;
		}
		
		public function upgrade():Boolean{
			return null;
		}

		public function getSelection():Vector.<Selection>
		{
			return null;
		}
		
		protected function onTouch(event:TouchEvent):void
		{
			var touch:Touch = event.getTouch(this,TouchPhase.ENDED);
			if(touch){
				UnitManager.getInstance().menuCircle.focus(this,parent.x,parent.y);
			}
		}
	}
}