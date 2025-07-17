package modules.nnGame.inerGame.view.pockerPart.card
{
	import ui.niuniuGame.niuniuPart.item.PockerItemUI;
	
	/**别人手里的牌*/
	public class OtherHandlePocker extends BasePocker
	{
		public function OtherHandlePocker(skin:PockerItemUI)
		{
			super(skin);
		}
		
		override public function up():void
		{
			if(state == STATE_UP)
			{
				return;
			}
			
			skin.valueImg.visible = false;
			skin.backImg.visible  = true;
			
			state = STATE_UP;
		}
		
		override public function back():void
		{
			if(state == STATE_BACK)
			{
				return;
			}
			skin.backImg.visible  = true;
			skin.valueImg.visible = false;
			
			state = STATE_BACK;
		}
		
		override public function down():void
		{
			if(state == STATE_DOWN)
			{
				return;
			}
			skin.backImg.visible  = false;
			skin.valueImg.visible = true;
			
			state = STATE_DOWN;
		}
	}
}