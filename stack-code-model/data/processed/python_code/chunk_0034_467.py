package com.profusiongames.platforms 
{
	import starling.display.Image;
	import starling.textures.Texture;
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class SpacePlatform extends Platform 
	{
		[Embed(source = "../../../../lib/Graphics/platforms/space/ground_tile_big.png")]private var _ground:Class;
		[Embed(source = "../../../../lib/Graphics/platforms/space/ground_tile_medium.png")]private var _ground_med:Class;
		[Embed(source="../../../../lib/Graphics/platforms/space/ground_tile_small.png")]private var _ground_small:Class;
		private var _image:Image;
		public function SpacePlatform() 
		{
			_image = new Image(Texture.fromBitmap(new _ground()));
			addChild(_image);
			pivotX = _image.width / 2;
		}
		
		
		override public function changeForAltitude(to:String):void
		{
			removeChild(_image);
			_image.dispose();
			
			if (to == "medium")
				_image = new Image(Texture.fromBitmap(new _ground_med()));
			else if (to == "small")
				_image = new Image(Texture.fromBitmap(new _ground_small()));
				
			addChild(_image);
			pivotX = _image.width / 2;
		}
		
	}

}