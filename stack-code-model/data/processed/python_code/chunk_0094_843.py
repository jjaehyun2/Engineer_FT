package code
{
	import flash.display.Bitmap;
	import flash.display.Loader;
	import flash.display.MovieClip;
	import flash.display.Sprite;
	import flash.net.URLLoader;
	import flash.net.URLRequest;

	import starling.core.Starling;
	import starling.events.Event;
	import starling.textures.Texture;
	
	/****************************
	 * SpriteSheetStage class
	 * 
	 * @langversion ActionScript 3.0
	 * @playerversion Flash 10.0.0
	 */
	public class SpriteSheetStage extends MovieClip
	{
		//***********************
		// Properties:
		
		protected var _animator:*;
		protected var _fps:uint = 30;
		protected var _inited:Boolean = false;
		protected var _starling:Starling;
		
		public var initFunction:Function;
		
		//***********************
		// Constructor:
		
		public function SpriteSheetStage()
		{
			start();
		}
		
		//***********************
		// Events:
		
		protected function initAnimator( event:* ):void
		{
			// Flag ourselves as inited when the animator is ready to render
			if( animator ){
				_inited = true;
				
				// Relay event
				dispatchEvent(new SpriteSheetEvent(SpriteSheetEvent.READY));
			}else{
				trace("[SpriteSheetStage] Error: Animator can't be located.");
			}
		}
		
		//***********************
		// Methods:
		
		//-----------------------------
		// Sprite sheet commands
		
		public function addSpriteSheet( ssname:String, xmlpath:String, pngpath:String, x:Number, y:Number ):SpriteSheetInstance
		{
			if( animator ){
				return animator.addSpriteSheet( ssname, xmlpath, pngpath, x, y );
			}
			return null;
		}
		
		public function duplicateSpriteSheet( ssname:String, newssname:String, x:Number, y:Number ):SpriteSheetInstance
		{
			if( animator ){
				return animator.duplicateSpriteSheet( ssname, newssname, x, y );
			}
			return null;
		}
		
		public function getSpriteSheet( ssname:String ):SpriteSheetInstance
		{
			if( animator ){
				return animator.getSpriteSheet( ssname );
			}
			return null;
		}
		
		//-----------------------------
		// Start the Starling framework
		
		public function start():void
		{
			Starling.handleLostContext = true;
			
			// Startup starling and listen for the root created event...
			_starling = new Starling(SpriteSheetGenerator, stage);
			_starling.addEventListener(Event.ROOT_CREATED, initAnimator);
			_starling.start();
		}
		
		//***********************
		// Public properties:
		
		//---------------
		// fps
		
		public function set fps( value:uint ):void
		{
			if( animator ){
				animator.fps = value;
			}
			_fps = value;
		}
		
		public function get fps():uint
		{
			return _fps;
		}
		
		//---------------
		// animator
		
		public function get animator():SpriteSheetGenerator
		{
			if( _animator == null ){
				if( Starling.current != null ){
					if( Starling.current.stage != null && Starling.current.stage.numChildren > 0 ){
						_animator = Starling.current.stage.getChildAt(0);
						
						if( animator ){
							animator.fps = _fps;
						}
					}
				}
			}
			return _animator;
		}
		
		//---------------
		// inited
		
		public function get inited():Boolean
		{
			return _inited;
		}
	}
}