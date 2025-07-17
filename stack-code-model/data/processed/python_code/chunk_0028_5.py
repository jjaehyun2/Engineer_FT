package modules.srddzGame.srddzInerGame.controller
{
	import common.CommonModule;
	import common.event.EventCenter;
	import common.tools.SoundPlay;
	import common.view.PopBox;
	
	import laya.media.SoundManager;
	
	import manager.MessageManager;
	import manager.UIManager;
	
	import modules.gameCommon.view.NewDissolvePage;
	import modules.srddzGame.SrddzGameModule;
	import modules.srddzGame.srddzInerGame.model.SrddzModel;
	import modules.srddzGame.srddzInerGame.model.data.FeijiData;
	import modules.srddzGame.srddzInerGame.model.data.JishuArrData;
	import modules.srddzGame.srddzInerGame.model.data.PaixingLogic;
	import modules.srddzGame.srddzInerGame.view.SrddzView;
	import modules.srddzGame.srddzInerGame.view.playerInfoPart.GiftEff;
	import modules.srddzGame.srddzInerGame.view.pockerPart.card.BasePocker;
	import modules.srddzGame.srddzInerGame.view.pockerPart.singlePart.BaseActTipItem;
	
	import net.Message;
	import net.ProtoMessage;
	
	import rb.framework.mvc.AbstractLayer;
	import rb.framework.mvc.core.LayerTypes;
	
	
	/**四人斗地主*/
	public class SrddzController extends AbstractLayer
	{
		public function SrddzController()
		{
			super();
			super.setType(LayerTypes.CONTROLLER);
		}
		
		//用来监听协议，从而刷新数据，并且通知界面更改
		override public function onAdd():void
		{
			super.onAdd();
			
		}
		
		//移除监听
		override public function onRemove():void
		{
			super.onRemove();
		}
		
		/**出牌*/
		public function discard(cards:Array):void
		{
			
		}
		
		/**房间信息*/
		public function ACK_RoomInfo(info:Object):void
		{
			//			message ACK_RoomInfo {
			//				required int32 ID   			= 1;
			//				optional int32 Type 			= 2;
			//				optional int32 City 			= 3;
			//				optional int32 Level     		= 4;
			//				optional int32 MinCoin  		= 5; 		//最小底分
			//				optional int32 MaxCoin  		= 6; 		//最大底分
			//				repeated int32 Rule   			= 7; 		//规则ID
			//				
			//				//---------------------------------------
			//				
			//				optional int32 Seat  		= 8;        // 座位数量
			//				optional int32 UserCount     = 9; 		// 用户数量
			//				optional int32 CurIndex      = 10;       // 当前出牌的用户
			//				optional int32 CurToolIndex  = 11;       // 当前操作用户
			//				optional int32 ZhuangIndex   = 12;       // 庄家的UID
			//				optional string MSG 			= 13;		// 
			//			}
			
			trace("ACK_Room_Info",info,"ACK_Room_Info");
			model.srddzMsgs.ACK_RoomInfo = info;
			
			model.roomOwnerUid = info.RoomOwner;
			
			UserData.uniqueCode=info.uniqueCode;
			UserData.roomtype = info.Type;
			UserData.Rule=info.Rule;
			if(UserData.isReplay)
			{
				UserData.roomid = info.RID;
			}
			
			trace(UserData.uniqueCode)
			
			if(info.gameState == 1)//走断线重连
			{
				model.isGameStart = true;
				view.playerInfoPage.hideBtnsByGameStart();
				view.playerInfoPage.hideReadySimbol();
			}
			view.playerInfoPage.updateLeaveDisbandBtns();
			
			
			if(UserData.isReplay)
			{
				model.srddzMsgs.ACK_RoomInfo.isGameStart = 1;//
			}
			
			view.tableInfoPage.updateLeftRound();
			view.tableInfoPage.updateKaijuren(info.nickName);
			if(!info.direction)
			{
				info.direction = 0;
			}
			
			view.tableInfoPage.updateRoomId();
			
			view.tableInfoPage.updateDifen();
			view.tableInfoPage.updateBeishu();
			view.tableInfoPage.updatePlayState();
			
			if(info.Rule[3] == 101)
			{
				UserData.needOneTwo = true;
			}
			else
			{
				UserData.needOneTwo = false;
			}
			
			//view.srddzPage.clockPart.setWenli(); xuyaobu
		}
		
		/**玩家信息*/
		public function ACK_Room_User(info:Object):void
		{
			//			message ACK_Room_User {
			//				required int32 RID   			= 1;
			//				repeated ACK_User_Info Users 	= 2;     // 房间用户信息, 按照Index顺序
			//			}
			
			trace("ACK_Room_User",info,"ACK_Room_User");
			model.srddzMsgs.ACK_Room_User = info;
			
			model.updatePlayerInfoVec(info.Users);
			view.playerInfoPage.updatePlayerInfos(model.playerInfoVec);
			
			
			if(model.isSelfSitDown == false && model.isGameStart == false)
			{
				for(var i:int=0;i<model.chairNum;i++)
				{
					if(model.playerByPos(i) == null)
					{
						var sitDownObj:Object = {sid:UserData.SID,index:i};
						sendMsgCommond(ProtoMessage.getProtoMessage(Message.MSG_Sitdown,sitDownObj));
						break;
					}
				}
			}
		}
		
		
		/**进入房间*/
		public function ACKBC_Into_Room(info:Object):void
		{
			trace("ACKBC_Into_Room");
			trace(info);
			trace("ACKBC_Into_Room"); 
			
			model.srddzMsgs.ACKBC_Into_Room = info;
			//UserData.roomtype = info.Type;
			
			UserData.roomid = info.RID;
			
			view.tableInfoPage.updateRoomId();//设置房间号显示
			
			info.nickname = info.Name;
			info.uid = info.UID;
			info.ip = info.IP;
			info.pos = info.Index;
			info.golds = info.Coin;
			
			model.updateOnePlayerInfo(info);//更新对比用户信息
			
			view.playerInfoPage.updateOnePlayerInfo(info);
			
			view.playerInfoPage.updateSitDownUpBtn();
			
			
			
			
			EventCenter.instance.event(EventCenter.COMMON_INFOLIST_NOTICE,{color:0,msg:"玩家["+info.nickname+"]进入了房间！"});
		}
		
		/**
		 * 坐下
		 * @param	info
		 */
		public function ACKBC_Sitdown(info:Object):void 
		{
			if (_actived) //判断当前模块是否打开
			{
				trace("MSG_ACKBC_Sitdown", info);
				model.srddzMsgs.ACKBC_Sitdown = info;
				model.sitDown(info.uid, info.index,info.score);
				
				view.playerInfoPage.updatePlayerInfos(model.playerInfoVec);
				
				view.playerInfoPage.updateSitDownUpBtn();
				
				view.tableInfoPage.updateKaijuren(info.nickName);
				
				if(info.uid == UserData.selfuid)
				{
					var readObj:Object = {sid:UserData.SID};
					sendMsgCommond(ProtoMessage.getProtoMessage(Message.User_Ready,readObj));
					EventCenter.instance.event(EventCenter.COMMON_INFOLIST_NOTICE,{color:0,msg:"玩家["+model.getPlayerNicknameByUid(info.uid)+"]坐下了"+info.index+"号座位！"});
				}
				
				if(view.calculatePage.perPage)
				{
					view.calculatePage.perPage.updateBtns();
				}
				
			}
		}
		
		/**
		 * 站起
		 * @param	info
		 */
		public function ACKBC_Standup(info:Object):void 
		{
			if (_actived) 
			{
				trace("MSG_ACKBC_Standup",info);
				model.srddzMsgs.ACKBC_Standup = info;
				model.standup(info.uid, info.index);
				
				view.playerInfoPage.updatePlayerInfos(model.playerInfoVec);
				view.playerInfoPage.updateSitDownUpBtn();
				view.playerInfoPage.updateStartBtn();
				view.tableInfoPage.updateKaijuren(info.nickName);
				if(view.calculatePage.perPage)
				{
					view.calculatePage.perPage.updateBtns();
				}
				
				
				EventCenter.instance.event(EventCenter.COMMON_INFOLIST_NOTICE,{color:0,msg:"玩家["+model.getPlayerNicknameByUid(info.uid)+"]站起了！"});
				
			}
		}
		
		
		/**玩家准备*/
		public function ACKBC_Ready(info:Object):void
		{
			if(actived)
			{
				//				message ACKBC_Ready {
				//					int32 ReadyCount  = 1; // 已经准备好的用户
				//					string UID        = 2; //  
				//					string MSG        = 3; // 
				//				}
				trace("ACKBC_Ready");
				
				trace(info);
				
				trace("ACKBC_Ready");
				
				if(model.isGameStart == true)
				{
					return;
				}
				
				SoundPlay.instance.playReadySound();
				model.srddzMsgs.ACKBC_Ready = info;
				//				GameModule.instance.majiangGameContext.majiangModel.majiangMsgs.control_game_operation_ready_Info = info;
				
				//				optional int32 uid =1 [default = 0];//用户ID
				//				optional int32 pos =2 [default = 0];//用户位置
				
				//重新设置游戏，准备新的一局
				info.uid = info.UID;
				info.pos = model.getPlayerPosByUid(info.uid);
				
				model.updateReadyState(info.pos,true,0);//info.piao
				
				view.playerInfoPage.updatePlayerInfos(model.playerInfoVec,false);
				
				if(info.pos == model.selfChairPos)
				{
					//					GameModule.inGame=true;
					//view.calculatePage.perPage.getPiaoSelePart().seleIdx(info.piao);
					
					view.playerInfoPage.hideReadyBtn();
					view.playerInfoPage.hideDizhuNM();
					trace("ready..........");
					
					view.calculatePage.reset();//影藏结算界面
					view.calculatePage.reset();//影藏结算界
					
					model.reset();
					view.srddzPage.reset();
				}
				
			}
		}
		
		/**通知第一个坐下的人*/
		public function NotifyStartGame(info:Object):void
		{
			if(actived)
			{
				trace("NotifyStartGame::" + info + "NotifyStartGame");
				model.srddzMsgs.NotifyStartGame = info;
				
				if(info.uid == UserData.selfuid)
				{
					view.playerInfoPage.showStartBtn();
				}
			}
		}
		
		/**开始*/
		public function ACKBC_Sddz_Start(info:Object):void
		{
			if(actived)
			{
				//				int32 RoundCount = 1; //当前已进行局数
				//				int32 TotalRoundCount = 2; //总局数
				//				int64 LeftTime = 3; //距离房间结束剩余秒数
				
				trace("ACKBC_Sddz_Start",info,"ACKBC_Sddz_Start");
				
				model.srddzMsgs.ACKBC_Sddz_Start = info;
				model.srddzMsgs.ACK_RoomInfo.RoundCount = info.RoundCount;
				resetSelf();
				model.isGameStart = true;
				
				view.startGame();
				view.playerInfoPage.hideReadySimbol();
				view.playerInfoPage.hideBtnsByGameStart();
				view.playerInfoPage.updateLeaveDisbandBtns();
				view.tableInfoPage.updateRoomId();
				view.tableInfoPage.updateLeftRound();
				view.tableInfoPage.updateDifen();
			}
		}
		
		/**游戏开始发牌*/
		public function ACK_User_SeatCard(info:Object):void
		{
			if(actived)
			{
				model.isClientPrePop = false;
				trace("ACK_User_SeatCard",info,"ACK_User_SeatCard");
				trace(model.srddzMsgs.ACKBC_Sddz_Start,"----------------------------------")
				model.srddzMsgs.ACK_User_SeatCard = info;
				
				model.resetCard();
				view.srddzPage.handlePart.reset();
				view.srddzPage.outputPart.reset();
				
				var i:int; 
				var j:int,k:int;
				var handleCards:Array = [];
				for(i=0;i<info.Cards.length;i++)
				{
					if(info.Cards[i].List.length != info.Cards[i].ListLen)
					{
						for(k=0;k<info.Cards[i].ListLen;k++)
						{
							info.Cards[i].List.push({CID:0});
						}
					}
					
					handleCards.length = 0;
					//更新玩家手里的牌
					for(j=0;j<info.Cards[i].List.length;j++)
					{
						handleCards.push(info.Cards[i].List[j].CID);
					}
					model.updateHandleCards(i,handleCards);
					view.srddzPage.handlePart.updateOnePosAllCards(i,model.handleCards[i]);
					
					//更新玩家已经打出去的牌
					if(info.Cards[i].Out)
					{
						//同步打出去的牌
						for(j=0;j<info.Cards[i].Out.length;j++)//同步打出去的牌
						{
							model.outputCards[i].push(info.Cards[i].Out[j].CID);//这个是记牌器用的
						}
					}
				}
				view.srddzPage.dipaiPart.showBack();
			}
			
		}
		
		/***/
		public function ACKBC_Sddz_Card_Init(info:Object):void
		{
			if(actived)
			{
				//				repeated int32 CurCards 	= 1;           // 当前打出的牌
				//				int32 CurIndex  			= 2;           // 当前用户(需要出牌的)
				//				int32 CurTime   			= 3;           // 当前回合时间
				//				int32 DizhuIndex  		    = 4;       	   // 地主Index
				//				int32 StartGame 			= 5;           // 是否已经开始 0=否 1=是
				//				int32 CurOutputIndex 		= 6; 		   // 当前出牌的玩家
				//				int32 Difen                  = 7;   //当前的底分
				//				repeated int32 Dipai  = 8; //当前的底牌 
				//				int32 Stage              = 9;//当前的阶段
				//				repeated bool HaveJiao = 10;//玩家是否叫过分
				//				repeated int32 JiaoFen = 11;//玩家的叫分
				//				repeated bool HaveJiabei = 12;//是否选择过加倍
				//				repeated bool IsJiabei =13;//是否加倍
				//				repeated bool IsMing = 14;//玩家是否明牌
				//Beishu
				
//				bool IsStrictWin = 23;
//				bool IsSeleBaodao =24;
//				bool IsSeleStrictWin = 25;
//				repeated int32 BaodaoCards = 26;//报到的牌
				
				trace("ACKBC_Sddz_Card_Init",info,"ACKBC_Sddz_Card_Init");
				
				model.srddzMsgs.ACKBC_Sddz_Card_Init = info;
				model.stage = info.Stage;
				
				model.difen = info.Difen;
				model.beishu = info.Beishu;
				model.isHuang = info.IsHuang== undefined ? false :  info.IsHuang;
				model.isTouliao = info.IsTouliao== undefined ? false :  info.IsTouliao;
				model.isMingW = info.IsMingW==undefined ? false : info.IsMingW;
				model.baodaoState = info.BaodaoState == undefined? 0 :info.BaodaoState;
				model.baodaoNum = info.BaodaoNum == undefined? 0 :info.BaodaoNum;
				model.isStrictWin = info.IsStrictWin == undefined? false :info.IsStrictWin;
				model.isSeleBaodao = info.IsSeleBaodao == undefined? false :info.IsSeleBaodao;
				model.isSeleStrictWin = info.IsSeleStrictWin == undefined? false :info.IsSeleStrictWin;
				model.baodaoCards =  info.BaodaoCards == undefined? [] :info.BaodaoCards;
				
		
				
				
				
				var i:int;
				for(i=0;i<model.chairNum;i++)
				{
					
					model.jiaofenVec[i] = info.JiaoFen[i];//玩家的叫分 -1 只能出一个炸弹 2 只能出两个炸弹
					model.outZhadanNumVec[i] = info.OutZhadan[i];
					
					if(model.stage == 1)
					{
						if(info.HaveJiao[i] == true)
						{
							view.srddzPage.actTipPart.showActTip(i,info.JiaoFen[i]);
						}
					}
					else
					{
						model.jiabeiVec[i] = info.IsJiabei[i];
						model.mingpaiVec[i] = info.IsMing[i];
						
						if(model.stage == 2)
						{
							if(info.HaveJiabei[i] == true)
							{
								if(info.IsJiabei[i] == true)
								{
									view.srddzPage.actTipPart.showActTip(i,BaseActTipItem.ACTTIP_JIABEI);
								}
								else
								{
									view.srddzPage.actTipPart.showActTip(i,BaseActTipItem.ACTTIP_BUJIABEI);
								}
							}
							else
							{
								if(model.isSelfSitDown && i == model.selfChairPos)
								{
									view.srddzPage.handleBtns.showjiabei();
									view.srddzPage.clockPart.showjiabei(10);
								}
							}
						}
						else if(model.stage == 3)
						{
							//							repeated int32 LastOpt = 16;//玩家最后的操作
							//							repeated SddzPerCards LastOptParam = 17;//玩家最后操作的参数
							
							if(info.LastOpt[i] == 1)//不出
							{
								view.srddzPage.actTipPart.showActTip(i,BaseActTipItem.ACTTIP_BUCHU);
							}
							else if(info.LastOpt[i] == 2)//出牌
							{
								view.srddzPage.outputPart.showCards(info.LastOptParam[i].Cards,i);
							}
						}
						
					}
					
				}
				
				if(model.stage == 2 || model.stage == 3)
				{
					model.dipaiCards = info.Dipai.concat();
					view.srddzPage.dipaiPart.showCards(model.dipaiCards);//底牌
					view.playerInfoPage.updateJiabei();//倍数
					model.dizhuPos = info. DizhuIndex;
					view.playerInfoPage.showDizhuNM();//地主农民图标
					view.srddzPage.handlePart.updateAllCards(model.handleCards);
					
					if(model.stage == 3)
					{
						model.curOutputPos = info.CurOutputIndex;
						if(model.curOutputPos >= 0)
						{
							model.curOutputCards = info.CurCards;
							view.srddzPage.outputPart.showCards(model.curOutputCards,model.curOutputPos);
						}
						
						view.srddzPage.clockPart.noticeShowClock(info.CurIndex,10);
						view.srddzPage.outputPart.hideCards(info.CurIndex);
					}
					
				}
				
				view.tableInfoPage.updateBeishu();
				view.tableInfoPage.updateDifen();
				view.tableInfoPage.updatePlayState();
				
				
				//				model.curOutputPos = info.CurOutputIndex;
				//				model.curOutputCards = info.CurCards;
				//				model.dizhuPos = info.DizhuIndex;
				//				
				//				model.isGameStart = info.StartGame;
				//				model.curHandlePos = info.CurIndex;
				//				model.difen = info.Difen;
				//				model.dipaiCards = info.Dipai;
				//				
				//				//界面相关 断线重连后面来补
				//				
				//				view.srddzPage.outputPart.showCards(model.curOutputCards,model.curOutputPos);
				
			}
		}
		
		/**通知玩家叫分*/
		public function ACKBC_Sddz_JiaoDizhu(info:Object):void
		{
			if(actived)
			{
				//				int32  Uid = 1;		//通知叫地主的玩家
				//				int32 CurFen = 2; //当前的叫分 玩家叫的分必须大于这个分
				
				trace("ACKBC_Sddz_JiaoDizhu",info,"ACKBC_Sddz_JiaoDizhu");
				model.srddzMsgs.ACKBC_Sddz_JiaoDizhu = info;
				
				var pos:int = model.getPlayerPosByUid(info.Uid);
				model.difen = info.CurFen;
				view.tableInfoPage.updateDifen();
				
				if(pos == model.selfChairPos)
				{
					view.srddzPage.handleBtns.showJiaodizhu();
				}
				view.srddzPage.clockPart.noticeShowClock(pos,10);
				
			}
		}
		
		/**叫分*/
		public function ACKBC_Sddz_Jiaofen(info:Object):void
		{
			if(actived)
			{
				//				int32  Uid = 1;		//UserID
				//				int32  Fen = 2;      //0分表示不叫
				
				trace("ACKBC_Sddz_Jiaofen",info,"ACKBC_Sddz_Jiaofen");
				model.srddzMsgs.ACKBC_Sddz_Jiaofen = info;
				var pos:int = model.getPlayerPosByUid(info.Uid);
				view.srddzPage.actTipPart.showActTip(pos,info.Fen);
				
				model.jiaofenVec[pos] = info.Fen;
				
				var soundFen:int = info.Fen;
				if(soundFen == -1)
				{
					soundFen = 0;
				}
				
				SoundManager.playSound("res/sounds/sddz/"+SoundPlay.instance.getSexRef(model.playerByPos(pos).sex)+"fen"+soundFen+".mp3");
				
				
				
				if(info.Fen > 0)//这个就是底分
				{
					model.difen = info.Fen;
					view.tableInfoPage.updateDifen();
				}
			}
		}
		
		/**通知地主是谁*/
		public function ACKBC_Sddz_Dizhu(info:Object):void
		{
			if(actived)//这个时候要给农民显示加倍按钮 地主选择加倍和明牌按钮 赢藏所有叫分按钮
			{
				//				int32  Uid = 1;		//地主
				//				int32  Fen = 2;      //分数
				//				bool Mingpai =3 ; //是否可以明牌，只有地主可以明牌
				//				bool Jiabei = 4;    //是否可以加倍  暂时都不可以加倍
				//				repeated int32 Dipai = 5 ;//底牌
				
				trace("ACKBC_Sddz_Dizhu",info,"ACKBC_Sddz_Dizhu");
				model.srddzMsgs.ACKBC_Sddz_Dizhu = info;
				
				var pos:int = model.getPlayerPosByUid(info.Uid);
				model.dizhuPos = pos;//确认地主的位置
				model.difen = info.Fen;
				
				view.srddzPage.actTipPart.hideAllActTip();//隐藏叫分相关按钮
				//view.srddzPage.handleBtns.showjiabei();//显示加倍明牌按钮
				
				
				view.playerInfoPage.showDizhuNM();//显示地主农民
				view.tableInfoPage.updateDifen();//更新底分
				
				model.addDipaiToHandleCards(model.dizhuPos,info.Dipai);//更新底牌，并且把底牌加给地主
				view.srddzPage.dipaiPart.showCards(model.dipaiCards);//显示底牌
				view.srddzPage.handlePart.updateOnePosAllCards(model.dizhuPos,model.handleCards[model.dizhuPos]);//更新地主手里的牌
				view.srddzPage.clockPart.showjiabei(10);
			}
		}
		
		/**通知玩家明牌*/
		public function ACKBC_Sddz_Mingpai(info:Object):void
		{
			if(actived)
			{
				//				int32  Uid = 1;		//明牌的玩家（特指地主可以明牌）
				//				bool Mingpai = 2;    //是否明牌
				//				repeated int32 Cards = 3;//明牌的玩家手里的牌
				
				trace("ACKBC_Sddz_Mingpai",info,"ACKBC_Sddz_Mingpai" );
				model.srddzMsgs.ACKBC_Sddz_Mingpai =info;
				
				var pos:int = model.getPlayerPosByUid(info.Uid);
				if(info.Mingpai == true)
				{
					model.beishu = model.beishu*2;
					model.updateMingpai(pos,info.Cards);
					view.srddzPage.handlePart.updateOnePosAllCards(pos,model.handleCards[pos]);//显示明牌 
					SoundManager.playSound("res/sounds/sddz/"+SoundPlay.instance.getSexRef(model.playerByPos(pos).sex)+"mingpai.mp3");
					
					view.tableInfoPage.updateBeishu();
					view.tableInfoPage.updatePlayState();
				}
			}
		}
		
		/**通知玩家加倍*/
		public function ACKBC_Sddz_Jiabei(info:Object):void
		{
			if(actived)
			{
				//				int32  Uid = 1;		//加倍的玩家（特指地主可以明牌）
				//				bool  Jiabei = 2;     //是否加倍
				
				trace("ACKBC_Sddz_Jiabei",info,"ACKBC_Sddz_Jiabei");
				model.srddzMsgs.ACKBC_Sddz_Jiabei = info;
				var pos:int = model.getPlayerPosByUid(info.Uid);
				
				if(info.Jiabei == true)
				{
					model.jiabeiVec[pos] = true;
					view.srddzPage.actTipPart.showActTip(pos,BaseActTipItem.ACTTIP_JIABEI);
					view.playerInfoPage.updateJiabei();
				
					
					SoundManager.playSound("res/sounds/sddz/"+SoundPlay.instance.getSexRef(model.playerByPos(pos).sex)+"jiabei.mp3");
					
				}
				else
				{
					model.jiabeiVec[pos] = false;
					view.srddzPage.actTipPart.showActTip(pos,BaseActTipItem.ACTTIP_BUJIABEI);
					SoundManager.playSound("res/sounds/sddz/"+SoundPlay.instance.getSexRef(model.playerByPos(pos).sex)+"bujiabei.mp3");
				}
			}
		}
		
		/**通知玩家出牌*/
		public function ACKBC_CurPlayer(info:Object):void
		{
			if(actived)
			{
				//				int32  	Seat   			= 1;  // 座位
				//				int32   	Type   			= 2;  // 操作类型
				//				repeated int32 		Tool   			= 3;  // 自摸, 暗杠,
				//				int32 		RoundTime  		= 4;  // 回合时间
				
				trace("ACKBC_CurPlayer",info,"ACKBC_CurPlayer");
				model.srddzMsgs.ACKBC_CurPlayer = info;
				
				var pos:int = info.Seat;
				view.srddzPage.clockPart.noticeShowClock(pos,10);
				if(pos == model.selfChairPos && model.isSelfSitDown)
				{
					if(model.curOutputPos == -1 && model.dizhuPos == model.selfChairPos)//没有人出过牌，并且地主是自己
					{
						var baodaoNum:int = model.getBaodaoNum();
						if(baodaoNum== 0)
						{
							view.srddzPage.handleBtns.showCtlBtns();
						}
						else if(model.isSeleBaodao == false && model.isStrictWin == false)//没有选择过报到
						{
							view.srddzPage.handleBtns.showBaodao(baodaoNum);
						}
						else if(model.isSeleBaodao == true && model.isSeleStrictWin == false)//选择过报到 没有选择过是否直接赢
						{
							if(model.baodaoState != 0)
							{
								view.srddzPage.handleBtns.showWay();
							}
							else
							{
								view.srddzPage.handleBtns.showCtlBtns();
							}
						
						}
						else if(model.isSeleBaodao == true && model.isSeleStrictWin == true)//都选择过了
						{
							view.srddzPage.handleBtns.showCtlBtns();
						}
					}
					else
					{
						view.srddzPage.handleBtns.showCtlBtns();
					}
					
					
					view.srddzPage.handlePart.canControl(pos,true);
				}
				
				view.srddzPage.actTipPart.hideJiabei();//暂时这么写
				view.srddzPage.outputPart.hideCards(pos);
				view.srddzPage.actTipPart.hideActTip(pos);
				
				//GiftEff.instance.showPockTypeEff(BasePocker.PAIXING_FEIJI,true);
				
			}
		}
		
		/*报到*/
		public function ACKBC_Srddz_Baodao(info:Object):void
		{
			if(actived)
			{
				trace("ACKBC_Srddz_Baodao",info,"ACKBC_Srddz_Baodao");
//				int32  Uid = 1;		//报到的玩家
//				int32 BaodaoNum = 2;//报到的数量 0不报到 
//				repeated int32 Cards = 3;//报到的牌
				
				model.srddzMsgs.ACKBC_Srddz_Baodao = info;
				var pos:int = model.getPlayerPosByUid(info.Uid);
				if(pos != model.dizhuPos)//不是地主
				{
					QuickUtils.popMessage("报到信息有误，报道的玩家可能作弊！");
					return;
				}
				
				
				
				model.isSeleBaodao = true;
				model.baodaoNum = info.BaodaoNum;
				model.baodaoCards = info.Cards;
				
				
				
				if(model.baodaoNum == 0)//玩家选择了不报到
				{
					model.baodaoState = 0;
					if(pos == model.selfChairPos)//自己
					{
						view.srddzPage.handleBtns.showCtlBtns();
					}
				}
				else
				{
					if(model.baodaoNum == 1)
					{
						model.baodaoState = 1;
					}
					else if(model.baodaoNum >= 1)
					{
						model.baodaoState =  2;
					}
					
					if(pos == model.selfChairPos)//自己
					{
						if(model.isSeleStrictWin == false)//还没有选择直接赢
						{
							view.srddzPage.handleBtns.showWay();
						}
						else
						{
							view.srddzPage.handleBtns.showCtlBtns();
						}
					}
					
				}
				view.tableInfoPage.updatePlayState();
				view.srddzPage.handlePart.updateAllCards(model.handleCards);
				
			}
		}
		
		/**直接赢通知*/
		public function ACKBC_Srddz_StrictWin(info:Object):void
		{
			if(actived)
			{
				trace("ACKBC_Srddz_StrictWin",info,"ACKBC_Srddz_StrictWin");
//				int32  Uid = 1;
//				bool  IsStrictWin = 2;//是否直接赢
				
				model.srddzMsgs.ACKBC_Srddz_StrictWin = info;
				var pos:int = model.getPlayerPosByUid(info.Uid);
				
				if(pos != model.dizhuPos)
				{
					return;
				}
				model.isSeleStrictWin = true;
				model.isStrictWin = info.IsStrictWin;
				
				if(model.isStrictWin == false && pos == model.selfChairPos)
				{
					view.srddzPage.handleBtns.showCtlBtns();
				}
			}
		}
		
		
		
		public function preSelfOutputCards(uid:int,type:int,cards:Array):void
		{
			if(AppConfig.autoPlay)
			{
				return;
			}
			
			var outObj:Object = {
				Uid:uid,
				Type:type,
				Cards:cards
			}
			
			ACKBC_Sddz_Chupai(outObj,false);
			model.isClientPrePop = true;
		}
		
		
		
		/**出牌*/
		public function ACKBC_Sddz_Chupai(info:Object,isFromServer:Boolean=true):void
		{
			if(actived)
			{
				//				int32  Uid = 1;		//出牌的玩家
				//				int32 Type = 2;//牌的类型
				//				repeated int32 Cards = 3;//出的牌
				
				trace("ACKBC_Sddz_Chupai",info,"ACKBC_Sddz_Chupai");
				model.srddzMsgs.ACKBC_Sddz_Chupai = info;
				var pos:int = model.getPlayerPosByUid(info.Uid);
				
				if(isFromServer)//如果这个出牌是来自服务器
				{
					if(info.Type >= 8)
					{
						model.outZhadanNumVec[pos] += 1;
					}
				}
				
				if(info.pos == model.selfChairPos)
				{
					if(model.isClientPrePop == true)
					{
						model.isClientPrePop = false;
						return;
					}
				}
				
				
				var preSelfOrNon:Boolean = true;
				
				if(model.curOutputPos != -1 && model.curOutputPos != pos)
				{
					preSelfOrNon = false;
				}
				
				
				
				model.outputPockers(pos,info.Cards);
				view.srddzPage.outputPart.showCards(info.Cards,pos);
				view.srddzPage.handlePart.updateOnePosAllCards(pos,model.handleCards[pos]);
				
				model.beishu = info.Beishu;
				view.tableInfoPage.updateBeishu();
				
				var jieshuData:JishuArrData = JishuArrData.getJishuArrData(model.curOutputCards);
				
				var paiSound:String = "";
				switch(info.Type)
				{
					case BasePocker.PAIXING_DAN:
						paiSound = "1-" + BasePocker.getV(model.curOutputCards[0]);
						break;
					case BasePocker.PAIXING_DUIZI:
						paiSound = "2-" + BasePocker.getV(model.curOutputCards[0]);
						break;
					case BasePocker.PAIXING_SAN:
						paiSound = "3-" + BasePocker.getV(model.curOutputCards[0]);
						break;
//					case BasePocker.PAIXING_SANYI:
//						paiSound = "3d1" ;
//						break;
					case BasePocker.PAIXING_SANER:
						paiSound = "3d2" ;
						break;
					case BasePocker.PAIXING_SHUNZI:
						GiftEff.instance.showPockTypeEff(BasePocker.PAIXING_SHUNZI);
						paiSound = "shunzi" ;
						break;
					case BasePocker.PAIXING_LIANDUI:
						paiSound = "liandui" ;
						break;
					case BasePocker.PAIXING_FEIJI:
						paiSound = "feiji" ;
						var feijiData:FeijiData = FeijiData.getFeiji(jieshuData);
						
						if(feijiData.type == FeijiData.FEIJI_NON)
						{
							GiftEff.instance.showPockTypeEff(BasePocker.PAIXING_FEIJI);
						}
						else
						{
							GiftEff.instance.showPockTypeEff(BasePocker.PAIXING_FEIJI,true);
						}
						break;
					case BasePocker.PAIXING_ZHADAN:
						paiSound = "zhadan" ;
						GiftEff.instance.showPockTypeEff(BasePocker.PAIXING_ZHADAN);
						break;
//					case BasePocker.PAIXING_SIDAIER:
//						var sidaierdData:SidaierData = SidaierData.getSidaierData(jieshuData);
//						if(sidaierdData.type == SidaierData.TYPE_DAN)
//						{
//							paiSound = "4d2" ;
//						}
//						else if(sidaierdData.type == SidaierData.TYPE_DUI)
//						{
//							paiSound = "4d4" ;
//						}
//						break;
					
					case BasePocker.PAIXING_TIANZHA:
						GiftEff.instance.showPockTypeEff(BasePocker.PAIXING_TIANZHA);
						paiSound = "huojian";
						break;
				}
				
				
				var yaoSound:String =  "yao" + (1+Math.round(Math.random()));
				if(preSelfOrNon == false)
				{
					var rad:Number = Math.random();
					if(rad >= 0.5)
					{
						paiSound = yaoSound;
					}
				}
				
				SoundManager.playSound("res/sounds/sddz/"+SoundPlay.instance.getSexRef(model.playerByPos(pos).sex)+ paiSound +".mp3");
			}
		}
		
		/**过*/
		public function ACKBC_Sddz_Pass(info:Object):void
		{
			if(actived)
			{
				//  int32  Uid = 1;		//UserID
				trace("ACKBC_Sddz_Pass",info,"ACKBC_Sddz_Pass");
				model.srddzMsgs.ACKBC_Sddz_Pass = info;
				
				var pos:int = model.getPlayerPosByUid(info.Uid);
				view.srddzPage.actTipPart.showActTip(pos,BaseActTipItem.ACTTIP_BUCHU);
				
				var passSound:String = "guo" + (1+Math.round(Math.random()*2));
				SoundManager.playSound("res/sounds/sddz/"+SoundPlay.instance.getSexRef(model.playerByPos(pos).sex)+ passSound +".mp3");
				
			}
		}
		
		/**游戏结束*/
		public function ACKBC_Sddz_End(info:Object):void
		{
			if(actived)
			{
				//				int32  Uid = 1;		//先出完的玩家
				//				repeated SeatCard Cards 			= 2;    // 所有玩家的牌 (不包括手牌)
				//				repeated int32 Dipai  = 3; //当前的底牌 
				
				trace("ACKBC_Sddz_End",info,"ACKBC_Sddz_End");
				model.srddzMsgs.ACKBC_Sddz_End = info;
				
				if(UserData.isReplay && model.isStrictShowCalc == true)
				{
					return;
				}
				
				
				
				var effStr:String;
				if(info.Uid == -1)//流局了 也就是解散的时候会发生
				{
					view.srddzPage.handleBtns.reset();
					model.isLiu = true;
					
					
					if(UserData.isReplay && model.isStrictShowCalc == true)
					{
						return;
					}
					
					effStr = "audio_liuju";
					SoundPlay.playEffect(effStr);
					pauseGameQueue();
					Laya.timer.once(4000, this, contineGameQueue);
				}
				else
				{
					var pos:int = model.getPlayerPosByUid(info.Uid);
					var isSelfWin:Boolean = false;
					var isDizhuWin:Boolean = false;
					
					
					if(pos == model.selfChairPos)
					{
						isSelfWin = true;
					}
					
					if(pos == model.dizhuPos)
					{
						isDizhuWin = true;
					}
					
					model.isLiu = false;
					if(isSelfWin == true)//自己糊了
					{
						effStr = "js_win";
					}
					else
					{
						effStr = "js_fail";
					}
					
					SoundPlay.playEffect(effStr);
					Laya.timer.once(2000, this, contineGameQueue);
					
				}
				gameOverDownCards(info);
				
				
				pauseGameQueue();
				
			}
		}
		
		/**胡牌和流局了倒下牌都走这里*/
		private function gameOverDownCards(info:Object):void
		{
			model.isEnd = true;
			
			model.dipaiCards = info.Dipai;
			view.srddzPage.dipaiPart.showCards(model.dipaiCards );
			
			var handleCards:Array = [];
			var i:int,j:int,k:int;
			
			var cardIdx:int;
			
			for(i=0;i<info.Cards.length;i++)
			{
				if(info.Cards[i].List.length != info.Cards[i].ListLen)
				{
					for(k=0;k<info.Cards[i].ListLen;k++)
					{
						info.Cards[i].List.push({CID:0});
					}
				}
				
				handleCards.length = 0;
				//更新玩家手里的牌
				for(j=0;j<info.Cards[i].List.length;j++)
				{
					handleCards.push(info.Cards[i].List[j].CID);
				}
				model.updateHandleCards(i,handleCards);
				view.srddzPage.handlePart.updateOnePosAllCards(i,model.handleCards[i]);
			}
		}
		
		
		
		/**小结算*/
		public function ACKBC_Sddz_Total(info:Object):void
		{
			if(actived)
			{
				trace("ACKBC_Sddz_Total",info,"ACKBC_Sddz_Total");
				model.srddzMsgs.ACKBC_Sddz_Total = info;
				
				model.srddzMsgs.ACK_RoomInfo.RoundCount = info.RoundCount;
				view.tableInfoPage.updateLeftRound(false);
				view.playerInfoPage.updateSitDownUpBtn(false);
				
				//				"服务器将于<span style='color:#E53333;'>7月4日20:00</span>整进行维护，预计<span style='color:#E53333;'>21:00</span>维护完成。<br />"
				//				+"现在起至维护完成期间将关闭房间创建和加入功能，已经在游戏中的玩家请注意服务器关闭时间。<br />"
				//					+"维护完成后将奉上<span style='color:#E53333;'>1000</span>钻石作为补偿，给大家带来的不便请大家谅解。<br />"
				//					+"<br />" 
				//					+"<span style='align:right;'>麻将运营团队</span>"
				
				var t:Number=QuickUtils.getLocalVar("hasConcern",0);
				
				if(t==0)
				{
					QuickUtils.setLocalVar("hasConcern",1);
					CommonModule.instance.commonContext.view.showNotice(
						"       微信搜索公众号<span style='color:#f6d368;'> "+AppConfig.nameTitle+"  </span>关注后即可获得更多福利哦！<br />",this,showCalculate);
				}
				else
				{
					showCalculate();
				}
				
				showCalculate();
			}
		}
		
		public function showCalculate():void
		{
			model.isGameStart = false;
			view.calculatePage.show();
			model.setPlayerReadyFalse();//重置坐下准备
		}
		
		/**大结算 用不到哈哈*/
		public function NOTIFY_Summary(info:Object):void
		{
			
		}
		
		/**离开房间*/
		public function ACKBC_Exit_Room(info:Object):void
		{
			if(actived)
			{
				trace("ACKBC_Exit_Room");
				trace(info);
				trace("ACKBC_Exit_Room");
				model.srddzMsgs.ACKBC_Exit_Room = info;
				info.uid = info.UID;
				
				if(info.uid == UserData.selfuid)
				{
					if(AppConfig.isNewHall)
					{
						QuickUtils.gotoHall();
					}
					else
					{
						endGameGotoHall(true);
					}
					return;
				}
				else
				{
					EventCenter.instance.event(EventCenter.COMMON_INFOLIST_NOTICE,{color:1,msg:"玩家["+model.getPlayerNicknameByUid(info.uid)+"]离开了房间！"});
					var pos:int = model.getPlayerPosByUid(info.uid);
					model.leavePlayer(info.uid);
					if(pos != -1)
					{
						view.playerInfoPage.updatePlayerInfos(model.playerInfoVec);
						view.playerInfoPage.showStartBtn(false);
					}
				}
				
				if(model.isGameStart || model.srddzMsgs.ACK_RoomInfo.RoundCount != 0)
				{
					view.playerInfoPage.showDizhuNM();
				}
			}
		}
		
		//解散相关
		public function AckDisband(info:Object):void
		{
			if(actived)
			{
				trace("AckDisband::" ,info , "解散相关");
				model.srddzMsgs.AckDisband = info;
				//todo
				
				//				Laya.timer.frameOnce(1,this,popDissolveRoomDetail,[info]);
				
				popDissolveRoomDetail(info);
				
			}
		}
		
		
		public function NotifyDisband(info:Object):void
		{
			if(actived)
			{
				trace("NotifyDisband::" ,info , "解散相关");
				
				
				model.srddzMsgs.NotifyDisband = info;
				//todo
				hideDissolveRoomDetail();
				
				//				message NotifyDisband{
				//					int32 roomId = 1;
				//					int32 result = 2; //1:成功 2:失败
				//				}
				
				var str:String = "";
				if(info.result == 1)
				{
					str = "解散成功！";
				}
				else
				{
					str = "解散失败！";
					//					pauseGameQueue();
					QuickUtils.popMessageBox(str,PopBox.BTN_NONE,this,null);
				}
			}
		}
		
		public function NotifyUserState(info:Object):void
		{
			if(actived)
			{
				trace("NotifyUserState",info,"NotifyUserState")
				//				message NotifyUserState {
				//					string id = 1; //user_id
				//					int32 state = 2; //1：上线 2：下线
				//				}
				
				model.srddzMsgs.NotifyUserState = info;
				var player:Object = model.playerByUid(info.id);
				player.state = info.state;
				player.offlineTime = info.offlineTime;
				
				var pos:int =model.getPlayerPosByUid(parseInt(info.id));
				var dir:int = model.getChairDirByPos(pos);
				var isGray:Boolean = false;
				if(info.state == 2)
				{
					isGray = true;
				}
				view.playerInfoPage.setGrayhead(dir,isGray,true,info.offlineTime);
			}
		}
		
		/**通知可以t人*/
		public function NotifyKick(info:Object):void
		{
			if(actived)
			{
				trace("NotifyKick",info,"NotifyKick");
				//repeated int32 indexs = 1; //当前可踢得玩家index
				var i:int,len:int=info.indexs.length,player:Object;
				for(i=0;i<len;i++)
				{
					player = model.playerByPos(info.indexs[i]);
					player.offlineTime = 0;
					player.canKick = true;
				}
				
				view.playerInfoPage.updateTirenBtn();
				
			}
		}
		
		/**t人返回结果*/
		public function KickResponse(info:Object):void
		{
			if(actived)
			{
				//				message KickResponse {//980
				//					int32 pos = 1; //被踢掉的玩家pos
				//					string uid = 2; //被踢掉的玩家user_id
				//				}
				if(QuickUtils.popBox)
				{
					QuickUtils.popBox.onhide();
				}
				
				model.standup(info.uid, -1);
				
				model.beKickedPlayer[info.pos] = info.uid;
				
				model.playerByUid(info.uid).offlineTime = 0;
				
				view.playerInfoPage.updatePlayerInfos(model.playerInfoVec);
				view.playerInfoPage.updateSitDownUpBtn();
				view.playerInfoPage.updateStartBtn();
				view.tableInfoPage.updateKaijuren(info.nickName);
				EventCenter.instance.event(EventCenter.COMMON_INFOLIST_NOTICE,{color:0,msg:"玩家["+model.getPlayerNicknameByUid(info.uid)+"]站起了！"});
				QuickUtils.popMessageBox("玩家["+model.getPlayerNicknameByUid(info.uid)+"]被其他玩家请离座位!",PopBox.BTN_QUEREN,this,onQuerenBeiTi);
			}
		}
		
		protected function onQuerenBeiTi():void
		{
			//
		}
		
		
		protected var pop:PopBox;
		
		/**房间未开始游戏解散*/
		public function NotifyDestoryRoom(info:Object):void
		{
			if(actived)
			{
				trace("NotifyDestoryRoom",info,"NotifyDestoryRoom");
				if(info.IsOwnerDisband !=undefined && info.IsOwnerDisband == true)
				{
					pop = QuickUtils.popMessageBox("房主解散了房间！",PopBox.BTN_QUEREN,this,onQueRenExit,"提示","left");
				}
				else
				{
					pop = QuickUtils.popMessageBox("由于在规定时间内未开始游戏，房间已经强制解散！",PopBox.BTN_QUEREN,this,onQueRenExit,"提示","left");
				}
			}
		}
		
		public function onQueRenExit(idx:int):void
		{
			if(AppConfig.isNewHall)
			{
				QuickUtils.gotoHall();
			}
			else
			{
				endGameGotoHall();
			}
		}
		
		protected function onPopPanelCallBack():void
		{
			if(AppConfig.isNewHall)
			{
				QuickUtils.gotoHall();
			}
			else
			{
				endGameGotoHall();
			}
		}
		
		public function endGameGotoHall(gotoHall:Boolean=true):void
		{
			trace("send MsgTypes.BASE_QUEUE,PomeloMessage.hall_g_o...");
			if(pop != null)
			{
				pop.onhide();
			}
			//this.notify(MsgNames.SOCKET_SEND,MsgTypes.BASE_QUEUE,PomeloMessage.hall_g_o,{},onGOCallBack);
			
			//			if(popBox)
			//			{
			//				popBox.onhide();
			//			}
			hideDissolveRoomDetail();
			contineGameQueue();
			
			MessageManager.instance.resetGameQueue();
			
			model.reset();
			view.reset();
			model.playerInfoVec.length = 0;
			
			if(UserData.isReplay)
			{
				UserData.isPreReplay = true;
				//这里需要跳转到上次的重播界面
				
				//LoginModule.showReplay(false);
			}
			
			CommonModule.instance.regotoCommonText();
			SrddzGameModule.instance.stopGame(gotoHall);
			
			
			
			UserData.isReplay = false;
			model.isGameStart == false;
			
			
		}
		
		public var dissolvePage:NewDissolvePage;
		
		public function popDissolveRoomDetail(info:Object):void
		{
			if(dissolvePage == null)
			{
				dissolvePage = new NewDissolvePage();
			}
			
			dissolvePage.update(info);
			
			QuickUtils.AddCenter(dissolvePage,UIManager.instance.popLayer);
			
			if(QuickUtils.popBox)
			{
				QuickUtils.popBox.onhide();
			}
		}
		
		public function hideDissolveRoomDetail():void
		{
			if(dissolvePage && dissolvePage.parent)
			{
				dissolvePage.parent.removeChild(dissolvePage);
			}
		}
		
		public function clear():void
		{
			model.reset();
			view.reset();
			model.playerInfoVec.length = 0;
			
			if(UserData.isReplay)
			{
				EventCenter.instance.event(EventCenter.REPLAY_back,null);
			}
			
			UserData.isReplay = false;
			model.isGameStart == false;
		}
		
		/**送礼物*/
		public function MSG_ACK_Gift(info:Object):void
		{
			if(actived)
			{
				
				trace("MSG_ACK_Gift",info,"MSG_ACK_Gift");
				//				int32 id = 1;
				//				int32 diamond = 2;
				//				string uid = 3;
				//				string tUid = 4;
				
				var player:Object = model.playerByUid(info.uid);
				var tplayer:Object =  model.playerByUid(info.tUid);
				
				player.Diamond = info.diamond;
				
				var fromDir:int = model.getChairDirByPos(player.pos);
				var toDir:int = model.getChairDirByPos(tplayer.pos);
				
				if(info.uid == UserData.uid)
				{
					UserData.Diamond = info.diamond;
				}
				
				
				GiftEff.instance.showGiftEff(fromDir,toDir,info.id);
			}
		}
		
		/**清除延迟回调相关*/
		public function clearTimeDelay():void
		{
			Laya.timer.clear(this, contineGameQueue);
		}
		
		public function resetSelf():void
		{
			model.reset();
			view.playerInfoPage.hideReadyBtn();
			view.playerInfoPage.hideDizhuNM();
			view.playerInfoPage.updateJiabei();//隐藏掉加倍
			
			view.calculatePage.reset();//影藏结算界面
			
			view.srddzPage.reset();
		}
		//以上为公共
		
		
		
		
		//
		
		
		protected function get model():SrddzModel
		{
			return SrddzGameModule.instance.gameContext.model;
		}
		
		protected function get view():SrddzView
		{
			return SrddzGameModule.instance.gameContext.view;
		}
		
		
		public function sendMsgCommond(commondId:Object,needCantrol:Boolean=true):void
		{
			if(needCantrol)
			{
				view.srddzPage.handlePart.canControl(model.selfChairPos,false);
			}
			EventCenter.instance.event(EventCenter.SOCKET_SEND,commondId);
		}
		
		/**暂停游戏消息队列*/
		public function pauseGameQueue():void
		{
			if(UserData.isReplay)
			{
				model.needCutdownReplay = true;
			}
			else
			{
				MessageManager.instance.pauseQueue(MessageManager.GAME);
			}
		}
		
		/**继续游戏消息队列*/
		public function contineGameQueue():void
		{
			if(UserData.isReplay)
			{
				model.needCutdownReplay = false;
			}
			else
			{
				MessageManager.instance.continueQueue(MessageManager.GAME);
			}
		}
		
		/**游戏时间已经结束*/
		public function onTimeOver():void
		{
			if(!model.isGameStart)
			{
				if(view.calculatePage.perPage.isShow)//小结算界面显示 ，重置小结算界面状态
				{
					view.calculatePage.perPage.timeOver();
				}
				else//显示返回界面
				{
					view.calculatePage.perPage.onClickConfirmBtn();
				}
			}
		}
	}
}