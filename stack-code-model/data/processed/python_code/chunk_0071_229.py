package  
{
	import flash.display.BitmapData;
	import net.flashpunk.Entity;
	import net.flashpunk.graphics.Image;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Lava extends Entity 
	{
		private var _image:Image;
		public function Lava(X:int,Y:int) 
		{
			super(X, Y);
			_image = new Image(new BitmapData(16, 16, true, 0x55FF6600));
			graphic = _image;
			setHitbox(16, 14, 0, -2);
			type = "Lava";
			layer = 100;
		}
		
	}

}