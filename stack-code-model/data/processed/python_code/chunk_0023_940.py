package libs.utils
{
	import flash.events.Event;
	import flash.events.HTTPStatusEvent;
	import flash.events.IOErrorEvent;
	
	import libs.vo.GlobalsVO;
	
	import mx.containers.Canvas;
	import mx.controls.Image;
	
	public class PreloadGraphics
	{
		
		
		
		private var _assetsRemaining:int = 0;
		private var _graphicPreloadContainer:Canvas;
		private var _gAssets:Array;
		private var _callBack:Function;
		
		private const DELIMITER:String = "?";
		
		
		public function PreloadGraphics()
		{
		}
		


		
		/**
		 * Load all graphics 
		 */
		 
		public function loadGraphics(callBack:Function):void {
			
			this._callBack = callBack;
			
			// Load all graphic assets from CSS name
			//_gAssets = GlobalsVO.getAssets();
			
			/* Once all the assets have finished 
			 * loading then run the menubar */
			_assetsRemaining = _gAssets.length;
						
			// Get reference to the application layer
			var app:Object = GlobalsVO.getGlobal(GlobalsVO.APPLICATION);
			
			// Create a constainer to pre-load the graphics
			_graphicPreloadContainer = new Canvas();
			app.addChild(_graphicPreloadContainer);
			
			// Loop through all the assets to load
			for(var i:Object in _gAssets) {
				var img:Image = new Image();
				// Load all graphics with cachebuster or not
				Boolean(GlobalsVO.getGlobal(GlobalsVO.EXTERNALVARS).cachebuster) ?
				img.source = GlobalsVO.getCSSProperty(_gAssets[i])+DELIMITER+int(Math.random()*1000000000) :
				img.source = GlobalsVO.getCSSProperty(_gAssets[i]);
				
				// Create a new child for the preload container
				_graphicPreloadContainer.addChild(img);
				
				// Add a listener when the image has successfully loaded
				//img.addEventListener(FlexEvent.CREATION_COMPLETE,onLoad);	
				img.addEventListener(HTTPStatusEvent.HTTP_STATUS,onStatus);	
				img.addEventListener(IOErrorEvent.IO_ERROR,onError);		
			}
		}
		
		asdfas
		public function onStatus(e:HTTPStatusEvent):void {
			/* trace("\n----------------------------\nonStatus: "+e.status);	
			trace("onStatus: "+e.currentTarget);	
			trace("onStatus: "+e.target);	
			trace("onStatus: "+e.type);	
			trace("onStatus: "+e.eventPhase); */	
		}
		
		
		public function onError(e:IOErrorEvent):void {
			//trace("Graphic file not found: "+e.currentTarget);	
		}
		
		
		
		/**
		 * After each graphic has loaded
		 * Store all graphics into the
		 * static class GlobalsVO for future
		 * graphic reference 
		 * @param e:Event - Get reference of
		 * the filename to store the alias
		 * CSS graphic name in GlobalsVO
		 */
		public function onLoad(e:Event):void {
			// Remove listener for each graphic
			//e.currentTarget.removeEventListener(FlexEvent.CREATION_COMPLETE,onLoad);				
			
			// Clear the canvas
			GlobalsVO.getGlobal(GlobalsVO.APPLICATION).removeAllChildren();
			
			// Store the current loaded graphic
			var source:String = e.currentTarget.source;
			
			if(e.currentTarget.source == null) {
				GlobalsVO.setGlobal(_gAssets[i],e.currentTarget);
			}
			
			/* If the loaded graphic was loaded
			 * with a cache buster "?", then remove
			 * the "?" and the remaining random number */
			if(source.indexOf("?") > -1) {
				source = source.substring(0, source.indexOf("?"));
			}
			
			/* Compair the loaded graphic with
			 * the CSS alias name for the graphic path */
			
			var i:int = 0;
			while(i<_gAssets.length) {

				/* If cache buster has involved, remove
				 * the extra cache buster information from the
				 * image file name */
				
				if(GlobalsVO.getCSSProperty(_gAssets[i]) == source) {
					// Store the graphic name and asset in GlobalsVO
					GlobalsVO.setGlobal(_gAssets[i],e.currentTarget);
					// All graphics have loaded
					if(--_assetsRemaining <=0) {
						//start();
					}
				}
				++i;
			}
		}

	}
}