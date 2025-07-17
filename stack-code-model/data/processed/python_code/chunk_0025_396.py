package hall.view.replay
{
	
	import common.event.EventCenter;
	
	import hall.HallModule;
	import hall.view.replay.item.DetailListItem;
	
	import laya.display.Sprite;
	import laya.events.Event;
	import laya.ui.Button;
	import laya.ui.Label;
	import laya.ui.List;
	import laya.utils.Handler;
	
	
	import manager.UIManager;
	
	import net.Message;
	import net.ProtoMessage;
	
	import ui.hall.replay.BattleDetailListPageUI;
	
	
	
	/**一个房间的战绩列表*/
	public class BattleDetailListView
	{
		protected var skin:BattleDetailListPageUI;
		
		protected var roomTypeTf:Label;
		protected var roomidTf:Label;
		protected var roomNumTf:Label;
		protected var viewDetailBtn:Button;
		protected var backBtn:Button;
		
		protected var detailList:List;
		
		public function BattleDetailListView()
		{
			skin = new BattleDetailListPageUI();
			skin.mouseThrough = true;
			init();
			
		}
		
		
		
		public function show():void
		{
			UIManager.instance.uiLayer.addChild(skin);
		}
		
		public function hide():void
		{
			skin.removeSelf();
		}
		
		
		protected function init():void
		{
			roomTypeTf = skin.roomTypeTf;
			roomidTf = skin.roomidTf;
			roomNumTf = skin.roomNumTf;
			viewDetailBtn = skin.viewDetailBtn;
			backBtn = skin.backBtn;
			
			detailList = skin.recordList;
			detailList.vScrollBarSkin = "";
			detailList.itemRender = DetailListItem;
			detailList.renderHandler = new Handler(this, updateListItem);
			
			backBtn.on(Event.CLICK,this,onClickBackBtn);
			viewDetailBtn.on(Event.CLICK,this,onClickDetailBtn);
			
		}
		
		private function updateListItem(cell:DetailListItem, index:int):void 
		{
			cell.setData(cell.dataSource,index+1);
		}
		
		protected function onClickBackBtn(e:Event):void
		{
			hide();
		}
		
		protected function onClickDetailBtn(e:Event):void
		{
			hide();
			var getRecord:Object = {
				"uniqueCode":data.uniqueCode
			};
			
			EventCenter.instance.event(EventCenter.SOCKET_SEND,ProtoMessage.getProtoMessage(Message.MSG_Room_Summary,getRecord));
			HallModule.instance.hallContext.hallView.hallLayer.onPlayView.singleBoardView.showInit();
		}
		
		protected var data:Object;
		
		
		public function updateData(dat:Object):void
		{
			data = dat;
			
			roomTypeTf.text = UserData.roomtype_reference[data.roomType];
			roomidTf.text = data.rid;
			
			var list:Array = data.list as Array;
			
			roomNumTf.text = list.length+"";
			detailList.array = list;
			detailList.scrollTo(0);
			detailList.refresh();
		}
		
		
	}
}