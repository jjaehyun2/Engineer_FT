package modules.game.majiangGame.view.majiangPart.singlePart
{
	import modules.game.GameModule;
	import modules.game.majiangGame.model.MajiangChiData;
	import modules.game.majiangGame.model.MajiangModel;
	import modules.game.majiangGame.view.card.pengGangCard.BasePengGangCards;

	public class BaseSinglePengGangPart
	{	
		protected var _cardsVec:Vector.<BasePengGangCards> = new Vector.<BasePengGangCards>(4);
		
		/**碰 杠发生的位置*/
		protected var _curIdx:int = -1;
		
		public function BaseSinglePengGangPart()
		{
			
		}
		
		public function show():void
		{
			
		}
		
		public function hide():void
		{
			
		}
		
		public function get visible():Boolean
		{
			return false;
		}
		
		public function chi(chidata:MajiangChiData,providerPos:int=0,chairPos:int=0):void
		{
			if(_curIdx >= _cardsVec.length)
			{
				return;
			}
			
			var arr:Array = [];
			arr.push(chidata.chicard);
			arr = arr.concat(chidata.chicards);
			
			arr.sort(compareFunction);
			
			_curIdx += 1;
			_cardsVec[_curIdx].chi(arr,chidata.chicard,providerPos);
			
			for(var i:int;i<_cardsVec.length;i++)
			{
				_cardsVec[i].updateChengbaoColor(chairPos,providerPos);
			}
			
		}
		
		public function get model():MajiangModel
		{
			return GameModule.instance.gameContext.model;
		}
		
		protected function compareFunction(A:int,B:int):int
		{
			if(A<B)
			{
				return -1;
			}
			else if(A==B)
			{
				return 0;
			}
			else
			{
				return 1;
			}
		}
		
		
		public function peng(cardIdx:int=0,fromdir:int=-1,providerPos:int=0,chairPos:int=0):void
		{
			if(_curIdx >= _cardsVec.length)
			{
				return;
			}
			
			_curIdx += 1;
			_cardsVec[_curIdx].peng(cardIdx,fromdir,providerPos);
			
			for(var i:int;i<_cardsVec.length;i++)
			{
				_cardsVec[i].updateChengbaoColor(chairPos,providerPos);
			}
		}
		
		public function gang(cardIdx:int,type:int,fromdir:int=-1,providerPos:int=0,chairPos:int=0):void
		{
			var isMingGang:Boolean = type == 1 ? false : true;
			var i:int;
			if(type != 0)
			{
				for(i=0;i<_curIdx+1;i++)
				{
					if(_cardsVec[i].cardIdx == cardIdx)
					{
						return;
					}
				}
				if(_curIdx >= _cardsVec.length)
				{
					return;
				}
				_curIdx += 1;
				_cardsVec[_curIdx].gang(cardIdx,isMingGang,fromdir,providerPos);
			}
			else
			{
				for(i=0;i<_curIdx+1;i++)
				{
					if(_cardsVec[i].cardIdx == cardIdx)
					{
						_cardsVec[i].gang(cardIdx,isMingGang,fromdir,providerPos);
						return;
					}
				}
				
				if(_curIdx >= _cardsVec.length)
				{
					return;
				}
				_curIdx += 1;
				_cardsVec[i].gang(cardIdx,isMingGang,fromdir,providerPos);
			}
			
			for(i=0;i<_cardsVec.length;i++)
			{
				_cardsVec[i].updateChengbaoColor(chairPos,providerPos);
			}
		}
		
		/**设置杠牌承包关系*/
		public function setChengbaoGang(cardIdx:int):void
		{
			var i:int=0,len:int=_cardsVec.length;
			for(i=0;i<len;i++)
			{
				if(_cardsVec[i].type == 3 && _cardsVec[i].cardIdx == cardIdx)
				{
					_cardsVec[i].setChengbaoGang();
				}
			}
		}
		
		public function setCardImg(cardIdx:int):void
		{
			_cardsVec[_curIdx].setCardImg(cardIdx);
		}
		
		public function update(pengArr:Array,mingGangArr:Array,anGangArr:Array):void
		{
			reset();
			//todo 不一定需要实现
		}
		
		/**重置*/
		public function reset():void
		{
			var i:int;
			var len:int = _cardsVec.length;
			
			for(i=0;i<len;i++)
			{
				_cardsVec[i].reset();
			}
			
			_curIdx = -1;
		}
		
		public function showHuAni(dir:int,cardIdx:int):void
		{
			var i:int;
			
			for(i=0;i<_curIdx+1;i++)
			{
				if(_cardsVec[i].cardIdx == cardIdx)
				{
					_cardsVec[i].showHuAni(dir);
					
					trace("penggang showHuAni:: i" + i + " dir::" + dir);
					
					break;
				}
			}
		}
		
		/**显示选牌效果*/
		public function showPreDiscardEff(cardIdx:int):void
		{
			var i:int,len:int = _cardsVec.length;
			for(i=0;i<len;i++)
			{
				if(_cardsVec[i].type == 0 || _cardsVec[i].type == 1)
				{
					_cardsVec[i].showPreDiscardEff(cardIdx);
				}
				else
				{
					_cardsVec[i].hidePreDiscardEff();
				}
			}
		}
		
		/**赢藏选牌效果*/
		public function hidePreDiscardEff():void
		{
			var i:int,len:int = _cardsVec.length;
			for(i=0;i<len;i++)
			{
				_cardsVec[i].hidePreDiscardEff();
			}
		}
	}
}