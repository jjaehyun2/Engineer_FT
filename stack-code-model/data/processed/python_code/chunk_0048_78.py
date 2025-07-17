package modules.game.majiangGame.view.majiangPart
{
	
	import modules.game.GameModule;
	import modules.game.majiangGame.model.MajiangChiData;
	import modules.game.majiangGame.model.MajiangModel;
	import modules.game.majiangGame.view.majiangPart.singlePart.BaseSinglePengGangPart;
	import modules.game.majiangGame.view.majiangPart.singlePart.pengGangPart.BottomSinglePengGangPart;
	import modules.game.majiangGame.view.majiangPart.singlePart.pengGangPart.LeftSinglePengGangPart;
	import modules.game.majiangGame.view.majiangPart.singlePart.pengGangPart.RightSinglePengGangPart;
	import modules.game.majiangGame.view.majiangPart.singlePart.pengGangPart.TopSinglePengGangPart;
	
	import ui.mainGame.majiangParts.BottomPengGangPartUI;
	import ui.mainGame.majiangParts.LeftPengGangPartUI;
	import ui.mainGame.majiangParts.RightPengGangPartUI;
	import ui.mainGame.majiangParts.TopPengGangPartUI;

	/**碰 杠的那一部分*/
	public class PengGangPart
	{
		protected var _bottom:BottomSinglePengGangPart;
		protected var _right:RightSinglePengGangPart;
		protected var _top:TopSinglePengGangPart;
		protected var _left:LeftSinglePengGangPart;
		
		protected var _PosChairVec:Vector.<BaseSinglePengGangPart> = new Vector.<BaseSinglePengGangPart>();
		
		
		public function PengGangPart(bottomSkin:BottomPengGangPartUI,rightSkin:RightPengGangPartUI,
									 topSkin:TopPengGangPartUI,leftSkin:LeftPengGangPartUI)
		{
			_bottom = new BottomSinglePengGangPart(bottomSkin);
			_right = new RightSinglePengGangPart(rightSkin);
			_top = new TopSinglePengGangPart(topSkin);
			_left = new LeftSinglePengGangPart(leftSkin);
			
			allReset();
		}
		
		public function allReset():void
		{
			_bottom.reset();
			_right.reset();
			_top.reset();
			_left.reset();
		}
		
		/**设置椅子数量*/
		public function setChairNum(num:int=3):void
		{
			_PosChairVec.length = 0;
			switch(num)
			{
				case 1:_PosChairVec.push(_bottom);break;//一个人自己玩 啊哈哈
				case 2:_PosChairVec.push(_bottom,_top);break; //两个人玩
				case 3:_PosChairVec.push(_bottom,_right,_left);break;
				case 4:_PosChairVec.push(_bottom,_right,_top,_left);break;
				default:_PosChairVec.push(_bottom,_right,_left);break;
			}
		}
		
		/**重置*/
		public function reset():void
		{
			var i:int;
			var len:int = _PosChairVec.length;
			for(i=0;i<len;i++)
			{
				_PosChairVec[i].reset();
			}
		}
		
		
		/**吃*/
		public function chi(chidata:MajiangChiData,chairPos:int):void
		{
			_PosChairVec[model.getChairDirByPos(chairPos)].chi(chidata,(model.chairNum + chairPos-1)%model.chairNum,chairPos);
		}
		
		public function recoveryChi(chidatas:Array,chairPos:int):void
		{
			for(var i:int = 0;i<chidatas.length;i++)
			{
				chi(chidatas[i],chairPos);
			}
			
		}
		
		/**碰*/
		public function peng(cardIdx:int,chairPos:int,providerPos:int=0):void
		{
			var dir:int = (model.chairNum + providerPos - chairPos)%model.chairNum;
			//var dir:int = model.getChairDirByPos(providerPos);
			_PosChairVec[model.getChairDirByPos(chairPos)].peng(cardIdx,dir,providerPos,chairPos);
		}
		
		public function recoveryPeng(cards:Array,chairPos:int,providers:Array):void
		{
			for(var i:int=0;i<cards.length;i++)
			{
				peng(cards[i],chairPos,providers[i]);
			}
		}
		
		/**杠*/
		public function gang(cardIdx:int,chairPos:int,type:int,providerPos:int=0):void
		{
			var dir:int = (model.chairNum + providerPos - chairPos)%model.chairNum;
			_PosChairVec[model.getChairDirByPos(chairPos)].gang(cardIdx,type,dir,providerPos,chairPos);
		}
		
		public function recoveryGang(cards:Array,chairPos,type,providers:Array):void
		{
			for(var i:int=0;i<cards.length;i++)
			{
				gang(cards[i],chairPos,type,providers[i]);
			}
		}
		
		public function setChengbaoGang(cardIdx:int,chairPos:int):void
		{
			_PosChairVec[model.getChairDirByPos(chairPos)].setChengbaoGang(cardIdx);
		}
		
		protected function get model():MajiangModel
		{
			return GameModule.instance.gameContext.model;
		}
		
		/**显示抢杠胡牌的闪电*/
		public function showHuAni(pos:int,cardIdx:int):void
		{
			var dir:int = model.getChairDirByPos(pos);
			
			_PosChairVec[dir].showHuAni(dir,cardIdx);
		}
		
		/**显示选牌效果*/
		public function showPreDiscardEff(cardIdx:int):void
		{
			var i:int,len:int=model.chairNum;
			for(i=0;i<len;i++)
			{
				_PosChairVec[i].showPreDiscardEff(cardIdx);
			}
		}
		
		/**赢藏选牌效果*/
		public function hidePreDiscardEff():void
		{
			var i:int,len:int=model.chairNum;
			for(i=0;i<len;i++)
			{
				_PosChairVec[i].hidePreDiscardEff();
			}
			
		}
	}
}