package org.openPyro.aurora{
	import flash.display.DisplayObject;
	import flash.text.TextFormat;
	
	import org.openPyro.controls.Button;
	import org.openPyro.controls.Label;
	import org.openPyro.controls.events.ButtonEvent;
	import org.openPyro.core.IStateFulClient;
	import org.openPyro.core.Padding;
	import org.openPyro.core.UIControl;
	import org.openPyro.events.PyroEvent;
	import org.openPyro.painters.IPainter;
	
	/**
	 * Class used for creating Button skins specified by painters that define
	 * the different button states.
	 */ 
	public class AuroraPainterButtonSkin extends UIControl implements IStateFulClient
	{
		
		public var labelIconGap:Number = 5;
		/**
		 * A skin for buttons using different painters.
		 * Note: Only padding left and padding top are respected if align is set to
		 * left
		 */ 
		public function AuroraPainterButtonSkin()
		{
			this.mouseChildren=false;
			this._padding = new Padding(0,10, 0,0);
		}
		
		override public function set skinnedControl(uic:UIControl):void
		{
			if(skinnedControl)
			{
				skinnedControl.removeEventListener(PyroEvent.PROPERTY_CHANGE, onSkinnedControlPropertyChange)
			}
			super.skinnedControl = uic;
			skinnedControl.addEventListener(PyroEvent.PROPERTY_CHANGE, onSkinnedControlPropertyChange)
			if(uic is Button)
			{
				this.changeState(null, Button(uic).currentState);
				updateLabel();
			}
			this.buttonMode = true;
			this.useHandCursor = true;
			
		}
		
		protected function onSkinnedControlPropertyChange(event:PyroEvent):void
		{
			if(skinnedControl is Button)
			{
				updateLabel();
			}
		}
		
		/////////////////// ICON /////////////////
		
		protected var _icon:DisplayObject;
		public function set icon(icn:DisplayObject):void
		{
			_icon = icn;
			addChild(_icon);
			if(skinnedControl){
				invalidateDisplayList();
			}
		}
		
		////////////////// LABEL /////////////////
		
		protected var _labelFormat:TextFormat = new TextFormat("Arial",11, 0x111111,true);
		
		public function set labelFormat(fmt:TextFormat):void
		{
			_labelFormat = fmt;
			if(label)
			{
				label.textFormat = fmt;
			}
			if(skinnedControl)
			{
				invalidateDisplayList();
			}
		}
		
		public function get labelFormat():TextFormat
		{
			return _labelFormat;
		}
		
		protected var label:Label;
		
		public function updateLabel():void{
			if(this.skinnedControl is Button){
				var bttn:Button = Button(this.skinnedControl);
				if(!bttn.label) return;
				if(!label){
					label = new Label();
					label.embedFonts = _embedFonts;
					label.textFormat = _labelFormat;
					addChild(label);
					
				}
				
				if(bttn.label != label.text){
					label.text = bttn.label;
				}
			}
			//this.invalidateDisplayList();
		}
		
		private var _embedFonts:Boolean = false;
		public function set embedFonts(val:Boolean):void{
			_embedFonts = val;
			if(label){
				label.embedFonts = val;
			}
		}
		
		private var _labelAlign:String = "center";
		public function set labelAlign(direction:String):void
		{
			_labelAlign = direction;
			if(skinnedControl){
				invalidateDisplayList();
			}
		}
		
		//////////// Colors ///////////////
		
		
		public var upPainter:IPainter;
		public var overPainter:IPainter;
		public var downPainter:IPainter;
		
		public function set painters(painter:IPainter):void{
			upPainter = overPainter = downPainter = painter;
			this.invalidateDisplayList();
		}
		
		public function setPainters(upPainter:IPainter, overPainter:IPainter=null, downPainter:IPainter=null):AuroraPainterButtonSkin{
			painters = upPainter;
			if(overPainter){
				this.overPainter = overPainter
			}
			if(downPainter){
				this.downPainter = downPainter;
			}
			return this;
		}
		
/*		public function set stroke(str:Stroke):void
		{
			_stroke = str;
			this.invalidateDisplayList();	
		} */
		
			
		///////////////// Button Behavior ////////
		
		public function changeState(fromState:String, toState:String):void
		{
			
			switch(toState){
				case (ButtonEvent.UP):		backgroundPainter = upPainter;
									  		break;
				case (ButtonEvent.OVER):	backgroundPainter = overPainter;
									  		break;
				case (ButtonEvent.DOWN):	backgroundPainter = downPainter;
									  		break;
				case (ButtonEvent.TOGGLED_ON):backgroundPainter = downPainter;
									  		break;
				case (ButtonEvent.TOGGLED_OFF):backgroundPainter = upPainter;
									 		break;
				default 					:backgroundPainter = upPainter;
									 		break;
				
					
			}
		}
		
		override public function dispose():void
		{
			if(this.parent)
			{
				this.parent.removeChild(this);
			}
		}
		
		override public function updateDisplayList(unscaledWidth:Number, unscaledHeight:Number):void
		{
			super.updateDisplayList(unscaledWidth, unscaledHeight);
			
			if(label){
				
				label.textField.autoSize = "left";
				if(label.textField && label.textField.text){
					label.y = (unscaledHeight-label.textField.textHeight)/2+_padding.top;
				}
				else{
					label.y = (unscaledHeight-label.height)/2+_padding.top;
				}
				if(this._labelAlign == "center"){
					label.x = (unscaledWidth-label.width)/2;
				}
				else if(_labelAlign == "left"){
					label.x = _padding.left;
				}
			}
			
			if(_icon){
				if(!label){
					_icon.x = (unscaledWidth-_icon.width)/2;
				}
				else{
					if(_labelAlign == "left"){
						_icon.x = label.x;
						label.x += _icon.width+5;
					}
					else{
						label.x+=_icon.width/2+labelIconGap/2;
						_icon.x = label.x-_icon.width-labelIconGap;
					}
				}
				_icon.y = (unscaledHeight-_icon.height)/2;
			}
		}
		
	}
}