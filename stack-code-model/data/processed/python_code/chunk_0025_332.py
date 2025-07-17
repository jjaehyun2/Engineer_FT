//-----------------------------------------------------------------------------
package 
//-----------------------------------------------------------------------------
{
    //-------------------------------------------------------------------------
    
    import flash.utils.*;
	import flash.events.*;
	import flash.display.*;
	import flash.system.*;
	import flash.net.*;
	import flash.text.*;

    //-------------------------------------------------------------------------
    [SWF(width = "1024", height = "600", backgroundColor="#000000")]
    
    public class AS3JS_Demo_20120727_Loader extends Sprite  
    //-------------------------------------------------------------------------
    {
		//---------------------------------------------------------------------
		
		[Embed(source="AS3JS_Demo_20120727_Icon.png")]
		private static var ProgressIcon:Class ;
		
		//---------------------------------------------------------------------
		
		private var splashContainer : DisplayObjectContainer 	= null ;
		private var progressIcon	: DisplayObject				= null ;
        private var progressBack    : Shape         			= null ;
        private var progressFront   : Shape         			= null ;
		private var progressWidth   : int						=   80 ;
		private var lastProgress	: Number 					=    0 ;
        
		//---------------------------------------------------------------------
		public function AS3JS_Demo_20120727_Loader ( ) : void 
		{		    
			stage.scaleMode = StageScaleMode.NO_SCALE ;
			stage.align     = StageAlign.TOP_LEFT ;
			stage.frameRate = 60 ;

            Security.allowInsecureDomain    ( "*" ) ;
            Security.allowDomain            ( "*" ) ;

            // Create splash container
            //
			splashContainer					= new Sprite ( ) ;
			stage.addChild					( splashContainer ) ;

            // Create splash back
            //
			var splashBack:Shape			= new Shape ( ) ;
            splashBack.graphics.lineStyle 	( 0, 0 ) ;
            splashBack.graphics.beginFill 	( 0x000000 ) ;
            splashBack.graphics.drawRect	( 0, 0, stage.stageWidth, stage.stageHeight ) ;
            splashBack.graphics.endFill   	( ) ;
            splashContainer.addChild 		( splashBack ) ;

			// Create progress icon
			//
			progressIcon					= new ProgressIcon ( ) as DisplayObject ;
			progressIcon.x					= ( stage.stageWidth  / 2 - progressIcon.width  / 2 ) ;
			progressIcon.y					= ( stage.stageHeight / 2 - progressIcon.height / 2 ) ;
			splashContainer.addChild 		( progressIcon ) ;	
						
            // Create progress bar back
            //
            progressBack    				= new Shape ( ) ;
            progressBack.graphics.lineStyle ( 1, 0x202020 ) ;
            progressBack.graphics.beginFill ( 0x000000 ) ;
            progressBack.graphics.drawRect	( ( stage.stageWidth - progressWidth ) / 2, ( stage.stageHeight + progressIcon.height ) / 2 + 16, progressWidth, 4 ) ;
            progressBack.graphics.endFill   ( ) ;
            splashContainer.addChild 		( progressBack ) ;

            // Create progress bar front
            //
            progressFront   				= new Shape ( ) ;
			splashContainer.addChild 		( progressFront ) ;
                    
            // Create the loader
            //
            var loader : Loader = new Loader ( ) ;
            loader.contentLoaderInfo.addEventListener ( ProgressEvent.PROGRESS, onProgress ) ;
            loader.contentLoaderInfo.addEventListener ( Event.COMPLETE,         onComplete ) ;
            loader.load ( new URLRequest ( "AS3JS_Demo_20120727.swf" ) ) ;
            stage.addChild ( loader ) ;
		}
        

        private function onProgress ( e:ProgressEvent ) : void
        {
            var perc:Number = e.bytesLoaded / e.bytesTotal ;
			
			if ( perc > lastProgress + 0.01 )
			{
				lastProgress = perc ;
				progressFront.graphics.lineStyle 	( 1, 0x202020 ) ;
				progressFront.graphics.beginFill 	( 0x808080 ) ;
				progressFront.graphics.drawRect		( ( stage.stageWidth - progressWidth ) / 2, ( stage.stageHeight + progressIcon.height ) / 2 + 16, Math.ceil ( perc * progressWidth ), 4 ) ;
				progressFront.graphics.endFill   	( ) ;
			}
        }

        private function onComplete ( e:Event ) : void
        {
			// Hide progress bar back and front
			//
			splashContainer.removeChild ( progressBack  ) ; 
            splashContainer.removeChild ( progressFront ) ;
			
			// Indicate the splash icon object to the main application
			//
			e.target.content.init ( splashContainer ) ;

			// Create a text field (TODO: localize it)
			//
			var fmt:TextFormat 	= new TextFormat ( ) ;
			fmt.font			= "Helvetica" ;
			fmt.size			= 11 ;
			var txt:TextField 	= new TextField ( ) ;
			txt.text 			= "...initializing..." ;
			txt.textColor		= 0x808080 ;
			txt.autoSize		= TextFieldAutoSize.CENTER ;
			txt.antiAliasType	= AntiAliasType.ADVANCED ;
			txt.x				= 0 ;
			txt.y				= ( stage.stageHeight + progressIcon.height ) / 2 + 10 ;
			txt.width 			= stage.stageWidth  ;
			txt.height			= 11 ;
			txt.setTextFormat	( fmt ) ;
			splashContainer.addChild ( txt ) ;
			
			// Release local references
			//
			progressIcon  	= null ;
            progressBack  	= null ;
            progressFront 	= null ;
			splashContainer	= null ;
		}        
        
    //-------------------------------------------------------------------------
    }
//-----------------------------------------------------------------------------
}
//-----------------------------------------------------------------------------