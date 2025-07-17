package modules.nnGame.inerGame.view.pockerPart.card
{
	import common.tools.SoundPlay;
	
	import laya.events.Event;
	
	import ui.niuniuGame.niuniuPart.item.PockerItemUI;
	
	
	/**玩家自己手里的牌*/
	public class BottomHandlePocker extends BasePocker
	{
		protected var orignalY:Number = 0;
		
		public function BottomHandlePocker(skin:PockerItemUI)
		{
			orignalY = skin.y;
			super(skin);
			canControl = true;
		}
		
		protected var readyOffsetY:int = -20;
		
		override public function up():void
		{
			if(state == STATE_UP)
			{
				return;
			}
			
			skin.valueImg.visible = true;
			skin.backImg.visible  = false;
			
			state = STATE_UP;
		}
		
		override public function back():void
		{
			if(state == STATE_BACK)
			{
				return;
			}
			
			skin.backImg.visible  = true;
			skin.valueImg.visible = false;
			
			state = STATE_BACK;
		}
		
		override public function down():void
		{
			if(state == STATE_DOWN)
			{
				return;
			}
			
			skin.backImg.visible  = false;
			skin.valueImg.visible = true;
			
			state = STATE_DOWN;
		}
		
		/**设置是否可以操作*/
		override public function set canControl(bool:Boolean):void
		{
			//			if(!model.isSelfSitDown)
			//			{
			//				bool=false;
			//			}
			bool = false;//这里牌面就不让玩家点了，防止出问题，有需求再说
			if(bool)
			{
				//todo
				skin.on(Event.MOUSE_OVER,this,onMouseOver);
				//skin.on(Event.MOUSE_MOVE,this,onMouseMove);
				Laya.stage.on(Event.CLICK,this,onClickStage);
				skin.on(Event.MOUSE_DOWN,this,onMouseDown);
				Laya.stage.on(Event.MOUSE_UP,this,onMouseUp);
				
				skin.on(Event.MOUSE_UP,this,onSkinMouseUp);
			}
			else
			{
				//todo
				skin.off(Event.MOUSE_OVER,this,onMouseOver);
				//skin.off(Event.MOUSE_MOVE,this,onMouseMove);
				Laya.stage.off(Event.CLICK,this,onClickStage);
				skin.off(Event.MOUSE_DOWN,this,onMouseDown);
				Laya.stage.off(Event.MOUSE_UP,this,onMouseUp);
				skin.off(Event.MOUSE_UP,this,onSkinMouseUp);
			}
		}
		
		protected function onMouseOver(e:Event):void
		{
			if(model.isMouseDwon)
			{
				skin.shadowImg.visible = !skin.shadowImg.visible;
				select = !select
			}
			
		}
		
		protected function onMouseMove(e:Event):void
		{
			//			if(model.isMouseDwon)
			//			{
			//				select = !select
			//			}
		}
		
		protected function onClickStage(e:Event):void
		{
			
			//trace("pock onClickStage::" ,e.target);
			if(e.target is PockerItemUI == false && e.target != skin.parent &&  e.target.parent != skin.parent.parent)
			{
				select = false;
			}
			
			//			select = !select
		}
		
		protected function onMouseDown(e:Event):void
		{
			select = !select;
			skin.shadowImg.visible = !skin.shadowImg.visible;
		}
		
		protected function onMouseUp(e:Event):void
		{
			skin.shadowImg.visible = false;
			model.isMouseDwon = false;
			
			
		}
		
		protected function onSkinMouseUp(e:Event):void
		{
			SoundPlay.playEffect("audio_deal_card");
		}
		
		override public function set select(bool:Boolean):void
		{
			if(bool)
			{
				skin.y = orignalY + readyOffsetY;
				
			}
			else
			{
				skin.y = orignalY;
			}
		}
		
		override public function get select():Boolean
		{
			return skin.y == orignalY + readyOffsetY;
		}
		
		
		
		override public function reset():void
		{
			super.reset();
		}
		
	}
}