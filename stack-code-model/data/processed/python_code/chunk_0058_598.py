package gui
{
	import flash.display.DisplayObject;
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.display.Stage;
	import flash.events.MouseEvent;
	import flash.geom.Rectangle;
	import flash.text.TextField;
	import flash.text.TextFieldAutoSize;
	import flash.text.TextFormat;
	
	public class TextBox extends Sprite
	{
		protected var m_text:TextField;
		private var m_htmltext:String;

		public static const TYPE_BUTTON:int = 2;
		public static const TYPE_TEXTFIELD:int = 1;
		
		private var m_type:int = TYPE_TEXTFIELD;
		private var m_callback:Function;
		
		public function TextBox() 
		{
			clear();
		}
		
		public function writeLn(_msg:String, _color:String = "#F28101") : void
		{
			var msg:String = _msg.replace("\n", "<br>");
			m_htmltext += "<font color=\"" + _color + "\">" + msg + "</font><br>";
			m_text.htmlText = m_htmltext;
		}
		
		public function write(_msg:String, _color:String = "#F28101") : void
		{
			m_htmltext +=  "<font color=\"" + _color + "\">" + _msg + "</font>";
			m_text.htmlText = m_htmltext;
		}		

		public function getTextMetrics():Rectangle 
		{
			var rec:Rectangle = new Rectangle();
			rec.x = m_text.x;
			rec.y = m_text.y;
			rec.width = m_text.textWidth;
			rec.height = m_text.textHeight;
			return rec;
		}
		
		public function clear() : void
		{
			if (m_text != null)
				removeChild(m_text);
			var text:TextField;
			text = new TextField();
			text.textColor = 0xF28101;
			text.backgroundColor = 0x01294F;
			text.background = true;
			text.wordWrap = true;
			text.name = "myWindow";
			text.multiline = true;
			text.htmlText = "";
			
			var textformat:TextFormat = new TextFormat("Verdana", 12);
			text.setTextFormat(textformat);
			text.defaultTextFormat = textformat;
			
			if (m_text != null)
			{
				text.x = m_text.x;
				text.y = m_text.y;
				text.width = m_text.width;
				text.height = m_text.height;
			}
			m_text = text;
			this.addChild(m_text);
			m_htmltext = "";
		}
		
		override public function get width():Number { return m_text.width; }
		override public function set width(value:Number):void 
		{
			m_text.width = value;
		}

		override public function get height():Number { return m_text.height; }
		override public function set height(value:Number):void 
		{
			m_text.height = value;
		}
		
		override public function get x():Number { return m_text.x; }
		override public function set x(value:Number):void 
		{
			m_text.x = value;
		}
		
		override public function get y():Number { return m_text.y; }
		override public function set y(value:Number):void 
		{
			m_text.y = value;
			var border:DisplayObject = getChildByName("border");
			if (border != null)
				border.y = value;
		}

		public function setType(_t:int):void 
		{
			m_type = _t;
			
			if (m_type == TYPE_BUTTON)
			{
				m_text.textColor = 0xF28101;
				m_text.backgroundColor = 0x011325;	
				m_text.selectable = false;
				var textformat:TextFormat = m_text.defaultTextFormat;
				textformat.align = "center";
				m_text.setTextFormat(textformat);
				m_text.defaultTextFormat = textformat;
				var shape:Shape = new Shape();
				shape.name = "border";
				shape.graphics.beginFill(0xffffff, 0);
				shape.graphics.lineStyle(3, 0xffffff);
				shape.graphics.drawRect(m_text.x - 1, m_text.y - 1, m_text.width + 2, m_text.height +2);
				shape.graphics.endFill();
				addChild(shape);
			}
		}

		public function getText():String
		{
			return m_text.text;
		}
		
		public function setClickCallback(_callback:Function):void 
		{
			m_callback = _callback;
			addEventListener(MouseEvent.CLICK, onClick);
		}
		
		public function onClick(_e:MouseEvent):void 
		{
			m_callback();
		}
	}
}