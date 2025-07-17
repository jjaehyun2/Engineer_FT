package com.profusiongames.beings 
{
	import flash.display.Sprite;
	import starling.core.Starling;
	import starling.display.MovieClip;
	import starling.textures.Texture;
	import starling.textures.TextureAtlas;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Birdo extends Enemy
	{
		[Embed(source = "../../../../lib/Graphics/char/boy_frames.png")]private var _animTexture:Class;
		[Embed(source = "../../../../lib/Graphics/char/boy_frames.xml", mimeType = "application/octet-stream")]private var _animXML:Class;
		private var _animation:MovieClip;
		private var _facingLeft:Boolean = true;
		private var _flySpeed:Number = 2.5;
		public function Birdo() 
		{
			var texture:Texture = Texture.fromBitmap(new _animTexture());
			var xmlData:XML = XML(new _animXML());
			var textureAtlas:TextureAtlas = new TextureAtlas(texture, xmlData);
			_animation = new MovieClip(textureAtlas.getTextures("bird_"), 30);
			_animation.play();
			addChild(_animation);
			Starling.juggler.add(_animation);
			
			pivotX = _animation.width / 2 + 6;
			pivotY = _animation.height / 2;
			
			_widthShrink = 8;
			_heightShrink = 9;
		}
		override public function frame():void
		{
			super.frame();
			move();
		}
		
		private function move():void 
		{
			if (_facingLeft)
			{
				x -= _flySpeed;
				if (x < 40)
				{
					_facingLeft = !_facingLeft;
					scaleX = -1;
				}
			}
			else
			{
				x += _flySpeed;
				if (x > Main.WIDTH - 40)
				{
					_facingLeft = !_facingLeft;
					scaleX = 1;
				}
			}
		}
	}

}