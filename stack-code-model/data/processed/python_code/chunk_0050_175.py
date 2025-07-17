package com.as3long.node.native.http 
{
	/**
	 * ...
	 * @author 黄龙
	 */
	public class BaseNativeObject 
	{
		
		public function BaseNativeObject(nativeObject:*) 
		{
			initObject(nativeObject);
		}
		
		public function initObject(obj:Object):void
		{
			for (var key:String in obj)
			{
				this[key] = obj[key];
			}
		}
		
	}

}