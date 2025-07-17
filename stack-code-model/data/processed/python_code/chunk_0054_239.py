package modules.game.majiangGame.view.card.pengGangCard
{
	import modules.game.majiangGame.view.card.outputCard.TopOutputCard;
	
	import ui.mainGame.Items.TopPengGangItemUI;

	public class TopPengGangCards extends BasePengGangCards
	{
		protected var _skin:*;
		
		public function TopPengGangCards(skin:*)
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
				_cardsVec[i] = new TopOutputCard(_skin["card"+i]);
			}
		}
		
		override public function show():void
		{
			_skin.visible = true;
			
			super.show();
		}
		
		override public function hide():void
		{
			_skin.visible = false;
			
			super.hide();
		}
		
		override public function get visible():Boolean
		{
			return _skin.visible;
		}
	}
}