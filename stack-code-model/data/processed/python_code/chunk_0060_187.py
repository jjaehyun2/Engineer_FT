package {
	import flash.display.Sprite;
	import flash.display.Stage;
	import flash.display.StageAlign;
	import flash.display.StageDisplayState;
	import flash.display.StageQuality;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.events.MouseEvent;


 	[SWF(backgroundColor="0xaaaaa3", frameRate="100" )]
 	
 	
	public class NormanJ extends Sprite
	{
		
		
		[Embed(source='assets/fonts/gotham.swf', symbol='gotham' )]
		public static const FONT_HAMBURGER:String;
		
		[Embed(source='assets/fonts/clarendonLight.swf', symbol='clarendonLight' )]
		public static const FONT_HAMBURGER1:String;
		
		[Embed(source='assets/fonts/clarendonNormal.swf', symbol='clarendonNormal' )]
		public static const FONT_HAMBURGER2:String;
		
		[Embed(source='assets/fonts/gothamBook.swf', symbol='gothamBook' )]
		public static const FONT_HAMBURGER3:String;
		
		
		private var _bg:Background = new Background();
		private var contact:Contact = new Contact;
		private var menuManager:MenuManager;
		
		public function NormanJ()
		{
			 this.addEventListener(Event.ADDED_TO_STAGE, init,false, 0, true);
		}
		
		private function init(e:Event):void
		{
			stage.align = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.NO_SCALE;
			stage.quality = StageQuality.BEST;	
			
			
			_bg.createBg();
			_bg.mc.x = (stage.stageWidth-_bg.mc.width)/2;
			_bg.mc.y = (stage.stageHeight-_bg.mc.height)/2;
			this.addChild(_bg.mc);
			stage.addEventListener(Event.RESIZE, onResize);			
			
			
			
			contact = new Contact;
			contact.createContact();
			this.addChild(contact.mc);
			contact.mc.x = bg.mc.x + 680;
			contact.mc.y = bg.mc.y + 35;
			
			menuManager = new MenuManager(bg,contact,this);
			menuManager.createMenu();
			menuManager.turnOnLinks();
			this.addChild(menuManager.mc);
			menuManager.mc.x = _bg.mc.x;
			menuManager.mc.y = _bg.mc.y ;
			
		
			stage.addEventListener(MouseEvent.CLICK, _handleClick)
			
			
		}
		
		
		private function goFullScreen():void
		{
			if (stage.displayState == StageDisplayState.NORMAL) {
			stage.displayState=StageDisplayState.FULL_SCREEN;
			} else {
			stage.displayState=StageDisplayState.NORMAL;
			}
		}
		
		
		

		private function _handleClick(event:MouseEvent):void
		{
		goFullScreen();
		}


		public function get bg():Background
		{
			return _bg;
		}
		
		public function get _stage():Stage
		{
			return stage;
		}//endfunction
		private function onResize(e:Event):void
		{
			bg.mc.x = (stage.stageWidth-bg.mc.width)/2;
			bg.mc.y = (stage.stageHeight-bg.mc.height)/2;
			menuManager.mc.x = bg.mc.x ;
			menuManager.mc.y = bg.mc.y ;
			contact.mc.x = bg.mc.x + 680;
			contact.mc.y = bg.mc.y + 35;
			
			
			
			
		}
		
	}
}