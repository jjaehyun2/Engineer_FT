package starling.display 
{
	import flash.display3D.textures.TextureBase;
	import flash.external.ExtensionContext;
	import flash.geom.Rectangle;
	import flash.utils.Dictionary;
	import starling.animation.DelayedCall;
	import starling.animation.IAnimatable;
	import starling.animation.Juggler;
	import starling.core.Starling;
	import starling.display.Image;
	import starling.display.MovieClip;
	import starling.textures.SubTexture;
	import starling.textures.Texture;
	import wingon.misc.ExtendedMath;
	
	public class AnimatedImage extends Image implements Updateable
	{				
		public const COMPLETE : String = "";
		public const START : String = "";
				
		private var _animations:Dictionary = new Dictionary();
		private var _frameTime:Number = 0;
		private var _fps:Number = 0;
		private var _fpsScale:Number = 0;
		private var _invFpsScale:Number = 0;
		private var _currentAnimation:String = "";
		private var _currentAnimationCache:Object = null;
		private var _currentFrame:uint = 0;
		private var _currentTime:Number = 0;
		private var _checkIfNewAnimation:Boolean = false; //Kollar om en ny animation spelades under signalen animationComplete kördes, isåfall så ändra inte variabler som redan är ändrade
		
		public function AnimatedImage( fps:Number = 10 )
		{
			super();
			_animations = new Dictionary();
			fpsScale = 1;
		}
		
		public function Update( passedTime:Number ):void
        {
			//Väntar på att play animation ska köras
			if ( _currentAnimationCache === null )
				return;
				
			_checkIfNewAnimation = false;
			_currentTime += passedTime;
			if ( _currentTime > _frameTime * _invFpsScale )
			{
				//Byt frame
				_currentTime -= _frameTime * _invFpsScale;
				_currentFrame++;
				if ( _currentFrame >= _currentAnimationCache.animation.length )
				{
					this.dispatchEventWith(COMPLETE, true);
					if ( _checkIfNewAnimation === false ) //ingen ny animation kördes
					{
						if ( _currentAnimationCache.loop )
							_currentFrame = 0;
						else
							_currentFrame--; //gå tillbaka till sista framen
					}
				}					
				
				if ( _checkIfNewAnimation === false )
					ChangeTexture();				
			}
		}
		
		public function AddAnimation( name:String, textures:Vector.<Texture>, frameSequence:Array = null, fps: Number = 10, loop:Boolean = true ):void
		{
			var animation:Vector.<Texture>;
			var i:int;
			if ( fps === 0 )
			{
				throw new Error( "AnimatedImage: Can't set fps to 0 in AddAnimation" );
			}
			if ( frameSequence === null )
			{
				animation = new Vector.<Texture>( textures.length, true );
				
				for ( i = 0; i < animation.length; i++ )
				{
					animation[i] = textures[i];
				}
			} else
			{
				animation = new Vector.<Texture>( frameSequence.length, true );
				
				for ( i = 0; i < animation.length; i++ )
				{
					var index:int = int(frameSequence[i]);
					animation[i] = textures[index];
				}
			}
			if ( _animations[name] == null )				
				_animations[name] = { name: name, animation: animation, frameTime:1 / fps, loop: loop };			
			else
			{
				var animObj:Object = _animations[name];
				animObj.animation = animation;
				animObj.frameTime = 1 / fps;
				animObj.loop = loop;				
			}
		}
		
		public function PlayAnimation( name:String, randomFrame:Boolean = false ):void
		{
			if ( name === _currentAnimation )
				return;
				
			var animation:Object = _animations[name];
			
			if ( animation === null )
				throw new Error( "AnimatedImage: Couldn't play animation " + name );	
				
			_currentAnimationCache = animation;
			_checkIfNewAnimation = true;
			_currentAnimation = name;
			_frameTime = animation.frameTime;
			if ( randomFrame )
			{
				_currentFrame = ExtendedMath.randomIntRange( 0, _currentAnimationCache.animation.length - 1 );
			}else
			{
				_currentFrame = 0;
			}
			_currentTime = 0;
			ChangeTexture();
			this.dispatchEventWith(START, true);
		}
		
		private function ChangeTexture() : void
		{			
			if ( _currentAnimationCache.animation.length <= _currentFrame )
				throw new Error( "AnimatedImage: Missing frames for animation, make sure to load correct amount of frames" );
			var texture:Texture = _currentAnimationCache.animation[_currentFrame];			
			
			if ( !this.texture || texture.width != this.texture.width || texture.height != this.texture.height ||
				!texture.frame && !this.texture.frame && ( texture.frame.width != this.texture.frame.width || texture.frame.height != this.texture.frame.height ) )
			{
				this.texture = texture;
				readjustSize();
			}else
			{
				this.texture = texture;
			}
		}
				
		public function get currentAnimation():String 
		{
			return _currentAnimation;
		}
		
		public function get currentFrame():String 
		{
			return _animations[_currentAnimation].name;
		}
		
		public function get fpsScale():Number 
		{
			return _fpsScale;
		}
		
		public function set fpsScale(value:Number):void 
		{
			_fpsScale = value;
			_invFpsScale = 1 / _fpsScale;
		}
		
	}

}