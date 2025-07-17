package com.profusiongames.windows 
{
	import starling.display.Image;
	import starling.display.Sprite;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Window extends Sprite 
	{
		private var _background:Image;
		public function Window() 
		{
			
		}
		
		public function center():void
		{
			pivotX =  int(background.width / 2);
			pivotY =  int(background.height / 2);
			x = int(Main.WIDTH / 2);
			y =  int(Main.HEIGHT / 2);
		}
		
		public function get background():Image 
		{
			return _background;
		}
		
		public function set background(value:Image):void 
		{
			_background = value;
		}
		
		public function close():void
		{
			parent.removeChild(this);
			dispose();
		}
	}

}