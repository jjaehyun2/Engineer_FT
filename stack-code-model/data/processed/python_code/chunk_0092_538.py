package aisy.d_scroller
{
	import flash.events.MouseEvent;
	
	import org.ais.event.TEvent;
	import org.aisy.button.Button;
	import org.aisy.display.USprite;
	import org.aisy.listoy.Listoy;
	import org.aisy.listoy.ListoyEnum;
	import org.aisy.scroller.Scroller;
	import org.aisy.skin.AisySkin;

	public class D_Scroller extends USprite
	{
		public function D_Scroller()
		{
			init();
		}
		
		private function init():void
		{
			with (graphics) {
				beginFill(0xffffff, 0.5);
				drawRoundRect(0, 0, 700, 500, 20);
				endFill();
			}
			TEvent.trigger("UP_WINDOW_AIS", "SHOW", [this, Math.random(), 0, false, !AisySkin.MOBILE]);
			
			var s:USprite = new USprite();
			with (s.graphics) {
				beginFill(0xff0000, 0.5);
				drawRoundRect(0, 0, 900, 900, 30);
				endFill();
			}
			
			var arr:Array = [];
			for (var i:int = 0; i < 10; i++) {
				arr[arr.length] = i;
			}
			var l:Listoy = new Listoy();
			l.setMode(ListoyEnum.MODE_SHOW);
			l.setLayout(ListoyEnum.LAYOUT_VERTICAL);
//			l.setRowColumn(arr.length, 1);
			l.setRowColumn(8, 1);
			l.setItemRenderer(D_Item);
			l.setDataProvider(arr);
			l.initializeView();
			
			var _scroller:Scroller = new Scroller();
//			_scroller.setDelay(0);
			_scroller.setSource(l);
			_scroller.setSize(l.width, 500);
			_scroller.setSkinClassName(AisySkin.SCROLLER_SKIN);
//			_scroller.setSkinClass(ScrollerSkin_0);
//			_scroller.setEnabled(false);
			addChild(_scroller);
			
			var btn:Button = new Button();
			btn.setSkinClassName("_AISY_BUTTON");
			btn.setText(AisySkin.MOBILE ? "移动" : "桌面");
			btn.x = _scroller.width + (AisySkin.MOBILE ? 0 : _scroller.getChildAt(_scroller.numChildren - 1).width + 1);
			addChild(btn);
			
			btn.setClick(__btnHandler);
		}
		
		private function __btnHandler(e:MouseEvent):void
		{
			AisySkin.MOBILE = !AisySkin.MOBILE;
			TEvent.trigger("UP_WINDOW_AIS", "CLEAR_ALL");
			new D_Scroller();
		}
		
	}
}