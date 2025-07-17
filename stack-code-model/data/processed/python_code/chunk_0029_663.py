package {
	
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.events.ProgressEvent;
	import flash.net.FileFilter;
	import flash.net.FileReference;
	import fr.kikko.lab.ShineMP3Encoder;
	
	public class Main extends Sprite {
		
		/** @private интерфейс из ui.swc */
		private var gui:ui;
		/** @private FileReference для открытия wav файла */
		private var fileReference:FileReference;
		
		public function Main():void {
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			
			// создаём интерфейс и немного его настраиваем
			gui = new ui();
			gui.loadbar.scaleX = 0;
			gui.x = 300;
			gui.y = 250;
			addChild(gui);
			
			// слушательн на кнопку "LOAD WAV"
			gui.loadButton.addEventListener(MouseEvent.CLICK, onLoadClicked);
		}
		
		/**
		 * @private Открываем окно выбора файлов.
		 */
		private function onLoadClicked(e:Event):void {
			fileReference = new FileReference();
			fileReference.browse([new FileFilter("Music", "*.wav")]);
			fileReference.addEventListener(Event.SELECT, onFileSelected);
		}
		/**
		 * @private После выбора файла зугружаем его байты.
		 */
		private function onFileSelected(e:Event):void {
			fileReference.addEventListener(Event.COMPLETE, onLoaded);
			fileReference.load();
		}
		/**
		 * @private Создаём кодировщик аудио и передаём ему загруженные байты,
		 * вешаем на него слушатели прогресса и окончания конывертации.
		 */
		private function onLoaded(e:Event):void {
			fileReference.removeEventListener(Event.SELECT, onFileSelected);
			fileReference.removeEventListener(Event.COMPLETE, onLoaded);
			
			var mp3Encoder:ShineMP3Encoder = new ShineMP3Encoder(fileReference.data);
			mp3Encoder.addEventListener(Event.COMPLETE, encodeComplete);
			mp3Encoder.addEventListener(ProgressEvent.PROGRESS, onProgress);
			mp3Encoder.start();
		}
		/**
		 * @private Обновляем прогрессбар.
		 */
		protected function onProgress(e:ProgressEvent):void {
			gui.loadbar.scaleX = e.bytesLoaded / e.bytesTotal;
		}
		/**
		 * @private Сохраняем сконвертированные байты в mp3 файл через FileReference.
		 */
		protected function encodeComplete(e:Event):void {
			e.target.removeEventListener(Event.COMPLETE, encodeComplete);
			e.target.removeEventListener(ProgressEvent.PROGRESS, onProgress);
			(new FileReference()).save(e.target.mp3Data, "converted.mp3");
		}
	
	}
}