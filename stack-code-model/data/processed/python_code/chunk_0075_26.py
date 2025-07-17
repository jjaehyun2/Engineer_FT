package h2olib.control
{
	import mx.controls.TextInput;
	
	[Style(name="errorSkin", type="Class", inherit="no")]
	
	public class TextInput extends mx.controls.TextInput
	{
		private var _originalBorderSkin:Class;
		
		public function TextInput()
		{
			super();
		}
		
		override protected function commitProperties():void
		{
			super.commitProperties();
			
			if(errorString == "" || !errorString)
			{
				if(!_originalBorderSkin)
				{
					_originalBorderSkin = getStyle('borderSkin');
				}
				this.setStyle('borderSkin', _originalBorderSkin);
			}
			else
			{
				
				this.setStyle('borderSkin', getStyle('errorSkin'));
			}
		}
	}
}