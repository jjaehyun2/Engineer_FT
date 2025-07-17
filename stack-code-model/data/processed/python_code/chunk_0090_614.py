package hall.view
{
	import common.baseui.UIBase;
	import common.event.EventCenter;
	
	
	import laya.display.Sprite;
	import laya.events.Event;
	import laya.ui.Box;
	import laya.ui.Image;
	import laya.ui.Label;
	import laya.utils.Browser;
	import laya.utils.Handler;
	
	import manager.TextManager;
	
	import net.Message;
	import net.ProtoMessage;
	
	import ui.hall.SingleBoardViewUI;

	public class SBoardView extends UIBase
	{
		protected var _skin:SingleBoardViewUI;
		public function SBoardView(container:Sprite=null)
		{
			super(container);
			skinRes ="";
		}
		
		override protected function onLoaded():void
		{
			super.onLoaded();
			_skin = new SingleBoardViewUI();
			_skin.mouseEnabled = true;
			if(_isShow)
			{
				container.addChild(_skin);
			}
			
			init();
		}
		
		protected function init():void
		{	
			_skin.shareBox.visible = false;
			
			_skin.list.array = [];
			_skin.backOnplay.on(Event.CLICK,this,function():void{
				this.hide();
				
				var battleDetail:Object ={ roomId : this.dataSource.homeOwner.roomId};
				EventCenter.instance.event(EventCenter.SOCKET_SEND,ProtoMessage.getProtoMessage(Message.MSG_BattleDetail,battleDetail));
				
			});
			
			_skin.shareBox.on(Event.CLICK,this,function():void{
				_skin.shareBox.visible = false;
				WX.onMenuShareAppMessage(null,Browser.window.wxInfo.nickname+"分享了微信打牌神器-"+AppConfig.nameTitle+"，邀您一起浪！");
			})
			
			_skin.shareScoreBtn.on(Event.CLICK,this,function():void{
				_skin.shareBox.visible = true;
				
				var str:String = "";
				
				if(data)
				{
					var i:int;
					for(i=0;i<data.length;i++)
					{
						if(i==0)
						{
							str += data[i].player + ":" + (data[i].score == undefined ? 0 : data[i].score);
						}
						else
						{
							str += "    " + data[i].player + ":" + (data[i].score == undefined ? 0 : data[i].score);
						}
					}
				}
				WX.onMenuShareAppMessage("【"+_skin.roomid.text+"】"+RecordView.gameName ,str,null,this,onHideShareScore);
			})
				
			EventCenter.instance.on(EventCenter.HALLVIEW_GETSINGLE,this,onGotData);
		}
		
		protected function onHideShareScore():void
		{
			_skin.shareBox.visible = false;
			WX.onMenuShareAppMessage(null,Browser.window.wxInfo.nickname+"分享了微信打牌神器-"+AppConfig.nameTitle+"，邀您一起浪！");
		}
		
		protected var dataSource:Object;
		
		private function getRule(dt:*):*
		{
			
			
			
			
			
			var ruleNumber:*
			var temoData:Array=WX.splitStr(dt,",");
			var isHas:Boolean=false;
			for (var k:int = 0,le:int=temoData.length; k < le; k++) 
			{
				switch(parseInt(temoData[k]))
				{
					case 4:
						ruleNumber=AppConfig.getRule(4);
						isHas=true;
						break;
					case 5:
						ruleNumber=AppConfig.getRule(5);
						isHas=true;
						break;
					case 18:
						ruleNumber=AppConfig.getRule(18);
						isHas=true;
						break;
					case 19:
						ruleNumber=AppConfig.getRule(19);
						isHas=true;
						break;
					case 20:
						ruleNumber=AppConfig.getRule(20);
						isHas=true;
						break;
					case 21:
						ruleNumber=AppConfig.getRule(21);
						isHas=true;
						break;
					case 22:
						ruleNumber=AppConfig.getRule(22);
						isHas=true;
						break;
					case 6:
						ruleNumber=AppConfig.getRule(6);
						isHas=true;
						break;
					case 7:
						ruleNumber=AppConfig.getRule(7);
						isHas=true;
						break;
					case 8:
						ruleNumber=AppConfig.getRule(8);
						isHas=true;
						break;
					default:
						break;
				}
				if(isHas==true) return ruleNumber;
			}	
		}
		
		private function onGotData(data:*):void
		{
			this.dataSource = data;
			RecordView.gameName = UserData.roomtype_reference[data.roomType];
			_skin.gameName.text=RecordView.gameName;
			
			trace("222222222222::" + data);
			if(data.list.length<1){
			trace(data.list.length,'--------------------------------')
				if(ModuleDef.CurGameModule&&ModuleDef.CurGameModule.inGame)
				{
					return;
				}else{
					
					return this.hide();;
				}
			}
			
			
			this.timeDate=AppConfig.getTimeDate(data.homeOwner.timestamp*1000);
			trace(data.homeOwner.rule,this.getRule(data.homeOwner.rule).desc)
			this.gameType=this.getRule(data.homeOwner.rule).desc;
			_skin.roomid.text=data.roomId||"";
			
			_skin.headIMG.skin=WX.splitStr(data.homeOwner.icon,"")[0]=='h'?data.homeOwner.icon:"common/morentouxiang.png";
			_skin.onplayTime.text=AppConfig.getTimeDate(data.homeOwner.timestamp*1000)||"";
			_skin.onplayName.text=data.homeOwner.nickName;
//			_skin.onplay.text=this.getRule(data.homeOwner.rule).desc||"";
			
			updata((data.list as Array).sort(compareFunction));
		}
		
		protected function compareFunction(A:Object,B:Object):int
		{
			if(A.score>B.score)
			{
				return -1;
			}
			else if(A.score==B.score)
			{
				return 0;
			}
			else
			{
				return 1;
			}
		}
		private var data:Array;//list数据数组
		private function updata(dt:*):void
		{
			trace(dt)
			
			var len1:int=dt.length-1;
			_skin.headIMGM.skin=WX.splitStr(dt[0].icon,"")[0]=='h'?dt[0].icon:"common/morentouxiang.png";
			_skin.headIMGL.skin=WX.splitStr(dt[len1].icon,"")[0]=='h'?dt[len1].icon:"common/morentouxiang.png";
			_skin.niknameM.text=dt[0].name;
			_skin.niknameL.text=dt[len1].name;
			this.data=[];
			for (var i:int = 0,len:int=dt.length; i < len; i++) 
			{
//				if(dt[i].houseowner==true){
//					_skin.headIMG.skin=WX.splitStr(dt[i].icon,"")[0]=='h'?dt[i].icon:"common/morentouxiang.png";
//					_skin.onplayTime.text=this.timeDate||"";
//					_skin.onplayName.text=dt[i].name;
//					_skin.onplay.text=this.gameType||"";
////					break;
//				}
				data.push({score:dt[i].score,player:dt[i].name,headimg:"http://thirdwx.qlogo.cn/mmopen/vi_32/"+dt[i].icon});
			}
			
			_skin.list.array = data;
			_skin.list.repeatY=6;
			// 使用但隐藏滚动条
			_skin.list.vScrollBarSkin = "";
			_skin.list.selectEnable = true;
			_skin.list.renderHandler = new Handler(this, this.onRender);
			_skin.list.refresh();
			
		}
		private function onRender(cell:Box, index:int):void 
		{
			//如果索引不再可索引范围，则终止该函数
			if(index > this.data.length)return;
			//获取当前渲染条目的数据
			var data:Object=this.data[index];
			var rank:Image=cell.getChildByName("rank") as Image;
			if(index<3){
				rank.visible=true;
				rank.skin="hall/hallRank"+(index+1)+".png"
			}else{
				rank.visible=false;
			}
			//根据子节点的名字listNumber，获取子节点对象。   
			var scoreText:Label=cell.getChildByName("onplayScore") as Label;
			scoreText.font=data.score>0?TextManager.NumberRedFont:TextManager.NumberLvFont;
			scoreText.text=data.score>0?"+"+data.score:data.score;  
			//scoreText.color=data.score<0?"#72fd0a":data.score==0?"#ffffff":"#fd0400";
			
			var playerText:Label=cell.getChildByName("onplayerName") as Label;
			playerText.text=data.player;
//			trace(cell._childs[0]._childs[0]._childs[0])
			var headerIMG:Image=cell.getChildByName("headImg") as Image;
			cell._childs[1]._childs[1]._childs[0].skin=data.headimg==""?"common/morentouxiang.png":data.headimg;
		}
		private var timeDate:String;
		private var gameType:String;
		public override function show():void
		{
			super.show();
			if(_skin)
			{
				container.addChild(_skin);
			}
		}
		
		public function showInit():void
		{
//			trace(_timeDate,_gameType)
//			this.timeDate=_timeDate;
//			this.gameType=_gameType;
			this.show();
		}
		
		public override function hide():void
		{
			super.hide();
			if(_skin && _skin.parent)
			{
				_skin.parent.removeChild(_skin);
			}
		}
	}
}