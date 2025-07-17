package org.openPyro.skins{
	import org.openPyro.core.UIControl;
	
	import flash.display.IBitmapDrawable;
	
	/**
	 * Defines an interface that all DisplayObjects
	 * that can be applied as Skins to OpenPyro controls
	 */ 
	public interface ISkin extends IBitmapDrawable{
		
		//function get selector():String;
		
		function set skinnedControl(uic:UIControl):void;
		function dispose():void;
		
	}
}