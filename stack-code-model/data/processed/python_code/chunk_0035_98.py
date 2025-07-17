package
{
	import flash.display.Graphics;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;


	public class Moon extends MovingObject
	{
		private var counter:int = 0;
		public function Moon(origin:Object, sizeWidth :int, sizeHeight :int, radius :int, speed :Number, reverse :Boolean,angle:int)
		{
			super(origin,sizeWidth,sizeHeight,radius,speed,reverse,angle);
			if(stage) 
			{
				Init();
			}
			else 
			{
				addEventListener(Event.ADDED_TO_STAGE, onAddedToStage);
			}
		}
		
		private function onAddedToStage(event: Event): void {
			removeEventListener(Event.ADDED_TO_STAGE, onAddedToStage);
			Init();
		}
		
		private function Init() :void {
            this.addEventListener(Event.ENTER_FRAME, moveDynamic);
			this.setSize();
			this.addEventListener(MouseEvent.CLICK, ClickHandler)
		}
		
		protected function setSize() :void
		{
			this.width = sizeWidth;
			this.height = sizeHeight;
		}

		private function ClickHandler (e:MouseEvent) : void {
			e.stopImmediatePropagation();
			var sattelite:Sattelite = new Sattelite(this,40,40,70 + Math.floor(Math.random() * 100), 3, false,360/this.counter);
			this.addChild(sattelite);
			this.counter++;
		}
	}
}