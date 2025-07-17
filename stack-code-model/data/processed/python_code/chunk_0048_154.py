﻿/**
 * Created by newkrok on 14/06/16.
 */
package net.fpp.pandastory.vo
{
	import net.fpp.common.geom.SimplePoint;

	public class LibraryElementDataVO
	{
		public var elementId:String;
		public var position:SimplePoint;
		public var rotation:Number;
		public var scaleX:Number;
		public var scaleY:Number;

		public function LibraryElementDataVO( elementId:String = '', position:SimplePoint = null, rotation:Number = 0, scaleX:Number = 0, scaleY:Number = 0 )
		{
			this.elementId = elementId;
			this.position = position;
			this.rotation = rotation;
			this.scaleX = scaleX;
			this.scaleY = scaleY;
		}
	}
}