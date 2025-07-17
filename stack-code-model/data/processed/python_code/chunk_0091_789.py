package common.view
{
	import common.event.EventCenter;
	
	import laya.events.Event;
	import laya.ui.Box;
	import laya.ui.Image;
	import laya.ui.Label;
	import laya.utils.Handler;
	
	import manager.UIManager;
	
	import net.Message;
	import net.ProtoMessage;
	
	import ui.common.TimeWarUI;

	public class TimeWarView
	{
		protected var _skin:TimeWarUI;
		
		public var isShow:Boolean = false;
		public function TimeWarView()
		{
			UIManager.instance.uiLayer.on(Event.CLICK,this,onClickUiLayer);
			
			_skin = new TimeWarUI();
			_skin.mouseThrough = true;
			
			EventCenter.instance.on(EventCenter.COMMON_INFOLIST_NOTICE,this,this.updata);
			EventCenter.instance.on(EventCenter.HALLVIEW_GETSINGLE,this,onTimeWalMessage);
			init();
		}
		
		protected function onClickUiLayer(e:Event):void
		{
			hide();
		}
		
		private var player:Array=[];
		private function onTimeWalMessage(data:*):void
		{
			trace(data.list)
			this.player=[];
			if(data.list.length<=0){
				var len:int=model.playerInfoVec.length;
				for (var i:int = 0; i < len; i++) 
				{
					if(model.playerInfoVec[i].pos!=-1 && !(model.playerInfoVec[i].uid==UserData.uid && model.isSelfSitDown==false)){
						this.player.push(model.playerInfoVec[i]);					
					}
				};
			}else{
				
				this.player=data.list;
			}
			trace(this.player);
			this.playerListData((this.player as Array).sort(compareFunction));
		}
		protected function compareFunction(A:Object,B:Object):int
		{
			if(A.score>B.score)
			{
				return -1;
			}
			else if(A.score==B.score)
			{
				if(parseInt(A.id)<parseInt(B.id)){
					return 1
				}else if(parseInt(A.id)>parseInt(B.id)){
					return -1;
				}else{
					return 0;
				}
			}
			else
			{
				return 1;
			}
		}
		private var playerData:Array;//玩家list数据
		private function playerListData(_dt:Array):void
		{
			//
			this.playerData =[];
			var len:int=this.player.length;
			for(var m:int =0;m<len;m++){
				var Name:String=_dt[m].nickname==undefined?_dt[m].name:_dt[m].nickname;
				//Name = decodeURIComponent(Name);
				this.playerData.push({score:_dt[m].score,name:Name});
			}
			_skin.playerList.array = this.playerData;
			_skin.playerList.repeatY=4;
			_skin.playerList.vScrollBarSkin="";//添加list滚动条功能（UI不可显示）
			_skin.playerList.selectEnable = true;
			_skin.playerList.renderHandler = new Handler(this, onRenderPlayer);
			_skin.playerList.refresh();
		}
		
		private function onRenderPlayer(cell:Box,index:int):void
		{
			if(index > this.playerData.length)return;
			var data:Object=this.playerData[index];
			
			var nikname:Label=cell.getChildByName("playerName") as Label;
//			data.name = decodeURIComponent(data.name);
			nikname.text = data.name;
			
			var score:Label=cell.getChildByName("playerScore") as Label;
			score.text = data.score+"";
		}
		
		protected function get model():*
		{
			return ModuleDef.CurGameModule.instance.gameContext.model;
			
		}
		
		
		private function init():void
		{
//			_skin.close.on(Event.CLICK,this,function(e:Event):void{
//				trace(e,"-----------------")
//				this.showOrHide();
////				e.stopPropagation();
//			});
			
			_skin.watchList.renderHandler = new Handler(this, onRenderWatch);

		}
		private var watchData:Array;//玩家list数据
		private function listData(_dt:Array):void
		{
			//围观用户的数据列表
			this.watchData =[];
			var len:int=_dt.length;
			for(var m:int =0;m<len;m++){
				this.watchData.push({headimg:_dt[m].Icon,name:_dt[m].nickname});
			}
			_skin.watchList.array = this.watchData;
			_skin.watchList.repeatX=5;
			//_skin.watchList.repeatY=2//this.watchData.length<=5?1:2;
			_skin.watchList.vScrollBarSkin="";//添加list滚动条功能（UI不可显示）
			_skin.watchList.selectEnable = true;
			_skin.watchList.refresh();
		}
		
		private function onRenderWatch(cell:Box,index:int):void
		{
			if(index > this.watchData.length)return;
			var data:Object=this.watchData[index];
						
			var watchIMG:Image=cell._childs[1]._childs[0].getChildByName("watchIMG") as Image; 
			watchIMG.visible=true;
			watchIMG.skin = data.headimg==""||WX.splitStr(data.headimg,"")[0]!='h'?"common/morentouxiang.png":data.headimg;
			
			var nikname:Label=cell.getChildByName("nikname") as Label;
			nikname.visible=true;
			nikname.text = data.name;
		}
		
		public function showOrHide():void
		{
			if(_skin.parent)
			{
				_skin.parent.removeChild(_skin);
				isShow = false;
			}
			else
			{
				this.show()
			}
		}
		
		public function show():void
		{			
			updata();
			QuickUtils.AddCenter(_skin,UIManager.instance.popLayer);
			//UIManager.instance.popLayer.addChild(_skin);
			isShow = true;
		}
		
		private function updata():void
		{
			trace("-----------------------------------------")
			var getRecord:Object = {
				"uniqueCode":UserData.uniqueCode
			};
			trace(UserData.uniqueCode)
			EventCenter.instance.event(EventCenter.SOCKET_SEND,ProtoMessage.getProtoMessage(Message.MSG_Room_Summary,getRecord));
			var dt:Array=[];
			var len:int=model.playerInfoVec.length;
			for (var i:int = 0; i < len; i++) 
			{
				if(model.playerInfoVec[i].pos==-1){
					dt.push(model.playerInfoVec[i]);
				}else if(model.playerInfoVec[i].uid==UserData.uid && model.isSelfSitDown==false){
					dt.push(model.playerInfoVec[i]);
				}else{
					
				}
			};
			_skin.watchNum.text="观众("+dt.length+")";
			trace(model.playerInfoVec)
			this.listData(dt);
			
		}
		
		public function hide():void
		{
			if(_skin.parent)
			{
				_skin.parent.removeChild(_skin);
			}
			isShow = false;
		}
	}
}