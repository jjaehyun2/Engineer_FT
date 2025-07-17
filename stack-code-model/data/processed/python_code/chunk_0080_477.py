package  
{
	import com.greensock.TweenLite;
	import flash.events.Event;
	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;
	import flash.text.TextField;
	import flash.text.TextFormat;
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class PauseWindow extends Window
	{
		public var toContinue:TextField = new TextField();
		
		public var soundText:TextField = new TextField();
		public var soundGraphic:SoundToggle = new SoundToggle();
		
		public function PauseWindow(width:int = 320, height:int = 240, windowTitle:String = "Paused...") 
		{
			super(width, height, windowTitle);
			
			
			soundText.defaultTextFormat = new TextFormat("_typewriter", 20,0xFFFFFF,true,null,null,null,null,"right");
			soundText.text = "Sound: ";
			soundText.x = -width/2 + 5;
			soundText.width = width/2 - 10
			soundText.height = 35;
			soundText.y = 0;
			soundText.selectable = false;
			addChild(soundText);
			
			soundGraphic.x = soundGraphic.width/2;
			soundGraphic.y = soundGraphic.height/2 - 4;
			soundGraphic.gotoAndStop(2);
			soundGraphic.addEventListener(MouseEvent.ROLL_OVER, highlightBox);
			soundGraphic.addEventListener(MouseEvent.ROLL_OUT, unhighlightBox);
			soundGraphic.addEventListener(MouseEvent.CLICK, toggle);
			addChild(soundGraphic);
			
			toContinue.defaultTextFormat = new TextFormat("_typewriter", 14, 0xFFFFFF, true, null, null, null, null, "center");
			toContinue.text = "P to Continue";
			toContinue.x = -width/2 + 5;
			toContinue.width = width - 10
			toContinue.height = 16;
			toContinue.y = height/2 - toContinue.height - 5;
			toContinue.selectable = false;
			//toContinue.border = true;
			//toContinue.borderColor = 0xFFFFFF
			addChild(toContinue);
			
			hookPListener();
		}
		
		private function toggle(e:MouseEvent):void 
		{
			trace("toggle" + soundGraphic.currentFrame);
			if(soundGraphic.currentFrame == 1) soundGraphic.gotoAndStop(2);
			else if(soundGraphic.currentFrame == 2) soundGraphic.gotoAndStop(1);
		}
		
		private function unhighlightBox(e:MouseEvent):void 
		{
			TweenLite.to(e.currentTarget, 2, { glowFilter: { color:0xFFFFFF, blurX:8, blurY:8, strength:2, alpha:0, remove:true }} );
		}
		
		private function highlightBox(e:MouseEvent):void 
		{
			TweenLite.to(e.currentTarget, 0.25, { glowFilter : { color:0xFFFFFF, blurX:8, blurY:8, strength:2, alpha:1 }} );
		}
		
		public function hookPListener():void
		{
			if(stage)
				stage.addEventListener(KeyboardEvent.KEY_DOWN, kDownP);
			else
				addEventListener(Event.ADDED_TO_STAGE, backupAddP);
		}
		private function backupAddP(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, backupAddP);
			stage.addEventListener(KeyboardEvent.KEY_DOWN, kDownP);
		}
		private function kDownP(e:KeyboardEvent):void {
			if (e.keyCode == 80) //P
			{
				removePListener();
				fadeOut();
			}
		}
		private function removePListener():void	{
			stage.removeEventListener(KeyboardEvent.KEY_DOWN, kDownP);
		}
		
	}

}