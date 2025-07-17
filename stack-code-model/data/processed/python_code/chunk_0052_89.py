package ui {
	
	import com.greensock.TweenMax;
	import flash.display.BlendMode;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	
	/**
	 * ...
	 * @author Adam Vernon
	 */
	public class SimpleScroller extends Sprite {
		
		//--In FLA--//
		public var bar:Sprite;
		//----------//
		
		public static const BAR_MOVED:String = "BAR_MOVED";
		public static const BAR_RELEASED:String = "BAR_RELEASED";
		
		private const _maxBarHeight:Number = 297;
		private const _minBarProp:Number = 0.08;
		private const _tDur:Number = 0.1;
		
		private var _visibleProportion:Number = 1;
		private var _scrollProp:Number = 0;
		private var _initMouseY:Number;
		private var _initBarY:Number;
		private var _currentlyDragging:Boolean = false;
		
		public function SimpleScroller() {
			ui_init();
		}
		
		private function ui_init():void {
			this.blendMode = BlendMode.LAYER;
			bar.buttonMode = true;
			bar.addEventListener(MouseEvent.MOUSE_DOWN, bar_mouseDown);
		}
		
		private function bar_mouseDown(evt:MouseEvent):void {
			_initMouseY = this.mouseY;
			_initBarY = bar.y;
			_currentlyDragging = true;
			this.stage.addEventListener(MouseEvent.MOUSE_MOVE, stage_mouseMove);
			this.stage.addEventListener(MouseEvent.MOUSE_UP, stage_mouseUp);
		}
		
		private function stage_mouseMove(evt:MouseEvent):void {
			var range:Number = _maxBarHeight - (_visibleProportion * _maxBarHeight);
			var dY:Number = this.mouseY - _initMouseY;
			var newY:Number = _initBarY + dY;
			if (newY > range) newY = range;
			if (newY < 0) newY = 0;
			bar.y = newY;
			_scrollProp = newY / range;
			
			dispatchEvent(new Event(BAR_MOVED));
		}
		
		private function stage_mouseUp(evt:MouseEvent):void {
			this.stage.removeEventListener(MouseEvent.MOUSE_MOVE, stage_mouseMove);
			this.stage.removeEventListener(MouseEvent.MOUSE_UP, stage_mouseUp);
			_currentlyDragging = false;
			
			dispatchEvent(new Event(BAR_RELEASED));
		}
		
		public function set visibleProportion(value:Number):void {
			var newVisibleProportion:Number = value;
			if (newVisibleProportion > 1) newVisibleProportion = 1;
			else if (newVisibleProportion < _minBarProp) newVisibleProportion = _minBarProp;
			
			if (newVisibleProportion == _visibleProportion) return;
			_visibleProportion = newVisibleProportion;
			
			TweenMax.to(bar, _tDur, { height:_visibleProportion * _maxBarHeight } );
		}
		
		public function get scrollProp():Number { return _scrollProp; }
		public function set scrollProp(value:Number):void {
			if (_currentlyDragging) return;
			
			_scrollProp = value;
			if (_scrollProp > 1) _scrollProp = 1;
			else if (_scrollProp < 0) _scrollProp = 0;
			
			var range:Number = _maxBarHeight - (_visibleProportion * _maxBarHeight);
			var newY:Number = range * _scrollProp;
			if (bar.y == newY) return;
			TweenMax.to(bar, _tDur, { y:newY } );
		}
		
	}
}