package modules.game.majiangGame.view.majiangPart.shaizi
{
	
	import common.event.EventCenter;
	import common.view.PopBox;
	
	import laya.events.Event;
	
	import ui.mainGame.majiangParts.animalEff.ShaiziEffUI;

	public class ShaiziEffPage
	{
		protected var _skin:ShaiziEffUI;
		protected var _value:int;
		
		protected var _shaizi0Time:int = 0;
		protected var _shaizi1Time:int = 0;
		
		public function ShaiziEffPage(skin:ShaiziEffUI)
		{
			_skin = skin;
			_skin.shaizi0.interval = _skin.shaizi1.interval = 50;
		}
		
		protected function onPlayComp(e:Event):void
		{
			_skin.shaizi0.stop();
			_skin.shaizi1.stop();
			
			_skin.shaizi0.visible = false;
			_skin.shaizi1.visible = false;
			
			_skin.value0.visible = true;
			_skin.value1.visible = true;
			
			var min:int = Math.max(_value-6,1);
			
			var value1:int = min+Math.round((6-min)*Math.random());
			if(value1 >= _value)
			{
				value1 = _value-1;
			}
			
			var value2:int = _value-value1;
			
			_skin.value0.skin = "gametable/shaizi/shaizi0"+value1+".png";
			_skin.value1.skin = "gametable/shaizi/shaizi0"+value2+".png";
			
			Laya.timer.once(2000,this,onComp);
		}
		
		protected function onComp():void
		{
			hide();
			EventCenter.instance.event(EventCenter.GAME_START_SHAIZI_DONGFENG_COMP);
		}
		
		public function play(value:int):void
		{
			
			trace("playshazi/////////////" + value );
			show();
			_skin.shaizi0.visible = true;
			_skin.shaizi1.visible = true;
			
			_skin.value0.visible = false;
			_skin.value1.visible = false;
			
			_value = value;
			
			if(_value < 2 || _value > 12)
			{
				QuickUtils.popMessageBox("筛子值小于2或者大于12  " + _value,PopBox.BTN_QUEREN,null,null,"错误");
				return;
			}
			
			_skin.shaizi0.play(Math.round((Math.random()*_skin.shaizi0.count)),true);
			_skin.shaizi1.play(Math.round((Math.random()*_skin.shaizi1.count)),true);
			
			Laya.timer.once(1000,this,onPlayComp);
		}
		
		public function reset():void
		{
			hide();
		}
		
		public function show():void
		{
			_skin.visible = true;
		}
		
		public function hide():void
		{
			_skin.visible = false;
		}
	}
}