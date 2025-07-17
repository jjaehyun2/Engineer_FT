package metaswarm.node.components.dot    {
	import flash.display.*;
	
	public class DotButton extends SimpleButton{
		
		private static const BLACK:uint = 0x231F20;
		private static const WHITE:uint = 0xFFFFFF;
		private static const BRIGHTRED:uint = 0xFF3333;
		private static const BRIGHTBLUE:uint = 0x66CDFF;
		
		public var size:uint;
		public var type:String;
	
		public function DotButton() {
			this.size = 3;
			this.type = "dot";
			downState      = new DotButtonState(BRIGHTBLUE, WHITE, size);
			overState      = new DotButtonState(BRIGHTRED, WHITE, size);
			upState        = new DotButtonState(BLACK, WHITE, size);
			hitTestState   = new DotButtonState(BLACK, WHITE, size); //change to overstate
			hitTestState.x = -(size / 4);
			hitTestState.y = hitTestState.x;
			useHandCursor  = true;
		}
		
		public function forceOver():void{
			upState = overState;
		}
		
		public function restoreOver():void{
			upState = hitTestState;
		}
		
	}
}