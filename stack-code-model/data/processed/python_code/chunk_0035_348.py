package modules.srddzGame.srddzInerGame.view.pockerPart.singlePart.handlePart
{
	import laya.events.Event;
	
	import modules.srddzGame.srddzInerGame.model.data.PaixingLogic;
	import modules.srddzGame.srddzInerGame.view.pockerPart.card.BottomHandlePocker;
	
	import ui.srddzGame.ddzPart.handlePart.OwnerHandlePartUI;
	
	/**自己手里的牌的部分*/
	public class BottomSingleHandlePart extends BaseSingleHandlePart
	{
		protected var gap:Number = 55;
		protected var _skin:OwnerHandlePartUI;
		
		public function BottomSingleHandlePart(skin:OwnerHandlePartUI)
		{
			_skin = skin;
			super(skin);
		}
		
		override protected function init():void
		{
			var i:int,len:int=_pockers.length;
			
			for(i=0;i<len;i++)
			{
				_pockers[i] = new BottomHandlePocker(_skin["card"+i]);
			}
			
			Laya.stage.on(Event.MOUSE_DOWN,this,onDownStage);
		}
		
		protected function onDownStage(e:Event):void
		{
			model.isMouseDwon = true;
		}
		
		override public function showCards(cards:Array,dir:int):void
		{
			var pos:int = model.getChairPosByDir(dir);
			//把报到的牌拿出来放到前面
			if(model.baodaoState != 0 && model.dizhuPos == pos)//报到了并且是地主，才需要特殊处理
			{
				cards = cards.concat();
				
				PaixingLogic.cutArrInArr(model.baodaoCards,cards);
				
				PaixingLogic.sortHandleCards(cards);
				PaixingLogic.sortHandleCards(model.baodaoCards);
				
				cards = cards.reverse();
				model.baodaoCards = model.baodaoCards.reverse();
				
				cards = model.baodaoCards.concat(cards);
			}
			else
			{
				PaixingLogic.sortHandleCards(cards);
				cards = cards.reverse();
			}
			
			
			
		
			hideAll();
			
			updateState(model.mingpaiVec[pos]);
			
			var i:int;
			
			for(i=0;i<cards.length;i++)
			{
				_pockers[i].setCardImg(cards[i]);
				_pockers[i].show();
				_pockers[i].select = false;
				_pockers[i].showDizhuImg(false);
				
				if(state == STATE_MINGPAI)
				{
					_pockers[i].down();
				}
				else
				{
					if(model.isSelfSitDown)
					{
						_pockers[i].up();
					}
					else
					{
						if(model.baodaoState != 0 && model.dizhuPos == pos)
						{
							if(i<model.baodaoCards.length)
							{
								_pockers[i].down();
							}
							else
							{
								_pockers[i].back();
							}
							
						}
						else
						{
							_pockers[i].back();
						}
					}
				}
				
			
				
				
				//updateState(model.mingpaiVec[pos]);
				
				if(i == cards.length -1)
				{
					if(pos == model.dizhuPos)
					{
						_pockers[i].showDizhuImg(true);
					}
					_pockers[i].showMingImg(model.mingpaiVec[pos]);
					
				}
				
				//trace("bottom showcards::" +_pockers[i].skin.visible  + " " + _pockers[i].skin.alpha + " " + cards[i]);
			}
			
			if(cards.length <= 17)
			{
				_skin.box1.x = gap*(17-cards.length)/2;
			}
			else
			{
				_skin.box1.x = 0;
			}
			
			
			
		}
		
		override protected function updateState(isMingPai:Boolean):void
		{
			super.updateState(isMingPai);
			
			if(state == STATE_MINGPAI)
			{
				down();
			}
			else
			{
				if(model.isSelfSitDown)
				{
					up();
				}
				else
				{
					back();
				}
			}
		}
		
		override public function set seleCards(cards:Array):void
		{
			var i:int=0,idx:int,temp:int;
			for(i=0;i<_pockers.length;i++)
			{
				_pockers[i].select = false;
				if(_pockers[i].visible)
				{
					temp = _pockers[i].cardIdx;
					idx = cards.indexOf(temp);
					
					if(idx != -1)
					{
						_pockers[i].select = true;
						cards.splice(idx,1);
					}
				}
			}
		}
		
		/**获取选中的牌*/
		override public function get seleCards():Array
		{
			var retArr:Array = [];
			var i:int;
			for(i=0;i<_pockers.length;i++)
			{
				if(_pockers[i].visible == true && _pockers[i].select == true)
				{
					retArr.push(_pockers[i].cardIdx);
				}
			}
			return retArr;
		}
		
		override public function set canControl(bool:Boolean):void
		{
			super.canControl = bool;
		}
		
		
		
		override public function reset():void
		{
			updateState(false);
			super.reset();
		}
		
	}
}