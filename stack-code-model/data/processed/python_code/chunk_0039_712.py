package com.profusiongames.items 
{
	import com.profusiongames.status.Status;
	import starling.display.Image;
	import starling.textures.Texture;
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Booster extends Status
	{
		[Embed(source="../../../../lib/Graphics/items/booster/booster.png")]private var _booster:Class;
		private var _image:Image;
		public function Booster() 
		{
			_image = new Image(Texture.fromBitmap(new _booster()));
			addChild(_image);
			pivotX = _image.width / 2;
			pivotY = _image.height / 2;
			
			isCollectable = true;
			type = "Booster";
			duration = 60 * 2.5;
		}
		
	}

}