package metaswarm.node.components.thumb   {
	import flash.display.*;
	import flash.text.*;
	
	public class ThumbButton extends SimpleButton {
		/*private var upColor:uint   = 0xFFCC00;
		private var overColor:uint = 0xCCFF00;
		private var downColor:uint = 0x00CCFF;
		private var black:uint = 0x231F20;*/
		
		private static const BLACK:uint = 0x231F20;
		private static const LIGHTGREY:uint = 0xfcfcfc;
		private static const WHITE:uint = 0xFFFFFF;
		private static const BRIGHTRED:uint = 0xFF3333;
		private static const BRIGHTBLUE:uint = 0x66CDFF;
		
		public var size:uint;
		public var type:String;
	
		public function ThumbButton(type:String) {
			this.size = 15;
			this.type = type;
			downState      = new ThumbButtonState(type, BRIGHTBLUE, BLACK, size);
			overState      = new ThumbButtonState(type, BRIGHTRED, BLACK, size);
			upState        = new ThumbButtonState(type, WHITE, BLACK, size);
			hitTestState   = new ThumbButtonState(type, WHITE, BLACK, size);
			hitTestState.x = -(size / 4);
			hitTestState.y = hitTestState.x;
			useHandCursor  = true;
		}
		
		public function make():void {
			//
		}
	}
}