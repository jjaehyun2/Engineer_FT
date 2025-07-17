package modules.sddzGame.sddzInerGame.view.pockerPart.singlePart.outputPart
{
	import laya.ui.View;
	
	import modules.sddzGame.SDdzGameModule;
	import modules.sddzGame.sddzInerGame.model.SddzModel;
	import modules.sddzGame.sddzInerGame.view.pockerPart.card.BasePocker;

	/**玩家出牌的类*/
	public class BaseSingleOutputPart
	{
		public var _pockers:Vector.<BasePocker> = new Vector.<BasePocker>(20);
		
		public var skin:View;
		
		/**第一组牌*/
		protected var firstList:Array = [];
		
		/**第二组牌*/
		protected var secondList:Array = [];
		
		public function BaseSingleOutputPart(skin:View)
		{
			this.skin = skin;
			init();
		}
		
		protected function init():void
		{
			var i:int,len:int=_pockers.length;
			
			for(i=0;i<len;i++){
				_pockers[i] = new BasePocker(skin["card"+i]);
			}
			hide();
		}
		
		public function showCards(cards:Array):void
		{
			
		}
		
		public function show():void
		{
			skin.visible = true;
		}
		
		public function hide():void
		{
			skin.visible = false;
		}
		
		public function get visible():Boolean
		{
			return skin.visible;
		}
		
		protected function hideAll():void
		{
			var i:int;
			for(i=0;i<_pockers.length;i++)
			{
				_pockers[i].hide();
			}
		}
	
		
		/**重置*/
		public function reset():void
		{
			hide();
			var i:int;
			for(i=0;i<_pockers.length;i++)
			{
				_pockers[i].reset();
				_pockers[i].down();
			}
		}
		
		
		protected function get model():SddzModel
		{
			return SDdzGameModule.instance.gameContext.model;
		}
		
		
		
	}
}