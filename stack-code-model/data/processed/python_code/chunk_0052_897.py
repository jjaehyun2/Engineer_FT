package org.ffilmation.engine.core {

		// Imports
		import flash.display.*

		/**
		* <p>The fElementContainer is the root displayObject for a renderable Element while the scene is being rendered.</p>
		*/
		public class fElementContainer extends Sprite {
		
			/**
			* The ID for this element.
			* Using this, you will be able to access the element from an Event listener attached to the container.
			*/
			public var fElementId:String

			/**
			* A pointer to the fElement this container represents.
			* Using this, you will be able to access the element from an Event listener attached to the container.
			*/
			public var fElement:fRenderableElement
			
			
		}
		

}