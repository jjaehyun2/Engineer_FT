package modules.game.majiangGame.view.majiangPart
{
	import common.view.PopBox;
	
	import laya.events.Event;
	
	import modules.game.GameModule;
	import modules.game.majiangGame.controller.MajiangGameController;
	import modules.game.majiangGame.model.MajiangModel;
	import modules.game.majiangGame.view.MajiangGameView;
	import modules.game.majiangGame.view.card.BaseCard;
	
	import net.Message;
	import net.ProtoMessage;
	
	import ui.mainGame.majiangParts.HandleBtnsPartUI;

	public class HandleBtnsPart
	{
		protected var _skin:HandleBtnsPartUI;
		
		protected var _skinOrignalX:int = 0;
		protected var _singleW:int  = 0;
		
		public function HandleBtnsPart(skin:HandleBtnsPartUI)
		{
			_skin = skin;
			
			_singleW = _skin.pengBtn.width+2;
			_skinOrignalX = _skin.x;
			add();
			
			show();
			reset();
		}
		
		public function show():void
		{
			_skin.visible = true;
		}
		
		public function hide():void
		{
			_skin.visible = false;
		}	
		
		protected function add():void
		{
			_skin.chiBtn.on(Event.CLICK,this,onClickChiBtn);
			_skin.pengBtn.on(Event.CLICK,this,onClickPengBtn);
			_skin.gangBtn.on(Event.CLICK,this,onClickGangBtn);
			_skin.huBtn.on(Event.CLICK,this,onClickHuBtn);
			_skin.cancelBtn.on(Event.CLICK,this,onClickCancelBtn);//过
			_skin.tingBtn.on(Event.CLICK,this,onClickTingBtn);
			_skin.kouBtn.on(Event.CLICK,this,onClickKouBtn);
		}
		
		protected var isZimo:Boolean = false;
		
//		public function showhuQiangGangHu():void
//		{
//			show();
//			var opration:int = 32;
//			
//			_skin.chiBtn.visible = false;
//			_skin.pengBtn.visible = false;
//			_skin.gangBtn.visible = false;
//			_skin.huBtn.visible = false;
//			_skin.kouBtn.visible = false;
//			_skin.tingBtn.visible = false;
//			_skin.cancelBtn.visible = true;
//			
//			var idx:int = 0;
//			
//			if(opration&2)
//			{
//				_skin.chiBtn.visible = true;
//				_skin.chiBtn.x = idx*_singleW;
//				idx ++;
//			}
//			
//			if(opration&4)//碰
//			{
//				_skin.pengBtn.visible = true;
//				
//				_skin.pengBtn.x = idx*_singleW;
//				idx ++;
//			}
//			
//			if(opration&8)//杠
//			{
//				_skin.gangBtn.visible = true;
//				
//				_skin.gangBtn.x = idx*_singleW;
//				idx ++;
//				
//			}
//			
//			if(opration&16)//听（16），
//			{
//				_skin.tingBtn.visible = true;
//				
//				_skin.tingBtn.x = idx*_singleW;
//				idx ++;
//			}
//			
//			if(opration&32)//胡（32），
//			{
//				isZimo = false;
//				_skin.huBtn.visible = true;
//				
//				_skin.huBtn.x = idx*_singleW;
//				idx ++;
//			}
//			
//			if(opration&64)//自摸（64），
//			{
//				isZimo = true;
//				_skin.huBtn.visible = true;
//				
//				_skin.huBtn.x = idx*_singleW;
//				idx ++;
//			}
//			
//			_skin.cancelBtn.x = idx*_singleW;
//			
//			_skin.x = _skinOrignalX - (idx+1)*_singleW/2;
//			
//			onClickCancelBtn();
//		}
		
		/**Type */
		protected function parseOpration(type:Array):int
		{
			var opration:int = 0;
			if(type[0] > 0) //hu
			{
				opration += 32; 
			}
			
			if(type[1] > 0) //gang
			{
				opration += 8;
			}
			
			if(type[2] > 0)//peng
			{
				opration += 4;
			}
			
			if(type[3] > 0)//chi
			{
				opration += 2;
			}
			
			return opration;
		}
		
		
		public function showBtnList(Type:Array=null):void
		{
			show();
			var opration:int;
			if(Type == null)
			{
				var info:Object = model.majiangMsgs.ACK_WaitTool;//control_game_mjopration_Info;
				opration = parseOpration(info.Type);
			}
			else
			{
				opration = parseOpration(Type);
			}
			
						
			_skin.chiBtn.visible = false;
			_skin.pengBtn.visible = false;
			_skin.gangBtn.visible = false;
			_skin.huBtn.visible = false;
			_skin.kouBtn.visible = false;
			_skin.tingBtn.visible = false;
			_skin.cancelBtn.visible = true;

			var idx:int = 0;
			if(opration&2)
			{
				_skin.chiBtn.visible = true;
				_skin.chiBtn.x = idx*_singleW;
				idx ++;
			}
			
			if(opration&4)//碰
			{
				_skin.pengBtn.visible = true;
				
				_skin.pengBtn.x = idx*_singleW;
				idx ++;
			}
			
			if(opration&8)//杠
			{
				_skin.gangBtn.visible = true;

				_skin.gangBtn.x = idx*_singleW;
				idx ++;

			}
			
			if(opration&16)//听（16），
			{
				_skin.tingBtn.visible = true;
				
				_skin.tingBtn.x = idx*_singleW;
				idx ++;
			}
			
			if(opration&32)//胡（32），
			{
				isZimo = false;
				_skin.huBtn.visible = true;
				
				_skin.huBtn.x = idx*_singleW;
				idx ++;
			}
			
			if(opration&64)//自摸（64），
			{
				isZimo = true;
				_skin.huBtn.visible = true;
				
				_skin.huBtn.x = idx*_singleW;
				idx ++;
			}
			
			_skin.cancelBtn.x = idx*_singleW;
			
			_skin.x = _skinOrignalX - idx*_singleW;
			
			if(model.curOutPutPos == (model.selfChairPos-1+4)%4)//当前出牌的玩家是我的上一家
			{
				if(model.checkHaveHua(model.selfChairPos) == true)
				{
					trace("玩家手里有花！！！");
					if(_skin.huBtn.visible != true)
					{
						reset();
					}
					return;
				}
			}
			
			if(AppConfig.autoPlay && model.isSelfSitDown)
			{
				if(AppConfig.autoDestory)
				{
					GameModule.instance.gameContext.controller.sendRandom();
				}
				
				
				if(_skin.huBtn.visible)
				{
					onClickHuBtn(null);
				}
				else if(_skin.gangBtn.visible)
				{
					if(model.getHuTipArr(-1).length > 0)
					{
						onClickCancelBtn(null);
					}
					else
					{
						onClickGangBtn(null);
					}
				
				}
				else if(_skin.pengBtn.visible)
				{
					if(model.getHuTipArr(-1).length > 0)
					{
						onClickCancelBtn(null);
					}
					else
					{
						onClickPengBtn(null);
					}
					
				}
				else if(_skin.chiBtn.visible)
				{
					if(model.getHuTipArr(-1).length > 0)
					{
						onClickCancelBtn(null);
					}
					else
					{
						onClickChiBtn(null);
					}
				}
				else
				{
					onClickCancelBtn(null);
				}
			}
		}
		
		public function showCanKouControll():void
		{
			show();
			_skin.chiBtn.visible = false;
			_skin.pengBtn.visible = false;
			_skin.gangBtn.visible = false;
			_skin.huBtn.visible = false;
			_skin.kouBtn.visible = true;
			_skin.tingBtn.visible = false;
			_skin.cancelBtn.visible = true;
			
			_skin.kouBtn.disabled = true;
			_skin.kouBtn.x = 0;
			_skin.cancelBtn.x = _singleW;
						
			_skin.x = _skinOrignalX - _singleW;
		}
		
		public function showCancelLp():void
		{
			show();
			_skin.chiBtn.visible = false;
			_skin.pengBtn.visible = false;
			_skin.gangBtn.visible = false;
			_skin.huBtn.visible = false;
			_skin.kouBtn.visible = false;
			_skin.tingBtn.visible = false;
			_skin.cancelBtn.visible = true;
			
			_skin.cancelBtn.x = 0;
			
			_skin.x = _skinOrignalX;
		}
		/**使扣的按钮能用*/
		public function showKouBtnEnable():void
		{
			_skin.kouBtn.disabled = false;
		}
		
		protected function onClickChiBtn(e:Event):void	
		{
			
			if(AppConfig.autoPlay)
			{
				onConFirmChi(0);
				
			}
			else
			{
				if(model.getChengbaoNumRefNum(model.selfChairPos,view.majiangPage.outputPart.getCurOutIdx()) == 2)
				{
					
					var str:String = model.warnCThenBaoipStr;
					
					QuickUtils.popMessageBox(str,PopBox.BTN_LABEL_QUEDINGQUXIAO,this,onConFirmChi,"提示","center",null,33);
				}
				else
				{
					onConFirmChi(0);
				}
			}
			reset();
			//bubian
		}
		
		protected function onConFirmChi(idx:int):void
		{
			if(idx == 0)
			{
				var cid1:int = view.majiangPage.outputPart.getCurOutputCardIdx();
				if(cid1 == 0)
					return;
				var cid2:int,cid3:int,defcid:int,cardIdx1:int,cardIdx2:int,chiCards:Array = [];
				
				var selfCards:Array = model.allCardsVec[model.selfChairPos].concat();
				var i:int,len:int = selfCards.length;
				
				//算左边的
				cardIdx1 = cid1-1;
				cardIdx2 = cid1-2;
				
				if(BaseCard.getTypeByCardIndex(cid1) == BaseCard.getTypeByCardIndex(cardIdx1) && BaseCard.getTypeByCardIndex(cid1) == BaseCard.getTypeByCardIndex(cardIdx2))//类型相同
				{
					if(selfCards.indexOf(cardIdx1) != -1 && selfCards.indexOf(cardIdx2) != -1)//表示全有
					{
						chiCards.push([cardIdx1,cardIdx2]);
					}
				}
				
				
				cardIdx1 = cid1-1;
				cardIdx2 = cid1+1;
				
				if(BaseCard.getTypeByCardIndex(cid1) == BaseCard.getTypeByCardIndex(cardIdx1) && BaseCard.getTypeByCardIndex(cid1) == BaseCard.getTypeByCardIndex(cardIdx2))//类型相同
				{
					if(selfCards.indexOf(cardIdx1) != -1 && selfCards.indexOf(cardIdx2) != -1)//表示全有
					{
						chiCards.push([cardIdx1,cardIdx2]);
					}
				}
				
				cardIdx1 = cid1+1;
				cardIdx2 = cid1+2;
				
				if(BaseCard.getTypeByCardIndex(cid1) == BaseCard.getTypeByCardIndex(cardIdx1) && BaseCard.getTypeByCardIndex(cid1) == BaseCard.getTypeByCardIndex(cardIdx2))//类型相同
				{
					if(selfCards.indexOf(cardIdx1) != -1 && selfCards.indexOf(cardIdx2) != -1)//表示全有
					{
						chiCards.push([cardIdx1,cardIdx2]);
					}
				}
				
				if(chiCards.length == 1 || AppConfig.autoPlay)
				{
					if(AppConfig.autoDestory)
					{
						GameModule.instance.gameContext.controller.sendRandom();
					}
					for(i=len-1;i<len;i--)
					{
						if(selfCards[i] != cardIdx1 && selfCards[i] != cardIdx2)
						{
							defcid = selfCards[i];
							break;
						}
					}
					
					var chiObj:Object = {SID:UserData.SID,CID1:cid1-1,CID2:chiCards[0][0]-1,CID3:chiCards[0][1]-1,DefCID:defcid-1};
					controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Chow,chiObj));
					reset();
				}
				else
				{
					view.majiangPage.chiSelePage.showCanChiCards(chiCards);
					reset();
				}
			}
			else
			{
				showBtnList();
				//onClickCancelBtn(null);
			}
		}
		
		
		protected function onClickPengBtn(e:Event):void	
		{
			if(AppConfig.autoPlay)
			{
				onConFirmPeng(0);
				
			}
			else
			{
				if(model.getChengbaoNumRefNum(model.selfChairPos,view.majiangPage.outputPart.getCurOutIdx()) == 2)
				{
					
					var str:String = model.warnCThenBaoipStr;
					
					QuickUtils.popMessageBox(str,PopBox.BTN_LABEL_QUEDINGQUXIAO,this,onConFirmPeng,"提示","center",null,33);
				}
				else
				{
					onConFirmPeng(0);
				}
			}
			
			reset();
		}
		
		private function onConFirmPeng(idx:int):void
		{
			if(idx == 0)
			{
				var cardIdx:int = view.majiangPage.outputPart.getCurOutputCardIdx();
				if(cardIdx == 0)
				{
					return;
				}
				var defcardIdx:int;
				var selfCards:Array = model.allCardsVec[model.selfChairPos].concat();
				var i:int,len:int = selfCards.length;
				for(i=len-1;i<len;i--)
				{
					if(selfCards[i] != cardIdx)
					{
						defcardIdx = selfCards[i];
						break;
					}
				}
				
				var pengObj:Object = {SID:UserData.SID,CID:cardIdx-1,DefCID:defcardIdx-1};
				controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Peng,pengObj));
			}
			else
			{
				showBtnList();
				//onClickCancelBtn(null);
			}
		}
		
		protected function compareFunction(A:int,B:int):int
		{
			if(A<B)
			{
				return -1;
			}
			else if(A==B)
			{
				return 0;
			}
			else
			{
				return 1;
			}
		}
		
		
		protected function onClickGangBtn(e:Event):void	
		{
			//			message Kong {
			//				string SID  = 1;
			//				int32 CID  = 2; 
			//			}
			
			model.tempGangCards = [];
			var allCards:Array = model.allCardsVec[model.selfChairPos];//.concat(model.theFourteenCardVec[model.selfChairPos]);
			if(model.theFourteenCardVec[model.selfChairPos] != -1)
			{
				allCards = allCards.concat(model.theFourteenCardVec[model.selfChairPos]);
			}
				
			var i:int,len:int=allCards.length;
			allCards.sort(compareFunction);
			
			if(model.theFourteenCardVec[model.selfChairPos] != -1 || allCards.length%3==2)//可以补杠   暗杠   60明  70暗  80补
			{
				//先来判断暗杠
				for(i=0;i<len;i++)//暗杠
				{
					if(allCards[i] == allCards[i+1] && allCards[i+1] == allCards[i+2] && allCards[i+2] == allCards[i+3])
					{
						model.tempGangCards.push({type:1,card:allCards[i]});
						i+=3;
					}
				}
				
				len = model.pengVec[model.selfChairPos].length;
				for(i=0;i<len;i++)//补杠
				{
					if(allCards.indexOf(model.pengVec[model.selfChairPos][i]) != -1)
					{
						trace("zhaodaole gang!!");
						model.tempGangCards.push({type:0,card:model.pengVec[model.selfChairPos][i]});
					}
				}
			}
			else//只有明杠
			{
				if(AppConfig.autoPlay)
				{
					onConFirmMingGang(0);
				}
				else
				{
					if(model.getChengbaoNumRefNum(model.selfChairPos,view.majiangPage.outputPart.getCurOutIdx()) == 2)
					{
						
						var str:String = model.warnCThenBaoipStr;
						
						QuickUtils.popMessageBox(str,PopBox.BTN_LABEL_QUEDINGQUXIAO,this,onConFirmMingGang,"提示","center",null,33);
					}
					else
					{
						onConFirmMingGang(0);
					}
				}
				
				reset();
				return;
				
			}
			
			if(model.tempGangCards.length == 1 || AppConfig.autoPlay)
			{
				var card:int = model.tempGangCards[0].card;
				var gangType:int  = model.tempGangCards[0].type;
				var gangObj:Object = {SID:UserData.SID,CID:card-1};
				controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Kong,gangObj));
				
			}
			else
			{
				//选择可以杠的牌
				model.isNextGang = true;
				view.majiangPage.handPart.showCanGangCards(model.tempGangCards);
				
				
				
			}
			reset();
		}
		
		protected function onConFirmMingGang(idx:int):void
		{
			if(idx == 0)
			{
				var cardIdx:int = view.majiangPage.outputPart.getCurOutputCardIdx();
				var allCards:Array = model.allCardsVec[model.selfChairPos].concat(model.theFourteenCardVec[model.selfChairPos]);
				var i:int=0;
				for(i=0;i<allCards.length;i++)
				{
					if(allCards[i] == allCards[i+1] && allCards[i+1] == allCards[i+2] && cardIdx == allCards[i])
					{
						model.tempGangCards.push({type:2,card:allCards[i]});
						break;
					}
				}
				
				if(model.tempGangCards.length == 1 || AppConfig.autoPlay)
				{
					var card:int = model.tempGangCards[0].card;
					var gangType:int  = model.tempGangCards[0].type;
					var gangObj:Object = {SID:UserData.SID,CID:card-1};
					controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Kong,gangObj));
					
				}
				else
				{
					//选择可以杠的牌
					model.isNextGang = true;
					view.majiangPage.handPart.showCanGangCards(model.tempGangCards);
				}
				
			}
			else
			{
				showBtnList();
				//onClickCancelBtn(null);
			}
		}
		
		protected function onClickHuBtn(e:Event):void	
		{
			
//			var obj:Object;
//			if(isZimo)
//			{
//				obj = {cmd:"ZIMO"};
//			}
//			else
//			{
//				obj = {cmd:"HULE"};
//				
//				//------------------------------------
////				//胡牌  MsgID : 320
////				message Win {
////					string SID = 1;
////					int32 CID = 2;
////				}
//				var card:int = view.majiangPage.outputPart.getCurOutputCardIdx()-1;
//				var huObj:Object = {SID:UserData.SID,CID:card};
//				trace(huObj,"-------------------------------");
//				controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Win,huObj));
//			}
			var card:int;
			if(model.theFourteenCardVec[model.selfChairPos] != -1)
			{
				card = model.theFourteenCardVec[model.selfChairPos]-1;
			}
			else
			{
				card = view.majiangPage.outputPart.getCurOutputCardIdx()-1;
			}
			
			if(card == -1)
			{
				card = model.lastHuanHuaCard-1;
			}
			
			
			var huObj:Object = {SID:UserData.SID,CID:card};
			trace(huObj,"-------------------------------");
			controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Win,huObj));
			
