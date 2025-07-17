/*
   Copyright aswing.org, see the LICENCE.txt.
 */

package org.aswing.skinbuilder
{
	import starling.display.DisplayObject;
	
	import org.aswing.AssetBackground;
	import org.aswing.lookandfeel.plaf.UIResource;
	
	public class SkinAssetBackground extends AssetBackground implements UIResource
	{
		
		public function SkinAssetBackground(asset:DisplayObject)
		{
			super(asset);
		}
	
	}
}