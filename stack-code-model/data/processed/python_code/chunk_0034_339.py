package modules.game.majiangGame.view
{
	import common.CommonModule;
	import common.event.EventCenter;
	import common.tools.SoundPlay;
	
	import laya.events.Event;
	import laya.ui.Image;
	
	import manager.TimeManager;
	
	import modules.game.GameModule;
	import modules.game.majiangGame.model.MajiangModel;
	
	import net.Message;
	import net.ProtoMessage;
	
	import ui.mainGame.TableInfoPageUI;

	/**桌子相关信息*/
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
			_skin.option.on(Event.CLICK,this,onClickSetBtn);
			_skin.scoreList.on(Event.CLICK,this,onClickScoreListBtn)
			_skin.infoListBtn.on(Event.CLICK,this,onClickInfoListBtn);
			
			
			
			EventCenter.instance.on(EventCenter.COMMON_INFOLIST_NOTICE,this,onGotInfo);
			
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
		
		protected function onGotInfo(info:Object):void
		{
			_infosimbol.visible = true;
		}
		
		
		public function updateRoomId():void
		{
			if(Number(_skin.roomNumTf.text) != UserData.roomid)
			{
				_skin.roomNumTf.text = "" + UserData.roomid;//让房间号显示出来
			}
			
			updateTime();
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
				
		protected function onClickSetBtn(e:Event):void
		{
			e.stopPropagation();
			SoundPlay.instance.playClickBtnSound();
			CommonModule.instance.commonContext.view.functionOption.showOrHide(-350,0);
		} 
		
		protected function onClickInfoListBtn(e:Event):void
		{
			_infosimbol.visible = false; 
			SoundPlay.instance.playClickBtnSound();
			CommonModule.instance.commonContext.view.infoListView.showOrHide();
			e.stopPropagation();
		}
		
		protected function updateTime():void
		{
			var date:Date = TimeManager.instance.date;
			var hours:Number = date.getHours();
			var mins:Number = date.getMinutes();

			var fengquan:String="";
			
			if(model.fengquan == 0)
			{
				fengquan = "东风圈";
			}
			else if(model.fengquan == 1)
			{
				fengquan = "南风圈";
			}
			else if(model.fengquan == 2)
			{
				fengquan = "西风圈";
			}
			else if(model.fengquan == 3)
			{
				fengquan = "北风圈";
			}
			_skin.fengquanTf.text=fengquan;
			_skin.difenTf.text = ""+1;
		}
		
		public function updateLeftRound(needTongbu:Boolean=true):void
		{
			var info:Object = model.majiangMsgs.ACK_RoomInfo;
			var rule:Array = info.Rule;
			var obj:Object = AppConfig.getRule(rule[1]);
			
			
			//disbandLeftTime
			
			GameModule.instance.gameContext.view.majiangPage.clockPart.showLeftRoundsNum();
			
			if(obj.type == 0)//局数
			{
				info.totalRound = obj.value;
				if(info.RoundCount+1 > obj.value)
				{
					_skin.leftTf.text = "当前" + (info.RoundCount + "/" + obj.value) + "局";
				}
				else
				{
					_skin.leftTf.text = "当前" + (info.RoundCount+1 + "/" + obj.value) + "局";
				}
				
				_skin.ruleTimeTf.text = "本局局数：" + obj.value +"局";
			}
			else
			{
				_skin.ruleTimeTf.text = "本局时长：" + obj.value +"分钟";
				if(model.isGameStart == true || info.RoundCount >= 1)//需要立即开始倒计时
				{
					startCutdown();
				}
				else
				{
					info.leftTime = obj.value*60;
					stopCutDown();
				}
				
				if(needTongbu)
				{
					UserData.leftTime = info.leftTime;
				}
				
				if(UserData.leftTime < 0)
				{
					UserData.leftTime = 0;
				}
				_skin.leftTf.text = AppConfig.getTFmt(UserData.leftTime);
				
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
		
		
		/**时间倒计时*/
		private function startCutdown():void
		{
			EventCenter.instance.on(EventCenter.ON_LITTLETIMEER,this,onCutDown);
		}
		
		/**停掉倒计时*/
		private  function stopCutDown():void
		{
			EventCenter.instance.off(EventCenter.ON_LITTLETIMEER,this,onCutDown);
		}
		
		public function onCutDown(dat:int):void
		{
			UserData.leftTime -= dat;
			if(UserData.leftTime < 0)
			{
				UserData.leftTime = 0;
				stopCutDown();
			}
			
			_skin.leftTf.text = AppConfig.getTFmt(UserData.leftTime);
			
			 
		}
		
	
		protected function get model():MajiangModel
		{
			return GameModule.instance.gameContext.model;
		}
		
		public function reset():void
		{
			
		}
	}
}