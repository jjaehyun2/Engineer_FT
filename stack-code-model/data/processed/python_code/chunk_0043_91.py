﻿package
{
	import flash.desktop.NativeApplication;
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;
	
	
	public class VectorHWAExample extends MovieClip
	{
		
		public function VectorHWAExample()
		{
			//listens for when the application looses focus
			NativeApplication.nativeApplication.addEventListener(Event.DEACTIVATE, onDeactivate);
			addEventListener(Event.ADDED, onAddedToStage);
		}
		
		private function onAddedToStage(e:Event):void
		{
			removeEventListener(Event.ADDED, onAddedToStage);
			addEventListener(Event.ENTER_FRAME, onEnterFrame);
			stage.addEventListener(MouseEvent.MOUSE_DOWN, onMouseDown);
			stage.addEventListener(MouseEvent.MOUSE_UP, onMouseUp);
		}
		
		//called when application looses focus
		private function onDeactivate(e:Event):void
		{
			//close the application
			//we could put some code on here to no close if running on the desktop
			NativeApplication.nativeApplication.exit();
		}
		
		private var mouseIsDown:Boolean = false;
		private function onMouseDown(e:MouseEvent):void
		{
			mouseIsDown = true;
		}
		
		private function onMouseUp(e:MouseEvent):void
		{
			mouseIsDown = false;
		}
		
		private function onEnterFrame(e:Event):void
		{
			if(!mouseIsDown)
			{
				return;
			}
			
			var s:Square = new Square();
			s.x = stage.mouseX;
			s.y = stage.mouseY;
			
			addChild(s);
		}
		
		
	}
	
}