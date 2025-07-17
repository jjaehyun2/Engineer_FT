package com.IndieGo.utils {
	
	import fl.transitions.Tween;
	import fl.transitions.easing.Elastic;
	import fl.transitions.easing.Strong;
	import fl.transitions.easing.None;

	public class Transforms {

		public var Stage:Object;
		private var ID:Object;

		public function Transforms( stage:Object ): void {

			Stage = stage;
			
			ID = {
				
				TX: {},
				TY: {}
				
			}
			
		}

		public function place( clip:Object, x:Number, y:Number, stage:Boolean = false, id:String = '' ): void {

			if ( !stage ) {

				x = Stage.stageWidth * x;
				y = Stage.stageHeight * y;

			}
			
			if ( !id ) {
				
				try { if ( clip.TX.isPlaying ) clip.TX.stop() } catch( err ) {}
				try { if ( clip.TY.isPlaying ) clip.TY.stop() } catch( err ) {}
				
			} else {
				
				try { if ( ID.TX[ id ].isPlaying ) ID.TX[ id ].stop() } catch( err ) {}
				try { if ( ID.TY[ id ].isPlaying ) ID.TY[ id ].stop() } catch( err ) {}
				
			}


			if ( clip.x !== x ) clip.x = x;
			if ( clip.y !== y ) clip.y = y;

		}
		
		public function size( clip:Object, w:Number, h:Number ): void {
			
			try { if ( clip.TW.isPlaying ) clip.TW.stop() } catch( err ) {}
			try { if ( clip.TH.isPlaying ) clip.TH.stop() } catch( err ) {}

			if ( clip.width !== w ) clip.width = w;
			if ( clip.height !== h ) clip.height = h;
			
		}

		public function scale( clip:Object, x:Number, y:Number ): void {
			
			try { if ( clip.TSX.isPlaying ) clip.TSX.stop() } catch( err ) {}
			try { if ( clip.TSY.isPlaying ) clip.TSY.stop() } catch( err ) {}

			if ( clip.scaleX !== x ) clip.scaleX = x;
			if ( clip.scaleY !== y ) clip.scaleY = y;
			
		}

		public function rotate( clip:Object, deg:Number ): void {
			
			try { if ( clip.TR.isPlaying ) clip.TR.stop() } catch( err ) {}
			
			if ( clip.rotation !== deg * 360 ) clip.rotation = deg * 360;
			
		}
		
		public function alpha( clip:Object, val:Number ): void {
			
			try { if ( clip.TA.isPlaying ) clip.TA.stop() } catch( err ) {}

			if ( clip.alpha !== val ) clip.alpha = val;
			
		}

		public function animPlace( clip:Object, x:Number, y:Number, stage:Boolean = false, type = 0, dur:Number = 2, id:String = '' ): void {
			
			if ( !stage ) {
				
				x = Stage.stageWidth*x;
				y = Stage.stageHeight*y;
				
			}

			if ( type === 0 ) type = Elastic.easeOut;
			else if ( type === 1 ) type = Strong.easeOut;

			if ( !id ) {
				
				try { if ( clip.TX.isPlaying ) clip.TX.stop() } catch( err ) {}
				try { if ( clip.TY.isPlaying ) clip.TY.stop() } catch( err ) {}
				
				if ( clip.x !== x ) clip.TX = new Tween( clip, 'x', type, clip.x, x, dur, true );
				if ( clip.y !== y ) clip.TY = new Tween( clip, 'y', type, clip.y, y, dur, true );
				
			} else {
				
				try { if ( ID.TX[ id ].isPlaying ) ID.TX[ id ].stop() } catch( err ) {}
				try { if ( ID.TY[ id ].isPlaying ) ID.TY[ id ].stop() } catch( err ) {}
				
				if ( clip.x !== x ) ID.TX[ id ] = new Tween( clip, 'x', type, clip.x, x, dur, true );
				if ( clip.y !== y ) ID.TY[ id ] = new Tween( clip, 'y', type, clip.y, y, dur, true );
				
			}

		}
		
		public function animSize( clip:Object, w:Number, h:Number, type = 0, dur:Number = 2 ): void {

			if ( type === 0 ) type = Elastic.easeOut;
			else if ( type === 1 ) type = Strong.easeOut;

			try { if ( clip.TW.isPlaying ) clip.TW.stop() } catch( err ) {}
			try { if ( clip.TH.isPlaying ) clip.TH.stop() } catch( err ) {}

			if ( clip.width !== w ) clip.TW = new Tween( clip, 'width', type, clip.width, w, dur, true );
			if ( clip.height !== h ) clip.TH = new Tween( clip, 'height', type, clip.height, h, dur, true );

		}

		public function animScale( clip:Object, x:Number, y:Number, type = 0, dur:Number = 2 ): void {

			if ( type === 0 ) type = Elastic.easeOut;
			else if ( type === 1 ) type = Strong.easeOut;

			try { if ( clip.TSX.isPlaying ) clip.TSX.stop() } catch( err ) {}
			try { if ( clip.TSY.isPlaying ) clip.TSY.stop() } catch( err ) {}

			if ( clip.scaleX !== x ) clip.TSX = new Tween( clip, 'scaleX', type, clip.scaleX, x, dur, true );
			if ( clip.scaleY !== y ) clip.TSY = new Tween( clip, 'scaleY', type, clip.scaleY, y, dur, true );

		}

		public function animRotate( clip:Object, deg:Number, type = 0, dur:Number = 2 ): void {

			try { if ( clip.TR.isPlaying ) clip.TR.stop() } catch( err ) {}

			if ( clip.rotation === deg * 360 ) return;

			if ( type === 0 ) type = Elastic.easeOut;
			else if ( type === 1 ) type = Strong.easeOut;

			clip.TR = new Tween( clip, 'rotation', type, clip.rotation, ( deg * 360 ), dur, true );

		}

		public function animAlpha( clip:Object, val:Number, dur:Number = 2 ): void {

			try { if ( clip.TA.isPlaying ) clip.TA.stop() } catch( err ) {}

			if ( clip.alpha !== val ) clip.TA = new Tween( clip, 'alpha', None.easeOut, clip.alpha, val, dur, true );

		}

	}

}