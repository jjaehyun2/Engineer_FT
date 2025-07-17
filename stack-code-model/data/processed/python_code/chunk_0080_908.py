package modules.srddzGame.srddzInerGame.view.pockerPart.singlePart.handlePart
{
	import laya.ui.View;
	import laya.utils.Tween;
	
	import modules.srddzGame.SrddzGameModule;
	import modules.srddzGame.srddzInerGame.model.SrddzModel;
	import modules.srddzGame.srddzInerGame.view.pockerPart.card.BasePocker;

	public class BaseSingleHandlePart
	{
		/**正常状态*/
		public static const STATE_NOMAL:int = 0;
		/**明牌状态*/
		public static const STATE_MINGPAI:int = 1;
		protected var state:int = 0;
		
		protected var _pockers:Vector.<BasePocker> = new Vector.<BasePocker>(33);//玩家手里最多有20张牌
		
		protected var skin:View;
		
		/**玩家手里的牌的基础类*/
		public function BaseSingleHandlePart(skin:View)
		{
			this.skin = skin;
			init();
		}
		
		protected function init():void
		{
			
		}
		
		protected function updateState(isMingPai:Boolean):void
		{
			if(isMingPai == true)
			{
				state = STATE_MINGPAI;
			}
			else
			{
				state = STATE_NOMAL;
			}
		}
		
		public function showCards(cards:Array,dir:int):void
		{
			
		}
		
		/**站起*/
		public function up():void
		{
			var i:int;
			for(i=0;i<_pockers.length;i++)
			{
				_pockers[i].up();
			}
		}
		
		/**盖住（别人的牌的表现同up*/
		public function back():void
		{
			var i:int;
			for(i=0;i<_pockers.length;i++)
			{
				_pockers[i].back();
			}
		}
		
		/**到下（自己的牌同up）*/
		public function down():void
		{
			var i:int;
			for(i=0;i<_pockers.length;i++)
			{
				_pockers[i].down();
			}
		}
		
		/**设置牌是否可以操作*/
		public function set canControl(bool:Boolean):void
		{
			var i:int;
			for(i=0;i<_pockers.length;i++)
			{
				_pockers[i].canControl = bool;
			}
		}
		
		
		/**设置选中的牌*/
		public function set seleCards(cards:Array):void
		{
			
		}
		
		/**获取选中的牌*/
		public function get seleCards():Array
		{
			return null;
		}
		
		public function hideAll():void
		{
			var i:int;
			for(i=0;i<_pockers.length;i++)
			{
				_pockers[i].hide();
				
			}
		}
		
		/**播放起牌动画*/
		public function playQipaiEff():void
		{
			var i:int;
			var len:int = _pockers.length;
			
			for(i=0;i<len;i++)
			{
				_pockers[i].skin.alpha = 0;
				Laya.timer.frameOnce(i,this,onSingleQiEff,[i],false);
			}
		}
		
		protected function onSingleQiEff(idx:int):void
		{
			Tween.to(_pockers[idx].skin,{alpha:1},100);
		}
		
		public function reset():void
		{
			var i:int,len:int=_pockers.length;
			for(i=0;i<len;i++)
			{
				_pockers[i].reset();
			}
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
		
		protected function get model():SrddzModel
		{
			return SrddzGameModule.instance.gameContext.model;
		}
	}
}