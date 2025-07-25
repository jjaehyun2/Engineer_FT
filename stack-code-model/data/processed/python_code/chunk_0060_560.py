package  
{
	import temple.core.display.CoreMovieClip;
	import temple.ui.buttons.MultiStateButton;
	import temple.ui.form.components.ComboBox;
	import temple.ui.form.components.DateSelector;
	import temple.ui.scroll.ScrollComponent;
	import temple.utils.localization.DateLabelFormat;
	import temple.utils.localization.EnglishDateLabels;
	import temple.utils.localization.IDateLabels;
	import temple.utils.types.DateUtils;

	import flash.events.Event;
	import flash.text.TextField;

	public class DateFormatTester extends CoreMovieClip 
	{
		public var mcDateSelector:DateSelector;
		public var txtFormat:TextField;
		public var txtOutput:TextField;
		
		public function DateFormatTester()
		{
			mcDateSelector.date = new Date();
			mcDateSelector.addEventListener(Event.CHANGE, handleChange);
			txtFormat.addEventListener(Event.CHANGE, handleChange);
			
			mcDateSelector.end = new Date(2100, 0, 1);
			
			MultiStateButton(ScrollComponent(ComboBox(mcDateSelector.day).list).scrollBar.button).outOnDragOut = false;
			MultiStateButton(ScrollComponent(ComboBox(mcDateSelector.month).list).scrollBar.button).outOnDragOut = false;
			MultiStateButton(ScrollComponent(ComboBox(mcDateSelector.year).list).scrollBar.button).outOnDragOut = false;
			
			setOutput();
		}
		
		public function set format(value:String):void
		{
			txtFormat.text = value;
			setOutput();
		}
		
		public function set language(value:IDateLabels):void
		{
			mcDateSelector.monthLabels = value;
			mcDateSelector.monthFormat = DateLabelFormat.SHORT;
			setOutput();
		}

		override public function destruct():void
		{
			super.destruct();
			
			if (mcDateSelector)
			{
				mcDateSelector.destruct();
				mcDateSelector = null;
			}
			if (txtFormat)
			{
				txtFormat.removeEventListener(Event.CHANGE, handleChange);
				txtFormat = null;
			}
			txtOutput = null;
		}

		private function handleChange(event:Event):void
		{
			setOutput();
		}

		private function setOutput():void
		{
			txtOutput.text = mcDateSelector.date ? DateUtils.format(txtFormat.text, mcDateSelector.date, mcDateSelector.monthLabels || EnglishDateLabels) : 'Error, no valid date';
		}
	}
}