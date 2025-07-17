package modules.game.majiangGame.view.card.handCard
{
	import ui.mainGame.Items.TopHandleItemUI;
	import modules.game.majiangGame.view.card.BaseCard;

	public class TopHandleCard extends BaseCard
	{
		
		public function TopHandleCard(skin:TopHandleItemUI)
		{
			super(skin);
			
			_skin = skin;
		}
		
		override public function up():void
		{
			if(state == CARCSTATE_UP)
			{
				return;
			}
			
			_skin.frontImg.visible = true;
			_skin.valueImg.visible = false;
			_skin.backImg.visible = false;
			_skin.downImg.visible = false;
			
			super.up();
		}
		
		override public function down():void
		{
			if(state == CARCSTATE_DOWN)
			{
				return;
			}
			
			
			_skin.frontImg.visible = false;
			_skin.valueImg.visible = true;
			_skin.backImg.visible = false;
			_skin.downImg.visible = true;
			
			super.down();
		}
		
		override public function back():void
		{
			if(state == CARCSTATE_BACK)
			{
				return;
			}
			
			_skin.frontImg.visible = false;
			_skin.valueImg.visible = false;
			_skin.backImg.visible = true;
			_skin.downImg.visible = false;
			
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
			trace("top ::cardIdx" + cardIdx);
			if(this.cardIdx == cardIdx)
			{
				return;
			}
			
			trace("top ::cardIdx" + cardIdx);
			
			if(CARD_REFERENCE.hasOwnProperty(cardIdx.toString()))
			{
				_skin.valueImg.skin = PREPATH + CARD_REFERENCE[cardIdx.toString()];
			}
			
			super.setCardImg(cardIdx);
		}
	}
}