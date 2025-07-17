package modules.game.majiangGame.view.card.outputCard
{
	
	import ui.mainGame.Items.OutputRightItemUI;
	
	public class RightOutputCard extends BaseOutputCard
	{
		
		public function RightOutputCard(skin:OutputRightItemUI)
		{
			super(skin);
			
			_skin = skin;
		}
		
		override public function down():void
		{
			if(state == CARCSTATE_DOWN)
			{
				return;
			}
			
			_skin.downImg.visible = true;
			_skin.valueImg.visible = true;
			_skin.backImg.visible = false;
			
			super.down();
		}
		
		override public function back():void
		{
			if(state == CARCSTATE_BACK)
			{
				return;
			}
			
			_skin.downImg.visible = false;
			_skin.valueImg.visible = false;
			_skin.backImg.visible = true;
			
			super.back();
		}
		
		override public function show():void
		{
			_skin.visible = true;
		}
		
		override public function hide():void
		{
			_skin.visible = false;
		}
		
		override public function setCardImg(cardIdx:int):void
		{
			if(this.cardIdx == cardIdx)
			{
				return;
			}
			
			_skin.valueImg.skin = PREPATH + CARD_REFERENCE[cardIdx.toString()];
			
			super.setCardImg(cardIdx);
		}
		
		
	}
}