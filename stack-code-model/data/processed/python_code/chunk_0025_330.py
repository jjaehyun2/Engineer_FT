package com.profusiongames.notifications 
{
	import starling.display.Image;
	import starling.display.Sprite;
	import starling.textures.Texture;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class EnemySign extends Sprite 
	{
		[Embed(source = "../../../../lib/Graphics/notifications/warning.png")]private var _warning:Class;
		private var _image:Image;
		public function EnemySign() 
		{
			_image = new Image(Texture.fromBitmap(new _warning()));
			addChild(_image);
		}
		
	}

}