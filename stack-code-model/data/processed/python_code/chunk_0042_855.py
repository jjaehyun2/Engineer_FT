package {
	
	import flash.display.Bitmap;
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.events.Event;
	import tools.Scrollbar;
	
	public class Main extends Sprite {
		
		// Прикрепляем изображение из папки lib  привязываем его к переменной.
		[Embed(source = '../lib/photo.jpg')] private var PhotoBitmap:Class;
		
		public function Main():void {
			
			// Создаём контейнер и добавляем его на сцену.
			var container:Sprite = new Sprite(); 
			//container.x = container.y = 100;
			addChild(container);
			
			// Из фото создаём битмап и помещаем его в контейнер. Его то мы и будем прокручивать.
			var scrolledBitmap:Bitmap = new PhotoBitmap as Bitmap; 
			container.addChild(scrolledBitmap); // 
			
			// Создаём маску и рисуем в ней прямоугольник.
			// Ширина маски будет равна ширине изображения.
			// А высота пусть будет равна трём сотням пикселей, хотя можно ввести любое значение (в разумных пределах).
			var bitmapMask:Shape = new Shape(); 
			bitmapMask.graphics.beginFill(0x000000);
			bitmapMask.graphics.drawRect(0, 0, scrolledBitmap.width, 300); 
			
			bitmapMask.graphics.endFill();
			container.addChild(bitmapMask);
			
			scrolledBitmap.mask = bitmapMask; // Применяем маску к изображению.
			
			// Вот и самое интересное. Тут мы создаём экземпляр нашего скроллбара.
			// Отдаём ему в параметры изображение и маску.
			// Добавляем на сцены чуть дальше правого края изображения.
			var scroller:Scrollbar = new Scrollbar(scrolledBitmap, bitmapMask);
			scroller.x = scrolledBitmap.width + 8;
			container.addChild(scroller);
		}
		
	}
}