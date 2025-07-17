package starling.display 
{
	import starling.animation.*;
	
	public class Camera implements IAnimatable
	{		
		private var _x: Number = 0;
		private var _y: Number = 0;
		
		private var _worldContainer: DisplayObject;
		private var _stage: Stage;
		
		public function Camera() {}
		
		public function Init( worldContainer: DisplayObject, stage: Stage ) : void
		{
			this._worldContainer = worldContainer;
			this._stage = stage;			
		}
		
		public function advanceTime(time:Number):void
		{
			
		}
		
		public function FocusAt( x: Number, y: Number ):void
		{
			this.x = x - this.width / 2;
			this.y = y - this.height / 2;
		}
		
		// ***** PROPERTIES ******
		public function get x():Number
		{
			return _x;
		}
		public function set x(x:Number):void
		{
			_x = x;
			_worldContainer.x = -_x;
		}
		
		public function get y():Number
		{
			return _y;
		}
		public function set y(y:Number):void
		{
			_y = y;
			_worldContainer.y = -_y;
		}
		
		public function get width():Number
		{
			return _stage.stageWidth;
		}
		public function get height():Number
		{
			return _stage.stageHeight;
		}
		
	}

}