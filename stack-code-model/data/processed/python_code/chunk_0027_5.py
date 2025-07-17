package modules.srddzGame.srddzInerGame.view.pockerPart.singlePart
{
	import ui.srddzGame.ddzPart.ActTipUI;

	public class BaseActTipItem
	{
		public static const ACTTIP_BUJIAO:int = 0;
		public static const ACTTIP_FEN1:int = 1;
		public static const ACTTIP_FEN2:int = 2;
		public static const ACTTIP_FEN3:int = 3;
		
		public static const ACTTIP_BUCHU:int = 4;
		
		public static const ACTTIP_JIABEI:int = 5;
		public static const ACTTIP_BUJIABEI:int = 6;
		
		
		protected var _skin:ActTipUI;
		
		public function BaseActTipItem(skin:ActTipUI)
		{
			_skin = skin;
			init();
		}
		protected function init():void
		{
			reset();
		}
		
		public function hideAll():void
		{
			reset();
		}
		
		/***/
		public function showActTip(type:int):void
		{
			hideAll();
			switch(type)
			{
				case ACTTIP_BUJIAO:
					_skin.bujiao.visible = true;
					break;
				case ACTTIP_FEN1:
					_skin.dang1.visible = true;
					break;
				case ACTTIP_FEN2:
					_skin.dang2.visible = true;
					break;
				case ACTTIP_FEN3:
					_skin.dang3.visible = true;
					break;
				case ACTTIP_BUCHU:
					_skin.buchu.visible = true;
					break;
			}
		}
		
		
		/**叫分完成以后要清除所有 加倍明牌选择完成以后要清除所有 */
		public function reset():void
		{
			_skin.bujiao.visible = false;
			_skin.dang1.visible = false;
			_skin.dang2.visible = false;
			_skin.dang3.visible = false;
			
			_skin.buchu.visible = false;
		}
		
		public function show():void
		{
			_skin.visible = true;
		}
		
		public function hide():void
		{
			_skin.visible = false;
		}
		
		public function showEff(type:int):void
		{
			
		}
	}
}