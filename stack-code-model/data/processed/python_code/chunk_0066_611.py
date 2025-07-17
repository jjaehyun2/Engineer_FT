package modules.srddzGame.srddzInerGame.view
{
	import modules.srddzGame.srddzInerGame.view.pockerPart.ActTipPart;
	import modules.srddzGame.srddzInerGame.view.pockerPart.ClockPart;
	import modules.srddzGame.srddzInerGame.view.pockerPart.DipaiPart;
	import modules.srddzGame.srddzInerGame.view.pockerPart.HandleBtnsPart;
	import modules.srddzGame.srddzInerGame.view.pockerPart.HandlePart;
	import modules.srddzGame.srddzInerGame.view.pockerPart.OutputPart;
	
	import ui.srddzGame.PockerPageUI;

	public class SrddzPage
	{
		protected var _skin:PockerPageUI;

		public function get skin():PockerPageUI
		{
			return _skin;
		}
		
		public var handlePart:HandlePart;
		public var outputPart:OutputPart;
		public var handleBtns:HandleBtnsPart;
		public var dipaiPart:DipaiPart;
		public var clockPart:ClockPart;
		public var actTipPart:ActTipPart;
		
		public function SrddzPage(skin:PockerPageUI)
		{
			if(skin)
			{
				_skin = skin;
				_skin.mouseThrough = true;
				
				handlePart = new HandlePart(_skin.handlePart0,_skin.handlePart1,_skin.handlePart2,_skin.handlePart3);
				outputPart = new OutputPart(_skin.outputPart0,_skin.outputPart1,_skin.outputPart2,_skin.outputPart3);
				handleBtns = new HandleBtnsPart(_skin.ctlPart);
				dipaiPart = new DipaiPart(_skin.dipaiPart);
				clockPart = new ClockPart(_skin.clockPart);
				actTipPart = new ActTipPart(_skin.actTip0,_skin.actTip1,_skin.actTip2,_skin.actTip3);
			}
		}
		
		public function setChairNum(num:int=4):void
		{
			num = 4;//保证一下只有3咯
			handlePart.setChairNum(num);
			outputPart.setChairNum(num);
			clockPart.setChairNum(num);
			actTipPart.setChairNum(num);
		}
		
		public function reset():void 
		{
			handlePart.reset();
			outputPart.reset();
			handleBtns.reset();
			clockPart.reset();
			dipaiPart.reset();
			actTipPart.hideAllActTip();
		}
	}
}