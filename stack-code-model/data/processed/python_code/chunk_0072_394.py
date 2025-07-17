package 
{
	import com.alienos.sgs.as3.client.*;
	import flash.events.*;
	import flash.display.*;
	import flash.text.*;
	import flash.ui.*;
	import flash.utils.ByteArray;
	
	/**
	 * Part of the PDS Chat Video Tutortial
	 * @author Sebastian Herrlinger
	 */
	public class Main extends Sprite 
	{
		
		private var fieldFormat:TextFormat = new TextFormat('Arial', 12, 0x444444, true);
		private var nameField:TextField = new TextField();
		private var chatField:TextField = new TextField();
		private var messageField:TextField = new TextField();
		
		private var sgsClient:SimpleClient = null;
		private var chatChannel:ClientChannel = null;
		
		public function Main():void 
		{
			if (stage) init();

			else addEventListener(Event.ADDED_TO_STAGE, init);

		}
		
		private function init(e:Event = null):void 
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);
			stage.align     = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.NO_SCALE;
			createGUI();
					
		}
		
		private function createGUI():void
		{
			var title:TextField = new TextField();
			title.defaultTextFormat = new TextFormat('Arial', 20, 0x444444, true);
			title.text = 'Simple PDS Chat Client';
			title.autoSize = TextFieldAutoSize.LEFT;
			title.x = title.y = 5;
			addChild(title);
			nameField.x = chatField.x = messageField.x = 5;
			nameField.y = 35
			chatField.y = 60;
			messageField.y = 365;
			nameField.defaultTextFormat =
				chatField.defaultTextFormat = 
				messageField.defaultTextFormat = fieldFormat;
			nameField.type = 
				messageField.type = TextFieldType.INPUT;
			nameField.border =
				chatField.border = 
				messageField.border = true;
			nameField.borderColor = 
				chatField.borderColor = 
				messageField.borderColor = 0x444444;
			nameField.width = 
				chatField.width = 
				messageField.width = 300;
			nameField.height = 
				messageField.height = 20;
			chatField.height = 300;
			nameField.background = 
				chatField.background = 
				messageField.background = true;
			chatField.selectable = false;
			nameField.text = 'Name';
			messageField.text = 'Message';
			addChild(nameField);
			addChild(chatField);
			addChild(messageField);
			messageField.addEventListener(KeyboardEvent.KEY_UP, messageKey);
			trace("wtf");
		}
		
		private function messageKey(evt:KeyboardEvent):void
		{
			if (evt.keyCode == Keyboard.ENTER) {
				if(sgsClient != null) {
					sendMessage();
				} else {
					sgsClient = new SimpleClient('localhost', 1139);
					sgsClient.login(nameField.text, "password");
					sgsClient.addEventListener(SgsEvent.CHANNEL_JOIN, channelJoin);
				}
			}
		}
		
		private function sendMessage():void
		{
			var buf:ByteArray = new ByteArray();
			buf.writeUTFBytes(nameField.text + ': ' + messageField.text);
			messageField.text = '';
			sgsClient.channelSend(chatChannel, buf);
		}
		
		private function channelJoin(evt:SgsEvent):void
		{
			chatChannel = new ClientChannel(evt.channel.name, evt.channel.rawId);
			sgsClient.addEventListener(SgsEvent.CHANNEL_MESSAGE, channelMessage);
			sendMessage();
		}
		
		private function channelMessage(evt:SgsEvent):void
		{
			addMessage(evt.channelMessage.readUTFBytes(evt.channelMessage.bytesAvailable));
		}
		
		private function addMessage(msg:String):void
		{
			chatField.appendText(msg + "\n");
			chatField.scrollV = chatField.maxScrollV;
		}
		
	}
	
}