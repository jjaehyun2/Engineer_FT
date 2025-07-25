﻿package  {
	
	import flash.system.Security;
	import flash.display.*;
	import flash.events.*;
	import pano.ExtraInterface;
	import flash.net.*;
	import flash.filters.GlowFilter;
	
	public class Logo extends Sprite{
		
		private var EIF:ExtraInterface;
		private var logo:logoSprite;
		private var url:String;
		
		private const VER:String = "1.20140501";
		public function Logo()
		{
			Security.allowDomain("*");
			EIF = ExtraInterface.getInstance();
			//stage.scaleMode = StageScaleMode.NO_SCALE
			if (stage == null)
			{
				this.addEventListener(Event.ADDED_TO_STAGE, this.startPlugin);
				this.addEventListener(Event.REMOVED_FROM_STAGE, this.stopPlugin);
			}else
			{
				this.startPlugin();
			}
		}
		
		private function startPlugin(e:Event = null):void
		{
			//this.alpha = 0;this.visible = false;
			stage.showDefaultContextMenu = false;
			EIF = ExtraInterface.getInstance();
			
			if(EIF.ready) 
			{
				EIF.trace((new Date).toLocaleTimeString()+" : Loading Logo(Ver "+VER+") Plugin ... ");
				EIF.addPluginEventListener(ExtraInterface.PLUGINEVENT_REGISTER, this.registerEvent);
			}
			
		}
		
		private function stopPlugin(e):void
		{
			EIF.trace((new Date).toLocaleTimeString()+" : UnLoad Logo Plugin Success !");
		}
		
		private function registerEvent(e):void
		{
			url = EIF.call("getPluginsConfig" , "logo").url;
			logo = new logoSprite();
			//logo.filter = [new GlowFilter(0xffffff,0.8,4,4,2,2)]
			addChild(logo);
			resize();
			stage.addEventListener(Event.RESIZE, resizeHandler,false,0,true);
			addEventListener(MouseEvent.CLICK, clickHandler,false,0,true);
		}
		
		private function resizeHandler(e):void
		{
			resize()
		}
		
		private function clickHandler(e):void
		{
			EIF.trace( "goto : "+ url );
			navigateToURL(new URLRequest(url),"_blank");
		}
		
		public function resize():void
		{
			var w = this.stage.stageWidth;
			var h = this.stage.stageHeight;
			
			this.x = w - logo.width - 20;
			this.y = 20;
			
			//this.x = (550 + w)/2 - logo.width - 20
			//this.y = (400 - h)/2 + 20;
			//trace("LOGO RESIZE :: "+this.x + ":"+this.y)
			//_pano.height = h - 125;
			//_pano.x = (550  - w)/2 + 345;
			//_pano.y = (400  -  h)/2;
			//thumb.x = w - thumb.width - 10;
			//thumb.y = h - thumb.height - 10;
		}

	}
	
}