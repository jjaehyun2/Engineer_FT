package view {
	import flash.display.Graphics;
	import flash.display.Sprite;
	import flash.display.Stage;
	import flash.events.TimerEvent;
	import flash.text.TextField;
	import flash.utils.Timer;
	
	/**
	 * ...
	 * @author hongjie
	 */
	public final class Alert extends Sprite {
	
		private var _tf:TextField;
		
		private var _time:Timer;
		
		public function Alert(content:String) {
			super();
			this.mouseChildren = false;
			this.mouseEnabled = false;
			
			_tf = new TextField();
			_tf.mouseEnabled = false;
			_tf.text = content;
			_tf.textColor = 0xffffff;
			_tf.x = 5;
			_tf.y = 5;
			addChild(_tf);
			
			const g:Graphics = this.graphics;
			g.beginFill(0x363636);
			g.drawRect(0, 0, _tf.textWidth + 10, _tf.textHeight + 10);
			g.endFill();
		}
		
		public function show(stage:Stage):void {
			this.x = (stage.stageWidth - _tf.textWidth - 10) >> 1;
			this.y = (stage.stageHeight - _tf.textHeight - 10) >> 1;
			stage.addChild(this);
			
			_time = new Timer(2000, 1);
			_time.addEventListener(TimerEvent.TIMER_COMPLETE, _onTimerCompleted);
			_time.start();
		}
		
		private function _onTimerCompleted(e:TimerEvent):void {
			_time.removeEventListener(TimerEvent.TIMER_COMPLETE, _onTimerCompleted);
			this.parent.removeChild(this);
		}
		
	}

}