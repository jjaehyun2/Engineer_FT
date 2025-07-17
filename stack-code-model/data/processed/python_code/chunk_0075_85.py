package
{
	import flash.events.MouseEvent;
	
	import app.AppContainer;
	
	import org.hammerc.components.Button;
	import org.hammerc.components.Group;
	import org.hammerc.tween.Tween;
	
	[SWF(width=800, height=600, frameRate=60)]
	public class EarthquakeEffect extends AppContainer
	{
		private var _group:Group;
		
		public function EarthquakeEffect()
		{
			super();
		}
		
		override protected function createChildren():void
		{
			super.createChildren();
			
			_group = new Group();
			_group.percentWidth = 100;
			_group.percentHeight = 100;
			addElement(_group);
			
			var btn:Button = new Button();
			btn.width = 200;
			btn.height = 75;
			btn.label = "开始地震";
			btn.horizontalCenter = btn.verticalCenter = 0;
			btn.addEventListener(MouseEvent.CLICK, clickHandler);
			_group.addElement(btn);
		}
		
		private function clickHandler(event:MouseEvent):void
		{
			Tween.to(_group, 0.1, {y:-10, repeat:5, onComplete:completeHandler});
		}
		
		private function completeHandler():void
		{
			_group.y = 0;
		}
	}
}