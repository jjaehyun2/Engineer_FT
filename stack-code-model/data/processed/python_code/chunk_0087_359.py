package hall.view
{
	import common.baseui.UIBase;
	import common.event.EventCenter;
	
	import hall.view.item.AgentAddView;
	import hall.view.item.AgentGiveView;
	import hall.view.item.AgentItem;
	import hall.view.item.GiveLogView;
	
	import laya.display.Sprite;
	import laya.events.Event;
	import laya.net.HttpRequest;
	import laya.ui.List;
	import laya.utils.Handler;
	
	import ui.hall.DailiViewUI;
	
	/**代理主页*/
	public class AgentView extends UIBase
	{
		
		protected var _skin:DailiViewUI;
		
		protected var _playerList:List;
		
		public function AgentView(container:Sprite=null)
		{
			super(container);
			skinRes = "";
		}
		
		
		override protected function onLoaded():void
		{
			super.onLoaded();
			_skin = new DailiViewUI();
			_skin.mouseEnabled = true;
			if(_isShow)
			{
				container.addChild(_skin);
			}
			
			init();
		}
		
		private var hr:HttpRequest;
		
		protected function init():void
		{
			hr = new HttpRequest();
			
			_playerList = _skin.playerList;
			_playerList.vScrollBarSkin = "";
			_playerList.itemRender = AgentItem;
			_playerList.renderHandler = new Handler(this, updateListItem);
			_playerList.array = [];
			_playerList.refresh();
			
			hr.on(Event.COMPLETE, this, onRefreshList);
			
			EventCenter.instance.on(EventCenter.HALL_UPDATE_AGENTSBELONG,this,requestAgentsBelong);
			EventCenter.instance.on(EventCenter.HALL_SHOW_AGENTDETAILVIEW,this,onShowDetailView);
			
			_skin.addBtn.on(Event.CLICK,this,onClickAddBtn);
			_skin.giveBtn.on(Event.CLICK,this,onClickGiveBtn);
			_skin.giveLogBtn.on(Event.CLICK,this,onClickGiveLogBtn);
			
			updateUI();
			
			
		}
		
		protected function requestAgentsBelong():void
		{
			
			var data:Object = {
				target_uid:parseInt(UserData.selfuid)
			};
			
			var query:Array=[];
			for(var k in data){
				query.push(k+"="+encodeURIComponent(data[k]));
			}
			data=query.join("&");
			
			hr.send("phpApi/api/getAgentsBelong.php",data, "post", "text");
		}
		
		protected var _addAgentView:AgentAddView;
		
		protected function onClickAddBtn(e:Event):void
		{
			if(!_addAgentView)
			{
				_addAgentView = new AgentAddView();
			}
			
			_addAgentView.show();
		}
		 
		protected var _giveAgentView:AgentGiveView;
		
		protected function onClickGiveBtn(e:Event):void
		{
			if(!_giveAgentView)
				
			{
				_giveAgentView = new AgentGiveView();
			}
			_giveAgentView.show();
		}
		
		protected var _giveLogView:GiveLogView;
		
		protected function onClickGiveLogBtn(e:Event):void
		{
			if(!_giveLogView)
			{
				_giveLogView = new GiveLogView();
			}
			_giveLogView.show(0);
		}
		
		protected function onShowDetailView(data:Object):void
		{
			if(!_giveLogView)
			{
				_giveLogView = new GiveLogView();
			}
			_giveLogView.show(1,data);
		}
		
		
		protected function onRefreshList(data:String):void
		{
			var response:Object = JSON.parse(data);
			
			_playerList.array = response.data;
			_playerList.refresh();
			
			trace("Agent:: onRefreshList",response.data);
		}
		
		public override function show():void
		{
			super.show();
			if(_skin)
			{
				container.addChild(_skin);
				requestAgentsBelong();
			}
			
		}
		
		
		public override function hide():void
		{
			super.hide();
			if(_skin && _skin.parent)
			{
				_skin.parent.removeChild(_skin); 
			}
			
			updateUI();
		}
		
		protected function updateUI():void
		{
			if(_skin)
			{
				_skin.levelImg.skin = "hall/level"+UserData.level+".png";
			}
			
		}
		
		/**更新玩家的代理列表*/
		private function updateListItem(cell:AgentItem, index:int):void 
		{
			cell.setData(cell.dataSource,index+1);
		}
		 
		
	}
	
	
}