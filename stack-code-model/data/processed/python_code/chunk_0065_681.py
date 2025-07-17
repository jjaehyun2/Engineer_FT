package com.catalystapps.gaf.display
{
	import starling.textures.TextureSmoothing;
	import starling.display.Image;

	/**
	 * @private
	 */
	public class GAFImage extends Image
	{
		//--------------------------------------------------------------------------
		//
		//  PUBLIC VARIABLES
		//
		//--------------------------------------------------------------------------
		
		//--------------------------------------------------------------------------
		//
		//  PRIVATE VARIABLES
		//
		//--------------------------------------------------------------------------
		
		private var _assetTexture: GAFTexture;
		
		//--------------------------------------------------------------------------
		//
		//  CONSTRUCTOR
		//
		//--------------------------------------------------------------------------
		
		/**
		 * GAFImage represents display object that is part of the <code>GAFMovieClip</code> 
		 */
		public function GAFImage(assetTexture: GAFTexture)
		{
			this._assetTexture = assetTexture;			
			
			super(this._assetTexture.texture);
		}

		//--------------------------------------------------------------------------
		//
		//  PUBLIC METHODS
		//
		//--------------------------------------------------------------------------
		
		//--------------------------------------------------------------------------
		//
		//  PRIVATE METHODS
		//
		//--------------------------------------------------------------------------
		
		//--------------------------------------------------------------------------
		//
		// OVERRIDDEN METHODS
		//
		//--------------------------------------------------------------------------
		
		/**
		 * Disposes all resources of the display object
		 */
		override public function dispose(): void
		{
			(this.filter) ? this.filter.dispose() : null;
			this.filter = null;
			
			super.dispose();
		}
		
		//--------------------------------------------------------------------------
		//
		//  EVENT HANDLERS
		//
		//--------------------------------------------------------------------------
		
		//--------------------------------------------------------------------------
		//
		//  GETTERS AND SETTERS
		//
		//--------------------------------------------------------------------------
		
		public function get assetTexture(): GAFTexture
		{
			return _assetTexture;
		}
		
	}
}