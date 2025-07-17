package modules.game.majiangGame.view.majiangPart.singlePart.handlePart
{
	import modules.game.majiangGame.view.card.handCard.LeftHandleCard;
	import modules.game.majiangGame.view.majiangPart.singlePart.BaseSingleHandlePart;
	
	import ui.mainGame.majiangParts.LeftHandlePartUI;

	public class LeftSingleHandlePart extends BaseSingleHandlePart
	{
		protected var _skin:LeftHandlePartUI;
		
		public function LeftSingleHandlePart(skin:LeftHandlePartUI)
		{
			super(skin);
			_skin = skin;
			
			_OrignalY = _skin.y;
			
			init();
		}
		
		protected function init():void
		{
			_SingleCardH = _skin.card0.height*_skin.scaleX;
			
			var i:int;
			var len:int = _preThirteenCards.length;
			
			for(i=0;i<len;i++)
			{
				_preThirteenCards[i] = new LeftHandleCard(_skin["card"+i]);
				
			}
			_theFourteenCard = new LeftHandleCard(_skin["card13"]);
			
			tingImg = _skin.tingImg;
			
			up();
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
				if(UserData.isReplay)
				{
					_skin.y = _OrignalY + _SingleCardH/2;
				}
				else
				{
					_skin.y = _OrignalY + _SingleCardH;
				}
				
			}
			else
			{
				_skin.y = _OrignalY;
			}
		}
		
		/**显示玩家听了的状态*/
		override public function showTinged():void
		{
			if(needTingEff)
			{
				var i:int;
				var len:int = _preThirteenCards.length;
				
				for(i=0;i<len;i++)
				{
					(_preThirteenCards[i] as LeftHandleCard).showTingEff();
				}
			}
			
			
		}

	}
}