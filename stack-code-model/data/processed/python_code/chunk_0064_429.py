package modules.game.majiangGame.view.playerInfoPart
{
	
	import laya.events.Event;
	import laya.ui.CheckBox;
	
	import ui.gameCommon.PiaoSelePartUI;

	public class PiaoSelePart
	{
		
		protected var needPiao:Boolean = true;
		protected var skin:PiaoSelePartUI;
		
		protected var piaoCheckBoxVec:Vector.<CheckBox> = new Vector.<CheckBox>(3);
		
		protected var curPiaoValue:int = 0;
		
		public function PiaoSelePart(skin:PiaoSelePartUI)
		{
			this.skin = skin;
			
			init();
		}
		
		protected function init():void
		{
			var i:int,len:int = piaoCheckBoxVec.length;
			
			for(i=0;i<len;i++)
			{
				piaoCheckBoxVec[i] = skin["piao"+i];
				
				piaoCheckBoxVec[i].on(Event.CLICK,this,onClickCheckBox,[i,i]);
			}
			
			seleIdx(0);
			
			hide();
		}
		
		protected function onClickCheckBox(e:Event,args:Object):void
		{
			var idx:int = args as int;
			
			trace("onClickCheckBox::" + args);
			seleIdx(idx);
		}
		
		public function seleIdx(idx:int):void
		{
//			if(UserData.roomtype == 11)
//			{
//				needPiao = true;
//			}
//			else
//			{
//				needPiao = false;
//			}
//			
//			if(needPiao == false)
//			{
//				skin.visible = false;
//			}
//			else
//			{
//				skin.visible = true;
//			}
			
			var i:int,len:int = piaoCheckBoxVec.length;
			
			for(i=0;i<len;i++)
			{
				if(i == idx)
				{
					piaoCheckBoxVec[i].selected = true;
				}
				else
				{
					piaoCheckBoxVec[i].selected = false;
				}
			}
			
			curPiaoValue = idx;
		}
		
		public function getCurPiaoValue():int
		{
			return curPiaoValue;
		}
		
		public function reset():void
		{
			seleIdx(0);
			
			if(UserData.roomtype == 11)
			{
				needPiao = true;
			}
			else
			{
				needPiao = false;
			}
			
		}
		
		public function show():void
		{
			if(needPiao)
			{
				skin.visible = true;
			}
			else
			{
				skin.visible = false;
			}
			
		}
		
		public function hide():void
		{
			skin.visible = false;
		}
	}
}