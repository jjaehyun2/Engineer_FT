package
{
	import LS_Classes.tooltipHelper;
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.external.ExternalInterface;
	import flash.text.TextField;
	
	public dynamic class DropDown extends MovieClip
	{
		 
		
		public var combo_mc:comboBox;
		
		public var formHL_mc:MovieClip;
		
		public var label_txt:TextField;
		
		public var base:MovieClip;
		
		public var div:MovieClip;
		
		public var mHeight:Number;
		
		public function DropDown()
		{
			super();
			addFrameScript(0,this.frame1);
		}
		
		public function onOpen(param1:Event) : *
		{
			ExternalInterface.call("hideTooltip");
		}
		
		public function onChange(param1:Event) : *
		{
			ExternalInterface.call("llcomboBoxID",this.id,this.combo_mc.selectedIndex);
		}
		
		public function deselectElement(param1:MouseEvent) : *
		{
		}
		
		public function selectElement(param1:MouseEvent) : *
		{
			ExternalInterface.call("PlaySound","UI_Generic_Over");
		}
		
		public function onMouseOver(param1:MouseEvent) : *
		{
			this.base.mainMenu_mc.setCursorPosition(this.id);
			if(this.tooltip != null && this.tooltip != "" && !this.combo_mc.m_isOpen)
			{
				this.base.curTooltip = this.pos;
				this.tooltipYOffset = -4;
				this.tooltipOverrideW = this.base.ElW;
				tooltipHelper.ShowTooltipForMC(this,root,"bottom");
			}
		}
		
		public function onMouseOut(param1:MouseEvent) : *
		{
			if(this.base.curTooltip == this.pos && this.base.hasTooltip)
			{
				ExternalInterface.call("hideTooltip");
				this.base.hasTooltip = false;
			}
			this.base.curTooltip = -1;
		}
		
		function frame1() : *
		{
			this.base = root as MovieClip;
			addEventListener(MouseEvent.MOUSE_OVER,this.onMouseOver);
			addEventListener(MouseEvent.MOUSE_OUT,this.onMouseOut);
			this.combo_mc.addEventListener(Event.CHANGE,this.onChange);
			this.combo_mc.addEventListener(Event.OPEN,this.onOpen);
			this.combo_mc.m_dropOutYDisplacement = -2;
			this.combo_mc.bgHSpacing = -3;
			this.div = new scrollbarDivider();
			this.div.x = 241;
			this.div.y = 2;
			this.combo_mc.divider = this.div;
			this.mHeight = 30;
		}
	}
}