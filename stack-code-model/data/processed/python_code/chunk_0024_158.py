package modules.game.majiangGame.view.majiangPart.hupaiTip
{
	import modules.game.majiangGame.view.card.outputCard.RightOutputCard;
	
	import laya.ui.View;
	
	public class RightHupaiTipPart extends BaseSingleHupaiTipPart
	{
		public function RightHupaiTipPart(skin:View)
		{
			super(skin);
			init();
		}
		
		private function init():void
		{
			for(var i:int=0;i < 9;i++)
			{
				allCards[i] = new RightOutputCard(_skin["card"+i]);
			}
		}
		override protected function setBackSize(nums:int):void
		{
			_skin["backimg"].height = 411 - (9-nums)*(SingleCardH-11);
			
			_skin["liangImg"].y = _skin["backimg"].y + _skin["backimg"].height;
		}
	}
}