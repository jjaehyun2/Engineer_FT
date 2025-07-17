package com.profusiongames.scenery 
{
	import starling.display.Image;
	import starling.events.EnterFrameEvent;
	import starling.textures.Texture;
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Cloud extends Scenery
	{
		[Embed(source="../../../../lib/Graphics/scenery/clouds/cloud_side_shadow.png")]private var _cloud:Class;
		private var _image:Image;
		public function Cloud() 
		{
			_image = new Image(Texture.fromBitmap(new _cloud()));
			addChild(_image);
			pivotX = _image.width / 2;
			
			//alpha = 0.2;
			
			//addEventListener(EnterFrameEvent.ENTER_FRAME, frame);
		}
		
		private function frame(e:EnterFrameEvent):void 
		{
			x += 1 / layer.scrollScale;
			if (x > 500+ width ) x = -width;
		}
		
	}

}