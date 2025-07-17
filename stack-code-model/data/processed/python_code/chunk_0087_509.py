package modules.game.majiangGame.view.card.hupartCard
{
	import modules.game.majiangGame.view.card.BaseCard;

	public class HuaItemCard extends BaseCard
	{
		public function HuaItemCard(skin:*)
		{
			super(skin);
		}
		
		private var nowNum:int = 1;
		
		public const path:String = "gametable/mahjongpai/";
		
//		public const HUA_IMAGE:Object = {
//			32:"huazhong.png",33:"huafa.png",34:"huabai.png",
//			28:"huadong.png",29:"huanan.png",30:"huaxi.png",31:"huajbei.png",
//			35:"huachun.png",36:"huaxia.png",37:"huaqiu.png",38:"huajdong.png",
//			39:"huamei.png",40:"hualan.png",41:"huazhu.png",42:"huaju.png"
//		};
		
		public const HUA_IMAGE:Object = {
			32:"zzhong.png",33:"zfa.png",34:"zbai.png",
			28:"zdong.png",29:"hjdong.png",30:"zxi.png",31:"zbei.png",
			35:"hchun.png",36:"hxia.png",37:"hqiu.png",38:"hjdong.png",
			39:"hmei.png",40:"hlan.png",41:"hzhu.png",42:"hju.png"
		};
		
		override public function down():void
		{
			if(state == CARCSTATE_DOWN)
			{
				return;
			}
		
			_skin.downImg.visible = true;
			_skin.valueImg.visible = true;
//			_skin.valueNum.visible = true;
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
//			_skin.valueNum.visible = true;
			super.back();
		}
		
		override public function show():void
		{
			_skin.downImg.visible = true;
			_skin.valueImg.visible = true;
//			_skin.valueNum.visible = true;
			_skin.visible = true;
		}
		
		override public function hide():void
		{
			_skin.downImg.visible = false;
			_skin.valueImg.visible = false;
//			_skin.valueNum.visible = false;
			_skin.visible = false;
			nowNum = 0
			this.cardIdx = 0;
		}
		
		override public function setCardImg(cardIdx:int):void
		{
			if(this.cardIdx == cardIdx)
			{
				return;
			}
			_skin.valueImg.skin = path + HUA_IMAGE[cardIdx.toString()];
			super.setCardImg(cardIdx);
		}
		
		public function setNum():void{
			if(nowNum == 4)return;
			nowNum ++;
//			_skin.valueNum.skin = path + getNumUrl(nowNum);
		}
		
		private function getNumUrl(num:int):String{
			var url:String = "";
				switch(num){
					case 1:
						url = "hua1.png";
						break;
					case 2:
						url = "hua2.png";
						break;
					case 3:
						url = "hua3.png";
						break;
					case 4:
						url = "hua4.png";
						break;
				}
			return url;
		}		
	
	
	}
}