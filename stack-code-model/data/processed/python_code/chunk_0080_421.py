package metaswarm.node.components.databox   {
	import flash.display.*;
	import flash.text.*;
	
	public class CustomSimpleButton extends SimpleButton {
		/*private var upColor:uint   = 0xFFCC00;
		private var overColor:uint = 0xCCFF00;
		private var downColor:uint = 0x00CCFF;
		private var black:uint = 0x231F20;*/
		
		private static const BLACK:uint = 0x231F20;
		private static const WHITE:uint = 0xFFFFFF;
		private static const BRIGHTRED:uint = 0xFF3333;
		private static const BRIGHTBLUE:uint = 0x66CDFF;
		
		public var size:uint;
		public var type:String;
	
		public function CustomSimpleButton(type:String) {
			this.size = 15;
			this.type = type;
			downState      = new ButtonDisplayState(type, BRIGHTBLUE, BLACK, size);
			overState      = new ButtonDisplayState(type, BRIGHTRED, BLACK, size);
			upState        = new ButtonDisplayState(type, WHITE, BLACK, size);
			hitTestState   = new ButtonDisplayState(type, WHITE, BLACK, size);
			hitTestState.x = -(size / 4);
			hitTestState.y = hitTestState.x;
			useHandCursor  = true;
		}
		
		public function make():void {
			/*downState      = new ButtonDisplayState(downColor, size, txt);
			overState      = new ButtonDisplayState(overColor, size, txt);
			upState        = new ButtonDisplayState(upColor, size, txt);
			hitTestState   = new ButtonDisplayState(upColor, size, txt);
			hitTestState.x = -(size / 4);
			hitTestState.y = hitTestState.x;
			useHandCursor  = true;*/
		}
	}
}