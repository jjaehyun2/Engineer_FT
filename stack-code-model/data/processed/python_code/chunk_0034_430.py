// CAMERA

package org.ffilmation.engine.core {
	
		// Imports
		import flash.display.BlendMode
		
		/**
		* <p>The fCamera defines which part of the scene is shown.
		* Use the scene's setCamera method to asign any camera to the scene, and then move the camera</p>
		*
		* <p>YOU CAN'T CREATE INSTANCES OF THIS ELEMENT DIRECTLY.<br>
		* Use scene.createCamera() to add new cameras to the scene</p>
		*
		* @see org.ffilmation.engine.core.fScene#createCamera()
		* @see org.ffilmation.engine.core.fScene#setCamera()
		*
		*/
		public class fCamera extends fElement {
		
			// Constants
			private static var count:Number = 0
			
			/**
			* Constructor for the fCamera class
			*
			* @param scene The scene associated to this camera
		  *
			* @private
			*/
			function fCamera(scene:fScene) {
			
				 var myId:String = "fCamera_"+(fCamera.count++)
				 
				 // Previous
				 super(<camera id={myId}/>,scene)			 
				 
			}
			
			
		}
}