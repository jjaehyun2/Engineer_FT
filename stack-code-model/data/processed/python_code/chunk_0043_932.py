package com.demy.waterslide 
{
	/**
	 * ...
	 * @author 
	 */
	public class GameStage 
	{
		private var _name:String;
		
		public function GameStage(name:String) 
		{
			_name = name;
		}
		
		public function setName(value:String):void
		{
			_name = value;
		}
		
		public function get name():String 
		{
			return _name;
		}
		
	}

}