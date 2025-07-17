package ui {
	
	import com.greensock.TweenMax;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import data.Solver;
	import flash.text.TextField;
	import flash.text.TextFieldType;
	import flash.utils.Dictionary;
	
	/**
	 * ...
	 * @author Adam Vernon
	 */
	public class MainScreen extends Sprite {
		
		//--In FLA--//
		public var findButton:PushButton;
		public var clearButton:PushButton;
		public var scroller:SimpleScroller;
		public var resultsTF:TextField;
		public var cube1:EntryCube;
		public var cube2:EntryCube;
		public var cube3:EntryCube;
		public var cube4:EntryCube;
		public var cube5:EntryCube;
		public var cube6:EntryCube;
		public var cube7:EntryCube;
		public var cube8:EntryCube;
		public var cube9:EntryCube;
		public var cube10:EntryCube;
		public var cube11:EntryCube;
		public var cube12:EntryCube;
		public var cube13:EntryCube;
		public var cube14:EntryCube;
		public var cube15:EntryCube;
		public var cube16:EntryCube;
		//----------//
		
		private var _cubes:Vector.<EntryCube> = new <EntryCube>[];
		private var _solver:Solver = new Solver();
		private var _textCanScroll:Boolean = false;
		private const _scrollFadeDur:Number = 0.2;
		
		public function MainScreen() {
			ui_init();
		}
		
		private function ui_init():void {
			findButton.addEventListener(MouseEvent.CLICK, findButton_click);
			findButton.buttonEnabled = false;
			
			clearButton.addEventListener(MouseEvent.CLICK, clearButton_click);
			clearButton.buttonEnabled = false;
			
			_cubes.push(cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8, cube9, cube10, cube11, cube12, cube13, cube14, cube15, cube16);
			for each (var cube:EntryCube in _cubes) {
				cube.addEventListener(EntryCube.CHAR_ENTERED, cube_charEntered);
			}
			
			scroller.addEventListener(SimpleScroller.BAR_MOVED, scroller_barMoved);
			scroller.addEventListener(SimpleScroller.BAR_RELEASED, scroller_barReleased);
			TweenMax.set(scroller, { autoAlpha:0 } );
			
			resultsTF.addEventListener(Event.SCROLL, resultsTF_scroll);
		}
		
		private function cube_charEntered(evt:Event):void {
			//Includes some focus hackiness for jumping from TextField to TextField when entering chars on iOS//
			var nextCube:int = _cubes.indexOf(evt.currentTarget as EntryCube) + 1;
			if ((nextCube < 16) && ((evt.currentTarget as EntryCube).inputTF.text != "")) {
				this.stage.focus = null;
				this.stage.focus = _cubes[nextCube].inputTF;
				_cubes[nextCube].inputTF.dispatchEvent(new MouseEvent(MouseEvent.CLICK, false, false, 384, 512, _cubes[nextCube].inputTF));
				_cubes[nextCube].inputTF.requestSoftKeyboard();
				_cubes[nextCube].inputTF.setSelection(0, _cubes[nextCube].inputTF.text.length);
			} else if (nextCube == 16) {
				stage.focus = null;
			}
			var allCubesReady:Boolean = true;
			var noCubesReady:Boolean = true;
			for each (var cube:EntryCube in _cubes) {
				allCubesReady &&= cube.inputTF.text != "";
				noCubesReady &&= cube.inputTF.text == "";
			}
			findButton.buttonEnabled = allCubesReady;
			clearButton.buttonEnabled = ! noCubesReady;
		}
		
		private function findButton_click(evt:MouseEvent):void {
			var letters:Vector.<String> = new <String>[];
			for each (var cube:EntryCube in _cubes) {
				letters.push(cube.inputTF.text.toUpperCase());
			}
			_solver.letters = letters;
			_solver.words_find();
			results_format(_solver.foundWords);
		}
		
		private function results_format(list:Vector.<String>):void {
			if (list.length == 0) {
				resultsTF.text = "Found no words!";
				return;
			}
			resultsTF.text = "Found " + list.length.toString() + " words!";
			
			var lengthDic:Dictionary = new Dictionary(true);
			for each (var word:String in list) {
				var len:int = word.length;
				if (! (len in lengthDic)) lengthDic[len] = new <String>[word];
				else lengthDic[len].push(word);
			}
			for (var i:int = 16; i > 2; i--) {
				if (i in lengthDic) {
					(lengthDic[i] as Vector.<String>).sort(string_compare);
					for each (var sortedWord:String in lengthDic[i]) {
						resultsTF.appendText("\n -  " + sortedWord + "  (" + i.toString() + ")");
					}
				}
			}
			resultsTF_change();
		}
		
		private function string_compare(a:String, b:String):int {
			if (a == b) return 0;
			if (a > b) return 1;
			return -1;
		}
		
		private function resultsTF_change(evt:Event=null):void {
			scroller.visibleProportion = resultsTF.height / resultsTF.textHeight;
			var scrollingNow:Boolean = resultsTF.textHeight > resultsTF.height;
			if (scrollingNow != _textCanScroll) {
				_textCanScroll = scrollingNow;
				TweenMax.to(scroller, _scrollFadeDur, { autoAlpha: _textCanScroll ? 1 : 0 } );
			}
		}
		
		private function scroller_barMoved(evt:Event):void {
			resultsTF.scrollV = Math.round(1 + (scroller.scrollProp * (resultsTF.maxScrollV - 1)));
		}
		
		private function scroller_barReleased(evt:Event):void {
			scroller.scrollProp = (resultsTF.scrollV - 1) / (resultsTF.maxScrollV - 1);
		}
		
		private function resultsTF_scroll(evt:Event):void {
			scroller.scrollProp = (resultsTF.scrollV - 1) / (resultsTF.maxScrollV - 1);
		}
		
		private function clearButton_click(evt:MouseEvent):void {
			for each (var cube:EntryCube in _cubes) {
				cube.inputTF.text = "";
			}
			this.stage.focus = _cubes[0].inputTF;
			clearButton.buttonEnabled = false;
			findButton.buttonEnabled = false;
			
			resultsTF.text = "";
			resultsTF_change();
		}
		
		
	}
}