/* 
 * PROJECT: FLARToolKit
 * --------------------------------------------------------------------------------
 * This work is based on the FLARToolKit developed by
 *   R.Iizuka (nyatla)
 * http://nyatla.jp/nyatoolkit/
 *
 * The FLARToolKit is ActionScript 3.0 version ARToolkit class library.
 * Copyright (C)2008 Saqoosha
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * 
 * For further information please contact.
 *	http://www.libspark.org/wiki/saqoosha/FLARToolKit
 *	<saq(at)saqoosha.net>
 * 
 */
package org.libspark.flartoolkit.core.raster 
{
	import flash.display.BitmapData;
	
	import org.libspark.flartoolkit.core.FLARException;
	import org.libspark.flartoolkit.core.labeling.rlelabeling.FLARLabeling_Rle_IRasterDriver;
	import org.libspark.flartoolkit.core.rasterdriver.IFLARHistogramFromRaster;
	import org.libspark.flartoolkit.core.rasterfilter.FLARGs2BinFilter;
	import org.libspark.flartoolkit.core.squaredetect.FLARContourPickup_IRasterDriver;
	import org.libspark.flartoolkit.core.types.FLARBufferType;
	import org.libspark.flartoolkit.core.types.FLARIntSize;
	/**
	 * このクラスは、BitmapDataをバッファ荷物グレースケールラスタです。
	 */
	public class FLARGrayscaleRaster extends FLARGrayscaleRaster_BaseClass_
	{
		public function FLARGrayscaleRaster(i_width:int,i_height:int,i_raster_type:int,i_is_alloc:Boolean=true)
		{
			super(i_width,i_height,i_raster_type,i_is_alloc);
		}
		protected override function initInstance(i_size:FLARIntSize, i_raster_type:int, i_is_alloc:Boolean):void
		{
			if (i_raster_type != FLARBufferType.OBJECT_AS3_BitmapData){
				throw new FLARException();
			}
			this._buf = i_is_alloc?new BitmapData(i_size.w, i_size.h, false):null;
			this._pixdrv = new FLARGsPixelDriver_AsBitmap();
			this._pixdrv.switchRaster(this);
			this._is_attached_buffer = i_is_alloc;
			return;
		}
		public override function createInterface(i_iid:Class):Object
		{
			if (this.isEqualBufferType(FLARBufferType.OBJECT_AS3_BitmapData))
			{
				if(i_iid==FLARLabeling_Rle_IRasterDriver){
					return new FLARRlePixelDriver_ASBmp(this);
				}
				if(i_iid==IFLARHistogramFromRaster){
					return new FLARHistogramFromRaster_AnyGs(this);
				}
				if(i_iid==FLARContourPickup_IRasterDriver){
					return FLARContourPickupFactory.createDriver(this);
				}
				if (i_iid == FLARGs2BinFilter) {
					return new FLARGs2BinFilter(this);
				}
			}
			return this.createInterface(i_iid);
		}
		public function getBitmapData():BitmapData
		{
			return BitmapData(this._buf);
		}
	}
}