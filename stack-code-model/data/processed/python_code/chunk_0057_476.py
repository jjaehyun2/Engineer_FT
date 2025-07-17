package modules.game.majiangGame.view.majiangPart
{
	import modules.game.GameModule;
	import modules.game.majiangGame.model.MajiangModel;
	import modules.game.majiangGame.view.majiangPart.singlePart.BaseHandleEffItem;
	
	import ui.mainGame.majiangParts.HandleEffUI;

	public class HandleEffPart
	{
		protected var _skin:HandleEffUI;
		protected var _items:Vector.<BaseHandleEffItem> = new Vector.<BaseHandleEffItem>(4);
		protected var _PosChairVec:Vector.<BaseHandleEffItem> = new Vector.<BaseHandleEffItem>();
		
		public function HandleEffPart(skin:HandleEffUI)
		{
			_skin  = skin;
			
			init();
		}
		
		/**设置椅子数量*/
		public function setChairNum(num:int=3):void
		{
			_PosChairVec.length = 0;
			switch(num)
			{
				case 1:_PosChairVec.push(_items[0]);break;//一个人自己玩 啊哈哈
				case 2:_PosChairVec.push(_items[0],_items[1]);break; //两个人玩
				case 3:_PosChairVec.push(_items[0],_items[1],_items[3]);break;
				case 4:_PosChairVec.push(_items[0],_items[1],_items[2],_items[3]);break;
				default:_PosChairVec.push(_items[0],_items[1],_items[3]);break;
			}
		}
		
		protected function init():void
		{
			var i:int,len:int = _items.length;
			
			for(i=0;i<len;i++)
			{
				_items[i] = new BaseHandleEffItem(_skin["item"+i]); 
			}
		}
		
		public function showEffByPos(pos:int,type:int):void
		{
			var dir:int = model.getChairDirByPos(pos);
			
			_PosChairVec[dir].showEff(type);
			
		}
		
		protected function get model():MajiangModel
		{
			return GameModule.instance.gameContext.model;
		}
	}
}