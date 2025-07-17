package modules.sddzGame.sddzInerGame.view
{
	import common.CommonModule;
	import common.event.EventCenter;
	import common.tools.SoundPlay;
	
	import laya.events.Event;
	import laya.ui.Image;
	
	import modules.sddzGame.SDdzGameModule;
	import modules.sddzGame.sddzInerGame.model.SddzModel;
	
	import net.Message;
	import net.ProtoMessage;
	
	import ui.sddzGame.TableInfoPageUI;

	public class TableInfoPage
	{
		protected var _skin:TableInfoPageUI;
		protected var _PowerBarOrignalW:Number;
		protected var _infosimbol:Image;
		
		public function TableInfoPage(skin:TableInfoPageUI)
		{
			_skin = skin;
			_infosimbol = _skin.infoSImg;
			_infosimbol.visible = false;
			skin.mouseThrough = true;
			//_skin.option.on(Event.CLICK,this,onClickSetBtn);
			_skin.scoreList.on(Event.CLICK,this,onClickScoreListBtn)
			_skin.infoListBtn.on(Event.CLICK,this,onClickInfoListBtn);
			
			_skin.helpBtn.on(Event.CLICK,this,onClickHelpBtn);
			_skin.setBtn.on(Event.CLICK,this,onClickSetBtn);
			
			EventCenter.instance.on(EventCenter.COMMON_INFOLIST_NOTICE,this,onGotInfo);
		}
		
		protected function onClickHelpBtn(e:Event):void
		{
			CommonModule.instance.commonContext.view.vgameHelpView.show();
		}
		
		public function playVoicePlay():void
		{
			Laya.timer.frameLoop(1, this, onTimeLoop);
		}
		
		protected function onTimeLoop():void
		{
			if(_skin.voicePlay.rotation%360==0){
				_skin.voicePlay.rotation=0;
			}
			_skin.voicePlay.rotation+=10;
		}
		
		public function stopVoicePlay():void
		{
			Laya.timer.clear(this,onTimeLoop);
		}
		
		public function updateRoomId():void
		{
			if(Number(_skin.roomNumTf.text) != UserData.roomid)
			{
				_skin.roomNumTf.text = "" + UserData.roomid;//让房间号显示出来
			}
		}
		
		/**更新底分*/
		public function updateDifen():void
		{
			_skin.difenTf.text = "" + model.difen;
		}
		
		/**更新倍数*/
		public function updateBeishu():void
		{
			_skin.beishuTf.text = "" + model.beishu;
		}
		
		
		protected function onClickSetBtn(e:Event):void
		{
//			e.stopPropagation();
//			SoundPlay.instance.playClickBtnSound();
//			CommonModule.instance.commonContext.view.functionOption.showOrHide(-170,-190);
			CommonModule.instance.commonContext.view.settingView.showOrHide();
		} 
		
		private function onClickScoreListBtn(e:Event):void
		{
			var getRecord:Object = {
				"uniqueCode":UserData.uniqueCode
			};
			trace(UserData.roomid)
			EventCenter.instance.event(EventCenter.SOCKET_SEND,ProtoMessage.getProtoMessage(Message.MSG_Room_Summary,getRecord));
			SoundPlay.instance.playClickBtnSound();
			//GameModule.instance.gameContext.view.timeWar.showOrHide();
			CommonModule.instance.commonContext.view.timeWarView.showOrHide();
			e.stopPropagation();
		}
		
		protected function onClickInfoListBtn(e:Event):void
		{
			_infosimbol.visible = false; 
			SoundPlay.instance.playClickBtnSound();
			CommonModule.instance.commonContext.view.infoListView.showOrHide();
			e.stopPropagation();
		}
		
		protected function onGotInfo(info:Object):void
		{
			_infosimbol.visible = true;
		}
		
		public function updateLeftRound(needTongbu:Boolean=true):void
		{
			var info:Object = model.sddzMsgs.ACK_RoomInfo;
			var rule:Array = info.Rule;
			var obj:Object = AppConfig.getRule(rule[1]);
			
			//GameModule.instance.gameContext.view.majiangPage.clockPart.showLeftRoundsNum();
			if(obj.type == 0)//局数
			{
				info.totalRound = obj.value;
				if(info.RoundCount+1 > obj.value)
				{
					_skin.roundCountTf.text = "" + info.RoundCount + "/" + obj.value + "";
//					_skin.leftTf.text = "当前" + (info.RoundCount + "/" + obj.value) + "局";
				}
				else
				{
					_skin.roundCountTf.text = "" + (info.RoundCount+1) + "/" + obj.value + "";
					//_skin.leftTf.text = "当前" + (info.RoundCount+1 + "/" + obj.value) + "局";
				}
			}
			else
			{
				//暂时不要不管我的事情哦
			}
			
			if(model.isGameStart == true || info.RoundCount >= 1)//需要立即开始倒计时
			{
				_skin.weikaishiBox.visible = false;
			}
			else
			{
				UserData.leftDissolveTime = info.disbandLeftTime;
				_skin.leftDissolveTf.text = AppConfig.getTFmt(UserData.leftDissolveTime,true);
				_skin.weikaishiBox.visible = true;
				startDissolveCutdown();
			}
			
		}
		
		
		public function updateKaijuren(nickName:String):void
		{
			if(nickName == null || nickName == "")
			{
				nickName = "无";
			}
			_skin.kaijuTf.text = "开局人：" + nickName;
		}
		
		/**开始游戏之前开局倒计时*/
		private function startDissolveCutdown():void
		{
			EventCenter.instance.on(EventCenter.ON_LITTLETIMEER,this,onCutDown1);
		}
		
		/**开始游戏之后开局倒计时*/
		private function stopDissolveCutdown():void
		{
			EventCenter.instance.off(EventCenter.ON_LITTLETIMEER,this,onCutDown1);
		}
		
		private function onCutDown1(dat:int):void
		{
			UserData.leftDissolveTime -= dat;
			if(UserData.leftDissolveTime < 0)
			{
				UserData.leftDissolveTime = 0;
				stopDissolveCutdown();
			}
			_skin.leftDissolveTf.text = AppConfig.getTFmt(UserData.leftDissolveTime,true);
		}

		
		protected function get model():SddzModel
		{
			return SDdzGameModule.instance.gameContext.model;
		}
		
		public function reset():void
		{
			
		}
		
		
	}
}