package gui
{
	import flash.display.Sprite;
	import flash.geom.Matrix;
	import flash.geom.Rectangle;
	import flash.events.Event;
	import flash.events.MouseEvent;

	public class VideoControlSlide extends Sprite
	{
		public  var value		: Number = 0.0;	// 値
		public	var length		: uint;			// バーの長さ
		protected var spriteBar	: Sprite;		// バー
		public var spriteValue	: Sprite;		// 値
		
		public function VideoControlSlide( width:uint )
		{
			length = width;
			
			graphicgBar();
			graphicgValue();
			
			// 描画位置
			spriteValue.x = (spriteBar.width - spriteValue.width) / 2;
			spriteValue.y = spriteBar.height / 2 - spriteValue.height / 2;
		}
		
		private function graphicgBar():void
		{
			var matrix : Matrix = new Matrix();
			matrix.createGradientBox( length, 6, 90 * Math.PI / 180 );
			
			spriteBar = new Sprite();
			spriteBar.graphics.lineStyle( 1.0, 0x111111 );
			spriteBar.graphics.beginGradientFill( "linear", [0x999999, 0x111111], [1.0, 1.0], [0, 127], matrix );
			spriteBar.graphics.drawRect( 0, 0, this.length, 6 );
			spriteBar.graphics.endFill();
			addChild( spriteBar );
		}
		
		private function graphicgValue():void
		{
			var limit_length : uint = length - 1;
			var matrix:Matrix = new Matrix();
			matrix.createGradientBox( limit_length, 5, 90 * Math.PI / 180 );
			
			spriteValue = new Sprite();
			spriteValue.graphics.beginGradientFill( "linear", [0xFFFFFF, 0x666666], [1.0, 1.0], [127, 255], matrix );
			spriteValue.graphics.drawRect( 0, 0, limit_length, 5 );
			spriteValue.graphics.endFill();
			addChild( spriteValue );
		}
		
		/*
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
			
			// マウスアップ時のイベント処理
			var stop:Function = function():void
			{
				stage.removeEventListener( MouseEvent.MOUSE_MOVE, onMouseMove );
				stage.removeEventListener( Event.ENTER_FRAME, onEnterFrame );
			};
			
			stage.addEventListener( Event.MOUSE_LEAVE, stop );
			stage.addEventListener( MouseEvent.MOUSE_UP, stop );
			
			addEventListener( Event.ENTER_FRAME, onEnterFrame );
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
		*/
	}
}