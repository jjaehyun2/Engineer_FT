package modules.xiangshanGame.majiangGame.controller
{
	import common.event.EventCenter;
	
	import modules.game.majiangGame.controller.MajiangGameController;
	import modules.xiangshanGame.majiangGame.model.XiangSMJModel;
	
	public class XiangSMJGameController extends MajiangGameController
	{
		public function XiangSMJGameController()
		{
			super();
		}
		
		/**补花*/
		override public function ACK_TransferHuaResponse(info:Object):void
		{
			if(actived)
			{
				pauseGameQueue();
				if(UserData.isReplay == false)
				{
					Laya.timer.once(500,this,realHuanhua,[info]);
				}
				else
				{
					realHuanhua(info);
				}
				
			}
		}
		
		override public function clearTimeDelay():void
		{
			super.clearTimeDelay();
			Laya.timer.clear(this, realHuanhua);
			
			
			//Laya.timer.clear(this,real_control_game_operation_hu);
			//Laya.timer.clear(this, onDelayCallHu);
			//Laya.timer.clear(this, onDelayCallZhuama);
			
		}
		
		protected function realHuanhua(info:Object):void
		{
			if(UserData.isReplay)
			{
				if(info.index == undefined)
				{
					info.index = 0;
				}
				
				info.huas = info.hua_list;
				info.cards = info.card_ids;
			}
			
			model.majiangMsgs.ACK_TransferHuaResponse = info;
			info.count = info.huas.length;
			info.pos = info.index;
			trace("ACK_TransferHuaResponse");
			trace(info);
			trace("ACK_TransferHuaResponse");
			
			var i:int,len:int = info.huas.length;
			info.Huas = [];
			for(i=0;i<len;i++)
			{
				info.Huas[i] = info.huas[i]+1;
			}
			
			len = info.cards.length;
			info.Cards = [];
			for(i=0;i<len;i++)
			{
				info.Cards[i] = info.cards[i]+1;
			}
			
			
			model.updateBuhua(info.pos,info.Huas,info.Cards);
			
			len = model.huaVec[info.pos].length;
			model.overHuaVec[info.pos] = len;  //用一个数组记录第一轮所有的花牌
			for(i=0;i<len;i++)
			{
				view.majiangPage.showBuhua(model.huaVec[info.pos][i],info.pos,true);
			}
			
			view.playerInfoPage.updateHua(info.pos);
			
			if(info.pos == model.selfChairPos)
			{
				if(UserData.isReplay == false)
				{
					view.majiangPage.handPart.updateOnePosAllCards(info.pos,model.allCardsVec[info.pos]);
				}
			}
			
			if(UserData.isReplay)
			{
				view.majiangPage.handPart.updateOnePosAllCards(info.pos,model.allCardsVec[info.pos]);
			}
			model.leftDesktopCardsNum -= info.count;
			view.majiangPage.clockPart.noticeShowLeftCardsNum();
			
			EventCenter.instance.once(EventCenter.GAME_BUHUAN_COMPLETE,this,contineGameQueue);
//			if(UserData.isReplay)
//			{
//				Laya.timer.once(5000,this,beContineGameQueue);
//			}
			
		}
		
//		protected function beContineGameQueue():void
//		{
//			EventCenter.instance.off(EventCenter.GAME_BUHUAN_COMPLETE,this,contineGameQueue,true);
//			contineGameQueue();
//		}
		
		override protected function seatPingBi(i:int,info):void
		{
			if(info.Cards[i].type == 1)//吃
			{
				var arr:Array = model.getChiCards(i,info.Cards[i].lastCardId+1);
				view.majiangPage.handPart.canControl(i,true,(model as XiangSMJModel).getChiRefCards(arr));
			}
			else
			{
				view.majiangPage.handPart.canControl(i,true,[info.Cards[i].lastCardId+1]);
			}
		}
		
		override protected function pingbiChi(info:Object):void
		{
			view.majiangPage.handPart.canControl(info.pos,true,(model as XiangSMJModel).getChiRefCards(info.chicards));
		}
		
		//todo
	}
}