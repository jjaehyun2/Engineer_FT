package modules.sddzGame.sddzInerGame.view.pockerPart.singlePart.handlePart
{
	
	import laya.events.Event;
	
	import modules.sddzGame.sddzInerGame.model.data.PaixingLogic;
	import modules.sddzGame.sddzInerGame.view.pockerPart.card.BottomHandlePocker;
	
	import ui.sddzGame.ddzPart.handlePart.OwnerHandlePartUI;
	
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
			//Laya.stage.on(Event.MOUSE_UP,this,onUpStage);
		}
		
		protected function onDownStage(e:Event):void
		{
			model.isMouseDwon = true;
		}
		
	
		
		
		
		override public function showCards(cards:Array,dir:int):void
		{
			PaixingLogic.sortHandleCards(cards);
			cards = cards.reverse();
			var pos:int = model.getChairPosByDir(dir);
			
			hideAll();
			
			updateState(model.mingpaiVec[pos]);
			
			var i:int;
			
			for(i=0;i<cards.length;i++)
			{
				_pockers[i].setCardImg(cards[i]);
				_pockers[i].show();
				_pockers[i].select = false;
				_pockers[i].showDizhuImg(false);
				updateState(model.mingpaiVec[pos]);
				
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
			
			if(cards.length > 10)//需要两排
			{
				_skin.box1.x = 0;
			}
			else
			{
				_skin.box1.x = gap*(10-cards.length)/2;
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