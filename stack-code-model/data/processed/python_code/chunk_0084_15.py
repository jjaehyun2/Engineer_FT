package com.illuzor.notificationTest {
	
	import adobe.utils.CustomActions;
	import com.illuzor.notification.NotificationInterface;
	import flash.desktop.NativeApplication;
	import flash.display.SimpleButton;
	import flash.events.Event;
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.text.TextField;
	import flash.ui.Multitouch;
	import flash.ui.MultitouchInputMode;
	import flash.text.TextFieldAutoSize;
	import flash.events.MouseEvent;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	public class Main extends Sprite {
		
		private var notification:NotificationInterface;
		
		public function Main():void {
			stage.scaleMode = StageScaleMode.NO_SCALE;
			stage.align = StageAlign.TOP_LEFT;
			stage.addEventListener(Event.DEACTIVATE, deactivate);
			trace("start")
			// touch or gesture?
			Multitouch.inputMode = MultitouchInputMode.TOUCH_POINT;
			
			var textButton:TextField = new TextField();
			textButton.autoSize = TextFieldAutoSize.LEFT;
			textButton.text = "ShowMessage";
			addChild(textButton);
			
			textButton.scaleX = textButton.scaleY = 5;
			textButton.y = 100;
			textButton.x = (stage.stageWidth - textButton.width) / 2;
			textButton.border = true;
			textButton.selectable = false;
			textButton.addEventListener(MouseEvent.CLICK, onClick);
			notification = new NotificationInterface();
			// entry point
			trace("Notification created")
			// new to AIR? please read *carefully* the readme.txt files!
		}
		
		private function onClick(e:MouseEvent):void {
			trace("click");
	
			notification.notify("Hello!")
		}
		
		private function deactivate(e:Event):void {
			// auto-close
			NativeApplication.nativeApplication.exit();
		}
		
	}
	
}