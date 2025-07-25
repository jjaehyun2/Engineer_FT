package com.distriqt.test.branch
{
	import feathers.controls.Button;
	import feathers.controls.ScrollContainer;
	import feathers.layout.HorizontalAlign;
	import feathers.layout.HorizontalLayout;
	import feathers.layout.VerticalAlign;
	import feathers.layout.VerticalLayout;
	import feathers.themes.MetalWorksMobileTheme;
	
	import starling.display.Sprite;
	import starling.events.Event;
	import starling.text.TextField;
	import starling.text.TextFormat;
	import starling.utils.Color;
	
	public class Main extends Sprite implements ILogger
	{
		////////////////////////////////////////////////////////
		//	CONSTANTS
		//
		
		
		////////////////////////////////////////////////////////
		//	VARIABLES
		//
		
		private var _tests		: BranchTests;
		
		private var _container	: ScrollContainer;
		private var _text		: TextField;
		
		
		////////////////////////////////////////////////////////
		//	FUNCTIONALITY
		//
		
		
		/**
		 *  Constructor
		 */
		public function Main()
		{
			super();
			addEventListener( Event.ADDED_TO_STAGE, addedToStageHandler );
		}
		
		
		public function log( tag:String, message:String ):void
		{
			trace( tag+"::"+message );
			if (_text)
				_text.text = tag+"::"+message + "\n" + _text.text ;
		}
		
		
		////////////////////////////////////////////////////////
		//	INTERNALS
		//
		
		
		private function init():void
		{
			var tf:TextFormat = new TextFormat( "_typewriter", 12, Color.WHITE, HorizontalAlign.LEFT, VerticalAlign.TOP );
			_text = new TextField( stage.stageWidth, stage.stageHeight, "", tf );
			_text.y = 40;
			_text.touchable = false;
			
			var layout:VerticalLayout = new VerticalLayout();
			layout.horizontalAlign = HorizontalAlign.RIGHT;
			layout.verticalAlign = VerticalAlign.BOTTOM;
			layout.gap = 5;
			
			_container = new ScrollContainer();
			_container.y = 50;
			_container.layout = layout;
			_container.width = stage.stageWidth;
			_container.height = stage.stageHeight-50;
			
			_tests = new BranchTests( this );
			
			addAction( "Initialise", _tests.initSession );
			addAction( "Latest Params", _tests.getLatestReferringParams );
			
//			addAction( "Get Short Url", _tests.getShortUrl );
			addAction( "Set Identity", _tests.setIdentity );
			
			addAction( "Standard :Track", _tests.trackStandard );
			addAction( "Custom :Track", _tests.trackCustom );
			
			addAction( "Validate :Debug", _tests.validateIntegration );
			
			
			addAction( "Generate Short Link :BUO", _tests.createObjectAndGenerateShortLink );
			
			addChild( _text );
			addChild( _tests );
			addChild( _container );
		}
		
		
		private function addAction( label:String, listener:Function, parent:Sprite=null ):void
		{
			var b:Button = new Button();
			b.label = label;
			if (listener != null)
				b.addEventListener( starling.events.Event.TRIGGERED, listener );
			else
				b.isEnabled = false;
			
			if (parent != null) parent.addChild( b );
			else if (_container != null) _container.addChild( b );
		}
		
		
		////////////////////////////////////////////////////////
		//	EVENT HANDLERS
		//
		
		protected function addedToStageHandler(event:Event):void
		{
			removeEventListener(Event.ADDED_TO_STAGE, addedToStageHandler );
			new MetalWorksMobileTheme();
			init();
		}
		
		
	}
}