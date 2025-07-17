package com.vini123.component.text
{
	import com.vini123.implement.IDestroy;
	
	import flash.text.TextField;
	import flash.text.TextFieldAutoSize;
	import flash.text.TextFieldType;
	import flash.text.TextFormat;
	
	/**
	 * 
	 * @author vini123
	 *  
	 *   说明：
	 *   1, 仅仅增加了几个属性。maxWidth，maxHeight, maxLines,
	 *   2, textFormat的某些属性，在这里成为该类的set属性。
	 *   3, 非多行文本。如果有\n这些，也可以实现换行。
	 * 	 http://help.adobe.com/zh_CN/FlashPlatform/reference/actionscript/3/flash/text/TextField.html
	 *   http://help.adobe.com/zh_CN/FlashPlatform/reference/actionscript/3/flash/text/TextFormat.html
	 */	
	public class Text extends TextField implements IDestroy
	{
		protected var format:TextFormat
		
		/**
		 * 当设置最大显示宽度的时候，追尾形象表示的字符 
		 */		
		public var signs:String = "";
			
		private var _maxWidth:int;
		
		private var _maxHeight:int;
		
		private var _maxLines:int; 
		
		/**
		 * 原始本应该显示的字符 (当设置长度后，超过了的情况下。返回的是set过来的字符。如果是input，没set text该值为null)
		 */		
		private var _rawtext:String;
		
		public function Text(font:String = "微软雅黑" , size:int = 12 , color:uint = 0xffffff , bold:Boolean = false)
		{
			format = new TextFormat(font, size, color, bold);
			autoSize =  TextFieldAutoSize.LEFT;
			defaultTextFormat = format;
		}

		/**
		 * 
		 * @return 
		 *  返回真实的文本
		 */		
		public function get rawtext():String
		{
			return _rawtext;
		}
		
		/**
		 * 
		 * @param value
		 * 
		 */		
		override public function set text(value:String):void
		{
			if(!value)
				return;
			
			defaultTextFormat = format;
			_rawtext = value;
			
			if(_maxWidth && _maxWidth > 0)
			{
				resetText();
				return;
			}
			super.text = value;
		}
		
		/**
		 * @private
		 *   文字的最大显示宽度（该设置只支持单行文本。多行文本设置这个意义不大）
		 */
		public function set maxWidth(value:int):void
		{
			if(_maxWidth == value)
				return;
			
			defaultTextFormat = format;
			
			_maxWidth = value;
			resetText();
		}
		
		/**
		 * @private
		 * 文字的最大显示高度（该设置只支持多行文本。单行文本设置这个没啥意义）
		 */
		public function set maxHeight(value:int):void
		{
			if(_maxHeight == value)
				return;
			
			defaultTextFormat = format;
			
			_maxHeight = value;
			resetText();
		}
		
		/**
		 * 
		 * @param value
		 *  文字的最大行数（该设置只支持多行文本。单行文本没意义）
		 */		
		public function set maxLines(value:int):void
		{
			if(_maxLines == value)
				return;
			
			defaultTextFormat = format;
			
			_maxLines = value;
			resetText();
		}
		
		override public function set multiline(value:Boolean):void
		{
			if(super.multiline == value)
				return;
			
			super.multiline = value;
			resetText();
		}
		
		private function resetText():void
		{
			if(!_rawtext)
				return;
			
			super.text = "";
			
			var i:int = 0, len:int = _rawtext.length;
			if(!multiline && _maxWidth > 0)
			{
				for(i = 0; i< len; i++)
				{
					appendText(_rawtext.charAt(i));
					if(textWidth > _maxWidth)
					{
						i = (signs && signs.length > 0) ? (i - signs.length) :i;
						
						if(i < 0)
							i = 0;
						
						super.text = _rawtext.substring(0, i) + signs;
						break;
					}
				}
			}
			else if(multiline && _maxHeight> 0)
			{
				for(i = 0; i< len; i++)
				{
					appendText(_rawtext.charAt(i));
					if(textHeight >= _maxHeight)
					{
						i = (signs && signs.length > 0) ? (i - signs.length) :i;
						
						if(i < 0)
							i = 0;
						
						super.text = _rawtext.substring(0, i) + signs;
						break;
					}
				}
			}
			else if(multiline && _maxLines > 1)
			{
				for(i = 0; i< len; i++)
				{
					appendText(_rawtext.charAt(i));
					if(numLines >= _maxLines)
					{
						i = (signs && signs.length > 0) ? (i - signs.length) :i;
						
						if(i < 0)
							i = 0;
						
						super.text = _rawtext.substring(0, i) + signs;
						break;
					}
				}
			}
			else
			{
				super.text = _rawtext;
			}
			
			if(type == TextFieldType.INPUT)
			{
				setSelection(length, length);
			}
		}

		/**
		 * 重写TextFormat的一些方法 
		 * 
		 */	
		
		/**
		 * 
		 * @param 字体
		 * 
		 */		
		public function set font(value:String):void
		{
			format.font = value;
			setTextFormat(format);
		}
		
		/**
		 * 
		 * @param value
		 *  文字大小
		 */		
		public function set size(value:int):void
		{
			format.size = value;
			setTextFormat(format);
		}
		
		/**
		 * 
		 * @param value
		 *  文字颜色
		 */		
		public function set color(value:int):void
		{
			format.color = value;
			setTextFormat(format);
		}
		
		/**
		 * 
		 * @param value
		 *  文字是否粗体
		 */		
		public function set bold(value:Boolean):void
		{
			format.bold = value;
			setTextFormat(format);
		}
		
		public function set align(value:String):void
		{
			format.align = value;
			setTextFormat(format);
		}
		
		/**
		 * 
		 * @param value
		 *  文字是否使用斜体
		 */		
		public function set italic(value:Boolean):void
		{
			format.italic = value;
			setTextFormat(format);
		}
		
		/**
		 * 
		 * @param value
		 *  左边距（以像素为单位）
		 */		
		public function set leftMargin(value:Number):void
		{
			format.leftMargin = value;
			setTextFormat(format);
		}
		
		/**
		 * 
		 * @param value
		 *  右边距（以像素为单位）
		 */		
		public function set rightMargin(value:Number):void
		{
			format.rightMargin = value;
			setTextFormat(format);
		}
		
		/**
		 * 
		 * @param value
		 *  水平方向文字之间的间距
		 */		
		public function set letterSpacing(value:Number):void
		{
			format.letterSpacing = value;
			setTextFormat(format);
		}
		
		/**
		 * 
		 * @param value
		 *  垂直方向文字之间的间距
		 */		
		public function set leading(value:Number):void
		{
			format.leading = value;
			setTextFormat(format);
		}

		/**
		 * 
		 * @param value
		 *  文字是否带下划线
		 */		
		public function set underline(value:Boolean):void
		{
			format.underline = value;
			setTextFormat(format);
		}
		
		public function destroy():void
		{
			format = null;
			this.text = "";
		}
	}
}