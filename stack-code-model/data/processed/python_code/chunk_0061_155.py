package modules.game.majiangGame.view.majiangPart
{
	import modules.game.GameModule;
	import modules.game.majiangGame.model.MajiangModel;
	import modules.game.majiangGame.view.majiangPart.hupaiTip.BaseSingleHupaiTipPart;
	import modules.game.majiangGame.view.majiangPart.hupaiTip.BottomHupaiTipPart;
	import modules.game.majiangGame.view.majiangPart.hupaiTip.LeftHupaiTipPart;
	import modules.game.majiangGame.view.majiangPart.hupaiTip.RightHupaiTipPart;
	
	import laya.ui.View;

	public class HupaiTipPart
	{
		protected var _bottom:BaseSingleHupaiTipPart;
		protected var _right:BaseSingleHupaiTipPart;
		protected var _top:BaseSingleHupaiTipPart;
		protected var _left:BaseSingleHupaiTipPart;
		
		protected var _PosChairVec:Vector.<BaseSingleHupaiTipPart> = new Vector.<BaseSingleHupaiTipPart>();
		
		public function HupaiTipPart(bottomSkin:View,rightSkin:View,topSkin:View,leftSkin:View)
		{
			_bottom = new BottomHupaiTipPart(bottomSkin);
			_right = new RightHupaiTipPart(rightSkin);
			_top = new BaseSingleHupaiTipPart(topSkin);
			_left = new LeftHupaiTipPart(leftSkin);
			
			setChairNum(model.chairNum);
			allReset();
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
			
			//reset();
		}
		
		public function cancelShowHuTip(pos:int):void
		{
			_PosChairVec[model.getChairDirByPos(pos)].reset();
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
		
		public function showHuTip(pos:int,cards:Array):void
		{
			if(UserData.roomtype == 11)
			{
				_PosChairVec[model.getChairDirByPos(pos)].showHuTip(cards);
			}
			else
			{
				if(model.getChairDirByPos(pos) == 0)
				{
					_PosChairVec[model.getChairDirByPos(pos)].showHuTip(cards);
				}
			}
			
			
				
		}
		
		/**显示可以胡哪些些牌的提示*/
		public function showCanHuCards(pos:int,cards:Array):void
		{
			_PosChairVec[model.getChairDirByPos(pos)].showCanHuCards(cards);
		}
		
		
		public function cancelTingpai(pos:int):void
		{
			_PosChairVec[model.getChairDirByPos(pos)].reset();
		}
		protected function allReset():void
		{
			_bottom.reset();
			_right.reset();
			_top.reset();
			_left.reset();
		}
		
		protected function get model():MajiangModel
		{
			return GameModule.instance.gameContext.model;
		}
	}
}