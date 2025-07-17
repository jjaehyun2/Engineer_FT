package gui
{
	import flash.display.Shape;
	import flash.text.TextFieldType
	import flash.text.TextFormat;

	public class TextInput extends TextBox
	{
		
		public function TextInput() 
		{
			m_text.type = TextFieldType.INPUT;
			m_text.textColor = 0xFFFFFF;
			m_text.backgroundColor = 0xF28101;		
		}
		
		public function get textformat():TextFormat
		{
			return m_text.defaultTextFormat;
		}
		
	}
	
}