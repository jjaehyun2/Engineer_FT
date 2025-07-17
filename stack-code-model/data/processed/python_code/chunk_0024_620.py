package modules.game.majiangGame.view.calculate.item
{
	import laya.display.Sprite;
	import laya.ui.Image;
	
	import modules.game.GameModule;
	import modules.game.majiangGame.model.MajiangModel;
	import modules.game.majiangGame.view.majiangPart.singlePart.handlePart.BottomSingleHandlePart;
	import modules.game.majiangGame.view.majiangPart.singlePart.pengGangPart.BottomSinglePengGangPart;
	
	import ui.mainGame.majiangParts.Newcalculate.CalculatePerItemUI;

	public class CalculatePerCardItem
	{
		protected var headImg:Image;
		private var headw:Number=0,headh:Number=0;
		
		protected var _skin:CalculatePerItemUI;
		
		protected var _huPengCards:BottomSinglePengGangPart;
		protected var _huHandleCards:BottomSingleHandlePart;
		
		public function CalculatePerCardItem(skin:CalculatePerItemUI)
		{
			_skin = skin;
			
			_huPengCards = new BottomSinglePengGangPart(_skin.pengGangCards);
			_huHandleCards = new BottomSingleHandlePart(_skin.handCards,false);
			
			headImg = _skin.headImg;
			headw = headImg.width;
			headh = headImg.height;
			
		}
		
		public function update(pos:int):void
		{
			var jiesuanObj:Object = model.majiangMsgs.ACKBC_Total;
			var huPlayer:Object = model.playerByPos(pos);
			
			if(huPlayer.Icon != "")
			{
				var photo:Sprite=new Sprite();
				photo.loadImage(huPlayer.Icon,0,0,headw,headh);//AppConfig.httpPhotoUrl+obj.uid
				photo.mouseEnabled=true;
				headImg.addChild(photo);
			}
			//显示牌
			updateCars(pos);
			//显示牌型
			if(jiesuanObj.Msg && jiesuanObj.Msg[pos])
			{
				_skin.paixingTf.text = jiesuanObj.Msg[pos];
			}
			else
			{
				_skin.paixingTf.text = "";
			}
			
			if(jiesuanObj.Tai && jiesuanObj.Tai[pos])
			{
				_skin.taishuTf.text = "（合计："+jiesuanObj.Tai[pos]+"台）";
			}
			else
			{
				_skin.taishuTf.text = "";
			}
		}
		
		private function updateCars(pos:int):void
		{
			_skin.visible = true;
			
			var info:Object = model.majiangMsgs.ACKBC_Total;
			if(info.attached)
			{
				var attachInfo:Object = JSON.parse(info.attached);
			}
			
			//先把这个位置玩家碰杠的牌展示出来
			var totalPengGangNum:int = 0;
			
			var i:int = 0;
			var len:int;
			
			if(model.anGangVec[pos])
			{
				len = model.anGangVec[pos].length;
			}
			else
			{
				len = 0;
			}
			
			for(i=0;i<len;i++)
			{
				var dir:int = (model.chairNum + model.anGangFromVec[pos][i] - pos)%model.chairNum;
				_huPengCards.gang(model.anGangVec[pos][i],1,dir,model.anGangFromVec[pos][i],pos);
			}
			
			totalPengGangNum += len;
			
			if(model.mingGangVec[pos])
			{
				len = model.mingGangVec[pos].length;
			}
			else
			{
				len = 0;
			}
			
			for(i=0;i<len;i++)
			{
				var dir1:int = (model.chairNum + model.mingGangFromVec[pos][i] - pos)%model.chairNum;
				_huPengCards.gang(model.mingGangVec[pos][i],2,dir1,model.mingGangFromVec[pos][i],pos);
				
				if(attachInfo)
				{
					if(pos == attachInfo.index && parseInt(attachInfo.cid)+1 == model.mingGangVec[pos][i])
					{
						_huPengCards.setChengbaoGang(model.mingGangVec[pos][i]);
					}
				}
			}
			totalPengGangNum += len;
			
			if(model.chiVec[pos])
			{
				len = model.chiVec[pos].length;
			}
			else
			{
				len = 0;
			}
			for(i=0;i<len;i++)
			{
				_huPengCards.chi(model.chiVec[pos][i],model.chiFromVec[pos][i],pos);
			}
			totalPengGangNum += len;
			
			
			if(model.pengVec[pos])
			{
				len = model.pengVec[pos].length;
			}
			else
			{
				len = 0;
			}
			
			for(i=0;i<len;i++)
			{
				var dir:int = (model.chairNum + model.pengFromVec[pos][i] - pos)%model.chairNum;
				_huPengCards.peng(model.pengVec[pos][i],dir,model.pengFromVec[pos][i],pos);
			}
			totalPengGangNum += len;
			
			_skin.handCards.x = _skin.pengGangCards.x + totalPengGangNum*20;
			
			_huHandleCards.setPreThirteenCards(model.allCardsVec[pos],model.getChairDirByPos(pos),false,false);
			_huHandleCards.setTheFourteenCard(model.majiangMsgs.ACKBC_Total.WinCard+1,model.getChairDirByPos(pos));
			_huHandleCards.canControl = false;
		}
		
		public function reset():void
		{
			_skin.visible = false;
			_huPengCards.reset();
			_huHandleCards.reset();
		}
		
		protected function get model():MajiangModel
		{
			return GameModule.instance.gameContext.model;
		}
	}
}