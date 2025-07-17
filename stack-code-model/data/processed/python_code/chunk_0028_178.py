package modules.gameCommon.chat
{
	
	import common.event.EventCenter;
	
	import laya.events.Event;
	import laya.ui.Image;
	import laya.ui.View;
	import laya.utils.Handler;
	
	import modules.gameCommon.chat.item.ChatItem;
	

	

	public class ChatPage
	{
		protected var _type:int = 1;
		private var _skin:*;
		public function get skin():View
		{
			return _skin;
		}
		
		private var expressArr:Array;
		public function ChatPage(skin:*,tp:int=1)//ChatPageUI
		{
			_skin = skin;
			_type = tp;
			
			(_skin as View).mouseThrough = true;
			initUI();
		}
		
		protected function initUI():void
		{
			_skin.chatList.itemRender = ChatItem;
			_skin.chatList.vScrollBarSkin = "";
			_skin.chatList.selectEnable = true;
			_skin.chatList.selectHandler = new Handler(this, onSelectRound);
			_skin.chatList.renderHandler = new Handler(this, updateRoundItem);
			expressArr = new Array();
			for(var i:int=1;i <= 16;i++)
			{
				(_skin["face" + i] as Image).on(Event.CLICK,this,onTouchexpress);
				expressArr.push(_skin["face" + i]);
			}
			
			var chatConf:Array;
			
			if(_type == 1)
			{
				chatConf = AppConfig.Chat_Message;
			}
			else if(_type == 2)
			{
				chatConf = AppConfig.Sddz_Chat_Message;
			}
			else
			{
				chatConf = AppConfig.Chat_Message;
			}
			
			
			setChatContetn(chatConf);
//			Laya.stage.on(Event.KEY_UP,this,onEnterUp);
			_skin.touchhide.mouseEnabled = true;
			_skin.touchhide.on(Event.CLICK,this,onhideUI);
		}
		
		private function onTouchexpress(e:Event):void
		{
			var index:int = expressArr.indexOf(e.currentTarget);
			EventCenter.instance.event(EventCenter.SEND_CHAT_MESSAGE,UserData.uid+"#express|" + index);
			hide();

		}
		private function onhideUI(e:Event):void
		{
			switchState();
		}
	
		
		private function updateRoundItem(cell:*, index:int):void //* 是 RoundReportItem
		{
			//console.log(cell,index);
			cell.setData(cell.dataSource);
		}
		
		private function onSelectRound(index:int):void
		{
			//trace("当前选择的索引：" + index);
		}
		
		public function setChatContetn(content:Array):void
		{
			_skin.chatList.array =content;
			_skin.chatList.refresh();
		}
		public function show():void
		{
			_skin.visible = true;					
		}
		
		public function hide():void
		{
			_skin.visible = false;
		}
		
		public function switchState(offsetX:Number=0,offsetY:Number=0):void
		{
			_skin.visible = !_skin.visible;

		}
	}
}