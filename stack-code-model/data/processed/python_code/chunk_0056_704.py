package modules.game.majiangGame.view.calculate
{
	import modules.game.GameModule;
	import modules.game.majiangGame.model.MajiangModel;
	import modules.game.majiangGame.view.MajiangGameView;
	
	import laya.events.Event;
	
	import ui.mainGame.majiangParts.Newcalculate.NewCalculateRoundItemUI;
	import ui.mainGame.majiangParts.Newcalculate.NewCalculateRoundPageUI;

	public class CalculateRoundPart
	{
		protected var _skin:NewCalculateRoundPageUI;
		
		protected var _items:Vector.<NewCalculateRoundItemUI> = new Vector.<NewCalculateRoundItemUI>(4);
		public function CalculateRoundPart(skin:NewCalculateRoundPageUI)
		{
			_skin = skin;
			
			reset();
		}
		
		protected function onClickShareBtn(e:Event):void
		{
			//WXLogicModel.shareScreenResult();

		}
		
		protected function onClickBackBtn(e:Event):void
		{
			//切换到大厅
			if(AppConfig.isNewHall)
			{
				QuickUtils.gotoHall();
			}
			else
			{
				GameModule.instance.gameContext.controller.endGameGotoHall();
			}
			
//			
		}
		
		
		/**显示并更新界面*/
		public function show():void
		{
			
		}
		
		public function showGetTicketNum(nums:int):void
		{
			//_skin.getquanlbl.text = nums.toString();
		}
		
		public function hide():void
		{
			_skin.visible = false;
		}
		
		public function reset():void
		{
			_skin.visible = false;
		}
		
		protected function get model():MajiangModel
		{
			return GameModule.instance.gameContext.model;
		}
		
		protected function get view():MajiangGameView
		{
			return GameModule.instance.gameContext.view;
		}
		
	}
}