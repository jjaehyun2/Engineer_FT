package {
	
	import flash.display.BitmapData;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.net.URLRequest;
	
	/**
	 * A carousel of images showing only the user facing side of the carousel.
	 * Each image in the carousel can be clicked to open
	 */
	public class ImageCarousel extends Sprite {
		
		public var environment:Environment3D = new Environment3D(300, 225, 500);
		public var target:RotateViewImage;
		public var radius:Number = 225;
		public var offsetY:Number = 130;
		public var angle:Number = 0;
		public var visibleImages:int = 10;
		public var speedFactor:Number = 4000;
		public var sizeFactor:Number = .53;
		public var divsX:int = 3;
		public var divsY:int = 2;
		private var _images:Array;
		
		public function set images(a:Array):void {
			
			// remove all pre-existing carousel images
			while(numChildren){
				removeChildAt(0);
			}
			
			// if a valid array is passed
			if (a && a.length) {
				
				// add enterframe event handler if needed
				if (!_images) {
					addEventListener(Event.ENTER_FRAME, turnTable);
				}
				
				// populate images through a loop, creating new _CarouselItem instances
				_images = [];
				var image:_CarouselItem;
				var i:int = a.length;
				while (i--){
					image = new _CarouselItem(ImageData(a[i]));
					
					// add mouse interactions
					image.addEventListener(MouseEvent.CLICK, selectImage);
					image.addEventListener(MouseEvent.ROLL_OVER, hoverImage);
					image.addEventListener(MouseEvent.ROLL_OUT, unhoverImage);
					
					// add to display list (empty at this point)
					addChild(image);
					
					// add to array
					_images[i] = image;
				}
			}else{
				
				// no images, remove enterframe event handler
				removeEventListener(Event.ENTER_FRAME, turnTable);
				
				// null images array
				_images = null;
			}
		}
		
		/**
		 * Constructor
		 */
		public function ImageCarousel(images:Array = null){
			if (images) this.images = images;
		}
		
		/**
		 * Event handler; called when a carousel image is clicked
		 * loads the main image into the carousel target (RotateViewImage)
		 */
		private function selectImage(event:MouseEvent):void {
			if (target) {
				target.showImage(_CarouselItem(event.target).imageData);
			}
		}
		
		/**
		 * Event handler; called when a carousel image is rolled over with the mouse
		 * Displays hover image state
		 */
		private function hoverImage(event:MouseEvent):void {
			_CarouselItem(event.target).hoverState();
		}
		
		/**
		 * Event handler; called when the mouse rolls off a carousel image
		 * Restores image state
		 */
		private function unhoverImage(event:MouseEvent):void {
			_CarouselItem(event.target).normalState();
		}
		
		
		/**
		 * Event handler; enterframe
		 * spins the carousel based on mouse movement allowing a user to see
		 * all the images contained within the carousel
		 */
		private function turnTable(event:Event):void {
			
			// alter angle of spin based on mouse location
			angle -= (mouseX - environment.originX)/speedFactor;
			
			// counter for carousel images
			var i:int = _images.length;
			
			// spacing based on visibleImages
			var spacing:Number = Math.PI/visibleImages;
			
			// angle limits so the first and last image
			// end facing the user
			var minAngle:Number = (1-i)*spacing - (Math.PI/2);
			var maxAngle:Number = -(Math.PI/2);
			if (angle < minAngle) {
				angle = minAngle;
			}else if (angle > maxAngle){
				angle = maxAngle;
			}
			
			var image:_CarouselItem;
			
			// item indices on this side of the carousel
			var minIndex:int = -Math.floor((angle+Math.PI)/spacing);
			var maxIndex:int = minIndex + visibleImages - 1;
			var currAngle:Number;
			var offAngle:Number;
			var cornerAngle:Number;
			var cornerRadius:Number;
			var x1:Number;
			var z1:Number;
			var x2:Number;
			var z2:Number;
			
			// loop through all carousel images
			while (i--){
				
				// get current image in loop and clear its graphics
				image = _CarouselItem(_images[i]);
				image.graphics.clear();
				
				// if within the visible range, draw
				if (i >= minIndex && i <= maxIndex) {
					
					// determine angles of edges based on angle of image
					currAngle = angle + i*spacing;
					offAngle = Math.atan(image.bitmapData.width*sizeFactor/(2*radius));
					cornerRadius = radius/Math.cos(offAngle);
					
					// find locations of each corner using angle and cornerRadius
					cornerAngle = currAngle - offAngle;
					x1 = Math.cos(cornerAngle)*cornerRadius;
					z1 = Math.sin(cornerAngle)*cornerRadius;
					cornerAngle = currAngle + offAngle;
					x2 = Math.cos(cornerAngle)*cornerRadius;
					z2 = Math.sin(cornerAngle)*cornerRadius;
					
					// height based on offsetY and image height
					var h:Number = offsetY - image.bitmapData.height*sizeFactor;
					
					// draw the image mesh with the calculated locations
					ImageMesh3D.draw(image.graphics, image.bitmapData, divsX, divsY, 
						x1, h, z1, x2, h, z2,
						x2, offsetY, z2, x1, offsetY, z1, environment, 1);
				}
			}
		}
	}
}

import flash.display.BitmapData;
import flash.display.Sprite;
import flash.filters.GlowFilter;
import flash.geom.Point;

/**
 * Carousel item displayed in the carousel view
 */
internal class _CarouselItem extends Sprite {
	
	public var bitmapData:BitmapData;
	public var imageData:ImageData;
	private var reflectionHeight:Number = 50;
	private static var hoverFilter:GlowFilter = new GlowFilter(0xFFFFFF, 1.0, 16.0, 16.0, 2, 2, true);
		
	/**
	 * Constructor
	 */
	public function _CarouselItem(imageData:ImageData){
		this.imageData = imageData;
		normalState();
	}
	
	/**
	 * Displays item normal state - original bitmap plus reflection
	 */
	public function normalState():void {
		this.bitmapData = ImageReflection.addReflection(imageData.bitmapData, reflectionHeight);
	}
	
	
	/**
	 * Displays item hover state - original bitmap plus glow plus reflection
	 */
	public function hoverState():void {
		var orig:BitmapData = imageData.bitmapData;
		var glowBmp:BitmapData = new BitmapData(orig.width, orig.height, true, 0x00000000);
		glowBmp.applyFilter(orig, orig.rect, new Point(0, 0), hoverFilter);
		this.bitmapData = ImageReflection.addReflection(glowBmp, reflectionHeight);
	}
}