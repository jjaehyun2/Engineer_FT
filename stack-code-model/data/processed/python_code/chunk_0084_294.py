package com.profusiongames.beings 
{
	import starling.core.Starling;
	import starling.display.MovieClip;
	import starling.events.Event;
	import starling.textures.Texture;
	import starling.textures.TextureAtlas;
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Kopter extends Enemy 
	{
		[Embed(source = "../../../../lib/Graphics/char/boy_frames.png")]private var _animTexture:Class;
		[Embed(source = "../../../../lib/Graphics/char/boy_frames.xml", mimeType = "application/octet-stream")]private var _animXML:Class;
		private var _animation:MovieClip;
		private var _flyingUp:Boolean = true;
		private var _flySpeed:Number = 1;
		private var _deltaY:Number = 40;
		private var _originY:int = 0;
		public function Kopter() 
		{
			var texture:Texture = Texture.fromBitmap(new _animTexture());
			var xmlData:XML = XML(new _animXML());
			var textureAtlas:TextureAtlas = new TextureAtlas(texture, xmlData);
			_animation = new MovieClip(textureAtlas.getTextures("enemy0"), 30);
			_animation.play();
			addChild(_animation);
			Starling.juggler.add(_animation);
			
			bouncePower = 10;
			_widthShrink = 11;
			_heightShrink = 16;
			addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event):void 
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);
			_originY = y;
		}
		override public function frame():void
		{
			super.frame();
			move();
		}
		
		private function move():void 
		{
			if (_flyingUp)
			{
				y -= _flySpeed;
				if (y < _originY - _deltaY)
				{
					_flyingUp = !_flyingUp;
				}
			}
			else
			{
				y += _flySpeed;
				if (y > _originY + _deltaY)
				{
					_flyingUp = !_flyingUp;
				}
			}
		}
	}

}