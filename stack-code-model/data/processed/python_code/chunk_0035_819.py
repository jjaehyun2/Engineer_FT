package 
{
	import flash.display.Sprite;
	import flash.geom.Matrix;
	import gui.*;

	public class VideoControlGuiFactory
	{
		public var param : VideoControlGuiParam;
		
		public function VideoControlGuiFactory( param : VideoControlGuiParam )
		{
			this.param = param;
			background();
			line();
			startButton();
			pauseButton();
			topButton();
			seekbar();
			time();
			timeTotal();
			speaker();
			mute();
			volume();
			scale();
			reduction();
		}
		
		public function startButton() : void
		{
			var icon : Sprite = new Sprite();
			icon.graphics.beginFill( 0xFFFFFF );
			icon.graphics.moveTo( 0, 0 );
			icon.graphics.lineTo( 12, 6 );
			icon.graphics.lineTo( 0, 12 );
			icon.graphics.lineTo( 0, 0 );
			icon.graphics.endFill();
			
			param.start = new VideoControlButton( button( icon ) );
		}
		
		public function pauseButton() : void
		{
			var icon : Sprite = new Sprite();
			icon.graphics.beginFill( 0xFFFFFF );
			icon.graphics.drawRect( 0, 0, 3, 12 );
			icon.graphics.drawRect( 9, 0, 3, 12 );
			icon.graphics.endFill();
			
			param.pause = new VideoControlButton( button( icon ) );
		}
		
		public function topButton() : void
		{
			var icon : Sprite = new Sprite();
			icon.graphics.beginFill( 0xFFFFFF );
			icon.graphics.drawRect( 0, 0, 3, 12 );
			icon.graphics.moveTo( 4, 6 );
			icon.graphics.lineTo( 10, 12 );
			icon.graphics.lineTo( 10, 0 )
			icon.graphics.endFill();
			
			param.top = new VideoControlButton( button( icon ) );
		}
		
		public function seekbar() : void
		{
			param.seek = new VideoSeekSlide( 260 );
		}
		
		public function time() : void
		{
			param.time = new Hex60Text( 3 );
		}
		
		public function timeTotal() : void
		{
			param.timeTotal = new Hex60Text( 3 );
		}
		
		public function speaker() : void
		{
			var icon : Sprite = new Sprite();
			icon.graphics.beginFill( 0xFFFFFF );
			icon.graphics.drawRect( 0, 4, 7, 4 );
			icon.graphics.endFill();
			icon.graphics.beginFill( 0xFFFFFF );
			icon.graphics.moveTo( 1, 6 );
			icon.graphics.lineTo( 7, 12 );
			icon.graphics.lineTo( 7, 0 );
			icon.graphics.endFill();
			icon.graphics.lineStyle( 1.0, 0xFFFFFF );
			icon.graphics.moveTo( 12, 0 );
			icon.graphics.lineTo( 9, 3 );
			icon.graphics.moveTo( 12, 6 );
			icon.graphics.lineTo( 9, 6 );
			icon.graphics.moveTo( 12, 12 );
			icon.graphics.lineTo( 9, 9 );
			
			param.speaker = new VideoControlButton( button( icon ) );
		}
		
		public function mute() : void
		{
			var icon : Sprite = new Sprite();
			icon.graphics.beginFill( 0xFFFFFF );
			icon.graphics.moveTo( 1, 5 );
			icon.graphics.lineTo( 1, 9 );
			icon.graphics.lineTo( 3, 9 );
			icon.graphics.lineTo( 5, 7 );
			icon.graphics.lineTo( 3, 5 );
			icon.graphics.endFill();
			icon.graphics.beginFill( 0xFFFFFF );
			icon.graphics.moveTo( 8, 1 );
			icon.graphics.lineTo( 6, 3 );
			icon.graphics.lineTo( 6, 4 );
			icon.graphics.lineTo( 7, 5 );
			icon.graphics.lineTo( 8, 4 );
			icon.graphics.endFill();
			icon.graphics.beginFill( 0xFFFFFF );
			icon.graphics.moveTo( 8, 13 );
			icon.graphics.lineTo( 6, 11 );
			icon.graphics.lineTo( 6, 10 );
			icon.graphics.lineTo( 7, 9 );
			icon.graphics.lineTo( 8, 10 );
			icon.graphics.endFill();
			icon.graphics.lineStyle( 1, 0xFFFFFF );
			icon.graphics.moveTo( 0, 0 );
			icon.graphics.lineTo( 14, 14 );
			icon.graphics.moveTo( 14,0 );
			icon.graphics.lineTo( 0, 14 );
			
			param.mute = new VideoControlButton( button( icon ) );
		}
		
		public function volume() : void
		{
			param.volume = new VideoSpeakerSlide( 56 );
		}
		
		public function scale() : void 
		{
			var icon : Sprite = new Sprite();
			icon.graphics.beginFill( 0xFFFFFF );
			icon.graphics.drawRect( 3, 4, 6, 4 );
			icon.graphics.endFill();
			icon.graphics.lineStyle( 1.0, 0xFFFFFF );
			icon.graphics.moveTo( 0, 2 );
			icon.graphics.lineTo( 0, 0 );
			icon.graphics.lineTo( 2, 0 );
			icon.graphics.moveTo( 0, 9 );
			icon.graphics.lineTo( 0, 11 );
			icon.graphics.lineTo( 2, 11 );
			icon.graphics.moveTo( 11, 9 );
			icon.graphics.lineTo( 11, 11 );
			icon.graphics.lineTo( 9, 11 );
			icon.graphics.moveTo( 11, 2 );
			icon.graphics.lineTo( 11, 0 );
			icon.graphics.lineTo( 9, 0 );
			
			param.scale = new VideoControlButton( button( icon ) );
		}
		
		public function reduction() : void 
		{
			var icon : Sprite = new Sprite();
			icon.graphics.beginFill( 0xFFFFFF );
			icon.graphics.drawRect( 3, 4, 6, 4 );
			icon.graphics.endFill();
			icon.graphics.lineStyle( 1.0, 0xFFFFFF );
			icon.graphics.moveTo( 0, 2 );
			icon.graphics.lineTo( 2, 2 );
			icon.graphics.lineTo( 2, 0 );
			icon.graphics.moveTo( 0, 9 );
			icon.graphics.lineTo( 2, 9 );
			icon.graphics.lineTo( 2, 11 );
			icon.graphics.moveTo( 11, 9 );
			icon.graphics.lineTo( 9, 9 );
			icon.graphics.lineTo( 9, 11 );
			icon.graphics.moveTo( 11, 2 );
			icon.graphics.lineTo( 9, 2 );
			icon.graphics.lineTo( 9, 0 );
			
			param.reduction = new VideoControlButton( button( icon ) );
		}
		
		public function background() : void 
		{
			var width : int = 544;
			var matrix:Matrix = new Matrix();
			matrix.createGradientBox( width, 25, 90 * Math.PI / 180 );
			
			var backgrand : Sprite = new Sprite();
			backgrand.graphics.beginGradientFill( "linear", [0x666666, 0x222222, 0x666666,], [1.0, 1.0, 1.0], [0, 127, 255], matrix );
			backgrand.graphics.drawRect( 0, 0, width, 25 );
			backgrand.graphics.endFill();
			backgrand.graphics.lineStyle( 1.0, 0xAAAAAA );
			backgrand.graphics.moveTo( 0, 0 );
			backgrand.graphics.lineTo( width, 0 );
			backgrand.graphics.moveTo( 0, 0 );
			backgrand.graphics.lineTo( 0, 25 );
			backgrand.graphics.lineStyle( 1.0, 0x222222 );
			backgrand.graphics.moveTo( width, 25 );
			backgrand.graphics.lineTo( width, 0 );
			backgrand.graphics.moveTo( width, 25 );
			backgrand.graphics.lineTo( 0, 25 );
			
			param.backgrand = backgrand;
		}
		
		public function line() : void
		{
			var line : Sprite = new Sprite();
			line.graphics.lineStyle( 1.0, 0x222222 );
			line.graphics.moveTo( 0, 0 );
			line.graphics.lineTo( 0, 25 );
			line.graphics.lineStyle( 1.0, 0xAAAAAA );
			line.graphics.moveTo( 1, 0 );
			line.graphics.lineTo( 1, 25 );
			
			param.line = line;
			
			var line2 : Sprite = new Sprite();
			line2.graphics.lineStyle( 1.0, 0x222222 );
			line2.graphics.moveTo( 0, 0 );
			line2.graphics.lineTo( 0, 25 );
			line2.graphics.lineStyle( 1.0, 0xAAAAAA );
			line2.graphics.moveTo( 1, 0 );
			line2.graphics.lineTo( 1, 25 );
			param.line2 = line2;
		}
		
		private function button( icon : Sprite ) : Sprite
		{
			var bg : Sprite = new Sprite();
			
			bg = new Sprite();
			bg.graphics.beginFill( 0xFFFFFF, 0 );
			bg.graphics.drawRect( 0, 0, 25, 25 );
			bg.graphics.endFill();
			
			icon.x = bg.width / 2 - icon.width / 2;
			icon.y = bg.height / 2 - icon.height / 2;
			
			bg.addChild( icon );
			
			return bg;
		}
	}
}