package com.utilities
{
	import flash.events.MouseEvent;
    import flash.net.*;
	/**
	 * ...
	 * @author Ian Stokes www.unit2design.com 2010
	 */
	public class LinkButtons
	{
	static public function getUrl(str:String):void{
		var request:URLRequest = new URLRequest(str);
		navigateToURL(request,"_blank");
	}
    static public function getUrlSelf(str:String):void{
    	var request:URLRequest = new URLRequest(str);
		navigateToURL(request,"_self");
	}
	static public function getZip(str:String):void{
	   var request:URLRequest = new URLRequest(str);
	   navigateToURL(request);
	}	
	}
}