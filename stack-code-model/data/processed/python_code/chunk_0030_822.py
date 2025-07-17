package  com.illuzor.utils
{
	import flash.text.TextField;
	import flash.utils.Timer;
	import flash.events.TimerEvent;
	import com.illuzor.events.ToolsEvent;
	
	/**
	 * ...
	 * @author iLLuzor  //  illuzor@gmail.com  //  http://illuzor.com
	 * Небольшой тул для некоторых нужд.
	 */
	
	public class Tool {
		static private var textField:TextField;
		static private var currentSymbol:uint = 0;
		static private var symbols:Array;
		static private var nextFunction:Function;
		static private var ttext:String;
		static private var timer:Timer;
		static private var uf:Boolean;
		
		/**
		 * Автоматическая анимация текста в зависимости от длительности озвучки.
		 * 
		 * @param tf Тестовое поле для анимации.
		 * @param text Строка для отображения.
		 * @param soundTime Длительность звука в миллисекундах.
		 * @param func Функция, которую нужно выполнить после завершения.
		 */
		
		public static function animateString(tf:TextField, text:String, soundTime:uint, func:Function):void {
			uf = true;
			currentSymbol = 0;
			ttext = text;
			nextFunction = func;
			textField = tf;
			symbols = new Array();

			timer = new Timer(soundTime / text.length, text.length);
			timer.start();
			timer.addEventListener(TimerEvent.TIMER, addChar);
			timer.addEventListener(TimerEvent.TIMER_COMPLETE, timerEnds);
		}
		
		static private function addChar(e:TimerEvent):void {
				if (ttext.charAt(currentSymbol) == "@") {
					textField.appendText("\n" )
				} else {
					textField.appendText(ttext.charAt(currentSymbol));
				}
			currentSymbol++;
		}
		
		static private function timerEnds(e:TimerEvent):void {
			uf = false;
			nextFunction();
		}
		
		static public function clear(tf:TextField):void {
			if(uf == true)timer.stop();
			
			tf.text = "";
		}
	}
}