/***********************************************************************************************************************
 * Copyright (c) 2010. Vaclav Vancura.
 * Contact me at vaclav@vancura.org or see my homepage at vaclav.vancura.org
 * Project's GIT repo: http://github.com/vancura/vancura-as3-libs
 * Documentation: http://doc.vaclav.vancura.org/vancura-as3-libs
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
 * documentation files (the "Software"), to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
 * and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all copies or substantial portions
 * of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
 * TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
 * THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 * DEALINGS IN THE SOFTWARE.
 **********************************************************************************************************************/

package org.vancura.vaclav.core.utils {
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.BlendMode;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.geom.Rectangle;
	import flash.system.System;
	import flash.text.AntiAliasType;
	import flash.text.TextFormat;
	import flash.utils.getTimer;

	import org.vancura.vaclav.core.display.GraphicsUtil;
	import org.vancura.vaclav.core.display.QBitmap;
	import org.vancura.vaclav.core.display.QTextField;
	import org.vancura.vaclav.core.global.addChildren;

	/*
	 * Class: Stats
	 *
	 * Hi-ReS! Stats
	 * Original code by Mr.doob (<http://www.mrdoob.com>)
	 * Eyecandified by Vaclav Vancura (<http://vaclav.vancura.org>)
	 *
	 * Released under MIT license:
	 * http://www.opensource.org/licenses/mit-license.php
	 *
	 * How to use:
	 *
	 * (start code)
	 * 		addChild( new Stats() );
	 * (end)
	 *
	 * Version log:
	 *
	 * 2009-11-04	- Whole package moved to vancura-core (v.vancura)
	 * 2009-11-04	- Changed font to UNI0553 by miniml.com (v.vancura)
	 * 2008-10-20	- Added to as3-org-vancura (v.vancura)
	 * 2008-10-19	- Added NaturalDocs comments (v.vancura)
	 * 2008-10-16	- Eye candy (v.vancura)
	 * 2008-07-12	- Some speed and code optimisations (Mr.doob)
	 * 2008-02-15	- Class renamed to Stats (previously FPS) (Mr.doob)
	 * 2008-01-05	- Click changes the fps of flash (half up increases, half down decreases) (Mr.doob)
	 * 2008-01-04	- Log shape for MEM (Mr.doob & Theo)
	 * 2008-01-04	- More room for MS (Mr.doob)
	 * 2008-01-04	- Shameless ripoff of Alternativa's FPS look ;) (Mr.doob)
	 * 2008-12-13	- First version (Mr.doob)
	 *
	 * Author: Mr.doob <http://www.mrdoob.com>
	 * Author: Vaclav Vancura <http://vaclav.vancura.org>
	 */
	public class Stats extends Sprite {


		[Embed(source='../../../../../../lib/fonts/uni05_53.ttf', fontName='uni0553', mimeType='application/x-font', unicodeRange='U+0030-U+0039,U+002E,U+0046,U+0050,U+0053,U+004D,U+004D,U+0045,U+0020,U+003A,U+002F')]
		private static var _fontUni0553:Class;

		private static const _WIDTH:Number = 80;

		private var _fpsGraphBD:BitmapData;
		private var _memGraphBD:BitmapData;
		private var _msGraphBD:BitmapData;

		private var _fpsGraphBM:Bitmap;
		private var _memGraphBM:Bitmap;
		private var _msGraphBM:Bitmap;

		private var _textFormat:TextFormat = new TextFormat('uni0553', 8);
		private var _fpsText:QTextField;
		private var _msText:QTextField;
		private var _memText:QTextField;
		private var _fps:int;
		private var _timer:int;
		private var _ms:int;
		private var _msPrev:int = 0;
		private var _mem:Number = 0;



		/**
		 * Constructor.
		 */
		public function Stats():void {
			_fpsGraphBD = new BitmapData(_WIDTH, 50, false, 0x000000);
			_msGraphBD = new BitmapData(_WIDTH, 50, false, 0x000000);
			_memGraphBD = new BitmapData(_WIDTH, 50, false, 0x000000);
			_fpsGraphBM = new QBitmap({bitmapData: _fpsGraphBD, y:27, alpha:0.33, blendMode:BlendMode.SCREEN});
			_msGraphBM = new QBitmap({bitmapData: _msGraphBD, y:27, alpha:0.33, blendMode:BlendMode.SCREEN});
			_memGraphBM = new QBitmap({bitmapData: _memGraphBD, y:27, alpha:0.33, blendMode:BlendMode.SCREEN});
			_fpsText = new QTextField({defaultTextFormat: _textFormat, antiAliasType:AntiAliasType.NORMAL, y:-3, width:_WIDTH, height:10, textColor:0xFFFF00});
			_msText = new QTextField({defaultTextFormat: _textFormat, antiAliasType:AntiAliasType.NORMAL, y:5, width:_WIDTH, height:10, textColor:0x00FF00});
			_memText = new QTextField({defaultTextFormat: _textFormat, antiAliasType:AntiAliasType.NORMAL, y:13, width:_WIDTH, height:10, textColor:0x00FFFF});

			GraphicsUtil.drawRect(this, 0, 0, _WIDTH, 27 + 50, 0x000000, 0.75);

			addChildren(this, _fpsGraphBM, _msGraphBM, _memGraphBM, _fpsText, _msText, _memText);

			addEventListener(MouseEvent.CLICK, _onMouseClick);
			addEventListener(Event.ENTER_FRAME, _onEnterFrame);
		}



		// Event listeners
		// ---------------


		private function _onMouseClick(e:MouseEvent):void {
			if(this.mouseY > this.height * 0.35) {
				stage.frameRate--;
			}
			else {
				stage.frameRate++;
			}

			_fpsText.text = 'FPS: ' + _fps + '/' + stage.frameRate;
		}



		private function _onEnterFrame(e:Event):void {
			_timer = getTimer();
			_fps++;

			if(_timer - 1000 > _msPrev) {
				_msPrev = _timer;
				//noinspection NestedFunctionCallJS
				_mem = Number((System.totalMemory / 1048576).toFixed(3));

				var f:uint = Math.min(50, 50 / stage.frameRate * _fps);
				var t:uint = ((_timer - _ms ) >> 1);

				//noinspection NestedFunctionCallJS
				var m:uint = Math.min(50, Math.sqrt(Math.sqrt(_mem * 5000))) - 2;

				_fpsGraphBD.scroll(1, 0);
				_msGraphBD.scroll(1, 0);
				_memGraphBD.scroll(1, 0);

				var r1:Rectangle = new Rectangle(0, 50 - f, 1, f);
				var r2:Rectangle = new Rectangle(0, 50 - t, 1, t);
				var r3:Rectangle = new Rectangle(0, 50 - m, 1, m);

				_fpsGraphBD.fillRect(r1, 0xFFFF00);
				_msGraphBD.fillRect(r2, 0x00FF00);
				_memGraphBD.fillRect(r3, 0x00FFFF);

				_fpsText.text = 'FPS: ' + _fps + '/' + stage.frameRate;
				_memText.text = 'MEM: ' + _mem;

				_fps = 0;
			}

			_msText.text = 'MS: ' + (_timer - _ms);
			_ms = _timer;
		}
	}
}