/**
 * Copyright (c) 2012 - 2100 Sindney
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
package bloom.core 
{
	import flash.display.DisplayObjectContainer;
	import flash.text.TextField;
	import flash.text.TextFormat;
	
	import bloom.brushes.TextBrush;
	import bloom.events.BrushEvent;
	import bloom.themes.ThemeBase;
	
	/** 
	 * Dispatched when the format of textField has changed.
	 * @eventType bloom.events.BrushEvent
	 */
	[BrushEvent(name = "redraw", type = "bloom.events.BrushEvent")]
	
	/**
	 * TextBase
	 * 
	 * @author sindney
	 */
	public class TextBase extends TextField implements IComponent {
		
		protected var _brush:TextBrush;
		
		protected var _margin:Margin;
		
		protected var _enabled:Boolean = true;
		
		public function TextBase(p:DisplayObjectContainer = null) {
			super();
			_margin = new Margin();
			if (p != null) p.addChild(this);
		}
		
		public function move(x:Number, y:Number):void {
			this.x = x;
			this.y = y;
		}
		
		public function size(w:Number, h:Number):void {
			width = w;
			height = h;
		}
		
		protected function onBrushChanged(e:BrushEvent):void {
			if (defaultTextFormat != _brush.textFormat) {
				defaultTextFormat = _brush.textFormat;
				setTextFormat(defaultTextFormat);
				dispatchEvent(new BrushEvent("redraw"));
			}
		}
		
		///////////////////////////////////
		// getter/setters
		///////////////////////////////////
		
		public function set brush(b:TextBrush):void {
			if (_brush != b) {
				if (_brush) _brush.removeEventListener(BrushEvent.REDRAW, onBrushChanged);
				_brush = b;
				if (_brush) {
					onBrushChanged(null);
					_brush.addEventListener(BrushEvent.REDRAW, onBrushChanged);
				}
			}
		}
		
		public function get brush():TextBrush {
			return _brush;
		}
		
		public function set enabled(value:Boolean):void {
			if (_enabled != value) {
				_enabled = tabEnabled = mouseEnabled = value;
				alpha = _enabled ? 1 : ThemeBase.ALPHA;
			}
		}
		
		public function get enabled():Boolean {
			return _enabled;
		}
		
		public function get margin():Margin {
			return _margin;
		}
		
		///////////////////////////////////
		// toString
		///////////////////////////////////
		
		override public function toString():String {
			return "[bloom.core.TextBase]";
		}
		
	}

}