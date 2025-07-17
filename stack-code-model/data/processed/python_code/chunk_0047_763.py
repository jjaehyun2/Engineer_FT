package views {
	import flash.display.Sprite;
	
	import mx.controls.Label;
	import mx.events.FlexEvent;
	
	public class HelloWorldSprite extends Sprite {
		public function HelloWorldSprite() {
			super();
			var _this:HelloWorldSprite = this;
			var lbl:Label = new Label();
			lbl.addEventListener(FlexEvent.CREATION_COMPLETE, 
				function (event:FlexEvent):void {
					lbl.text = 'Hello World !!!';
				}
			);
			this.addChild(lbl);
		}
	}
}