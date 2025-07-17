//-----------------------------------------------------------------------------
package 
//-----------------------------------------------------------------------------
{
    //-------------------------------------------------------------------------
    
	import flash.text.*;
    import flash.utils.*;
	import flash.events.*;
	import flash.display.*;
	import flash.display3D.*;
	import flash.system.Capabilities;
	import flash.net.*;

    import com.stonetrip.shiva.engine.*;

    //-------------------------------------------------------------------------
    [SWF(width = "1024", height = "600", backgroundColor="#000000")]
    
    public class FlashInteractionDemo_20120624 extends Sprite  
    //-------------------------------------------------------------------------
    {
		//---------------------------------------------------------------------
        private const kTotalStackSizeInBytes : int =    2 * 1024 * 1024 ;
        private const kTotalHeapSizeInBytes  : int =  256 * 1024 * 1024 ;
		
		//---------------------------------------------------------------------
		private var splashScreen : DisplayObject = null ;
		private var as3demobutton:Sprite;
        
		//---------------------------------------------------------------------
		public function FlashInteractionDemo_20120624 ( ) : void 
		{		    
            addEventListener ( Event.ADDED_TO_STAGE, onAddedToStage ) ;
        }

		//---------------------------------------------------------------------
		public function init ( splash:DisplayObject ) : void 
		{
			splashScreen = splash ;
		}

		//---------------------------------------------------------------------
        private function onAddedToStage ( _e:Event ) : void 
        {
            removeEventListener ( Event.ADDED_TO_STAGE, onAddedToStage ) ;

			// Configure stage initial params
			//
			stage.scaleMode = StageScaleMode.NO_SCALE ;
			stage.align     = StageAlign.TOP_LEFT ;
			stage.frameRate = 30 ;
			
			if ( getFlashPlayerMajorVersion ( ) < 11 )
			{
				displayFlashPlayerVersionError ( ) ;
			}
			else
			{
				// Request 3D context
				//
				stage.stage3Ds[0].addEventListener ( Event.CONTEXT3D_CREATE, onContext3DCreate ) ;
				stage.stage3Ds[0].requestContext3D ( ) ;
			}
		}
		
       //---------------------------------------------------------------------
		private function getFlashPlayerMajorVersion ( ) : int
		{
			var flashPlayerMajorVersion:int = 0;
 
			var versionString:String = Capabilities.version;
			var pattern:RegExp = /^(\w*) (\d*),(\d*),(\d*),(\d*)$/;
			var result:Object = pattern.exec(versionString);
			if (result != null) 
			{
				flashPlayerMajorVersion = int(result[2]);
			} 
			return flashPlayerMajorVersion;
		}
		
       //---------------------------------------------------------------------
		private function displayFlashPlayerVersionError ( ) : void
		{
			// Create a text field (TODO: localize it)
			//
			var fmt:TextFormat 	= new TextFormat ( ) ;
			fmt.font			= "Helvetica" ;
			fmt.size			= 11 ;
			var txt:TextField 	= new TextField ( ) ;
			txt.text 			= "Sorry, Flash Player 11 is required to view this content." ;
			txt.textColor		= 0x808080 ;
			txt.autoSize		= TextFieldAutoSize.CENTER ;
			txt.antiAliasType	= AntiAliasType.ADVANCED ;
			txt.x				= 0 ;
			txt.y				= stage.stageHeight / 2 ;
			txt.width 			= stage.stageWidth  ;
			txt.height			= 11 ;
			txt.setTextFormat	( fmt ) ;
			stage.addChild 		( txt ) ;
		}

        //---------------------------------------------------------------------
		private function onContext3DCreate ( _e:Event ) : void
		{
		    if ( _e != null && _e.target != null )
		    {
        	    Bridge.init ( kTotalStackSizeInBytes, kTotalHeapSizeInBytes, stage, _e.target as Stage3D, onEngineInitialized, onEngineEvent, [  ], 2, 1 ) ;
    		}
    		else
    		{
    		    trace ( "Could not create Context3D!" ) ;
		    }
		}

		//---------------------------------------------------------------------
		private function onEngineInitialized ( ) : void
		{
    		addEventListener ( Event.ENTER_FRAME, onEnterFrame ) ;
        }
        		
		//---------------------------------------------------------------------
		
		private function onEngineEvent ( _args:Array, _returns:Array ) : void 
		{
            const kVarTypeNil       : int = 0 ;
            const kVarTypeNumber    : int = 1 ;
            const kVarTypeString    : int = 2 ;
            const kVarTypeBoolean	: int = 3 ;

            if ( _args[2] == kVarTypeString )
			{
				if ( _args[3] == "image" )
				{
					var imageLoader:Loader = new Loader();
					var image:URLRequest = new URLRequest("http://www.stonetrip.com/press/tn_ShiVaEditor.png");
					imageLoader.load(image);
					stage.addChild (imageLoader);
					imageLoader.x = 160;
					imageLoader.y = 280;
				} 
				
				if ( _args[3] == "button" )
				{
					as3demobutton = new Sprite();
					as3demobutton.graphics.beginFill(0xFFCC00);
 					as3demobutton.graphics.drawRect(550, 300, 300, 80); //Set the X,Y, Width, and Height of the button graphic
					as3demobutton.graphics.endFill();
					//button hand and click stuff
					as3demobutton.useHandCursor = true;
					as3demobutton.buttonMode = true;
					as3demobutton.mouseChildren = false;
					
					as3demobutton.addEventListener(MouseEvent.CLICK, as3buttonClickHandler);
					as3demobutton.addEventListener(MouseEvent.ROLL_OVER, as3buttonRollOverHandler);
					as3demobutton.addEventListener(MouseEvent.ROLL_OUT, as3buttonRollOutHandler);
					
					var myFormat:TextFormat = new TextFormat();
					myFormat.size = 20;
					var text:TextField = new TextField();
					text.defaultTextFormat = myFormat;
					text.text = "Click me! I change color.";
					text.textColor = 0xFFFFFF;
					text.width = 250;
					text.selectable = false;
					text.mouseEnabled = false;
										
					stage.addChild ( as3demobutton ) ;
					stage.addChild(text);
					text.x = 600;
					text.y = 330;

				}
			}
		}
		    
		//---------------------------------------------------------------------
		private function onEnterFrame ( _e:Event ) : void
		{
			// Fade out splash screen if any
			//
			if ( splashScreen != null )
			{
				splashScreen.alpha = Math.max ( 0.0, splashScreen.alpha - 2.0 / stage.frameRate ) ;
				
				if ( splashScreen.alpha == 0 )
				{
					stage.removeChild 	( splashScreen ) ;
					splashScreen 		= null ;
				}
			}
		}
		
		//---------------------------------------------------------------------		
		private function as3buttonClickHandler(event:MouseEvent):void
		{
			turnButtonGreen();
		}
 
		private function as3buttonRollOverHandler(event:MouseEvent):void
		{
			turnButtonRed();
		}
 
		private function as3buttonRollOutHandler(event:MouseEvent):void
		{
			turnButtonYellow();
		}
 
		private function turnButtonRed():void
		{
			as3demobutton.graphics.beginFill(0xFF0000);
			as3demobutton.graphics.drawRect(550, 300, 300, 80);
			as3demobutton.graphics.endFill();
		}
 
		private function turnButtonYellow():void
		{
			as3demobutton.graphics.beginFill(0xFFCC00);
			as3demobutton.graphics.drawRect(550, 300, 300, 80);
			as3demobutton.graphics.endFill();
		}
 
		private function turnButtonGreen():void
		{
			as3demobutton.graphics.beginFill(0x008000);
			as3demobutton.graphics.drawRect(550, 300, 300, 80);
			as3demobutton.graphics.endFill();
		}

    //-------------------------------------------------------------------------
    }
//-----------------------------------------------------------------------------
}
//-----------------------------------------------------------------------------