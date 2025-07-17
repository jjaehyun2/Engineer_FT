package com.grantech.controls.items
{
	import feathers.controls.Button;

	import starling.display.Image;
	import starling.textures.Texture;
	
	public class InspectorButtonItemRenderer extends InspectorBaseItemRenderer
	{
		public function InspectorButtonItemRenderer() { super(); }
		override protected function redrawControl():void
		{
			super.redrawControl();

			if (this.valueDisplay == null)
			{
				this.valueDisplay = new Button();
				this.valueDisplay.layoutData = VALUE_LAYOUTDATA;
				this.addChild(this.valueDisplay);
			}
			
			var button:Button = valueDisplay as Button;
			if( this.value is Texture )
			{
				button.defaultIcon = new Image(this.value as Texture);
				button.defaultIcon.width = button.defaultIcon.height = height - 4;
			}
			else
			{
				button.label = this.value;
			}
			
			// if (!button.hasEventListener(Event.TRIGGERED))
			// 	button.addEventListener(Event.TRIGGERED, button_triggeredHandler);
		}
	}
}