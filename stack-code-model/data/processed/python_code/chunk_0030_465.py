package {
	
	import flash.events.Event;
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Graphics;
	import flash.display.Loader;
	import flash.display.LoaderInfo;
	import flash.display.Shape;
	import flash.geom.Matrix;
	import flash.geom.Point;
	import flash.net.URLRequest;
	
	/**
	 * A image viewer showing an image spinning up from the
	 * ground of a 3D space
	 */
	public class RotateViewImage extends Shape {
		
		public var environment:Environment3D = new Environment3D(300, 200, 400);	// environment for rendering the image
		public var divsX:int = 7;					// mesh divisions along x for image being viewed
		public var divsY:int = 4;					// mesh divisions along y for image being viewed
		public var radius:Number = 100;				// radius to use for the spinning image 
		public var imageHeight:Number;				// height of the image being viewed
		public var maxWidth:Number = 300;			// max width to use for the image when being displayed
		public var maxHeight:Number = 250;			// max height to use for the image when being displayed
		public var offsetY:Number = 75;				// vertical offset for the position of the image
		public var reflectionHeight:Number = 50;	// the height of the reflection applied to the image
		public var rotationFrames:int = 40;			// the number of frames to use in the image rotation animation
		public var rotations:int = 1;				// the number of times to rotate the image rotating into view
			
		public var loader:Loader = new Loader();	// loader used to load an external image
		private var origBitmap:BitmapData;			// reference to the original bitmapData instance being viewed
		private var currFrame:int = 0;				// current frame in the animation
		private var scaleRatio:Number = 1;			// scaleRatio to assure the image fits within maxWidth and maxHeight
		
		/**
		 * BitmapData instance of the image being viewed
		 * When assigned, a reflection is automatically applied
		 */
		public function get bitmapData():BitmapData {
			return origBitmap;
		}
		public function set bitmapData(b:BitmapData):void {
			
			// if a valid bitmapData is assigned
			if (b) {
				
				// reset spin animation frames to start (0)
				currFrame = 0;
				
				// add enterframe handler for spinning intro
				addEventListener(Event.ENTER_FRAME, turnTable);
				
				// calulate sizing to fit the image in the defined max height and width
				scaleRatio = Math.min(1, Math.min(maxWidth/b.width, maxHeight/b.height));
				imageHeight = scaleRatio*b.height;
				radius = scaleRatio*b.width/2;
				
			// invalid or null bitmapData assigned
			}else{
				removeEventListener(Event.ENTER_FRAME, turnTable);
			}
			
			// retain the original bitmapData
			origBitmap = b;
		}
		
		/**
		 * Constructor; optional bitmapData to load into the viewer
		 */
		public function RotateViewImage(bitmapData:BitmapData = null){
			if (bitmapData) this.bitmapData = bitmapData;
				
			// default name is image; this is used to identify the current image
			name = "image";
			
			// add listener for loading an external image
			loader.contentLoaderInfo.addEventListener(Event.INIT, imageLoaded);
		}
		
		/**
		 * Loads an external image into the viewer
		 */
		public function load(request:URLRequest):void {
			
			// do not animate spinning when loading a new image
			removeEventListener(Event.ENTER_FRAME, turnTable);
			
			// clear any existing image within the viewer
			graphics.clear();
			
			// dispatch the OPEN event indicating that a
			// new image is being loaded in
			dispatchEvent(new Event(Event.OPEN));
			
			// load the new image into loader
			loader.load(request);
		}
		
		/**
		 * Loads a new image via an ImageData instance
		 */
		public function showImage(data:ImageData):void {
			name = data.title;
			load(new URLRequest(data.imageURL));
		}
		
		/**
		 * Event handler; called when image has been loaded
		 * Assigns bitmapData from the Bitmap instance loaded
		 */
		private function imageLoaded(event:Event):void {
			try {
				
				// get bitmapData from the Bitmap loaded into loader
				bitmapData = Bitmap(LoaderInfo(event.target).content).bitmapData;
			}catch(err:Error){}
				
			// dispatch COMPLETE event indicating image has been loaded
			dispatchEvent(new Event(Event.COMPLETE));
		}
		
		/**
		 * Crops a bitmapData to only show its top by indicated amount
		 */
		private function cropBitmap(bmp:BitmapData, amount:Number):BitmapData {
			
			// assure that the amount is above 0
			if (amount > 0) {
				
				// create a new bitmapData containing only the cropped portion of the image
				var cropped:BitmapData = new BitmapData(bmp.width, bmp.height*amount, true, 0x00000000);
				cropped.copyPixels(bmp, cropped.rect, new Point(0, 0));
				return cropped;
			}
			
			// return null if invalid amount
			return null;
		}
		
		/**
		 * Ease method used in spinning an image up from the ground
		 */
		private function spinEase(t:Number):Number {
			t = t-1;
			return 1-t*t;
		}
		
		/**
		 * Event handler; enterframe for spinning an image up
		 */
		private function turnTable(event:Event):void {
			
			// get amount of spin from frame location applying ease
			var t:Number = spinEase(currFrame/rotationFrames);
			
			// determine angle from rotations and t
			var angle:Number = rotations*2*Math.PI*t;
			
			// define image corners based on angle and radius
			var x:Number = Math.cos(angle)*radius;
			var z:Number = Math.sin(angle)*radius;
			var h:Number = offsetY - t*imageHeight;
			var h2:Number = offsetY + reflectionHeight;
			
			// clear existing graphics
			graphics.clear();
			
			// apply crop
			var bmp:BitmapData = cropBitmap(origBitmap, t);
			
			// apply reflection to crop
			bmp = ImageReflection.addReflection(bmp, reflectionHeight/scaleRatio);
			
			// draw 3D mesh on cropped, reflected bitmap
			ImageMesh3D.draw(graphics, bmp, divsX, divsY, 
				-x, h, -z, x, h, z,
				x, h2, z, -x, h2, -z, environment);

			// update to the next frame, removing the enterframe
			// event if the last frame has been reached
			if (currFrame >= rotationFrames) {
				removeEventListener(Event.ENTER_FRAME, turnTable);
			}else{
				currFrame++;
			}
		}
	}
}