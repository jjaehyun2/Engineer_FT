package modules.game.majiangGame.view.majiangPart.singlePart.handlePart
{
	import modules.game.majiangGame.view.card.handCard.BottomHandleCard;
	import modules.game.majiangGame.view.majiangPart.singlePart.BaseSingleHandlePart;
	
	import ui.mainGame.majiangParts.BottomHandlePartUI;

	public class BottomSingleHandlePart extends BaseSingleHandlePart
	{
		protected var _skin:BottomHandlePartUI;
		
		protected var needAlpha:Boolean = true;
		
	
		
		public function BottomSingleHandlePart(skin:BottomHandlePartUI,needAlpha:Boolean=true)
		{
			super(skin);
			
			_skin = skin;
			tingImg = skin.tingImg;
			
			_OrignalX = _skin.x;
			
			this.needAlpha = needAlpha;
			
			init();
		}
		
		protected function init():void
		{
			_SingleCardW = _skin.card0.width*_skin.scaleX;
			var i:int;
			var len:int = _preThirteenCards.length;
			
			for(i=0;i<len;i++)
			{
				_preThirteenCards[i] = new BottomHandleCard(_skin["card"+i],needAlpha);
				
			}
			_theFourteenCard = new BottomHandleCard(_skin["card13"],needAlpha);
			
			canControl = false;
		}
		
		override public function judegCanTingOut(cardIdx):Boolean
		{
			
			if(model.TingHuCardVec[model.getChairPosByDir(1)].indexOf(cardIdx) != -1 ||
				model.TingHuCardVec[model.getChairPosByDir(2)].indexOf(cardIdx) != -1)//找到了
			{
				return true;
			}
			return false;
		}
		
		
		override public function set canControl(bool:Boolean):void
		{
			var i:int;
			var len:int = _preThirteenCards.length;
			
			var cardIdx:int = 0;
			var isAllCannotPop:Boolean = true;
			
			for(i=0;i<len;i++)
			{
				if(model && model.isTingVec[model.selfChairPos] == true)//自己听了前面的牌就不能操作啦
				{
					_preThirteenCards[i].canControl = false;
				}
				else
				{
					if(bool == true)
					{
						cardIdx = _preThirteenCards[i].cardIdx;
						
						if(model.TingHuCardVec[model.getChairPosByDir(1)].indexOf(cardIdx) != -1 ||
							model.TingHuCardVec[model.getChairPosByDir(2)].indexOf(cardIdx) != -1)//找到了
						{
							_preThirteenCards[i].canControl = false;
						}
						else
						{
							_preThirteenCards[i].canControl = true;
							
							if(_preThirteenCards[i].visible)
							{
								isAllCannotPop = false;
							}
						}
					}
					else
					{
						_preThirteenCards[i].canControl = bool;
					}
				}
			}
			
			if(bool == true)
			{
				cardIdx = _theFourteenCard.cardIdx;
				
				if(model.TingHuCardVec[model.getChairPosByDir(1)].indexOf(cardIdx) != -1 ||
					model.TingHuCardVec[model.getChairPosByDir(2)].indexOf(cardIdx) != -1)//找到了
				{
					_theFourteenCard.canControl = false;
				}
				else
				{
					_theFourteenCard.canControl = true;
					
					if(_theFourteenCard.visible)
					{
						isAllCannotPop = false;
					}
				}
			}
			else
			{
				_theFourteenCard.canControl = bool;
			}
			
			if(isAllCannotPop == true && bool == true)
			{
				for(i=0;i<len;i++)
				{
					if(model && model.isTingVec[model.selfChairPos] == true)//自己听了前面的牌就不能操作啦
					{
						_preThirteenCards[i].canControl = false;
					}
					else
					{
						_preThirteenCards[i].canControl = bool;
					}
					
				}
				_theFourteenCard.canControl = bool;
			}
			
			
		}
		
		/**承包关系，设置手里某张牌不能出*/
		override public function canControlWitchDark(cards:Array):void
		{
			var bool:Boolean = true;
			var i:int;
			var len:int = _preThirteenCards.length;
			
			var cardIdx:int = 0;
			var isAllCannotPop:Boolean = true;
			
			for(i=0;i<len;i++)
			{
				cardIdx = _preThirteenCards[i].cardIdx;
				
				if(cards.indexOf(cardIdx) != -1)//找到了
				{
					_preThirteenCards[i].canControlWitchDark = false;
				}
			}
			
			if(bool == true)
			{
				cardIdx = _theFourteenCard.cardIdx;
				
				if(cards.indexOf(cardIdx) != -1)//找到了
				{
					_theFourteenCard.canControlWitchDark = false;
				}
			}
			
		}
		
		override public function show():void
		{
			_skin.visible = true;
		}
		
		
		override public function hide():void
		{
			_skin.visible = false;
		}
		
		override public function get visible():Boolean
		{
			return _skin.visible;
		}
		
		override public function movePeng(bool:Boolean):void
		{
			if(bool)
			{
				_skin.x = _OrignalX + _SingleCardW;
			}
			else
			{
				_skin.x = _OrignalX;
			}
		}
		
		override public function setTingImgXAndW(cardNum:int):void
		{
			tingImg.x = (13 - cardNum)*(_SingleCardW+1);
			tingImg.width = 1014 - tingImg.x;
		}
		
		
		override public function judgeEveryCanTing():void
		{
			super.judgeEveryCanTing();
			
			if(model.isHu)
			{
				return;
			}
			
			trace("judgeEveryCanTing");
			var i:int;
			var len:int = _preThirteenCards.length;
			
			var cardIdx:int =-1;
			var arr:Array;
			
			for(i=0;i<len;i++)
			{
				if(_preThirteenCards[i].visible == true)
				{
					if(model.isTingVec[model.getChairPosByDir(0)] == true)
					{
						_preThirteenCards[i].showCanTingImg(false);
					}
					else
					{
						cardIdx = _preThirteenCards[i].cardIdx;
						
						arr = model.getHuTipArr(cardIdx);
						
						if(arr.length > 0)
						{
							_preThirteenCards[i].showCanTingImg(true);
						}
						else
						{
							_preThirteenCards[i].showCanTingImg(false);
						}
					}
					
					
				}
			}
			
			if(model.isTingVec[model.getChairPosByDir(0)] == true)
			{
				_theFourteenCard.showCanTingImg(false);
			}
			else
			{
				if(_theFourteenCard.visible == true)
				{
					cardIdx = _theFourteenCard.cardIdx;
					
					arr = model.getHuTipArr(cardIdx);
					if(arr.length > 0)
					{
						_theFourteenCard.showCanTingImg(true);
					}
					else
					{
						_theFourteenCard.showCanTingImg(false);
					}
				}
			}
			
			
		}
	}
}