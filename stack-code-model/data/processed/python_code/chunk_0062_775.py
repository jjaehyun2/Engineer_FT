package  {
	
	import flash.display.Bitmap;
	import starling.display.Shape;
	import starling.display.Sprite;
	import starling.events.Event;
	import starling.textures.Texture;
	
	public class GraphicsTest extends Sprite {

		[Embed(source = "../assets/single_image.jpg")]
		private const ImageClass:Class;
		
		public function GraphicsTest() {
			addEventListener(Event.ADDED_TO_STAGE, onAdded);
		}
		
		private function onAdded(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, onAdded);

			var testShape:Shape = new Shape();
			addChild(testShape);
			testShape.graphics.beginTextureFill(Texture.fromBitmap(new ImageClass() as Bitmap));
			testShape.graphics.drawRect(0,0,stage.stageWidth, stage.stageHeight);
			testShape.graphics.endFill();
		}
		
	}
}