package modules.srddzGame.srddzInerGame.view.pockerPart
{
	import common.tools.SoundPlay;
	
	import laya.events.Event;
	
	import modules.srddzGame.SrddzGameModule;
	import modules.srddzGame.srddzInerGame.controller.SrddzController;
	import modules.srddzGame.srddzInerGame.model.SrddzModel;
	import modules.srddzGame.srddzInerGame.model.data.JishuArrData;
	import modules.srddzGame.srddzInerGame.model.data.PaixingLogic;
	import modules.srddzGame.srddzInerGame.view.SrddzView;
	import modules.srddzGame.srddzInerGame.view.pockerPart.card.BasePocker;
	
	import net.Message;
	import net.ProtoMessage;
	
	import ui.srddzGame.ddzPart.PlayerCtlPartUI;

	public class HandleBtnsPart
	{
		protected var singleBtnW:Number = 183;
		protected var gap:Number = 20;
		
		protected var _skin:PlayerCtlPartUI;
		
		protected var state:int = -1;
		
		public function HandleBtnsPart(skin:PlayerCtlPartUI)
		{
			_skin = skin;
			
			init();
		}
		
		protected function init():void
		{
			addListener();
		}
		
		
		
		protected function get model():SrddzModel
		{
			return SrddzGameModule.instance.gameContext.model;
		}
		
		protected function get controller():SrddzController
		{
			return SrddzGameModule.instance.gameContext.controller;
		}
		
		protected function get view():SrddzView
		{
			return SrddzGameModule.instance.gameContext.view;
		}
		
		protected function resetBox():void
		{
			_skin.jiaofenBox.visible = false;
			_skin.baodaoBox.visible = false;
			_skin.wayBox.visible = false;
			_skin.ctlBox.visible = false;
			_skin.jiabeiBox.visible = false;
		}
		
		/**显示叫地主（暂时只有叫分）*/
		public function showJiaodizhu():void
		{
			if(model.isSelfSitDown == false)
			{
				return;
			}
			resetBox();
			_skin.jiaofenBox.visible = true;
			
			var num:int = 0;
			_skin.fen0Btn.visible = true;
			num +=1;
			
			if(model.srddzMsgs.ACK_RoomInfo.Rule[3] == 102)
			{
				_skin.fen1Btn.visible = model.difen==0;
				if(_skin.fen1Btn.visible)
				{
					_skin.fen1Btn.x = (singleBtnW+gap)*num;
					num +=1;
				}
			}

			_skin.fen2Btn.visible = model.difen <= 1;
			if(_skin.fen2Btn.visible)
			{
				_skin.fen2Btn.x = (singleBtnW+gap)*num;
				num += 1;
			}
			_skin.fen3Btn.visible = model.difen <= 2;
			if(_skin.fen3Btn.visible)
			{
				_skin.fen3Btn.x = (singleBtnW+gap)*num;
				num +=1;
			}
			_skin.jiaofenBox.x =(singleBtnW+gap)*(4-num)/2;
			
			if(AppConfig.autoPlay)//自动打牌
			{
				Laya.timer.once(AppConfig.autoPlayDelay,this,onClickFenBtn,[3]);
			}
			
			
		}
		
		/**显示加倍*/
		public function showjiabei():void
		{
			if(model.isSelfSitDown == false)
			{
				return;
			} 
			

			resetBox();
			_skin.jiabeiBox.visible = true;
			
			var num:int = 0;
			
			_skin.jiabeiBtn.visible = true;
			num+=1;
			_skin.bujiaBtn.visible = true;
			_skin.bujiaBtn.x = (singleBtnW+gap)*num;
			num += 1;
			_skin.jiabeiBox.x =(singleBtnW+gap)*(4-num)/2;
			
			if(AppConfig.autoPlay){
				
				Laya.timer.once(AppConfig.autoPlayDelay,this,onClickJiaBtn,[false]);
			}
		}
		
		/**显示报到*/
		public function showBaodao(baodaoNum:int):void
		{
			if(model.isSelfSitDown == false)
			{
				return;
			} 
			resetBox();
			_skin.baodaoBox.visible = true;
			
			var num:int = 0;
			
			if(baodaoNum >= 1)
			{
				_skin.baoBtn.visible = true;
				_skin.baoBtn.x = (singleBtnW+gap)*num;
				num+=1;
				
			}
			
			_skin.notbaoBtn.visible = true;
			_skin.notbaoBtn.x = (singleBtnW+gap)*num;
			num+=1;
			_skin.baodaoBox.x = (singleBtnW+gap)*(4-num)/2;
			
			if(AppConfig.autoPlay){
				Laya.timer.once(AppConfig.autoPlayDelay,this,onClickBaoBtn,[0]);
			}
			
		}
		
		/**显示报到后选择哪种赢*/
		public function showWay():void
		{
			if(model.isSelfSitDown == false)
			{
				return;
			} 
			resetBox();
			_skin.wayBox.visible = true;
			var num:int = 0;
			
			_skin.normalBtn.visible = true;
			num+=1;
			_skin.directBtn.visible = true;
			num+=1;
			_skin.wayBox.x = (singleBtnW+gap)*(4-num)/2;
			
			if(AppConfig.autoPlay){
				Laya.timer.once(AppConfig.autoPlayDelay,this,onClickWayBtn,[false]);
			}
			
		}
		
		/**要不起按钮后面再加上去*/
		public function showCtlBtns():void
		{
			if(model.isSelfSitDown == false)
			{
				return;
			}
			
			resetBox();
			_skin.ctlBox.visible = true;
			
			var num:int = 0;
			
			_skin.mingpaiBtn.visible = false;
			if(model.curOutputPos == -1 && model.dizhuPos == model.selfChairPos && model.mingpaiVec[model.selfChairPos] == false)//当前没有人出过牌并且自己是地主
			{
				_skin.mingpaiBtn.visible = true;
				num += 1;
			}
			
			_skin.buchuBtn.visible = false;
			_skin.tishiBtn.visible = false;
			_skin.chupaiBtn.visible = false;
			_skin.buqiBtn.visible = false;
			
			if(model.curOutputPos != -1 && model.curOutputPos != model.selfChairPos)//当前有人出过牌兵并且不是自己
			{
				//如果要得起
				var cards:Array = PaixingLogic.getBigThan(model.handleCards[model.selfChairPos],model.curOutputCards);
				if(cards.length > 0)
				{
					_skin.buchuBtn.visible = true;
					_skin.buchuBtn.x =  (singleBtnW+gap)*num;
					num += 1;
					
					_skin.tishiBtn.visible = true;
					_skin.tishiBtn.x = (singleBtnW+gap)*num;
					num += 1;
					
					_skin.chupaiBtn.visible = true;
					_skin.chupaiBtn.x =  (singleBtnW+gap)*num;
					num += 1;
					
					if(AppConfig.autoPlay){
						
						
						Laya.timer.once(AppConfig.autoPlayDelay,null,function (cards:Array):void{
							var paixing:int = PaixingLogic.getPaixing(cards);
							var chupaiObj:Object = {Sid:UserData.SID,Type:paixing,Cards:cards};
							controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Sddz_Chupai,chupaiObj));
						},[cards]);
						reset();
					}
				}
				else
				{
					_skin.buqiBtn.visible = true;
					_skin.buqiBtn.x =  (singleBtnW+gap)*num;
					num += 1;
					
					if(AppConfig.autoPlay){
						if(_skin.buqiBtn.visible)
						{
							onClickBuchuBtn();
						}	
					}
				}
			}
			else
			{
				_skin.chupaiBtn.visible = true;
				_skin.chupaiBtn.x =  (singleBtnW+gap)*num;
				num += 1;
				
				if(AppConfig.autoPlay)
				{
					var card:int = model.handleCards[model.selfChairPos][0];
					
					Laya.timer.once(AppConfig.autoPlayDelay,null,function (card:int):void{
						var paixing:int = BasePocker.PAIXING_DAN;
						var chupaiObj:Object = {Sid:UserData.SID,Type:paixing,Cards:[card]};
						controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Sddz_Chupai,chupaiObj));
					},[card]);
					
					reset();
				}
			}
			
			_skin.ctlBox.x =(singleBtnW+gap)*(4-num)/2; 
			
			
			
		}
		
		protected function addListener():void
		{
			_skin.fen0Btn.on(Event.CLICK,this,onClickFenBtn,[-1]);
			_skin.fen1Btn.on(Event.CLICK,this,onClickFenBtn,[1]);
			_skin.fen2Btn.on(Event.CLICK,this,onClickFenBtn,[2]);
			_skin.fen3Btn.on(Event.CLICK,this,onClickFenBtn,[3]);
			
			_skin.jiabeiBtn.on(Event.CLICK,this,onClickJiaBtn,[true]);
			_skin.bujiaBtn.on(Event.CLICK,this,onClickJiaBtn,[false]);
			
			_skin.mingpaiBtn.on(Event.CLICK,this,onClickMingBtn);
			_skin.buchuBtn.on(Event.CLICK,this,onClickBuchuBtn);
			_skin.tishiBtn.on(Event.CLICK,this,onClickTishiBtn);
			_skin.chupaiBtn.on(Event.CLICK,this,onClickChupaiBtn);
			_skin.buqiBtn.on(Event.CLICK,this,onClickBuchuBtn); 
			
			//报到
			_skin.baoBtn.on(Event.CLICK,this,onClickBaoBtn,[1]);
			_skin.notbaoBtn.on(Event.CLICK,this,onClickBaoBtn,[0]);
			
			//报到之后选择赢的方式
			_skin.normalBtn.on(Event.CLICK,this,onClickWayBtn,[0]);
			_skin.directBtn.on(Event.CLICK,this,onClickWayBtn,[1]);
			
		}
		
		/**报到相关*/
		protected function onClickBaoBtn(baodao:int,e:Event=null):void
		{
			switch(baodao)
			{
				case 0: // 不报到
					var jiaofenObj:Object = {Sid:UserData.SID,BaodaoNum:0,Cards:[]};
					var jiaofenObj:Object = {Sid:UserData.SID,BaodaoNum:baodaoNum,Cards:baodaoCards};
					controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Srddz_Baodao,jiaofenObj));
					break;
				case 1://报到
					//选择报到的牌 
					var baodaoNum:int =   model.getBaodaoNum();
					var baodaoCards:Array = model.getBaodaoCards();
					var jiaofenObj:Object = {Sid:UserData.SID,BaodaoNum:baodaoNum,Cards:baodaoCards};
					controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Srddz_Baodao,jiaofenObj));
					
					break;
			}
			reset();
		}
		
		/***/
		protected function onClickWayBtn(strict:int,e:Event=null):void
		{
			var isStrictWin:Boolean = false;
			if(strict == 0)//正常打
			{
				isStrictWin = false;
			}
			else if(strict == 1)//直接赢
			{
				isStrictWin = true;
			}
			
			var strictWinObj:Object = {Sid:UserData.SID,IsStrictWin:isStrictWin};
			controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Srddz_StrictWin,strictWinObj));
			
			reset();
		}
		
		
		/**叫分相关*/
		protected function onClickFenBtn(fen:int,e:Event=null):void
		{
			var jiaofenObj:Object = {Sid:UserData.SID,Fen:fen};
			controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Sddz_Jiaofen,jiaofenObj));
			
			reset();
		}
		
		protected function onClickJiaBtn(jiabei:Boolean,e:Event):void
		{
			var jiabeiObj:Object = {Sid:UserData.SID,Jiabei:jiabei};
			controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Sddz_Jiabei,jiabeiObj));
			
			reset();
		}
		
		protected function onClickMingBtn(e:Event):void
		{
			var mingObj:Object = {Sid:UserData.SID};
			controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Sddz_Mingpai,mingObj));
			_skin.mingpaiBtn.visible = false;//单独隐藏明牌按钮
		}
		
		protected function onClickBuchuBtn(e:Event=null):void
		{
			var passObj:Object = {Sid:UserData.SID};
			controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Sddz_Pass,passObj));
			view.srddzPage.handlePart.setSelfPockSele([]);
			reset();
		}
		
		protected function onClickTishiBtn(e:Event):void
		{
			e.stopPropagation();
			
			//把手里的牌拆成两份
			//先找没有报到牌
			var cards:Array ;
			
			if(model.baodaoState != 0 && model.dizhuPos == model.selfChairPos)
			{
				var handleCards:Array = model.handleCards[model.selfChairPos].concat();
				PaixingLogic.cutArrInArr(model.baodaoCards,handleCards);
				
				//PaixingLogic. 
				cards = PaixingLogic.getBigThan(handleCards,model.curOutputCards);
				
				if(cards.length == 0)
				{
					 cards = PaixingLogic.getBigThanWBaodao(model.baodaoCards,model.curOutputCards);
				}
			}
			else
			{
				cards = PaixingLogic.getBigThan(model.handleCards[model.selfChairPos],model.curOutputCards);
			}
			
			if(cards.length > 0)
			{
				view.srddzPage.handlePart.setSelfPockSele(cards);
			}
			else
			{
				//onClickBuchuBtn();
			}
			
		}
		
		protected function onClickChupaiBtn(e:Event):void
		{
			var cards:Array = view.srddzPage.handlePart.getSelfSelePockers();
			if(cards.length == 0)
			{
				SoundPlay.playEffect("audio_warning");
				QuickUtils.popMessage("你的出牌不能为空");
			}
			
			var paixing:int = PaixingLogic.getPaixing(cards);
			
			if(paixing == BasePocker.PAIXING_NON)
			{
				SoundPlay.playEffect("audio_warning");
				QuickUtils.popMessage("你的牌型不合法");
				return;
			}
			
			if(paixing >= 8 && model.selfChairPos != model.dizhuPos)//炸弹和对王   不是地主要不要判断能不能出
			{
				var jiaofen:int = model.jiaofenVec[model.selfChairPos];
				var curOutZhaNum:int = model.outZhadanNumVec[model.selfChairPos];
				
				if((jiaofen == -1 || jiaofen == 1) && curOutZhaNum >= 1)
				{
					SoundPlay.playEffect("audio_warning");
					QuickUtils.popMessage("你选择了不叫，只能出一个炸弹");
					return;
				}
				else if (jiaofen == 2 && curOutZhaNum >= 2)
				{
					SoundPlay.playEffect("audio_warning");
					QuickUtils.popMessage("你选择了叫2分，只能出两个炸弹");
					return;
				}
			}
			
			if(model.baodaoState != 0 && model.dizhuPos == model.selfChairPos)//保证如果手里的牌有报到的牌，那么必须是一个整体
			{
				var valid:Boolean = true;
				
				var i:int;
				var idx:int;
				for(i=0;i<cards.length;i++)
				{
					idx = model.baodaoCards.indexOf(cards[i]);
					
					if(idx != -1)
					{
						var tempV:int = BasePocker.getV(cards[i])
						
						var bJishu:JishuArrData = JishuArrData.getJishuArrData(model.baodaoCards);
						
						if(bJishu.eightArr.indexOf(tempV) != -1)
						{
							if(cards.length == 8 && paixing == BasePocker.PAIXING_ZHADAN)//都在正好
							{
								valid = true;
							}
							else
							{
								valid = false;
							}
						}
						else if(bJishu.sevenArr.indexOf(tempV) != -1)
						{
							if(cards.length == 7 && paixing == BasePocker.PAIXING_ZHADAN)//都在正好
							{
								valid = true;
							}
							else
							{
								valid = false;
							}
						}
						else if(paixing == BasePocker.PAIXING_TIANZHA)//天王炸弹
						{
							valid = true;
						}
						else
						{
							valid = false;
						}
						break;
					}
				}
				
				if(valid == false)
				{
					SoundPlay.playEffect("audio_warning");
					QuickUtils.popMessage("报到的牌必须要一起出");
					return;
				}
				
			
			}
			
			
			var chupaiObj:Object;
			if(model.curOutputCards.length == 0 || model.curOutputPos == model.selfChairPos)//
			{
				chupaiObj = {Sid:UserData.SID,Type:paixing,Cards:cards};
				controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Sddz_Chupai,chupaiObj));
				
				reset();
			}
			else
			{
				var retArr:Array = PaixingLogic.getBigThan(cards,model.curOutputCards);
				
				if(paixing == BasePocker.PAIXING_TIANZHA || paixing == BasePocker.PAIXING_ZHADAN)
				{
					if(retArr.length > 0)
					{
						chupaiObj = {Sid:UserData.SID,Type:paixing,Cards:cards};
						controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Sddz_Chupai,chupaiObj));
						reset();
					}
				}	
				else if(retArr.length == cards.length)//所选的牌组成的牌型正好可以大过
				{
					chupaiObj = {Sid:UserData.SID,Type:paixing,Cards:cards};
					
					controller.sendMsgCommond(ProtoMessage.getProtoMessage(Message.Sddz_Chupai,chupaiObj));
					
					reset();
				}
				else
				{
					SoundPlay.playEffect("audio_warning");
					QuickUtils.popMessage("你的出牌不能大于当前牌");
				}
			}
			
			
			
			
		}
		
		public function show():void
		{
			_skin.visible = true;
		}
		
		public function hide():void
		{
			_skin.visible = false;
		}
		
		public function get visible():Boolean
		{
			return _skin.visible;
		}
		
		public function reset():void
		{
			resetBox();
		}
		
	}
}