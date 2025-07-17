package com.profusiongames.beings 
{
	import com.profusiongames.items.Item;
	import com.profusiongames.status.Status;
	import com.profusiongames.util.Vector2D;
	import flash.display.Bitmap;
	import org.flashdevelop.utils.FlashConnect;
	import starling.core.Starling;
	import starling.display.MovieClip;
	import starling.textures.Texture;
	import starling.textures.TextureAtlas;
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Player extends Being
	{
		[Embed(source = "../../../../lib/Graphics/char/boy_frames.png")]private var _animTexture:Class;
		[Embed(source = "../../../../lib/Graphics/char/boy_frames.xml", mimeType = "application/octet-stream")]private var _animXML:Class;
		private var _animation:MovieClip;
		private var _animationForward:MovieClip;
		private var _animationLeft:MovieClip;
		private var _animationRight:MovieClip;
		private var _animationBack:MovieClip;
		private var _speed:Vector2D;
		public static var GRAVITY:Number = 0.5;
		private var _maxYSpeed:Number = 30; //going down
		private var _minYSpeed:Number = -30; //going up
		private var _maxXSpeed:Number = 5;
		
		private var _shouldFlash:int = 0;
		private var _flashRate:int = 10; //higher is slower, smaller is faster
		
		private var _angledDirection:Number = Math.PI / 8;
		private var _statuses:Vector.<Status> = new Vector.<Status>();
		
		public static var money:int = 999;
		
		public function Player() 
		{			
			var texture:Texture = Texture.fromBitmap(new _animTexture());
			var xmlData:XML = XML(new _animXML());
			var textureAtlas:TextureAtlas = new TextureAtlas(texture, xmlData);
			_animation = new MovieClip(textureAtlas.getTextures("boy_"), 20);
			_animationForward = new MovieClip(textureAtlas.getTextures("boy_forward_"), 20);
			_animationLeft = new MovieClip(textureAtlas.getTextures("boy_left_"), 20);
			_animationRight = new MovieClip(textureAtlas.getTextures("boy_right_"), 20);
			_animationBack = new MovieClip(textureAtlas.getTextures("boy_back_"), 20);
			//addChild(_animation);
			_animationForward.currentFrame = 1;
			addChild(_animationForward);
			
			//Starling.juggler.add(_animation);
			//Starling.juggler.add(_animationForward);
			
			
			pivotX = _animation.width / 2;
			pivotY = _animation.height / 2;
			reset();
		}
		
		public function reset():void
		{
			x = 50;
			y = 500;
			_speed = new Vector2D(0, -2);
			_statuses.length = 0;
			_numLives = 1;
			_shouldFlash = 0;
			resurrect();
		}
		
		override public function frame():void
		{
			super.frame();
			handleItems();
			move();
			//y -= 1.5;
			rotateTowardsMove();
			flashIfInvincible();
		}
		
		private function handleItems():void 
		{
			var status:Status;
			for (var i:int = 0; i < _statuses.length; i++)
			{
				status = _statuses[i];
				if (status.type == "Booster")
				{
					_speed.y = -12;
				}
				
				
				status.duration--;
				if (status.duration <= 0)
				{
					_statuses.splice(i, 1);
					i--;
				}
			}
		}
		
		private function rotateTowardsMove():void 
		{
			/*if (_speed.y > 0)
			{
				if (Math.abs(rotation) <= 0.05)
				{
					rotation = Math.random() > 0.5 ? 0.0001 : -0.0001;
				}
				if (Math.abs(rotation) != Math.PI && rotation >=0)
				{
					rotation += (Math.PI - rotation) / 8;
				}
				else if (Math.abs(rotation) != Math.PI && rotation<0)
				{
					rotation += (-Math.PI - rotation) / 8;
				}
			}
			else if (_speed.y < 0)*/
			{
				if (Math.abs(_speed.x) < 1)
				{
					if (rotation != 0)
					{
						rotation += (0 - rotation) / 4;
						if (Math.abs(rotation) <= 0.05)
						{
							rotation = 0;
						}
					}
				}
				else if (_speed.x >= 0 && rotation != _angledDirection)
				{
					rotation += (_angledDirection - rotation) / 4;
				}
				else if (_speed.x <= 0 && rotation != -_angledDirection)
				{
					rotation += (-_angledDirection - rotation) / 4;
				}
			}
			//else
			{
				
			}
		}
		private function flashIfInvincible():void 
		{
			if (_shouldFlash > 0)
			{
				_shouldFlash--;
				visible = (_shouldFlash % _flashRate < _flashRate/2);
			}
			else if (visible == false)
			{
				visible = true;
			}
		}
		
		private function move():void 
		{
			if (_speed.y > _maxYSpeed)
				_speed.y = _maxYSpeed;
			else if (_speed.y < _minYSpeed)
				_speed.y = _minYSpeed;
			x += _speed.x;
			y += _speed.y;
			_speed.x *= 0.99;
			_speed.y += GRAVITY;
		}
		
		public function bounce(amount:Number):void
		{
			_speed.y = -amount;
		}
		
		public function get isFalling():Boolean
		{
			return _speed.y > 0;
		}
		
		public function get isInvincible():Boolean
		{
			return _shouldFlash != 0
		}
		
		public function moveHorizontallyTowards(xPos:Number):void
		{
			
			//x = xPos;
			if (xPos > x)
			{
				_speed.x = _maxXSpeed;
				if (xPos < x + _speed.x)
					_speed.x = xPos - x;
			}
			else
			{
				_speed.x = -_maxXSpeed;
				if (xPos > x + _speed.x)
					_speed.x = xPos - x;
			}
		}
		
		public function collect(item:Item):void 
		{
			money += item.monetaryValue;
			if (item is Status)
			{
				_statuses.push(item as Status);
			}
		}
		
		public function collideWithEnemy(enemy:Enemy):void 
		{
			if (enemy is Birdo)
			{
				if (isFalling)
				{
					bounce(enemy.bouncePower);
					enemy.die();
				}
				else if(!isInvincible)
				{
					//instant hurt
					die();
					makeInvincible(60);
				}
			}
			else if (enemy is Spike)
			{
				if (!isInvincible)
				{
					//instant hurt
					die();
					_speed.y *= -4;
					makeInvincible(60);
				}
			}
			else if (enemy is Kopter)
			{
				if (isFalling && !isInvincible)
				{
					//instant hurt
					die();
					makeInvincible(60);
				}
				else 
				{
					bounce(enemy.bouncePower);
					enemy.die();
				}
			}
		}
		
		private function makeInvincible(number:int):void 
		{
			_shouldFlash = number;
		}
		
		
		private function createFrameArray(start:int = 0, count:int=0):Array
		{
			var arr:Array= []; // of int
			
			for (var j:int = start; j < count; j++) {
				arr.push(j);
			}
			FlashConnect.atrace(arr);
			return arr;
		}
	}

}