//			controller.sendMsgCommond(obj);
			
			reset();
		}
		
		protected function onClickCancelBtn(e:Event=null):void	
		{
			if(model.isNextCancelBtnKou)
			{
				model.tempKouCards.length = 0;
				
				if(model.koupaiwancheng)
				{
					model.isCancelTingp = false;
					showBtnList();
					view.majiangPage.handPart.showCancelKouCards();
					model.isNextCancelBtnKou = false;
					view.majiangPage.handPart.cancelTingpai();
					view.majiangPage.hideControlTip();
				}
				else
				{
					showCancelLp();
					model.isCancelTingp = true;
					
					//把扣掉的全都翻回来
					view.majiangPage.handPart.showCancelKouCards();
					view.majiangPage.handPart.showCanTingCards(model.tingCardsOfCancelBtn);
					
					model.isNextCancelBtnKou = false;
					view.majiangPage.hideControlTip();
					
				}
				
				model.koupaiwancheng = false;
				var obj1:Object = {cmd:"KPQX"};
				
				controller.sendMsgCommond(obj1,false);
				
				return;
			}
			else if(model.isCancelTingp)
			{
				model.isCancelTingp = false;
				view.majiangPage.handPart.cancelTingpai();
				showBtnList();
				return;
			}
			else
			{
				view.majiangPage.chiSelePage.hide();
				var passObj:Object = {SID:UserData.SID};
				controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Pass,passObj),false);
				
				if(AppConfig.autoPlay == true)
				{
					if(model.theFourteenCardVec[model.selfChairPos]!=-1)
					{
						var tempCard:Array = model.allCardsVec[model.selfChairPos].concat(model.theFourteenCardVec[model.selfChairPos]);
						if(tempCard.length%3 == 2)
						{
							controller.autoDiscard();
						}
					}
				}
				
