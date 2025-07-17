package modules.game.majiangGame.view.card.handCard
{
	import modules.game.majiangGame.view.card.BaseCard;
	
	import laya.display.Animation;
	import laya.ui.Image;
	
	import ui.mainGame.Items.RightHandleItemUI;

	/**右边的那帮牌*/
	public class RightHandleCard extends BaseCard
	{
		
		protected var tingpaiImg:Image;
		
		public function RightHandleCard(skin:RightHandleItemUI)
		{
			super(skin);
			
			_skin = skin;
			
			tingpaiImg = _skin.LiangEff;
			//loadMingEff();
		}
		
		protected var mingEffAni:Animation;
		
//		protected function loadMingEff():void
//		{
//			tingpaiImg.removeChildren();
//			tingpaiImg.skin= "";
//			
//			mingEffAni = new Animation();
//			mingEffAni.loadAtlas("res/animations/亮牌后效果.json");
//			mingEffAni.stop();
//			tingpaiImg.addChild(mingEffAni);
//		}
		
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
			trace("right ::cardIdx" + cardIdx);
			if(this.cardIdx == cardIdx)
			{
				return;
			}
			
			trace("right ::cardIdx" + cardIdx);
			
			if(CARD_REFERENCE.hasOwnProperty(cardIdx.toString()))
			{
				_skin.valueImg.skin = PREPATH + CARD_REFERENCE[cardIdx.toString()];
			}
			
			super.setCardImg(cardIdx);
		}
		
		override public function reset():void
		{
			super.reset();
			tingpaiImg.visible = false;
			//mingEffAni.stop();
		}
		
		public function showTingEff():void
		{
			tingpaiImg.visible = true;
			//mingEffAni.play();
		}
	}
}