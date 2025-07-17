package elements {
	
	import com.greensock.layout.AutoFitArea;
	import flash.display.Bitmap;
	import flash.display.Loader;
	import flash.display.MovieClip;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.display.Shape;
	import flash.net.URLRequest;
	import flash.events.MouseEvent;
	import com.greensock.TweenLite;
	
	/**
	 * класс страницы галереи (альбома)
	 * тут есть подложка, как в текстовой сранице, две стрелки переключения фотографий и сами фотографии.
	 */
	
	public class AlbumPage extends Sprite {
		/** @private список всех фотографий */
		private var xmlList:XMLList;
		/** @private белая полупрозрачная подложка */
		private var background:Shape;
		/** @private номер текущего фото */
		private var currentPhoto:uint;
		/** @private левая стрелка */
		private var leftArrow:ArrowButton;
		/** @private правая стрелка */
		private var righrArrow:ArrowButton;
		/** @private специальная штука для выравнивания фото. описание ниже */
		private var fitArea:AutoFitArea;
		/** @private загруженное изображение для отображения */
		private var image:Bitmap;
		/** @private триггер первой загрузки */
		private var firstLoad:Boolean = true;
		/** @private загрузчик для фото */
		private var loader:Loader;
		/** @private точно такая же крутилка, как в прелоадере */
		private var rotator:Rotator;
		/** @private загружается ли в данные момент изображение */
		private var loadingProgress:Boolean;
		/**
		 * Конструктор класса. ждёт добавления на сцену, принимает список фотографий
		 * 
		 * @param	xmlList список всех фотографий данной галереи.
		 */
		public function AlbumPage(xmlList:XMLList) {
			this.xmlList = xmlList;
			addEventListener(Event.ADDED_TO_STAGE, addedToStage);
		}
		/**
		 * добавление на сцену, создание подложки, стрелок, области позиционирования фото
		 * 
		 * @param	e событие добавления на сцену
		 */
		private function addedToStage(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, addedToStage);
			
			background = new Shape(); // создание и добавление подложки. рисуется она в resize()
			addChild(background);
			
			leftArrow = new ArrowButton(); // создание и настройка стрелок
			leftArrow.buttonMode = true;
			leftArrow.scaleX = -1; // отражаем левую стрелку по горизонтали. так как для обеих стрелок используется одно изображение.
			leftArrow.x = leftArrow.width + 50;
			addChild(leftArrow);
			
			righrArrow = new ArrowButton();
			righrArrow.buttonMode = true;
			addChild(righrArrow);
			
			leftArrow.addEventListener(MouseEvent.CLICK, prevPhoto); // добавление слушателей клика к стрелкам...
			righrArrow.addEventListener(MouseEvent.CLICK, nextPhoto); // ... для загрузки следующей или предыдущей фотки
			
			// это специальная интересная штука из бибилиотеки от greensock(как и TweenMax/TweenLite)
			// она определяет прямоугольную область. В эту область она автоматически вписывает указанное изображение
			// без потери пропорций.
			// в конструктор принимает контейнер, x, y, width, height, также можно задать цвет.
			// если добавить fitArea на сцену, прямоугольник будет виден. иногда полезно для тестирования
			fitArea = new AutoFitArea(this, 102, 136, stage.stageWidth - 204, stage.stageHeight - 210);
			
			loadPhoto(); // сразу грузим первое в спискефото, чтоб место не пустовало.
			
			this.alpha = 0; // немного анимируем, как и текстовую страницу
			TweenLite.to(this, .5, { alpha:1 } );
			
			resize(); // ресайз для расстановки элементов и перерисовки подложки. 
			
			stage.addEventListener(Event.RESIZE, resize); // слушатель ресайза
			addEventListener(Event.REMOVED_FROM_STAGE, removedFromStage); // слушатель удаления со сцены
		}
		/**
		 * Грузим следующую фотку.
		 * 
		 * @param	e событие клика
		 */
		private function nextPhoto(e:MouseEvent):void {
			if (!loadingProgress) { // если в данный момент не идёт загрузка
				if (currentPhoto < xmlList.length() - 1) { // если текущий номер фото меньше максимально возможного
					currentPhoto++; // прибавляем единицу
				} else {
					currentPhoto = 0; // иначе приравниваем нулю
				}
				loadPhoto(); // запускаем загрузку фото
			}
		}
		/**
		 * Грузим предыдущую фотку.
		 * 
		 * @param	e событие клика
		 */
		private function prevPhoto(e:MouseEvent):void {
			if (!loadingProgress) { // если в данный момент не идёт загрузка
				if (currentPhoto > 0) { // если текущий номер фото больше нуля
					currentPhoto--; // отнимаем единицу
				} else { // иначе приравниваем максимально возможный номер
					currentPhoto = xmlList.length() - 1;
				}
				loadPhoto(); // запускаем загрузку фото
			}
		}
		/**
		 * @private загрузка фото
		 */
		private function loadPhoto():void {
			loadingProgress = true; // включаем индикатор процесса загрузки
			
			if (firstLoad) { // если это самая первая загрузка
				firstLoad = false; // то следующие загрузки уже не будут первыми (кэп!)
			} else { // если загрузка не первая
				fitArea.release(image); // отсоединяем существующее изображение от fitArea
				removeChild(image); // и удаляем его со сцены
			}
			
			rotator = new Rotator(); // создаём крутилку, как в прелоадере
			rotator.x = (stage.stageWidth - rotator.width) / 2;
			rotator.y = (stage.stageHeight - rotator.height) / 2 + 30;
			addChild(rotator);
			
			loader = new Loader(); // создаём загрузчик и грузим фото по текущему номеру (currentPhoto)
			loader.load(new URLRequest(xmlList[currentPhoto].@url));
			loader.contentLoaderInfo.addEventListener(Event.COMPLETE, imageLoaded);
		}
		/**
		 * @private загрузка изображения завершена
 		 * 
		 * @param	e событие окончания загрузки
		 */
		private function imageLoaded(e:Event):void {
			e.target.removeEventListener(Event.COMPLETE, imageLoaded);
			
			removeChild(rotator); // удаляем крутилку
			rotator = null;
			
			image = e.target.content as Bitmap; // создаём изображение из загруженного контента
			image.smoothing = true; // включаем сглаживание, чтоб было красивей
			addChild(image); // добаввляем на сцену
			image.alpha = 0; // прячем изображение
			TweenLite.to(image, .5, { alpha:1 } ); // и плавно показвыаем его
			fitArea.attach(image); // затем прицепляем к fitArea
			loadingProgress = false; // отлючаем индикатор процесса загрузки
		}
		/**
		 * функция ресайза
		 * 
		 * @param	e событие ресайза
		 */
		private function resize(e:Event = null):void {
			background.graphics.clear(); // перерисовываем подложку
			background.graphics.beginFill(0xFFFFFF, .7);
			background.graphics.drawRect(40, 110, stage.stageWidth - 80, stage.stageHeight - 160)
			background.graphics.endFill();
			
			righrArrow.x = stage.stageWidth - righrArrow.width - 50; // задаём координаты стрелок
			leftArrow.y = righrArrow.y = (stage.stageHeight - leftArrow.height) / 2 + 30;
			
			fitArea.width = stage.stageWidth - 204; // корректируем размеры fitArea...
			fitArea.height = stage.stageHeight - 210;
			fitArea.update(); // ... и обновляем её, иначе картинка останется в прежнем размере
		}
		/**
		 * Удаление со сцены, отключаем всё ненужное
		 * 
		 * @param	e событие удаления со сцены
		 */
		private function removedFromStage(e:Event):void { 
			removeEventListener(Event.REMOVED_FROM_STAGE, removedFromStage);
			stage.removeEventListener(Event.RESIZE, resize);
			if (loadingProgress) { // если в момент удаления со сцены идёт загрузка...
				loader.unload(); // ... выгружаем изображение
				loader.contentLoaderInfo.removeEventListener(Event.COMPLETE, imageLoaded); // и удаляем слушатель окончания загрузки
			}
		}
		
	}
}