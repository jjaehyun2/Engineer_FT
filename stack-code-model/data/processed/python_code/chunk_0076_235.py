package com {
	import controls.Alert.AlertPopUp;
	
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Loader;
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;
	import flash.geom.Matrix;
	import flash.net.URLRequest;
	import flash.utils.ByteArray;
	
	import mx.core.UIComponent;
	
	public class ImageUtils {
		
		public static function read_image2(aFile:File,callback:Function):void {
			// Only this method works for the Mac and Linux...
			var uic:UIComponent = new UIComponent();
			var imageBytes:ByteArray = new ByteArray();
			var stream:FileStream = new FileStream();
			trace('ImageUtils.read_image2().1 --> aFile='+aFile.nativePath);
			stream.open(aFile, FileMode.READ);
			stream.readBytes(imageBytes);
			stream.close();
			var loader:Loader = new Loader();
			loader.contentLoaderInfo.addEventListener(Event.COMPLETE,
				function (event:Event):void {
					var scaleFactor:Number = 1;
					
//					if (loader.width > loader.height && loader.width > 128) {
//						scaleFactor = 128 / loader.width;
//						wasScaled = true;
//					}
//					if (loader.height > loader.width && loader.height > 128) {
//						scaleFactor = 128 / loader.height;
//						wasScaled = true;
//					}
					var bmd:BitmapData = Bitmap(loader.content).bitmapData;
					var scaledBMD:BitmapData = new BitmapData(loader.width * scaleFactor, loader.height * scaleFactor);
					var matrix:Matrix = new Matrix();
					matrix.scale(scaleFactor, scaleFactor);
					scaledBMD.draw(bmd, matrix, null, null, null, true);
					uic.x = (scaledBMD.width/2) * -1;
					uic.y = (scaledBMD.height/2) * -1;
					uic.addChild(new Bitmap(scaledBMD));
					loader.unload();
					bmd = null;
					if (callback is Function) {
						callback(uic);
					}
				});
			loader.loadBytes(imageBytes);
		}
		
		public static function load_image(url:String,callback:Function):* {
			var loader:Loader = new Loader();
			var request:URLRequest = new URLRequest(url);
			loader.contentLoaderInfo.addEventListener(Event.COMPLETE,function (event:Event):void {
				if (callback is Function) {
					var uic:UIComponent = new UIComponent();
					uic.addChild(loader);
					callback(uic,loader.content);
				}
			});
			loader.load(request);
		}

		public static function read_image(aFile:File,callback:Function):void {
			var aFileStream:FileStream = new FileStream();
			var bytes:ByteArray = new ByteArray();
			aFileStream.addEventListener(Event.COMPLETE, function (event:Event):void {
				aFileStream.readBytes(bytes,0,aFileStream.bytesAvailable);
				new ImageDecoder(bytes,ImageDecoder.options.LOADER,function (loader:Loader):void {
					if (callback is Function) {
						var uic:UIComponent = new UIComponent();
						uic.addChild(loader);
						callback(uic,loader.content);
					}
				});
			});
			aFileStream.addEventListener(IOErrorEvent.IO_ERROR, function (event:IOErrorEvent):void {
				//AlertPopUp.surpriseNoOkay('Cannot locate the image from "'+aFile.nativePath+'".\n'+event.toString(),'WARNING');
			});
			aFileStream.openAsync(aFile, FileMode.READ);
		}
	}
}