package devoron.components.filechooser
{
	import utils.image.ImageUtil;
	import devoron.file.FileInfo;
	import devoron.utils.airmediator.AirMediator;
	import utils.image.ImageDecoder;
	import devoron.file.LOC;
	import devoron.file.NATIVE;
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import org.aswing.AssetIcon;
	import org.aswing.Icon;
	import org.aswing.util.Stack;
	
	/**
	 * ImageFCH
	 * @author Devoron
	 */
	public class ImageFCH implements IFileChooserHelper
	{
		[Embed(source = "../../../../assets/icons/moduls/Chat/image_icon.png")]
		private var IMAGE_ICON16:Class;
		
		private var previewObjectCompleteListener:Function;
		private var path:String;
		
		public var objectsStack:Stack;
		private var enabled:Boolean = true;
		
		public var currentMode:Namespace;
		
		public function ImageFCH()
		{
			objectsStack = new Stack();
			
			/*if (CONFIG::air)
			{*/
			currentMode = NATIVE;
			/*}
			else {
				currentMode = LOC;
			}*/
			
		}
		
		/* INTERFACE devoron.components.filechooser.FileChooserHelper */
		
		public function getSupportedExtensions():Array
		{
			return ["jpg", "jpeg", "png"];
		}
		
		public function getType():String 
		{
			return "image";
		}
		
		public function getIcon():Icon 
		{
			return new AssetIcon(new IMAGE_ICON16, 16, 16);
		}
		
		public function isEnabled():Boolean 
		{
			return enabled;
		}
		
		public function setEnabled(b:Boolean):void 
		{
			enabled = b;
		}
		
		
		public function getPreviewObject(fi:FileInfo, previewObjectCompleteListener:Function):void
		{
			this.previewObjectCompleteListener = previewObjectCompleteListener;
			if (!fi.isDirectory && !running) {
				running = true;	
				AirMediator.getFile(fi.nativePath, onLoad, true);
				
				path = fi.nativePath;
				
			}
			if (!fi.isDirectory && running) {
				objectsStack.push( { fi:fi, listener:previewObjectCompleteListener } );
				//gtrace("загрузить " + 
			}
		}
		
		
		private function onLoad(fi:FileInfo):void
		{
			//gtrace(fi);
			var id:ImageDecoder = new ImageDecoder(fi.data, onDecode);
		}
		
		private var running:Boolean = false;
		private var date:Number;
		
		private function onDecode(bd:BitmapData):void
		{
			//var bitmap:Bitmap = new Bitmap(bd, "auto", true);
			var max:Number = Math.max (bd.width, bd.height);
			var bitmap:Bitmap = new Bitmap(ImageUtil.scaleBitmapData(bd, 90 / max, true), "auto", true);
			var assetIcon:AssetIcon = new AssetIcon(bitmap, 160, 90, false);
			previewObjectCompleteListener.call(null, { path:path, modificationDate:date, icon: assetIcon } );
			
			
			if (objectsStack.isEmpty()) {
				running = false;
			}
			else {
				var obj:Object = objectsStack.pop();
				var fi:FileInfo = obj.fi;
				var listener:Function = obj.listener;
				previewObjectCompleteListener = listener;
				path = fi.nativePath;
				date = fi.modificationDate.getUTCMilliseconds();
				
				
				AirMediator.getFile(fi.nativePath, onLoad, true);
			}
		}
	
	}

}