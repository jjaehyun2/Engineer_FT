package com.illuzor.directtest {
	
	import flash.display.Bitmap;
	import flash.external.ExternalInterface;
	import starling.display.Image;
	import starling.display.Sprite;
	import starling.events.Event;
	import starling.text.TextField;
	import starling.textures.Texture;
	

	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class StarlingClass extends Sprite {
		
		[Embed(source = "../../../../assets/img.png")]
		private const ImgClass:Class;
		private var textField:TextField;
		
		public function StarlingClass() {
			addEventListener(Event.ADDED_TO_STAGE, onAdded);
		}
		
		private function onAdded(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, onAdded);
			trace("start");
			
			var bitmap:Bitmap = new ImgClass() as Bitmap;
			
			var texture:Texture = Texture.fromBitmap(bitmap);
			var image:Image = new Image(texture);
			addChild(image);
			
			image.x = (stage.stageWidth - image.width) >> 1;
			image.y = (stage.stageHeight - image.height) >> 1;
			
			textField = new TextField(640, 240, "Start");
			textField.color = 0xFFFFFF;
			addChild(textField);
			
			if (ExternalInterface.available) {
				textField.text = "ExternalInterface availible";
				external();
			} else {
				textField.text = "ExternalInterface NOT availible";
			}
		}
		
		private function external():void {
			
			ExternalInterface.addCallback("getData", getData)
			ExternalInterface.call("inited");
		}
		
		private function getData(json:String):void {
			textField.text = "DATA RECEIVED: " + json;
		}
		
	}
}