package com.lowoui_as.component 
{
	import com.lowoui_as.Extension;
	import com.lowoui_as.core.UIComponent;
	import com.lowoui_as.events.ButtonEvent;
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.text.TextField;
	
	//[Event(name = "buttonOver", type = "com.lowoui_as.events.ButtonEvent")]
	//[Event(name = "buttonOut", type = "com.lowoui_as.events.ButtonEvent")]
	//[Event(name = "releaseOutside", type = "com.lowoui_as.events.ButtonEvent")]
	[Event(name = "select", type = "com.lowoui_as.events.ButtonEvent")]
	
	public class CheckBox extends UIComponent
	{		
		private var cName:TextField;
		private var cBg:MovieClip;
		
		public function CheckBox() 
		{
			selectedState = false;
			enabledState  = false;
			
			cName = this["name_"];
			cBg   = this["bg"];
			Extension.setTextDisabled(cName);
			
			cBg.addEventListener(MouseEvent.MOUSE_OVER, onBtn);
			cBg.addEventListener(MouseEvent.MOUSE_DOWN, onBtn);
		}

		private function onBtn(e:MouseEvent):void 
		{
			switch (e.type) 
			{
				case "mouseOver":
					//dispatchEvent(new ButtonEvent(ButtonEvent.OVER));
					if (selectedState) { cBg.gotoAndStop("selected_over"); }
					else                { cBg.gotoAndStop("over"); }
					
					cBg.addEventListener(MouseEvent.MOUSE_OUT,onBtn);
					break;
				case "mouseOut":
					//dispatchEvent(new ButtonEvent(ButtonEvent.OUT));
					if (selectedState) { cBg.gotoAndStop("selected_up"); }
					else                { cBg.gotoAndStop("up"); }
					
					cBg.removeEventListener(MouseEvent.MOUSE_OUT,onBtn);
					break;
				case "mouseDown":
					//dispatchEvent(new ButtonEvent(ButtonEvent.PRESS));
					if (selectedState)
					{
						selectedState = false;
						cBg.gotoAndStop("down");
					}
					else
					{
						selectedState = true;
						cBg.gotoAndStop("selected_down");
					}
					
					dispatchEvent(new ButtonEvent(ButtonEvent.SELECT));
					
					stage.addEventListener(MouseEvent.MOUSE_UP, onBtn);
					cBg.removeEventListener(MouseEvent.MOUSE_OUT,onBtn);
					break;
				case "mouseUp":
					stage.removeEventListener(MouseEvent.MOUSE_UP, onBtn);
					if (e.target == cBg) 
					{
						//dispatchEvent(new ButtonEvent(ButtonEvent.CLICK));
						if (selectedState) { cBg.gotoAndStop("selected_over");	}
						else               { cBg.gotoAndStop("over"); }
						
						cBg.addEventListener(MouseEvent.MOUSE_OUT,onBtn);
					}
					else 
					{
						//dispatchEvent(new ButtonEvent(ButtonEvent.RELEASE_OUTSIDE));
						if (selectedState) { cBg.gotoAndStop("selected_up"); }
						else               { cBg.gotoAndStop("up"); }
					}
					
					stage.removeEventListener(MouseEvent.MOUSE_UP,onBtn);
					break;
				default:
			}
		}
		
		public function get selected():Boolean
		{
			return selectedState;
		}
		public function setSelectedState(bool:Boolean):void
		{
			selectedState = bool;
			//dispatchEvent(new ButtonEvent(ButtonEvent.SELECT));
			
			if (selectedState) { cBg.gotoAndStop("selected_up"); }
			else               { cBg.gotoAndStop("up"); }
		}
		public function setEnabled(obj:Object,bool:Boolean):void
		{
			//override
			//super.setEnabled(obj, bool);
			obj.mouseChildren = bool;
			obj.mouseEnabled  = bool;
			
			enabledState = bool;
			if (enabledState) 
			{
				cName.alpha = 1;
				if (selectedState) { cBg.gotoAndStop("selected_disabled"); }
				else               { cBg.gotoAndStop("disabled"); }
			}
			else
			{
				cName.alpha = 0.3;
				if (selectedState) { cBg.gotoAndStop("selected_disabled"); }
				else               { cBg.gotoAndStop("disabled"); }
			}
		}
		
		override public function setName(str:String) : void
		{
			cName.text  = str;
			cName.width = cName.textWidth+20;
		}
		override public function setFocus(bool:Boolean) : void
		{
			if (bool)
			{
				if (selectedState) { cBg.gotoAndStop("selected_over"); }
				else               { cBg.gotoAndStop("over"); }
			}
			else
			{
				if (selectedState) { cBg.gotoAndStop("selected"); }
				else               { cBg.gotoAndStop("up"); }
			}
		}
	}
}