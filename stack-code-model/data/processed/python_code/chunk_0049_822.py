package modules.sddzGame.sddzInerGame.view.playerInfoPart
{
	import common.event.EventCenter;
	
	import laya.events.Event;
	
	import modules.sddzGame.SDdzGameModule;
	
	import net.Message;
	import net.ProtoMessage;
	
	import ui.gameCommon.items.GiftItemUI;
	
	public class GiftItem extends GiftItemUI
	{
		protected var tUid:String;
		protected var dat:Object;
		
		public function GiftItem()
		{
			super();
			
			this.on(Event.CLICK,this,onClick);
		}
		
		public function setData(dat:*,tUid):void
		{
			if(dat)
			{
				this.dat = dat;
				this.tUid = tUid;
				
				if(tUid == UserData.uid || SDdzGameModule.instance.gameContext.model.isSelfSitDown == false)
				{
					img.disabled = true;
				}
				else
				{
					img.disabled = false;
				}
					
				img.skin = "ani/"+dat.name+".png";
				
				var price:int = parseInt(dat.price);
				
				if(price > UserData.Diamond)
				{
					costTf.color = "#ff3d01";
				}
				else
				{
					costTf.color = "#2dc509";
				}
				
				costTf.text = dat.price;
			}
		}
		
		protected function onClick(e:Event):void
		{
			if(tUid == UserData.uid)
			{
				return;
			}
			
			if(SDdzGameModule.instance.gameContext.model.isSelfSitDown == false)
			{
				QuickUtils.popMessage("围观用户禁止送礼物！");
				return;
			}
			
			UserInfoPage.instance.hide();
			
			trace("送礼物咯：： id:" + dat.id + "  tUid:"+tUid );
			
			var giftObj:Object = {id:dat.id,tUid:tUid};
			EventCenter.instance.event(EventCenter.SOCKET_SEND,ProtoMessage.getProtoMessage(Message.MSG_Gift,giftObj));
			
			
		}
	}
}