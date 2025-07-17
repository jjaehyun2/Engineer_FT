package modules.game.majiangGame.view.majiangPart.singlePart.pengGangPart
{
	import modules.game.majiangGame.view.card.pengGangCard.LeftPengGangCards;
	import modules.game.majiangGame.view.majiangPart.singlePart.BaseSinglePengGangPart;
	
	import ui.mainGame.majiangParts.LeftPengGangPartUI;
	
	public class LeftSinglePengGangPart extends BaseSinglePengGangPart
	{
		protected var _skin:LeftPengGangPartUI;
		
		public function LeftSinglePengGangPart(skin:LeftPengGangPartUI)
		{
			super();
			
			_skin = skin;
			
			init();
		}
		
		protected function init():void
		{
			var i:int;
			var len:int = _cardsVec.length;
			
			for(i=0;i<len;i++)
			{
				_cardsVec[i] = new LeftPengGangCards(_skin["peng"+i]);
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
	}
}