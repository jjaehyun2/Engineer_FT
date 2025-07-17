package com.lowoui_as.component 
{
	import flash.display.Sprite;
	import flash.display.Loader;
	import flash.net.URLRequest;
	//import flash.events.Event;
	//import com.business.constants.Hud;
	
	public class LoaderIMG2 extends Sprite
	{
		private var loader:Loader;
		private var imgWidth:Number;
		private var imgHeight:Number;
		
		public function LoaderIMG2() 
		{
			imgWidth = 64;
			imgHeight = 64;
		}
		
		private function initLoader()
		{
			loader = new Loader();			
			loader.x = -imgWidth/2;
			loader.y = -imgHeight/2;
			this.addChild(loader);
		}
		public function load(url:String):void 
		{
			if (url == null||url == "") 
			{
				visible = false;
				return;
			}
			else
			{
				if (loader == null) { initLoader(); }
				
				loader.unload();
				
				visible = true;
				loader.load( new URLRequest(url) );
				//loader.contentLoaderInfo.addEventListener(Event.COMPLETE, loadComplete, false, 0, true );
			}           
		}
		/*private function loadComplete(evt:Event) : void
		{
			var obj:Object = evt.target.content;
			obj.x = -obj.width/2;
			obj.y = -obj.height/2;
		}*/
	}

}