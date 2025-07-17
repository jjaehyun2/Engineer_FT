package modules.srddzGame.srddzInerGame.view.pockerPart.singlePart.outputPart
{
	
	import modules.srddzGame.srddzInerGame.model.data.PaixingLogic;
	
	import ui.srddzGame.ddzPart.outputPart.OwnerOutputPartUI;
	
	public class BottomSingleOutputPart extends BaseSingleOutputPart
	{
		protected var _skin:OwnerOutputPartUI;
		
		protected var gap:Number = 30;
		
		public function BottomSingleOutputPart(skin:OwnerOutputPartUI)
		{
			_skin = skin;
			super(skin);
		}
		
		override public function showCards(cards:Array):void
		{
			show();
			cards = PaixingLogic.sortOutputCards(cards);
			
			hideAll();
			
			if(cards.length < _pockers.length/2)
			{
				_skin.box.x = gap*(_pockers.length/2 - cards.length)/2;
			}
			else
			{
				_skin.box.x = 0;
			}
			
			
			var i:int;
			for(i=0;i<cards.length;i++)
			{
				_pockers[i].setCardImg(cards[i]);
				_pockers[i].show();
			}
			
		}
	}
}