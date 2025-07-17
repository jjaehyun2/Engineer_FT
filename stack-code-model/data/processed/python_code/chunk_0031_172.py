package  
{
	import net.flashpunk.utils.Key;
	import net.flashpunk.utils.Input;
	import roshan.buffer.DIRECTION;
	public class xyKeyboard 
	{
		public static function getDirection():int {
			return toDirection(
				Input.check(Key.DOWN),
				Input.check(Key.LEFT),
				Input.check(Key.RIGHT),
				Input.check(Key.UP)
			);
		}
		
		public static function toDirection(down:Boolean = false, left:Boolean = false, 
										   right:Boolean = false, up:Boolean = false):int {
			var dir:int = -1;
		    if (down)          dir = DIRECTION.S;
			if (left)          dir = DIRECTION.W;
			if (right)         dir = DIRECTION.E;
			if (up)            dir = DIRECTION.N;
			if (left && down)  dir = DIRECTION.SW;
			if (left && up)    dir = DIRECTION.NW;
			if (right && up)   dir = DIRECTION.NE;
			if (right && down) dir = DIRECTION.SE;
			return dir;
		}
		
		public static function isDown(y1:int, y2:int):Boolean { return y1 < y2 }
		public static function isUp(y1:int, y2:int):Boolean { return y1 > y2 }
		public static function isLeft(x1:int, x2:int):Boolean { return x1 > x2 }
		public static function isRight(x1:int, x2:int):Boolean { return x1 < x2 }
		public static function dirFromXY(startX:int, startY:int, endX:int, endY:int):int {
			return	toDirection(isDown(startY, endY), isLeft(startX, endX),
								isRight(startX, endX), isUp(startY, endY));
		}

		public static function dirToX(dir:int):int {
			if (dir == 2) return -1; 
			if (dir == 6) return 1; 
			if (dir == 1) return -1; 
			if (dir == 3) return -1; 
			if (dir == 5) return 1; 
			if (dir == 7) return 1;
			return 0;
		}
		public static function dirToY(dir:int):int {
			if (dir == 0) return 1;
			if (dir == 4) return -1;
			if (dir == 1) return 1;
			if (dir == 3) return -1;
			if (dir == 5) return -1;
			if (dir == 7) return 1;
			return 0;
		}
		
		public static function roundToMapBox(coord:int):int {
			return Math.floor(coord / 20) * 20
		}
	}

}