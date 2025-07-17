/**
 *        __       __               __ 
 *   ____/ /_ ____/ /______ _ ___  / /_
 *  / __  / / ___/ __/ ___/ / __ `/ __/
 * / /_/ / (__  ) / / /  / / /_/ / / 
 * \__,_/_/____/_/ /_/  /_/\__, /_/ 
 *                           / / 
 *                           \/ 
 * http://distriqt.com
 *
 * This is a test application for the distriqt extension
 * 
 * @author Michael Archbold & Shane Korin
 * 	
 */
package
{
	import com.distriqt.extension.core.Core;
	import com.distriqt.extension.parse.Parse;
	import com.distriqt.extension.parse.ParseInstallation;
	import com.distriqt.extension.parse.events.ParseEvent;
	import com.distriqt.extension.parse.events.ParseObjectEvent;
	import com.distriqt.extension.parse.push.Channel;
	
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.text.TextField;
	import flash.text.TextFormat;
	
	
	/**	
	 * Sample application for using the Parse Native Extension
	 */
	public class TestParse extends Sprite
	{
		public static var APP_KEY 				: String = "APPLICATION_KEY";
		public static var PARSE_APPLICATION_ID 	: String = "";
		public static var PARSE_CLIENT_KEY 		: String = "";
		
		
		/**
		 * Class constructor 
		 */	
		public function TestParse()
		{
			super();
			
			create();
			init();
		}
		
		
		//
		//	VARIABLES
		//
		
		private var _text		: TextField;
		
		
		//
		//	INITIALISATION
		//	
		
		private function create( ):void
		{
			stage.align = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.NO_SCALE;
			
			_text = new TextField();
			_text.defaultTextFormat = new TextFormat( "_typewriter", 18 );
			addChild( _text );

			stage.addEventListener( Event.RESIZE, stage_resizeHandler, false, 0, true );
			stage.addEventListener( MouseEvent.CLICK, mouseClickHandler, false, 0, true );
			
			addEventListener( Event.ACTIVATE, activateHandler, false, 0, true );
			addEventListener( Event.DEACTIVATE, deactivateHandler, false, 0, true );
		}
		
		
		protected function init( ):void
		{
			try
			{
				Core.init();
				Parse.init( APP_KEY );
				
				message( "Parse Supported: " + Parse.isSupported );

				if (Parse.isSupported)
				{
					message( "Core Version:    " + Core.service.version );
					message( "Parse Version:   " + Parse.service.version );
					message( "Parse Notifications Enabled:   " + Parse.service.notificationsEnabled() );
					
					Parse.service.addEventListener( ParseEvent.NOTIFICATION, parse_notificationHandler );
					Parse.service.addEventListener( ParseEvent.FOREGROUND_NOTIFICATION, parse_notificationHandler );
					Parse.service.addEventListener( ParseEvent.BACKGROUND_NOTIFICATION, parse_notificationHandler );
					
					Parse.service.addEventListener( ParseEvent.REGISTERING, 		parse_printEventHandler );
					Parse.service.addEventListener( ParseEvent.REGISTER_SUCCESS, 	parse_registerHandler );
					Parse.service.addEventListener( ParseEvent.UNREGISTERED, 		parse_printEventHandler );
					
					Parse.service.addEventListener( ParseEvent.ERROR, parse_errorHandler );
					
					Parse.service.setupApplication( PARSE_APPLICATION_ID, PARSE_CLIENT_KEY, false );
					Parse.service.register( false );
				}
				
			}
			catch (e:Error)
			{
				message( "ERROR:" + e.message );
			}
		}
		
		
		//
		//	FUNCTIONALITY
		//
		
		protected function message( str:String ):void
		{
			trace( str );
			_text.appendText(str+"\n");
		}
		
		
		//
		//	EVENT HANDLERS
		//
		
		private function stage_resizeHandler( event:Event ):void
		{
			_text.width  = stage.stageWidth;
			_text.height = stage.stageHeight - 100;
		}
		
		
		private function mouseClickHandler( event:MouseEvent ):void
		{
			//
			//	Do something when user clicks screen?
			//	
			
			if (Parse.isSupported)
			{
				var installation:ParseInstallation = Parse.service.getCurrentInstallation();
				message( "Installation ID: " + installation.installationId );
				message( "Installation.alias: " + installation.getString( "alias" ) );
				
				installation.putString( "alias", "dsqt" );
				installation.saveInBackground();
			}
		}
		
		private function activateHandler( event:Event ):void
		{
		}
		
		private function deactivateHandler( event:Event ):void
		{
		}
		
		
		//
		//	EXTENSION HANDLERS
		//

		private function parse_notificationHandler( event:ParseEvent ):void
		{
			message("Remote notification received! :: " + event.type );
			message( event.data );	
		}
		
		
		private function parse_printEventHandler( event:ParseEvent ):void
		{
			message( event.type + " :: " + event.data );
		}
		
		
		private function parse_registerHandler( event:ParseEvent ):void
		{
			message( event.type );
			
//			Parse.service.subscribe( new Channel( "test_1" ) );
//			Parse.service.subscribe( new Channel( "test_2" ) );
			
			var subscriptions:Vector.<Channel> = Parse.service.getSubscriptions();

			message( "============= SUBSCRIPTIONS ==================" );
			for each (var channel:Channel in subscriptions)
				message( "CHANNEL:: " + channel.name );
			message( "==============================================" );
			
			
//			Parse.service.unsubscribe( new Channel( "test_1" ));
			
			
			Parse.service.getCurrentInstallation().addEventListener( ParseObjectEvent.SAVEINBACKGROUND_COMPLETE, installation_saveInBackgroundHandler, false, 0, true );
		}
		
		
		private function parse_errorHandler( event:ParseEvent ):void
		{
			message( "ERROR:: " + event.data );
		}
		
		
		private function installation_saveInBackgroundHandler( event:ParseObjectEvent ):void
		{
			message( "installation_saveInBackgroundHandler" );
		}

		
	}
}