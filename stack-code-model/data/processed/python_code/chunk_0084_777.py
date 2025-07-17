package com.illuzor.camera {
	
	import by.blooddy.crypto.image.JPEGEncoder;
	import fl.controls.Button;
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.net.FileReference;
	import flash.utils.ByteArray;
	
	/**
	 * ...
	 * @author illuzor // illuzor@gmail.com // illuzor.com
	 */
	public class Main extends Sprite {
		private var camera:CameraScreen;
		private var but:Button;
		private var bitmap:Bitmap;
		private var saveButton:Button;
		private var bitmapdata:BitmapData;
		private var currentPhoto:uint = 0;
		
		public function Main():void {
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void 
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);
			// entry point
			
			camera = new CameraScreen();
			addChild(camera);
			
			but = new Button();
			but.label = "Снять";
			but.x = stage.stageWidth - but.width - 10;
			but.y = stage.stageHeight - but.height - 10;
			addChild(but);
			DebugPanel.init(stage);
			DebugPanel.addText("started")
			but.addEventListener(MouseEvent.CLICK, getImage);
		}
		
		private function getImage(e:MouseEvent):void {
			currentPhoto++;
			but.removeEventListener(MouseEvent.CLICK, getImage);
			bitmapdata = new BitmapData(camera.width, camera.height);
			bitmapdata.draw(camera);
			bitmap = new Bitmap(bitmapdata);
			camera.visible = false;
			addChild(bitmap);
			
			but.label = "Ешё раз";
			but.addEventListener(MouseEvent.CLICK, showVideoAgain);
			
			saveButton = new Button();
			saveButton.label = "Сохранить";
			saveButton.x = but.x - saveButton.width - 10;
			saveButton.y = stage.stageHeight - but.height - 10;
			addChild(saveButton);
			
			saveButton.addEventListener(MouseEvent.CLICK, saveImage);
		}

		private function showVideoAgain(e:MouseEvent):void {
			but.removeEventListener(MouseEvent.CLICK, showVideoAgain);
			removeChild(bitmap);
			but.label = "Снять";
			camera.visible = true;
			removeChild(saveButton);
			but.addEventListener(MouseEvent.CLICK, getImage);
		}
		
		private function saveImage(e:MouseEvent):void {
			var bytes:ByteArray = JPEGEncoder.encode(bitmapdata);
			var file:FileReference = new FileReference();
			file.save(bytes, "photo" + String(currentPhoto) + ".jpg");
		}
		
	}
}