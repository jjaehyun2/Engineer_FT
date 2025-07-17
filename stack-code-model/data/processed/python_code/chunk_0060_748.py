package AdvPrintPage 
{
	import flash.display.Sprite;
	import flash.text.TextField;
	import flash.text.TextFormat;
	/**
	 * ...
	 * @author Jake
	 */
	public class TextPanel extends Sprite
	{
		private var nameField:TextField;
		private var flexIDField:TextField;
		private var modelField:TextField;
		private var ipField:TextField;
		private var warnField:TextField;
		private var warnColor:uint;
		private var displayText:TextFormat;
		
		private var printName:String = "Hostname: ";
		private var model:String = "Model: ";
		private var flexID:String = "Flex ID: ";
		private var ipAddress:String = "IP : ";
		private var warning:String = "Status: ";
		
		public function TextPanel(x:int, y:int, printName:String, model:String, flexID:String, ipAddress:String,warnStatus:Boolean) 
		{
			this.x = x;
			this.y = y;
			this.printName += printName;
			this.model += model;
			this.flexID += flexID;
			this.ipAddress += ipAddress;
			if (warnStatus) 
			{
				this.warning += "Warning! Ink Level Low. TKT Created"
				warnColor = 0xFF0000;
			}
			else 
			{
				this.warning += "Safe"
				warnColor = 0x0000FF;
			}
			displayText = new TextFormat(null, 14, null, true);
			displayName();
			displayModel();
			displayFlexID();
			displayIP();
			displayWarning();
		}
		
		private function displayModel():void 
		{
			modelField = new TextField();
			modelField.x = 0;
			modelField.y = 40;
			modelField.textColor = 0x000000;
			modelField.text = this.model;
			modelField.width = modelField.text.length * 10;
			modelField.setTextFormat(displayText);
			addChild(modelField);
		}
		private function displayName():void 
		{	
			nameField = new TextField();
			nameField.x = 0;
			nameField.y = 0;
			nameField.width = printName.length * 10;
			nameField.text = printName;
			nameField.setTextFormat(displayText);
			addChild(nameField);
		}
		private function displayFlexID():void 
		{	
			flexIDField = new TextField();
			flexIDField.x = 0;
			flexIDField.y = 60;
			flexIDField.width = flexID.length * 10;
			flexIDField.text = flexID;
			flexIDField.setTextFormat(displayText);
			addChild(flexIDField);
		}
		private function displayIP():void 
		{	
			ipField = new TextField();
			ipField.x = 0;
			ipField.y = 20;
			ipField.width = ipAddress.length * 10;
			ipField.height = 20;
			ipField.text = ipAddress;
			ipField.setTextFormat(displayText);
			addChild(ipField);
		}
		private function displayWarning():void 
		{
			warnField = new TextField();
			warnField.x = 0;
			warnField.y = 80;
			warnField.width = warning.length * 10;
			warnField.height = 20;
			warnField.text = warning;
			warnField.textColor = warnColor;
			warnField.setTextFormat(displayText);
			addChild(warnField);
		}
		
	}

}