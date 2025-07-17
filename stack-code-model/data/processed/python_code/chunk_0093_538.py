package gui
{
	import flash.display.Sprite;
	import flash.geom.Matrix;
	import flash.geom.Rectangle;
	import flash.events.Event;
	import flash.events.MouseEvent;

	public class VideoSpeakerSlide extends VideoControlSlide
	{
		public function VideoSpeakerSlide( width : uint )
		{
			super( width );
			
			addEventListener( MouseEvent.MOUSE_DOWN, onMouseDown );
		}
		
		private function onMouseDown( event : MouseEvent ):void
		{
			var limit_length : uint = length - 1;
			if ( mouseX > limit_length )
			{
				spriteValue.width = limit_length;
				return;
			}
			else if ( mouseX <= 0)
			{
				spriteValue.width = 0;
				return;
			}
			else
			{
				spriteValue.width = mouseX;
			}
			
			stage.addEventListener( MouseEvent.MOUSE_MOVE, onMouseMove );
			addEventListener( Event.ENTER_FRAME, onEnterFrame );
			
			// マウスアップ時のイベント処理
			var stop:Function = function():void
			{
				stage.removeEventListener( MouseEvent.MOUSE_MOVE, onMouseMove );
				removeEventListener( Event.ENTER_FRAME, onEnterFrame );
			};
			
			stage.addEventListener( Event.MOUSE_LEAVE, stop );
			stage.addEventListener( MouseEvent.MOUSE_UP, stop );
		} 
		
		private function onMouseMove( event:Event ):void
		{
			var limit_length : uint = length - 1;
			if ( mouseX > limit_length )
			{
				spriteValue.width = limit_length;
				return;
			}
			else if ( mouseX <= 0)
			{
				spriteValue.width = 0;
				return;
			}
			else
			{
				spriteValue.width = mouseX;
			}
		}
		
		private function onEnterFrame( event : Event ):void
		{
			var limit_length : uint = length - 1;
			value = spriteValue.width / limit_length;
			dispatchEvent( new Event(Event.CHANGE) );
		}
	}
}