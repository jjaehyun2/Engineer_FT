/*
 *      _________  __      __
 *    _/        / / /____ / /________ ____ ____  ___
 *   _/        / / __/ -_) __/ __/ _ `/ _ `/ _ \/ _ \
 *  _/________/  \__/\__/\__/_/  \_,_/\_, /\___/_//_/
 *                                   /___/
 * 
 * Tetragon : Game Engine for multi-platform ActionScript projects.
 * http://www.tetragonengine.com/ - Copyright (C) 2012 Sascha Balkau
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
package view.splash
{
	import lib.display.TetragonLogo;

	import tetragon.data.Settings;
	import tetragon.util.color.colorHexToColorTransform;
	import tetragon.view.native.View;

	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.filters.DropShadowFilter;
	import flash.geom.Matrix;
	
	
	/**
	 * A view that shows the engine's logo.
	 */
	public class SplashView extends View
	{
		//-----------------------------------------------------------------------------------------
		// Properties
		//-----------------------------------------------------------------------------------------
		
		private var _bitmapLogo:Bitmap;
		
		
		//-----------------------------------------------------------------------------------------
		// Private Methods
		//-----------------------------------------------------------------------------------------
		
		override protected function createChildren():void
		{
			var logoColor:uint = registry.settings.getNumber(Settings.SPLASH_LOGO_COLOR);
			if (isNaN(logoColor)) logoColor = 0xFFBF00;
			var ds:DropShadowFilter = new DropShadowFilter(1.0, 45, 0x000000, 0.4, 8.0, 8.0, 2);
			var logo:TetragonLogo = new TetragonLogo();
			logo.filters = [ds];
			var b:BitmapData = new BitmapData(logo.width + 40, logo.height + 40, true, 0x00000000);
			var m:Matrix = new Matrix();
			m.translate(20, 20);
			b.draw(logo, m, colorHexToColorTransform(logoColor));
			_bitmapLogo = new Bitmap(b);
		}
		
		
		override protected function addChildren():void
		{
			addChild(_bitmapLogo);
		}
	}
}