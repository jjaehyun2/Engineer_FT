package{
	import com.greensock.easing.Linear;
	import com.greensock.plugins.BezierPlugin;
	import com.greensock.plugins.TweenPlugin;
	import com.greensock.TweenMax;
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.events.MouseEvent;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	public class Main extends Sprite {
		private var clip:Sprite;
		
		public function Main() {
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			stage.scaleMode = StageScaleMode.NO_SCALE;
			stage.align = StageAlign.TOP_LEFT;
			TweenPlugin.activate([BezierPlugin]);
			// entry point
			
			clip = new Sprite();
			clip.graphics.beginFill(0x000000, .3);
			clip.graphics.drawCircle(0, 0, 20);
			clip.graphics.endFill();
			clip.x = 40;
			clip.y = 40;
			
			addChild(clip);
			
			stage.addEventListener(MouseEvent.CLICK, onClick);
			
			addEventListener(Event.ENTER_FRAME, update)
		}
		
		private function onClick(e:MouseEvent):void {
			TweenMax.to(clip, 3, { bezier: { type:"cubic",  values:[ {x:40,y:40}, {x:23,y:130}, {x:214,y:182}, {x:98,y:183}, {x:28,y:183}, {x:196,y:332}, {x:242,y:194}, {x:268,y:114}, {x:353,y:126}, {x:370,y:36}], ease:Linear.easeNone}});
		}
		
		private function update(e:Event):void {
			trace("update")
			var gr:Shape = new Shape();
			gr.graphics.beginFill(0x000000);
			gr.graphics.drawCircle(0, 0, 2);
			gr.graphics.endFill();
			
			gr.x = clip.x;
			gr.y = clip.y;
			addChild(gr);
		}
		
	}
	
}