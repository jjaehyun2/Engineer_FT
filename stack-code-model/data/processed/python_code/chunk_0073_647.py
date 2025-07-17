package com.lowoui_as.component 
{
	import com.lowoui_as.core.UIComponent;
	import com.lowoui_as.events.DragBarEvent;
	import flash.events.Event;
	import flash.events.FocusEvent;
	import flash.events.MouseEvent;
	import flash.text.TextField;

	public class TextArea extends UIComponent
	{
		private var textObj      :TextField;
		private var focusObj     :Object;
		private var bgObj        :Object;
		private var indicator    :Object;
		private var textFocus    :Boolean;
		private var w            :uint;
		private var h            :uint;
		
        protected var _scrollPolicy:String = "auto";
        // The current scroll position of the TextArea.
        protected var _position:int = 1;
		protected var _isHtml:Boolean;
		protected var _beSelect:Boolean;
		protected var _displayAsPassword:Boolean;
		
		public function TextArea() 
		{
			textObj   = this["tt"];
			focusObj  = this["focusCon"];
			bgObj     = this["bg"];
			indicator = this["scrollIndicator"];
			textFocus = false;
			w         = bgObj.width;
			h         = bgObj.height;
			
			_isHtml   = false;
			_beSelect = true;
			_displayAsPassword = false;
			
			indicator.visible = false;
			//addEventListener(InputEvent.INPUT, handleInput, false, 0, true);
			textObj.addEventListener(FocusEvent.FOCUS_IN, handleTextFieldFocusIn, false, 0, true);
		}
		
		private function onScroller(e:Event):void 
		{
			indicator.position = (textObj.scrollV-1) / (textObj.maxScrollV-1);
		}
		
		private function handleTextFieldFocusIn(e:FocusEvent):void 
		{
			trace("handleTextFieldFocusIn:");
			focusObj.gotoAndStop(2);
			stage.removeEventListener(MouseEvent.MOUSE_DOWN,fMouseDown);
			stage.addEventListener(MouseEvent.MOUSE_UP,fMouseUp);
		}
		private function fMouseUp(e:MouseEvent):void 
		{
			if(e.target.name!="tt"){focusObj.gotoAndStop(1);}
			stage.removeEventListener(MouseEvent.MOUSE_UP, fMouseUp);
			stage.addEventListener(MouseEvent.MOUSE_DOWN,fMouseDown);
		}
		private function fMouseDown(e:MouseEvent):void 
		{
			if (e.target.name != "tt") { focusObj.gotoAndStop(1); }
			else{focusObj.gotoAndStop(2);}
			stage.removeEventListener(MouseEvent.MOUSE_DOWN,fMouseDown);
		}
		private function checkTextHeight(_h:Number,_textHeight:Number):void
		{
			if (_textHeight > _h) 
			{
				indicator.visible = true;
				indicator.sHeight = h;
				indicator.addEventListener(DragBarEvent.DRAG, fOnDragIndicator);
				if (textObj != null) 
				{ textObj.addEventListener(Event.SCROLL, onScroller, false, 0, true); }
			}
			else
			{
				indicator.visible = false;
				if (textObj != null) 
				{ textObj.removeEventListener(Event.SCROLL, onScroller); }
			}
		}
		private function fOnDragIndicator(e:DragBarEvent):void 
		{
            textObj.scrollV = Math.round(indicator.position * (textObj.maxScrollV-1))+1;
		}
		
		public function set tWidth(value:uint) : void
		{
			w = value;
			
			textObj.width  = w - 10;
			focusObj.width = w;
			bgObj.width    = w;
			indicator.x    = w + 2;
		}

		public function get tWidth() : uint
		{
			return w;
		}
		public function set tHeight(value:uint) : void
		{
			h = value;
			
			textObj.height    = h;
			focusObj.height   = h;
			bgObj.height      = h;
			indicator.sHeight = h;
			checkTextHeight(h,textObj.textHeight);
		}		
		public function get tHeight() : uint
		{
			return h;
		}
		public function set text(str:String) : void
		{
			textObj.htmlText   = str;			
			textObj.scrollV = 1;
			checkTextHeight(h,textObj.textHeight);
		}
		
		public function get text() : String
		{
			return textObj.text;
		}
		public function get focus():Boolean
		{
			return textFocus;
		}
		public function set focus(bool:Boolean) : void
		{
			textFocus = bool;
			if (bool) {	focusObj.gotoAndStop(2); }
			else      { focusObj.gotoAndStop(1); }
		}
		
		public function get beSelect():Boolean
		{
			return _beSelect;
		}
		public function set beSelect(bool:Boolean) : void
		{
			_beSelect = bool;
			if (_beSelect) {textObj.addEventListener(FocusEvent.FOCUS_IN, handleTextFieldFocusIn, false, 0, true);}
			else           {textObj.removeEventListener(FocusEvent.FOCUS_IN, handleTextFieldFocusIn, false);}
		}
		/** The current scroll position of the TextArea. */
        /*public function get position():int { return _position; }
        public function set position(value:int):void 
		{
            _position = value;
            textObj.scrollV = _position;
        }*/
		
		[Inspectable(defaultValue="false")]
        public function get displayAsPassword():Boolean { return _displayAsPassword; }
        public function set displayAsPassword(value:Boolean):void {
            _displayAsPassword = value;
            if (textObj != null) { textObj.displayAsPassword = value; }
        }
	}
}