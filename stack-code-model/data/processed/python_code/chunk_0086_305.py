package net
{
	public class ProtoMessage
	{
		public function ProtoMessage()
		{
		}
		
		public static function getProtoMessage(ID:int,body:Object):Object
		{
			trace("sendMessageID::" + ID + " body::", body);
			
			var ProMessage:* = AppConfig.proto.Message;
			var message:Object = new Object();
			message.ID = ID;
			var BodyClass:*;
			switch(ID)
			{
				case Message.Login://登陆
					BodyClass = AppConfig.proto.Login;
					break;
				case Message.MSG_Notice://获取跑马灯公告
					BodyClass = AppConfig.proto.Notice;
					break;
				case Message.Create_Room://创建房间
					BodyClass = AppConfig.proto.Create_Room;
					break;
				case Message.Match_Room://匹配玩家
					BodyClass = AppConfig.proto.Match_Room;
					break;
				case Message.Cancel_Match_Room:
					BodyClass = AppConfig.proto.Cancel_Match_Room;
					break;
				case Message.Into_Room://加入房间
					BodyClass = AppConfig.proto.Into_Room;
					break;
				case Message.Put_Card:
					BodyClass = AppConfig.proto.Put_Card;
					break;
				case Message.Chow:
					BodyClass = AppConfig.proto.Chow;
					break;
				case Message.Peng:
					BodyClass = AppConfig.proto.Peng;
					break;
				case Message.Kong:
					BodyClass = AppConfig.proto.Kong;
					break;
				case Message.Pass:
					BodyClass = AppConfig.proto.Pass;
					break;
				case Message.MSG_Sitdown:
					BodyClass = AppConfig.proto.SitDown;
					break;
				case Message.MSG_Standup:
					BodyClass = AppConfig.proto.StandUp;
					break;
				case Message.User_Ready:
					BodyClass = AppConfig.proto.UserReady;
					break;
				case Message.Exit_Room:
					BodyClass = AppConfig.proto.ExitRoom;
					break;
				case Message.Start_Game:
					BodyClass = AppConfig.proto.Start_Game;
					break;
				case Message.MSG_Chat:
					BodyClass = AppConfig.proto.Chat;
					break;
				case Message.Win:
					BodyClass = AppConfig.proto.Win;
					break;
				case Message.Disband:
					BodyClass = AppConfig.proto.Disband;
					break;
				case Message.Vote:
					BodyClass = AppConfig.proto.Vote;
					break;
				case Message.MSG_Battle_Record:
					BodyClass = AppConfig.proto.BattleRecordRequest;
					break;
				case Message.MSG_Home_Owner:
					BodyClass = AppConfig.proto.HomeOwnerRequest;
					break;
				case Message.MSG_Room_Summary:
					BodyClass = AppConfig.proto.RoomSummaryRequest;
					break;
				case Message.KickRequest:
					BodyClass = AppConfig.proto.KickRequest;
					break;
				case Message.MSG_NOTIFY_RECHARGE:
					BodyClass = AppConfig.proto.NotifyRecharge;
					break;
				case Message.MSG_Gift:
					BodyClass = AppConfig.proto.MSG_Gift;
					break;
				case Message.MSG_BattleDetail:
					BodyClass = AppConfig.proto.MSG_BattleDetail;
					break;
				
				//斗地主追加的
//				public static const Sddz_Jiaofen:int = 1200;
//				public static const Sddz_Mingpai:int = 1201;
//				public static const Sddz_Jiabei:int = 1202;
//				public static const Sddz_Chupai:int = 1203;
//				public static const Sddz_Pass:int = 1204;
				
				case Message.Sddz_Jiaofen:
					BodyClass = AppConfig.proto.Sddz_Jiaofen;
					break;
				
				case Message.Sddz_Mingpai:
					BodyClass = AppConfig.proto.Sddz_Mingpai;
					break;
				
				case Message.Sddz_Jiabei:
					BodyClass = AppConfig.proto.Sddz_Jiabei;
					break;
				
				case Message.Sddz_Chupai:
					BodyClass = AppConfig.proto.Sddz_Chupai;
					break;
				
				case Message.Sddz_Pass:
					BodyClass = AppConfig.proto.Sddz_Pass;
					break;
				
				case Message.Srddz_Baodao:
					BodyClass = AppConfig.proto.Srddz_Baodao;
					break;
				
				case Message.Srddz_StrictWin:
					BodyClass = AppConfig.proto.Srddz_StrictWin;
					break;
				case Message.Roomowner_Disband_Room:
					BodyClass = AppConfig.proto.Roomowner_Disband_Room;
					break;
				case Message.Nn_Xiazhu:
					BodyClass = AppConfig.proto.Nn_Xiazhu;
					break;
				
					
			}
			message.MSG = BodyClass.encode(BodyClass.create(body)).finish();
			var messageBuffer:* = ProMessage.encode(ProMessage.create(message)).finish();
			return messageBuffer;
		}
	}
}