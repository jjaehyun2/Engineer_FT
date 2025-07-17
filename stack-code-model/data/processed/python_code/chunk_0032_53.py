package modules.srddzGame.srddzInerGame.view.pockerPart
{
	import modules.srddzGame.SrddzGameModule;
	import modules.srddzGame.srddzInerGame.model.SrddzModel;
	import modules.srddzGame.srddzInerGame.view.pockerPart.singlePart.outputPart.BaseSingleOutputPart;
	import modules.srddzGame.srddzInerGame.view.pockerPart.singlePart.outputPart.BottomSingleOutputPart;
	import modules.srddzGame.srddzInerGame.view.pockerPart.singlePart.outputPart.LeftSingleOutputPart;
	import modules.srddzGame.srddzInerGame.view.pockerPart.singlePart.outputPart.RightSingleOutputPart;
	
	import ui.srddzGame.ddzPart.outputPart.OtherOutputPartUI;
	import ui.srddzGame.ddzPart.outputPart.OwnerOutputPartUI;

	public class OutputPart
	{
		protected var _bottom:BottomSingleOutputPart;
		protected var _right:RightSingleOutputPart;
		protected var _top:BottomSingleOutputPart;
		protected var _left:LeftSingleOutputPart;
		
		protected var _PosChairVec:Vector.<BaseSingleOutputPart> = new Vector.<BaseSingleOutputPart>();
		
		public function OutputPart(b:OwnerOutputPartUI,r:OtherOutputPartUI,t:OwnerOutputPartUI,l:OtherOutputPartUI)
		{
			_bottom = new BottomSingleOutputPart(b);
			_right = new RightSingleOutputPart(r);
			_top = new BottomSingleOutputPart(t);
			_left = new LeftSingleOutputPart(l);
			
			allReset();
		}
		
		protected function allReset():void
		{
			_bottom.reset();
			_right.reset();
			_top.reset();
			_left.reset();
		}
		
		/**设置椅子数量*/
		public function setChairNum(num:int=4):void
		{
			_PosChairVec.length = 0;
			switch(num)
			{
				case 4:_PosChairVec.push(_bottom,_right,_top,_left);
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
		
		protected function get model():SrddzModel
		{
			return SrddzGameModule.instance.gameContext.model;
		}
	}
}