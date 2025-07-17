package modules.game.majiangGame.view
{
	import common.CommonModule;
	
	import laya.events.Event;
	
	import modules.game.GameModule;
	import modules.game.majiangGame.model.MajiangModel;
	import modules.game.majiangGame.view.calculate.CalculatePerPart;
	import modules.game.majiangGame.view.calculate.CalculateRoundPart;
	
	import ui.mainGame.NewCalculatePageUI;

	public class CalculatePage
	{
		protected var _skin:NewCalculatePageUI;
		
		protected var _perPage:CalculatePerPart;

		public function get perPage():CalculatePerPart
		{
			return _perPage;
		}

		protected var _roundPage:CalculateRoundPart;
		
		
		public function CalculatePage(skin:NewCalculatePageUI)
		{
			_skin = skin;
			
			_perPage = new CalculatePerPart(_skin.perPage);
			_roundPage = new CalculateRoundPart(_skin.roundPage);
			
			reset();
			
			//TimeManager.instance.timer.loop(1000,this,updateTime);
			_skin.showBtn.on(Event.CLICK,this,this.showPerCal)
//			updateTime();
		}
		public function showPerShowBtn():void
		{
			_skin.showBtn.visible=true;	
		}
//		protected function updateTime():void
//		{
//			
//		}
		
		private function showPerCal():void
		{
			_skin.perPage.visible=true;
			_skin.showBtn.visible=false;	
		}
		
		public function showGetTicket(nums:int):void
		{
			_roundPage.showGetTicketNum(nums);
		}
		
		public function show():void
		{
			if(UserData.isReplay)
			{
				view.replayControlView.moveCalculate();
			}
			
			_perPage.reset();
			_roundPage.reset();
			_skin.visible = true;
			_perPage.show();
			//GameModule.instance.gameContext.view.timeWar.hide();
			CommonModule.instance.commonContext.view.timeWarView.hide();
			//CommonModule.instance.commonContext.view.onRemove();
			
		}
		
		public function gameTimeOver():void
		{
			_perPage.timeOver();
		}
		
		
//		/**显示最终的结算界面*/
//		public function showRound():void
//		{
//			_perPage.reset();
//			_roundPage.reset();
//			_skin.visible = true;
//			_roundPage.show();
//		}
		
		public function reset():void
		{
			_skin.visible = false;
			_skin.showBtn.visible=false;
			_perPage.reset();
			_roundPage.reset();
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