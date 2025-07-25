package net.psykosoft.psykopaint2.base.utils.io
{

	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Loader;
	import flash.events.Event;
	import flash.utils.ByteArray;

	public class PngDecodeUtil
	{
		private var _pngDecodeCallback:Function;
		private var _loader:Loader;
		private var _bytes : ByteArray;
		private var _disposeWhenReady : Boolean;

		public function PngDecodeUtil() {
			super();
		}

		public function decode( bytes:ByteArray, onComplete:Function, disposeWhenReady : Boolean = false ):void {
			trace( this, "decoding: " + bytes.length + " bytes." );
			_loader = new Loader();
			_loader.contentLoaderInfo.addEventListener( Event.COMPLETE, onDecodingComplete );
			_pngDecodeCallback = onComplete;
			_disposeWhenReady = disposeWhenReady;
			_bytes = bytes;
			_loader.loadBytes( _bytes );
		}

		private function onDecodingComplete( event:Event ):void {
			removeListeners();
			trace( this, "decoded." );
			if (_disposeWhenReady)
				_bytes.clear();

			_bytes = null;
			var bmd:BitmapData = Bitmap(_loader.content).bitmapData;
			_pngDecodeCallback( bmd );
			_pngDecodeCallback = null;
		}

		private function removeListeners() : void
		{
			_loader.contentLoaderInfo.removeEventListener( Event.COMPLETE, onDecodingComplete );
		}
	}
}