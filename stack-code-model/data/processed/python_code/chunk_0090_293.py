package code
{
	import flash.display.Bitmap;
	import flash.events.Event;
	import flash.events.EventDispatcher;
	
	import starling.display.MovieClip;
	import starling.textures.TextureAtlas;
	
	/****************************
	 * SpriteSheetInstance class
	 * 
	 * @langversion ActionScript 3.0
	 * @playerversion Flash 10.0.0
	 */
	public class SpriteSheetInstance extends EventDispatcher
	{
		//***********************
		// Properties:
		
		protected var _baseName:String;
		protected var _id:String;
		protected var _inited:Boolean = false;
		protected var _loader:SpriteSheetLoader;
		protected var _movieClip:MovieClip;
		protected var _textureAtlas:TextureAtlas;
		protected var _x:Number;
		protected var _y:Number;
		
		//***********************
		// Constructor:
		
		public function SpriteSheetInstance(){
			//...
		}
		
		//***********************
		// Events:
		
		public function onSpriteSheetLoaded( event:SpriteSheetEvent ):void
		{
			event.currentTarget.removeEventListener(SpriteSheetEvent.SPRITE_SHEET_LOADED, onSpriteSheetLoaded);
			
			// Relay event
			dispatchEvent(new SpriteSheetEvent(SpriteSheetEvent.SPRITE_SHEET_LOADED));
		}
		
		//***********************
		// Public Properties:
		
		//---------------
		// baseName
		
		public function set baseName( value:String ):void
		{
			_baseName = value;
		}
		
		public function get baseName():String
		{
			return _baseName;
		}
		
		//---------------
		// id
		
		public function set id( value:String ):void
		{
			_id = value;
		}
		
		public function get id():String
		{
			return _id;
		}
		
		//---------------
		// inited
		
		public function set inited( value:Boolean ):void
		{
			_inited = value;
			
			if( value ){
				dispatchEvent(new SpriteSheetEvent(SpriteSheetEvent.SPRITE_SHEET_INIT));
			}
		}
		
		public function get inited():Boolean
		{
			return _inited;
		}
		
		//---------------
		// loader
		
		public function set loader( value:SpriteSheetLoader ):void
		{
			_loader = value;
		}
		
		public function get loader():SpriteSheetLoader
		{
			return _loader;
		}
		
		//---------------
		// movieClip
		
		public function set movieClip( value:MovieClip ):void
		{
			_movieClip = value;
		}
		
		public function get movieClip():MovieClip
		{
			return _movieClip;
		}
		
		//---------------
		// textureAtlas
		
		public function set textureAtlas( value:TextureAtlas ):void
		{
			_textureAtlas = value;
		}
		
		public function get textureAtlas():TextureAtlas
		{
			return _textureAtlas;
		}
		
		//---------------
		// xPosition
		
		public function set xPosition( value:Number ):void
		{
			_x = value;
		}
		
		public function get xPosition():Number
		{
			return _x;
		}
		
		//---------------
		// yPosition
		
		public function set yPosition( value:Number ):void
		{
			_y = value;
		}
		
		public function get yPosition():Number
		{
			return _y;
		}
	}
}