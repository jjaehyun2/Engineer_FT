package modules.game.majiangGame.view.majiangPart.huaPart
{
	import common.tools.SoundPlay;
	
	import laya.media.SoundManager;
	
	import modules.game.GameModule;
	import modules.game.majiangGame.model.MajiangModel;
	
	import ui.mainGame.majiangParts.huaBottomPartUI;
	import ui.mainGame.majiangParts.huaLeftPartUI;
	import ui.mainGame.majiangParts.huaRightPartUI;
	import ui.mainGame.majiangParts.huaTopPartUI;
	
	public class HuaPart
	{
		protected var _bottom:BaseBuhuaPart;
		protected var _right:BaseBuhuaPart;
		protected var _top:BaseBuhuaPart;
		protected var _left:BaseBuhuaPart;
		
		protected var _PosChairVec:Vector.<BaseBuhuaPart> = new Vector.<BaseBuhuaPart>();
		public function HuaPart(bottomSkin:huaBottomPartUI,rightSkin:huaRightPartUI,topSkin:huaTopPartUI,leftSkin:huaLeftPartUI)
		{
			_bottom = new BaseBuhuaPart(bottomSkin);
			_right = new BaseBuhuaPart(rightSkin);
			_top = new BaseBuhuaPart(topSkin);
			_left = new BaseBuhuaPart(leftSkin);
			
			allReset();
		}
		
		protected function allReset():void
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
				case 1:_PosChairVec.push(_bottom);
					break;//一个人自己玩 啊哈哈
				case 2:_PosChairVec.push(_bottom,_top);
					break; //两个人玩
				case 3:_PosChairVec.push(_bottom,_right,_left);
					break;
				case 4:_PosChairVec.push(_bottom,_right,_top,_left);
					break;
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
		
		/**显示一张补花的牌*/
		public function showBuhuaCard(cardIdx:int,pos:int,needShowEff:Boolean,isMopai:Boolean = false,isSound:Boolean=true):void
		{
			var dir:int = model.getChairDirByPos(pos);
			_PosChairVec[dir].showOneCard(pos,cardIdx,needShowEff,isMopai);
			if(isSound==true){
				SoundManager.playSound(SoundPlay.instance.getBuhua(model.playerByPos(model.selfChairPos).sex) , 1);
			}
		}
		
		public function showBuhuaCards(cards:Array,pos:int):void
		{
			var i:int,len:int=cards.length;
			for(i=0;i<len;i++)
			{
				showBuhuaCard(cards[i],pos,false,false,false);
			}
		}
		
		protected function get model():MajiangModel
		{
			return GameModule.instance.gameContext.model;
		}

		public function get PosChairVec():Vector.<BaseBuhuaPart>
		{
			return _PosChairVec;
		}

	}
}