package com.lowoui_as 
{
	public class Global
	{
		//Entry
		public static var manager:Object;
		//lobby
		public static var lobbyManager:Object;
		//battle
		public static var hudManager:Object;
		//comn
		public static var dialogManager:Object;

		public static var minimapManager:Object;
		public static var selectCharaterManager:Object;
		
		
		//cache
		//public static var currScene:String;
		
		public static var currMenuSelect:String;
		public static var escObjArr:Array;
		public static var isTabPanelShow:Boolean;
		public static var isGameOptionShow:Boolean;
		
		//keyboard state
		public static var isAltKeyPressed:Boolean;
		public static var isKeyLock:Boolean;
		
		//settings
		public static var isGfxMode:Boolean = false;//or flash mode
		public static var isTestMode:Boolean = false;
	}
}