package modules.srddzGame.srddzInerGame.view.calculate
{
	import laya.events.Event;
	
	import modules.srddzGame.SrddzGameModule;
	import modules.srddzGame.srddzInerGame.model.SrddzModel;
	import modules.srddzGame.srddzInerGame.view.SrddzView;
	
	import ui.srddzGame.calculate.CalculateRoundPageUI;
	
	public class CalculateRoundPart
	{
		protected var _skin:CalculateRoundPageUI;
		
		public function CalculateRoundPart(skin:CalculateRoundPageUI)
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
				SrddzGameModule.instance.gameContext.controller.endGameGotoHall();
			}
			
			//			
		}
		
		
		/**显示并更新界面*/
		public function show():void
		{
			
		}
		
		public function showGetTicketNum(nums:int):void
		{
			
		}
		
		public function hide():void
		{
			_skin.visible = false;
		}
		
		public function reset():void
		{
			_skin.visible = false;
		}
		
		protected function get model():SrddzModel
		{
			return SrddzGameModule.instance.gameContext.model;
		}
		
		protected function get view():SrddzView
		{
			return SrddzGameModule.instance.gameContext.view;
		}
	}
}