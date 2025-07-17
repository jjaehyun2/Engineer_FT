package  {

	import flash.display.MovieClip;
	import flash.filters.GlowFilter;


	public class Ball extends MovieClip {

		// Properties
		public var velocityX:Number = 20;
		public var velocityY:Number = 20;
		private var _startX:Number;
		private var _startY:Number;
		public var shouldMove:Boolean;

		public function Ball(xC:Number, yC:Number) {
			this.x = xC;
			this.y = yC;

			this.startX = xC;
			this.startY = yC;

			this.width = 28;
			this.height = 28;

			this.shouldMove = false;
		}

		// Flip x
		public function flipX(){
			this.velocityX *= -1;
		}

		// Flip y
		public function flipY(){
			this.velocityY *= -1;
		}

		// Get startX
		public function get startX():Number{
			return this._startX;
		}

		// Set startX
		public function set startX(x:Number):void{
			this._startX = x;
		}

		// Get startY
		public function get startY():Number{
			return this._startY;
		}

		// Set startY
		public function set startY(y:Number):void{
			this._startY = y;
		}

		// Reset position
		public function resetPos():void{
			this.x = this.startX;
			this.y = this.startY;
		}

		// Add to x
		public function addX():void{
			if (this.shouldMove){
				this.x += this.velocityX;
			}
		}

		// Add to y
		public function addY():void{
			if (this.shouldMove){
				this.y += this.velocityY;
			}
		}

		// Log
		public function log():void{
			trace("Position: [" + this.x + ", " + this.y + "], Velocity: " + this.velocityX);
		}

	}

}