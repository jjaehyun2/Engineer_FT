package modules.srddzGame.controller
{
	import common.event.EventCenter;
	
	import manager.MessageManager;
	
	import modules.srddzGame.SrddzGameModule;
	
	import net.Message;
	
	import rb.framework.mvc.AbstractLayer;
	
	public class SrddzMainController extends AbstractLayer
	{
		public function SrddzMainController()
		{
			super();
		}
		
		public override function onAdd():void
		{
			
			if(UserData.isReplay)
			{
				
			}
			else
			{
				EventCenter.instance.on(MessageManager.GAME,this,onMsg);
			}
		}
		
		public override function onRemove():void
		{
			if(UserData.isReplay)
			{
				
			}
			else
			{
				EventCenter.instance.off(MessageManager.GAME,this,onMsg);
			}
		}
		
		private function onMsg(msg:*):void
		{
			if(SrddzGameModule.isPauseGameQueue == true)
			{
				return;
			}
			
			procMsg(msg);
		}
		
		private function procMsg(msg:Object):void
		{
			if(msg is Message)
			{
				msg.complete();
			}
			
			trace("acc msgId::" + msg.messageId);
			
			var body:Object;
			
			switch(msg.messageId)
			{
				case Message.ACKBC_Into_Room:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACKBC_Into_Room.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACKBC_Into_Room(body);
					break;
				case Message.ACKBC_Sitdown:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACKBC_Sitdown.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACKBC_Sitdown(body);
					break; 
				case Message.ACKBC_Standup:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACKBC_Standup.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACKBC_Standup(body);
					break;
				
				case Message.ACK_RoomInfo:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACK_RoomInfo.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACK_RoomInfo(body);
					break;
				
				case Message.ACK_Room_User:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACK_Room_User.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACK_Room_User(body);
					break;
				
				
				case Message.ACKBC_Sddz_Start:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACKBC_Sddz_Start.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACKBC_Sddz_Start(body);
					break;
				
				case Message.ACK_User_SeatCard:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACK_User_SeatCard.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACK_User_SeatCard(body);
					break;
				
				case Message.ACKBC_Sddz_JiaoDizhu:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACKBC_Sddz_JiaoDizhu.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACKBC_Sddz_JiaoDizhu(body);
					
					break;
				
				case Message.ACKBC_Sddz_Mingpai:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACKBC_Sddz_Mingpai.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACKBC_Sddz_Mingpai(body);
					
					break;
				
				case Message.ACKBC_Sddz_Jiabei:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACKBC_Sddz_Jiabei.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACKBC_Sddz_Jiabei(body);
					
					break;
				
				case Message.ACKBC_Srddz_Baodao:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACKBC_Srddz_Baodao.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACKBC_Srddz_Baodao(body);
					break;
				
				case Message.ACKBC_Srddz_StrictWin:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACKBC_Srddz_StrictWin.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACKBC_Srddz_StrictWin(body);
					break;
				
				
				case Message.ACKBC_CurPlayer:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACKBC_CurPlayer.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACKBC_CurPlayer(body);
					break;
				
				case Message.ACKBC_Sddz_Jiaofen:
					if(UserData.isReplay)
					{
						
					}
					else
					{
						body = AppConfig.proto.ACKBC_Sddz_Jiaofen.decode(msg.params[0]);
					}
					SrddzGameModule.instance.gameContext.controller.ACKBC_Sddz_Jiaofen(body);
					break;
				
				case Message.ACKBC_Sddz_Dizhu:
					if(UserData.isReplay)
					{
						
					}
					else
					{
						body = AppConfig.proto.ACKBC_Sddz_Dizhu.decode(msg.params[0]);
					}
					SrddzGameModule.instance.gameContext.controller.ACKBC_Sddz_Dizhu(body);
					break;
				
				
				case Message.ACKBC_Sddz_Chupai:
					if(UserData.isReplay)
					{
						body = {};
						var arr:Array = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACKBC_Sddz_Chupai.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACKBC_Sddz_Chupai(body);
					break;
				
				
				
				case Message.ACKBC_Ready:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACKBC_Ready.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACKBC_Ready(body);
					break;
				
				case Message.ACKBC_Exit_Room:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACKBC_Exit_Room.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACKBC_Exit_Room(body);
					break;
				
				case Message.NotifyStartGame:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.NotifyStartGame.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.NotifyStartGame(body);
					break;
				
				case Message.MSG_ACKBC_Chat:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACKBC_SendMsg.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.view.onRecChat(body);
					break;
				
				case Message.ACKBC_Sddz_End:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACKBC_Sddz_End.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACKBC_Sddz_End(body);
					break;
				
				case Message.ACKBC_Sddz_Card_Init:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACKBC_Sddz_Card_Init.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACKBC_Sddz_Card_Init(body);
					break;
				case Message.ACKBC_Sddz_Total://小结算
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.ACKBC_Sddz_Total.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.ACKBC_Sddz_Total(body);
					break;
				case Message.MSG_NOTIFY_SUMMARY://大结算
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.TotalSummary.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.NOTIFY_Summary(body);
					break;
				case Message.AckDisband:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.AckDisband.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.AckDisband(body);
					break;
				case Message.NotifyDisband:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.NotifyDisband.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.NotifyDisband(body);
					break;
				case Message.NotifyUserState:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.NotifyUserState.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.NotifyUserState(body);
					break;
				case Message.MSG_NOTIFY_DESTORY_ROOM:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.NotifyDestoryRoom.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.NotifyDestoryRoom(body);
					break;
				case Message.NotifyKick:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.NotifyKick.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.NotifyKick(body);
					break;
				case Message.KickResponse:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.KickResponse.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.KickResponse(body);
					break;
				case Message.MSG_ACK_Gift:
					if(UserData.isReplay)
					{
						body = msg.body;
					}
					else
					{
						body = AppConfig.proto.MSG_ACK_Gift.decode(msg.params[0]);
					}
					
					SrddzGameModule.instance.gameContext.controller.MSG_ACK_Gift(body);
					break;
				
				case Message.ACKBC_Sddz_Pass:
					if(UserData.isReplay)
					{
						body = msg.body;
						trace("Message.Pass",body);
						//SDdzGameModule.instance.gameContext.controller.pass(body);
					}
					else
					{
						body = AppConfig.proto.ACKBC_Sddz_Pass.decode(msg.params[0]);
					}
					SrddzGameModule.instance.gameContext.controller.ACKBC_Sddz_Pass(body);
					
					break;
				
				
				
				case "":
					break;
				
				case "":
					break;
				
			}
			
			if(UserData.isReplay)
			{
				//				if(model.replayCurStep >= model.preStepNum-1)
				//				{
				//					model.saveStepData();
				//				}
				
			}
		}
	}
}