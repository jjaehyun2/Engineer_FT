package modules.sddzGame.sddzInerGame.view.pockerPart
{
	import modules.sddzGame.SDdzGameModule;
	import modules.sddzGame.sddzInerGame.model.SddzModel;
	import modules.sddzGame.sddzInerGame.view.pockerPart.singlePart.outputPart.BaseSingleOutputPart;
	import modules.sddzGame.sddzInerGame.view.pockerPart.singlePart.outputPart.BottomSingleOutputPart;
	import modules.sddzGame.sddzInerGame.view.pockerPart.singlePart.outputPart.LeftSingleOutputPart;
	import modules.sddzGame.sddzInerGame.view.pockerPart.singlePart.outputPart.RightSingleOutputPart;
	
	import ui.sddzGame.ddzPart.outputPart.OtherOutputPartUI;
	import ui.sddzGame.ddzPart.outputPart.OwnerOutputPartUI;

	/**玩家出出去的牌*/
	public class OutputPart
	{
		protected var _bottom:BottomSingleOutputPart;
		protected var _right:RightSingleOutputPart;
		protected var _left:LeftSingleOutputPart;
		
		protected var _PosChairVec:Vector.<BaseSingleOutputPart> = new Vector.<BaseSingleOutputPart>();
		
		public function OutputPart(bottom:OwnerOutputPartUI,right:OtherOutputPartUI,left:OtherOutputPartUI)
		{
			_bottom = new BottomSingleOutputPart(bottom);
			_right = new RightSingleOutputPart(right);
			_left = new LeftSingleOutputPart(left);
			
			allReset();
		}
		
		protected function allReset():void
		{
			_bottom.reset();
			_right.reset();
			_left.reset();
		}
		
		/**设置椅子数量*/
		public function setChairNum(num:int=3):void
		{
			_PosChairVec.length = 0;
			switch(num)
			{
				case 3:_PosChairVec.push(_bottom,_right,_left);
					break;
			}
		}
		
		/**显示牌*/
		public function showCards(cards:Array,pos:int):void
		{
			if(cards.length == 0)
			{
				return;
			}
			
			var dir:int = model.getChairDirByPos(pos);
			
			var i:int,len:int = _PosChairVec.length;
			for(i=0;i<len;i++)
			{
				if(i == dir)
				{
					_PosChairVec[i].showCards(cards);
				}
			}
		}
		
		/**隐藏牌*/
		public function hideCards(pos:int):void
		{
			var dir:int = model.getChairDirByPos(pos);
			
			var i:int,len:int = _PosChairVec.length;
			for(i=0;i<len;i++)
			{
				if(i == dir)
				{
					_PosChairVec[i].hide();
				}
			}
		}
		
		
		
		/**重置*/
		public function reset():void
		{
			var i:int;
			var len:int = _PosChairVec.length;
			for(i=0;i<len;i++)
			{
				_PosChairVec[i].reset();
			}
		}
		
		protected function get model():SddzModel
		{
			return SDdzGameModule.instance.gameContext.model;
		}
		
	}
}