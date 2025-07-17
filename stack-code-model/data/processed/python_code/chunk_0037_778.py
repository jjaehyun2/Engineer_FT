package modules.srddzGame.srddzInerGame.view.pockerPart
{
	import modules.srddzGame.SrddzGameModule;
	import modules.srddzGame.srddzInerGame.model.SrddzModel;
	import modules.srddzGame.srddzInerGame.view.pockerPart.singlePart.BaseActTipItem;
	
	import ui.srddzGame.ddzPart.ActTipUI;

	public class ActTipPart
	{
		protected var bottom:BaseActTipItem;
		protected var right:BaseActTipItem;
		protected var top:BaseActTipItem;
		protected var left:BaseActTipItem;
		
		protected var _PosChairVec:Vector.<BaseActTipItem> = new Vector.<BaseActTipItem>();
		
		public function ActTipPart(b:ActTipUI,r:ActTipUI,t:ActTipUI,l:ActTipUI)
		{
			bottom = new BaseActTipItem(b);
			right = new BaseActTipItem(r);
			top = new BaseActTipItem(t);
			left = new BaseActTipItem(l);
		}
		
		/**设置椅子数量*/
		public function setChairNum(num:int=4):void
		{
			_PosChairVec.length = 0;
			switch(num)
			{
				case 4:_PosChairVec.push(bottom,right,top,left);break;
			}
		}
		
		/**显示操作*/
		public function showActTip(pos:int,type:int):void
		{
			var dir:int = model.getChairDirByPos(pos);
			_PosChairVec[dir].showActTip(type);
		}
		
		/**隐藏对应的操作*/
		public function hideActTip(pos:int):void
		{
			var dir:int = model.getChairDirByPos(pos);
			_PosChairVec[dir].hideAll();
		}
		
		/**隐藏加倍*/
		public function hideJiabei():void
		{
//			var i:int;
//			for(i=0;i<_PosChairVec.length;i++)
//			{
//				_PosChairVec[i].hideJiabei();
//			}
		}
		
		/**隐藏所有操作*/
		public function hideAllActTip():void
		{
			var i:int;
			for(i=0;i<_PosChairVec.length;i++)
			{
				_PosChairVec[i].hideAll();
			}
		}
		
		protected function get model():SrddzModel
		{
			return SrddzGameModule.instance.gameContext.model;
		}
	}
}