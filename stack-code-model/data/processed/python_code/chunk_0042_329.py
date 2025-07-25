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
package org.libspark.flartoolkit.core.rasterfilter 
{
	import flash.geom.*;
	import flash.display.*;
	import org.libspark.flartoolkit.core.types.*;
	import org.libspark.flartoolkit.core.raster.*;
	import org.libspark.flartoolkit.core.raster.rgb.*;
	import org.libspark.flartoolkit.core.raster.*;
	import org.libspark.flartoolkit.core.raster.rgb.*;
	import jp.nyatla.as3utils.*;
	import flash.filters.*;	

	public class FLARRgb2GsFilter
	{
		private var _dest:Point = new Point(0,0);
		private var _src:Rectangle = new Rectangle();
        private var _ref_raster:FLARRgbRaster;
		private static const MONO_FILTER:ColorMatrixFilter = new ColorMatrixFilter([
			0,0,0, 0, 0,
			0,0,0, 0, 0,
			0.33,0.34,0.33, 0,
			0, 0, 0, 1, 0
		]);
        public function FLARRgb2GsFilter(i_ref_raster:FLARRgbRaster)
        {
            NyAS3Utils.assert(i_ref_raster.isEqualBufferType(FLARBufferType.OBJECT_AS3_BitmapData));
            this._ref_raster = i_ref_raster;
        }		
		/**
		 * RGB画像からGrayscale画像とBin画像を同時に生成します。
		 * @param	l
		 * @param	t
		 * @param	w
		 * @param	h
		 * @param	i_gs
		 * @param	i_bin
		 */
		public function convertRect(l:int, t:int, w:int, h:int, i_gs:FLARGrayscaleRaster):void
		{
			NyAS3Utils.assert (i_gs.isEqualBufferType(FLARBufferType.OBJECT_AS3_BitmapData));			
			var inbmp:BitmapData = this._ref_raster.getBitmapData();
			this._src.left  =l;
			this._src.top   =t;
			this._src.width =w;
			this._src.height = h;
			this._dest.x = l;
			this._dest.y = t;
			var gsbmp:BitmapData = i_gs.getBitmapData();
			gsbmp.applyFilter(inbmp,this._src,this._dest, MONO_FILTER);
		}
		/**
		 * 同一サイズの画像にグレースケール画像を生成します。
		 * @param i_raster
		 * @throws FLARException
		 */
		public function convert(i_gs:FLARGrayscaleRaster):void
		{
			var s:FLARIntSize = this._ref_raster.getSize();
			this.convertRect(0, 0, s.w, s.h, i_gs);			
		}
	}
}