package {
	
	import flash.display.DisplayObject;
	import flash.display.MovieClip;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.utils.getDefinitionByName;
	
	/**
	 * Стандартный self прелоадер из шаблона FlashDevelop. Немного модифицирован.
	 */
	
	public class Preloader extends MovieClip {
		/** @private крутилка показывает, что идёт загрузка */
		private var rotator:Rotator;
		
		public function Preloader() {
			if (stage) {
				stage.scaleMode = StageScaleMode.NO_SCALE;
				stage.align = StageAlign.TOP_LEFT;
			}
			addEventListener(Event.ENTER_FRAME, checkFrame);
			
			rotator = new Rotator(); // создаём крутилку и помещаем её в середину сцены (Rotator из swc)
			rotator.x = (stage.stageWidth - rotator.width) / 2;
			rotator.y = (stage.stageHeight - rotator.height) / 2;
			addChild(rotator);
		}
		/**
		 * @private функция из шаблона преорадера, проверяет, загружена ли флешка до конца
		 * 
		 */
		private function checkFrame(e:Event):void {
			if (currentFrame == totalFrames) {
				stop();
				loadingFinished();
			}
		}
		/**
		 * @private функция запускается, когда закончена загрузка флешки
		 *  создаётся экземпляр основного класса и добавляется на сцену, то есть флешка запускается.
		 */
		private function loadingFinished():void {
			removeEventListener(Event.ENTER_FRAME, checkFrame);
			var mainClass:Class = getDefinitionByName("Main") as Class;
			addChild(new mainClass() as DisplayObject);
		}
		/**
		 * Эта функция позволит в нужный момент удалить крутилку со сцены из класс Main
		 */
		public function removeRotator():void {
			removeChild(rotator);
		}
		
	}
}