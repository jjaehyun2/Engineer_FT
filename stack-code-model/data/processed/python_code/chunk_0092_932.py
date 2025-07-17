package vyperlogix {
	import controls.Alert.AlertPopUp;
	
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Loader;
	import flash.events.Event;
	import flash.utils.ByteArray;
	
	public class ImageDecoder {
		public static var options:Object = {
			LOADER: 'loader',
			DECODED_BITMAP_DATA: 'decodedBitmapData'
		};
		
		private var loader:Loader = new Loader();
		public var loading:Boolean;
		
		/**
		 * Constructor - Creates a new Image decoder 
		 * Decodes the byte array byteData, and when done calls callBack with the BitmapData
		 */
		public function ImageDecoder(byteData:ByteArray, option:String, callBack:Function):void {
			loading = true;
			loader.contentLoaderInfo.addEventListener(Event.COMPLETE,
				function(e:Event):void {
					loading = false;
					var decodedBitmapData:BitmapData = Bitmap(e.target.content).bitmapData;
					if (option == ImageDecoder.options.DECODED_BITMAP_DATA) {
						callBack(decodedBitmapData);
					} else if (option == ImageDecoder.options.LOADER) {
						callBack(loader);
					} else {
						//AlertPopUp.surpriseNoOkay('Cannot read the image at ImageDecoder due to bad or invalid options.','ERROR');
					}
				});
			loader.loadBytes(byteData);
		}
	}	
}