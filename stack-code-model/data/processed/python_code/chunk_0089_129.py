package modules.sddzGame.sddzInerGame.view.pockerPart.singlePart.outputPart
{
	
	import modules.sddzGame.sddzInerGame.model.data.PaixingLogic;
	
	import ui.sddzGame.ddzPart.outputPart.OwnerOutputPartUI;
	
	public class BottomSingleOutputPart extends BaseSingleOutputPart
	{
		protected var _skin:OwnerOutputPartUI;
		
		protected var gap:Number = 40;
		
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
			
			_skin.box.x = gap*(_pockers.length - cards.length)/2;
			
			var i:int;
			for(i=0;i<cards.length;i++)
			{
				_pockers[i].setCardImg(cards[i]);
				_pockers[i].show();
			}
		}
	}
}