package  
{
	import net.flashpunk.Entity;
	import net.flashpunk.graphics.Image;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Overlay extends Entity 
	{
		[Embed(source = "Assets/Graphics/vignette_darker_100.png")]private const OVER:Class;
		private var _image:Image;
		public function Overlay() 
		{
			_image = new Image(OVER);
			graphic = _image;
			layer = 9999;
			
			_image.scrollX = 0;
			_image.scrollY = 0;
			
			active = false;
		}
		
	}

}