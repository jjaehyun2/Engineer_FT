package hall.view.item
{
	import common.event.EventCenter;
	import common.view.PopBox;
	
	import laya.events.Event;
	import laya.net.HttpRequest;
	import laya.ui.List;
	import laya.utils.Handler;
	
	import manager.UIManager;
	
	import net.Message;
	import net.ProtoMessage;
	
	import ui.hall.item.GiveLogViewUI;

	public class GiveLogView
	{
		protected var _skin:GiveLogViewUI;
		protected var _logList:List;
		
		public function GiveLogView()
		{
			_skin = new GiveLogViewUI();
			init();
		}
		
		private var hr:HttpRequest;
		
		protected function init():void
		{
			hr = new HttpRequest();
			_logList = _skin.logList;
			_logList.vScrollBarSkin = "";
			_logList.itemRender = AgentLogItem;
			_logList.renderHandler = new Handler(this, updateListItem);
			_logList.array = [];
			_logList.refresh();
			
			_skin.closeBtn.on(Event.CLICK,this,onClose);
			_skin.searchBtn.on(Event.CLICK,this,onClickSearchBtn);
			
			hr.on(Event.COMPLETE, this, function(e:*=null):void{
				var response:Object = JSON.parse(hr.data);
				if (response.status == 1) {
					_logList.array = response.data;
					_logList.refresh();
				}else {
					QuickUtils.popMessageBox(response.msg,PopBox.BTN_QUEREN,this,null);
				}
			});
		}
		
		protected function onClose(e:Event):void
		{
			hide();
		}
		
		/**0查看所有记录，1查看特定玩家的记录*/
		protected var _type:int = 0;
		
		/**特定玩家附带的信息*/
		protected var _paramObj:* = null;
		
		public function show(type:int,paramObj:*=null):void
		{
			UIManager.instance.popLayer.addChild(_skin);
			
			_type = type;
			_paramObj = paramObj;
			if(_type == 0)
			{
				_skin.titleTf.text = "赠送记录";
			}
			else if(_type == 1)
			{
				_skin.titleTf.text = "赠送明细[" + _paramObj.id + " " +_paramObj. nick_name + "]";;
			}
			
			_logList.array =[];
			_logList.refresh();
			
		}
		
		public function hide():void
		{
			if(_skin && _skin.parent)
			{
				_skin.parent.removeChild(_skin);
			}
		}
		
		/**更新玩家的代理列表*/
		private function updateListItem(cell:AgentLogItem, index:int):void 
		{
			cell.setData(cell.dataSource,index+1);
		}
		
		/**查询*/
		private function onClickSearchBtn(e:Event):void
		{
//			trace(_skin.beginTimeTf.text);
			if(_skin.beginTimeTf.text == "" || _skin.endTimeTf.text == "")
			{
				return;
			}
			
			var fromDate:String = _skin.beginTimeTf.text + " 00:00:00";
			var endDate:String = _skin.endTimeTf.text + " 23:59:59";
			var fromID:String = UserData.selfuid;
			var condition:int = _skin.conditionRadio.selectedIndex;
			var toID:int = 0;
			if(_type == 1)
			{
				toID = _paramObj.id;
			}
			
			var data:Object = {
				fromDate:fromDate,
				endDate:endDate,
				fromID:parseInt(fromID),//
				condition:condition,
				type:_type,
				toID:toID
			};
			
			var query:Array=[];
			for(var k in data){
				query.push(k+"="+encodeURIComponent(data[k]));
			}
			data=query.join("&");
			hr.send("phpApi/api/giveLog.php",data, "post", "text");
			
			
		}
	}
}