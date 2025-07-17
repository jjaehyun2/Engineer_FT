package  
{
	import flash.text.TextField;
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class DisplayBox extends DisplayLabel
	{
		public var field:TextField = new TextField();
		
		public function DisplayBox() 
		{
			field = new TextField();
			field.textColor = 0xFFFFFF;
			field.x = -width / 2;
			field.text = "Test";
			field.autoSize = 'left';
			addChild(field);
		}
		
	}

}