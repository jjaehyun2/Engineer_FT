﻿/**
 * This code is part of the Bumpslide Library maintained by David Knape
 * Fork me at http://github.com/tkdave/bumpslide_as3
 * 
 * Copyright (c) 2010 by Bumpslide, Inc. 
 * http://www.bumpslide.com/
 *
 * This code is released under the open-source MIT license.
 * See LICENSE.txt for full license terms.
 * More info at http://www.opensource.org/licenses/mit-license.php
 */

package com.bumpslide.preloader {	import flash.display.*;	import flash.text.*;	import flash.utils.getTimer;	/**	 * ProgressBar for Preloader	 * 	 * @author David Knape	 */	public class ProgressBar extends MovieClip {
		// timeline movieclips		public var display_txt:TextField;		public var bar_mc:MovieClip;		public var border:MovieClip;		public var background:MovieClip;
		// properties		protected var _start:int;		protected var _delay:int = 750;		protected var _offset:Number = 0;		protected var _fullwidth:Number = 176;
		public function ProgressBar() {			stop();			init();				reset();		}				protected function init():void {			display_txt.autoSize = TextFieldAutoSize.LEFT;			}				public function reset():void {			visible = false;			_start = getTimer();			_offset = 0;			if(background) {				_fullwidth = background.width - ( bar_mc.x - background.x ) * 2;			}			if(bar_mc) bar_mc.width = 0;			setText('');		}
		public function setDelay(d:Number):void {			_delay = d;				}
		public function setPercent( pct:Number ):void {						// make sure percent is a float			if(pct > 1) pct /= 100;										// validate			if(pct < 0) return;						// wait for delay before displaying			if((getTimer() - _start) < _delay) {				return;			}					if(!visible) {				_offset = pct;				visible = true;			}			pct = (pct - _offset) / (1 - _offset);						updateDisplay(pct);		}	
		protected function updateDisplay(pct:Number):void {			//setText('Loading...  ' + Math.round( pct * 100 ) + '%' );			if(bar_mc) bar_mc.width = Math.round(_fullwidth * pct);		}
		public function setText(s:String):void {			if((getTimer() - _start) > _delay && !visible) {				visible = true;			}			if(display_txt) display_txt.text = s;		}
		public function hide():void {			visible = false;		}		}}