//				var obj1:Object = {cmd:"PASS"};
//				controller.sendMsgCommond(obj1,false);
//				trace("send pass cmd");
////				SoundPlay.instance.playClickBtnSound();
			}
			
			
			reset();
		}
		
		protected function onClickTingBtn(e:Event):void
		{
			var arr:Array = model.majiangMsgs.control_game_mjopration_Info.nopercard as Array;
			
			trace("ting ..............");
			trace(model.majiangMsgs.control_game_mjopration_Info);
			trace("ting ..............");
			
			
			var tingCards:Array = new Array();
			var kouCards:Array = new Array();
			
			var card:int = 0;
			var gangType:int = 0;
			var i:int;
			var len:int = arr.length;
			for(i=0;i<len;i++)
			{
				if(arr[i].type == 1)//听
				{
					tingCards.push(arr[i].card);
					kouCards = kouCards.concat(arr[i].nkoucard);
				}
			}
			
			
			var rkouCards:Array = [];
			for(i=0;i<kouCards.length;i++)
			{
				rkouCards.push(kouCards[i].card);
			}
			
			
			model.tingCardsOfCancelBtn = tingCards;
			
			trace("tingCards ::" + tingCards);
			trace("kouCards ::" + kouCards.length);
			
			
			if(kouCards.length > 0)//有可以扣的牌
			{
				
				trace("kouCards :: " + kouCards);
				
				
				view.majiangPage.handPart.showCanKouCards(rkouCards);
				view.majiangPage.showControlTip("请选择要扣的牌");
				
				//下一次点击取消按钮是不是到听的操作
				model.isNextCancelBtnKou = true;
				
				view.majiangPage.handleBtns.showCanKouControll();
				return;
			}
			else
			{
				view.majiangPage.handPart.showCanTingCards(model.tingCardsOfCancelBtn);
				model.isCancelTingp = true;
				showCancelLp();
			}
			
			
			
		}
		
		private function onCancelTingPaiBtn(e:Event):void
		{
			view.majiangPage.handPart.cancelTingpai();
			showBtnList();
		}
		
		protected function onClickKouBtn(e:Event):void
		{
			view.majiangPage.handPart.showCanTingCards(model.tingCardsOfKouBtn);
			
			
			
			view.majiangPage.hideControlTip();
			//
			var obj:Object = {cmd:"KPWC"};
			controller.sendMsgCommond(obj,false);
			
			showCancelLp();
			model.isCancelTingp = true;
		}
		
		
		protected function remove():void
		{
			
		}
		
		protected function get model():MajiangModel
		{
			return GameModule.instance.gameContext.model;
		}
		
		protected function get controller():MajiangGameController
		{
			return GameModule.instance.gameContext.controller;
		}
		
		protected function get view():MajiangGameView
		{
			return GameModule.instance.gameContext.view;
		}
		
		public function reset():void
		{
			_skin.chiBtn.visible = false;
			_skin.pengBtn.visible = false;
			_skin.gangBtn.visible = false;
			_skin.huBtn.visible = false;
			_skin.kouBtn.visible = false;
			_skin.tingBtn.visible = false;
			_skin.cancelBtn.visible = false;

			isZimo = false;
			
			show();
		}
	}
}