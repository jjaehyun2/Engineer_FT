package manager
{
	import common.event.EventCenter;
	import common.view.CloseMask;
	import common.view.PopBox;
	
	import hall.HallModule;
	
	import laya.utils.Dictionary;
	
	import net.Message;
	import net.Pomelo;

	public class MessageManager
	{
		public static const LOGIN:String = "MESSSAGE_LOGIN";
		public static const GAME:String = "MESSAGE_GAME";
		public static const HALL:String = "MESSAGE_HALL";
		public static const COMMON:String = "MESSAGE_COMMON";
		
		
		protected var queueDic:Dictionary = new Dictionary();
		public var pausedDic:Dictionary = new Dictionary();
		
		public static var instance:MessageManager = new MessageManager();
		
		/**请使用MessageManager.insatnce*/
		public function MessageManager()
		{
			queueDic[LOGIN] = [];
			queueDic[GAME] = [];
			queueDic[HALL] = [];
			queueDic[COMMON] = [];
			
			pausedDic[LOGIN] = false;
			pausedDic[GAME] = false;
			pausedDic[HALL] = false;
			pausedDic[COMMON] = false;
		}
		
		public function resetGameQueue():void
		{
			queueDic[GAME] = [];
		}
		
		public function resetHallQueue():void
		{
			queueDic[HALL] = [];
		}
		
		
		
		protected function modulejsLoaded():void
		{
			if(ModuleDef.CurGameModule)
			{
				ModuleDef.CurGameModule.instance.stopGame();
			}
			else
			{
				if(AppConfig.isNewHall)
				{
					QuickUtils.gotoHall()
				}
				else
				{
					HallModule.instance.gotoHall();
				}
			}
		}
		
		public function onGotMessage(data:Object):void
		{
			trace("onGotMessage ID:" + data.ID);//+ " msg" +data.MSG
			var ProBuffClass:*;
			var type:String;
			var body:Object;
			
			if(data.ID == -1)
			{
				var erro:Object = AppConfig.proto.ErrorItem.decode(data.MSG);
				trace(erro.message,erro.code);
				
				switch(erro.code)
				{
					case 100:
						return;
					case 99://设备在其他地方登陆
						QuickUtils.popMessageBox(erro.message,PopBox.BTN_QUEREN,this,closeUI);
						Pomelo.instance.needReconnect = false;
						break;
					
					case 330:
						QuickUtils.popMessageBox(erro.message,PopBox.BTN_QUEREN,this,closeUI);
						Pomelo.instance.needReconnect = false;
						break;
					case 340://系统为玩家补充金币
						QuickUtils.popMessageBox(erro.message,PopBox.BTN_QUEREN,this,null);
						break;
					
					case 205:
					case 107:
					case 260:
						HallModule.instance.gotoHall();
						QuickUtils.popMessage(erro.message);
						
						break;
					
					
					case 204:
						QuickUtils.popMessageBox(erro.message,PopBox.BTN_NONE,this,onClosePopMessage);
						break;
					case 103://房间不存在
						queueDic[GAME] = [];
						QuickUtils.popMessage(erro.message);
						if(AppConfig.isNewHall){
							if(UserData.uniqueCode){
								QuickUtils.gotoHall(1);
							}else{
								QuickUtils.gotoHall();
							}
						}else{
							if(ModuleDef.CurGameModule)//是否加载过西周麻将js部分
							{
								ModuleDef.CurGameModule.instance.stopGame();
							}
							else
							{
								if(LoadingManager.instance.isInLoadingGameJs)
								{
									AppConfig.needIntoGame = false;
									EventCenter.instance.once(EventCenter.LOAD_MODULES_JS_LOADED,this,modulejsLoaded);
								}
								else
								{
									if(UserData.uniqueCode){
										HallModule.instance.gotoHall();
										HallModule.instance.hallContext.hallView.hallLayer.onRecord({"uniqueCode":UserData.uniqueCode});
									}else{
										HallModule.instance.gotoHall();
									}
								}
							}
						}
						break;
					case 101://用户信息错误重新登录
						Pomelo.instance.reLogin();
						break;
					case 300://信息错误
						if(AppConfig.isNewHall)
						{
							QuickUtils.gotoHall();
						}
						else
						{
							//QuickUtils.popMessage(erro.message);
						}
						break;
					default:
						//QuickUtils.popMessage(erro.message);
						break;
				}	
				return;
			}
			
			switch(data.ID)
			{
				case Message.ACK_Login :
					type = MessageManager.LOGIN;
					break;
				case Message.MSG_ACK_Notice :
					type = MessageManager.HALL;
					break;
				case Message.ACK_User_Info :
					type = MessageManager.LOGIN;
					break;
				case Message.MSG_UPDATE_USERINFO:
					type = MessageManager.COMMON;
					break;
				case Message.ACK_RoomInfo :
					type=MessageManager.GAME;
					break;
				case Message.ACK_Room_User:
					type=MessageManager.GAME;
					break;
				case Message.ACK_Room_List :
					type=MessageManager.HALL;
					break;
				case Message.ACK_Find_Room :
					type=MessageManager.HALL;
					break;
				case Message.ACK_MSG :
					type=MessageManager.HALL;
					break;
				case Message.ACKBC_Into_Room :
					type=MessageManager.GAME;
					var msg1:Message = new Message(MessageManager.HALL,data.ID,data.MSG);
					dispatch(msg1);
					break;
				case Message.ACK_Into_MatchRoom: 
					type=MessageManager.HALL;
					break;
				case Message.ACKBC_Exit_Room: 
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Sitdown:
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Standup:
					type=MessageManager.GAME;
					break;
				case Message.ACK_Create_Room : 
					type=MessageManager.HALL;
					break;
				case Message.ACK_Match_Room:
					type=MessageManager.HALL;
					break;
				case Message.ACK_Cancel_Match_Room:
					type = MessageManager.HALL;
					break;
				case Message.ACKBC_Ready :
					type=MessageManager.GAME;
					break;
				case Message.ACK_User_SeatCard :
					type=MessageManager.GAME;
					break;
				
				case Message.ACKBC_Card_Init :
					type=MessageManager.GAME;
					break;
				
				case Message.Room_State :
					type=MessageManager.GAME;
					break
				
				case Message.ACKBC_Start :
					type=MessageManager.GAME;
					break;
				case Message.ACK_UserCard :
					type=MessageManager.GAME;
					break;
				case Message.ACK_StartChange3Card :
					type=MessageManager.GAME;
					break;
				case Message.ACK_StartFixMiss :
					type=MessageManager.GAME;
					break;
				case Message.ACK_Change3Card_OK :
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_FixMiss_OK ://定缺
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_CurPlayer ://出牌ID
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_GetCard :
					type=MessageManager.GAME;
					
					trace("ACKBC_GetCard::" + TimeManager.unixtime);
					
					break;
				case Message.ACKBC_PutCard : 
					type=MessageManager.GAME;
					
					trace("ACKBC_PutCard::" + TimeManager.unixtime);
					
					break;
				case Message.ACK_WaitTool ://验证吃彭刚 	
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Chow : 	
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Peng :
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Kong :
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Win :
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Draw :
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Total : 	//一局结束的结算	
					type=MessageManager.GAME;
					break;
//				case Message.ACKBC_Disband_Room ://解散房间广播  	
//					type=MessageManager.GAME;
//					break;
				case Message.ACKBC_RoundScore ://每次操作的结算 	
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_EffectEvent ://特效事件 	
					type=MessageManager.GAME;
					break;
				case Message.ACK_Benefits :// 救济金	
					type=MessageManager.GAME;
					break;
				case Message.ACK_NeedBenefits ://需要救济金(客户端弹出页面)
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Restart ://重新开始(客户端清空, 不包括用户信息) 	
					type=MessageManager.GAME;
					break;
				case Message.Card : 
					type=MessageManager.GAME;
					break;
				case Message.SeatCard ://玩家的牌,  用于进入玩家同步数据 	
					type=MessageManager.GAME;
					break;
				case Message.NotifyStartGame:
					type=MessageManager.GAME;
					break;
				case Message.MSG_ACKBC_Chat:
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Win://胡牌
					type=MessageManager.GAME;
					break;
				case Message.MSG_NOTIFY_SUMMARY:
					type=MessageManager.GAME;
					break;
				case Message.AckDisband:
					type=MessageManager.GAME;
					break;
				case Message.NotifyDisband:
					type=MessageManager.GAME;
					break;
				case Message.MSG_ACK_Battle_Record:
					type=MessageManager.HALL;
					break;
				case Message.MSG_ACK_Home_Owner:
					type=MessageManager.HALL;
					break;
				case Message.MSG_ACK_Room_Summary:
					type=MessageManager.COMMON;
					break;
				case Message.MSG_ACK_BattleDetail:
					type=MessageManager.HALL;
					break;
				case Message.NotifyUserState:
					type=MessageManager.GAME;
					break;
				case Message.NotifyKick:
					type=MessageManager.GAME;
					break;
				case Message.MSG_NOTIFY_DESTORY_ROOM:
					type=MessageManager.GAME;
					break;
				case Message.KickResponse:
					type=MessageManager.GAME;
					break;
				case Message.MSG_ACK_NOTIFY_RECHARGE:
					type=MessageManager.HALL;
					break;
				case Message.ACK_TransferHuaResponse:
					type=MessageManager.GAME;
					break;
				case Message.MSG_ACK_Gift:
					type=MessageManager.GAME;
					break;
				case Message.MSG_GameNotice:
					type=MessageManager.COMMON;
					break;
				//三人斗地主相关
//				public static const ACKBC_Sddz_Jiaofen:int =   1500;
//				public static const ACKBC_Sddz_Dizhu:int =     1501;
//				public static const ACKBC_Sddz_Pass:int =     1502;
//				public static const ACKBC_Sddz_End:int =       1503;
//				public static const ACKBC_Sddz_Total:int =     1504;
//				public static const ACKBC_Sddz_Card_Init:int = 1505;
//				public static const ACKBC_Sddz_Start:int =     1506;
//				public static const ACKBC_Sddz_Chupai:int =    1507;
//				public static const ACKBC_Sddz_JiaoDizhu:int = 1508;
//				public static const ACKBC_Sddz_Mingpai:int = 1509;
//				public static const ACKBC_Sddz_Jiabei:int = 1510;
				case Message.ACKBC_Sddz_Jiaofen:
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Sddz_Dizhu:
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Sddz_Pass:
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Sddz_End:
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Sddz_Total:
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Sddz_Card_Init:
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Sddz_Start:
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Sddz_Chupai:
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Sddz_JiaoDizhu:
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Sddz_Mingpai:
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Sddz_Jiabei:
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Srddz_Baodao:
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Srddz_StrictWin:
					type=MessageManager.GAME;
					break;
				case Message.ACKBC_Nn_Xiazhu:
					type=MessageManager.GAME;
					break;
					
				
			}
			
			var msg:Message = new Message(type, data.ID,data.MSG);
			
			if(data.ID == Message.MSG_ACK_Gift || data.ID == Message.MSG_ACKBC_Chat)//需要直接用的，不排队的放这里
			{
				dispatchStrict(msg);
			}
			else
			{
				dispatch(msg);
			}
			
		}
		
		private function closeUI():void
		{
			
			Laya.stage.addChild(new CloseMask)
		}
		
		protected function onClosePopMessage():void
		{
			if(ModuleDef.CurGameModule.inGame)//游戏时间已经结束
			{
				ModuleDef.CurGameModule.instance.gameContext.controller.onTimeOver();
			}
			else
			{
				if(AppConfig.isNewHall)
				{
					QuickUtils.gotoHall();
				}
				else
				{
					HallModule.instance.gotoHall();
				}
//				
			}
		}
		
		protected function dispatch(msg:Message):void
		{
			queueDic[msg.type].push(msg);
			if(!pausedDic[msg.type])
			{
				EventCenter.instance.event(msg.type,msg);
			}
		}
		
		/**消息不放在列队，直接发送*/
		protected function dispatchStrict(msg:Message):void
		{
			queueDic[msg.type].push(msg);
			EventCenter.instance.event(msg.type,msg);
		}
		
		public function pauseQueue(queueName:String):void
		{
			pausedDic[queueName] = true;
		}
		
		public function continueQueue(queueName:String):void
		{
			var queue:Array = queueDic[queueName];
			pausedDic[queueName] = false;
			var i:int,len:int = queue.length,msg:Message;
			if(len==0)
			{
				return;
			}
			for(i=0;i<queue.length+1;i++)
			{
				if(queue.length == len-1)
				{
					len = queue.length;
					i--;
				}
				msg = queue[i];
				if(!pausedDic[queueName] && msg)
				{
					EventCenter.instance.event(msg.type,msg);
				}
			}
		}
		
		public function completeMsg(msg:Message):void
		{
			var queue:Array = queueDic[msg.type];
			var i:int,len:int = queue.length;
			for(i=0;i<len;i++)
			{
				if(queue[i] == msg)
				{
					queue.splice(i,1);
					break;
				}
			}
				
				
		}
		
		
	}
}