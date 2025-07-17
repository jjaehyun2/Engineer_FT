package tools {
	
	import flash.display.DisplayObject;
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.geom.Rectangle;
	
	public class Scrollbar extends Sprite {
		
		private var scrolledObject:DisplayObject; // Ссылка на объект, который будет прокручиваться.
		private var maskObject:DisplayObject; // Маска, которая будет скрывать всё лишнее. Нам она нужна только для определния размера скроллбара.
		private var scrollBackground:Shape; // Подложка сроллбара.
		private var scrollButton:Sprite; // Ползунок скроллбара, который мы будем таскать вверх\вниз.
		
		// Конструктор принимает два параметра: объект для прокрутки и маска для него.
		public function Scrollbar(scrolledObject:DisplayObject, maskObject:DisplayObject) {
			this.scrolledObject = scrolledObject; // Присваиваем значения параметров переменным класса.
			this.maskObject = maskObject;
			
			addEventListener(Event.ADDED_TO_STAGE, addedToStage); // Слушаем добавление на сцену.
		}
		
		private function addedToStage(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, addedToStage); // Удаляем ненужный больше слушатель добавления на сцену.
			
			scrollBackground = new Shape(); // Создаём подложку скролла.
			scrollBackground.graphics.beginFill(0x272727); // И в ней рисуем прямоугольник.
			scrollBackground.graphics.drawRect(0, 0, 20, maskObject.height); // Ширину зададим 20 пикселей, а высота будет равна высоте маски.
			scrollBackground.graphics.endFill();
			addChild(scrollBackground);
			
			scrollButton = new Sprite(); // Создаём ползунок.
			scrollButton.graphics.beginFill(0x6F6F6F); // Цвет делаем чуть посветлей, чем у подложки.
			scrollButton.graphics.drawRect(0, 0, 20, maskObject.height / scrolledObject.height * maskObject.height); // Ширину также делаем в 20 пикселей.
			// А вот высота будет рассчитываться по специальной формуле. Сначала считаем, какую часть высоты скроллируемого объекта занимает высота маски.
			// Полученный результат умножаем на высоту маски. Тем самым получаем, что отношение высоты ползунка к высоте подложке равна
			// высоте маски к высоте скроллируемого объекта.
			scrollButton.graphics.endFill();
			scrollButton.buttonMode = true;
			addChild(scrollButton);
			
			scrollButton.addEventListener(MouseEvent.MOUSE_DOWN, startDragButton); // Добавляем слушатель нажатия кнопки мыши, чтобы начать перетаскивание ползунка.
			addEventListener(Event.REMOVED_FROM_STAGE, removedFromStage); // Слушатель на удаление экземпляра скроллабара со сцены.
		}
		
		private function startDragButton(e:MouseEvent):void {
			// Задаём границы перетаскивания ползунка (от верха до низа подложки).
			var bounds:Rectangle = new Rectangle(0, 0, 0, scrollBackground.height - scrollButton.height);
			scrollButton.startDrag(false, bounds); // Начинаем перетаскивание.
			
			stage.addEventListener(MouseEvent.MOUSE_UP, stopDragButton); // Добавляем к сцене слушатель отпускания кнопки мыши.
			addEventListener(Event.ENTER_FRAME, updateCoordinates); // Запускаем EnterFrame цикл, в котором будут обновляться координаты перетаскиваемого объекта.
		}
		
		private function updateCoordinates(e:Event):void {
			scrolledObject.y = - scrollButton.y / (scrollButton.height / scrollBackground.height);
			// При скролле у нас должна быть инверсия. То есть, тянем ползунок вниз, а скроллируемый объект движется вверх и наоборот.
			 // Для этого присваиваем скроллируемому объекту .y координату ползунка со знаком минус.
			 // Но этого недостаточно. Нужно учесть, что максимальный .y ползунка меньше, чем высота подложки.
			 // Для корректировки поделим .y скролла на отношение высоты ползунка к высоте подложки - scrollButton.height / scrollBackground.height;
		}
		
		private function stopDragButton(e:MouseEvent):void {
			stage.removeEventListener(MouseEvent.MOUSE_UP, stopDragButton); // Удаляем ненужные слушатели.
			removeEventListener(Event.ENTER_FRAME, updateCoordinates);
			
			stopDrag(); // Останавливаем перетаскивание.
		}
		
		private function removedFromStage(e:Event):void {
			removeEventListener(Event.REMOVED_FROM_STAGE, removedFromStage); // Удаляются ненужные больше слушатели.
			scrollButton.removeEventListener(MouseEvent.MOUSE_DOWN, startDragButton);
		}
		
	}
}