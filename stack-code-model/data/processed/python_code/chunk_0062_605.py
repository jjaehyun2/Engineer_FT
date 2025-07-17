package com.illuzor.otherside.controllers.storage {
	
	import com.illuzor.otherside.interfaces.IStorageController;
	import flash.net.SharedObject;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	internal final class StorageControllerFlash implements IStorageController {
		
		private var settings:SharedObject;
		
		public function init():void {
			settings = SharedObject.getLocal("OtherSideSavedata");
		}
		
		public function increaseRuns():void {
			
		}
		
		public function setBool(name:String, value:Boolean):void {
			
		}
		
		public function getBool(name:String):Boolean {
			return false;
		}
		
		public function setInt(name:String, value:int):void {
			
		}
		
		public function getInt(name:String):int {
			return 0;
		}
		
		public function setObj(name:String, value:Object):void {
			
		}
		
		public function getObj(name:String):Object {
			return null;
		}
		
	}
}