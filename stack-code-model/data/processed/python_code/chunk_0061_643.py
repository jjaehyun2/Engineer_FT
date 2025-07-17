package  {
	
	import flash.display.MovieClip;
	import flash.display.SimpleButton;
	import flash.text.TextField;
	import flash.events.MouseEvent;
	
	
	public class Main extends MovieClip {
		
		private var iStep:int;
		
		public var btnClick:SimpleButton;
		public var txtMsg:TextField;		
		
		public function Main() {
			// constructor code
			
			initialize();
			initButton();			
		}
		
		private function initialize():void {
			iStep = 0;
			txtMsg.text = '';
			
		}
		
		private function initButton():void {
			btnClick.addEventListener(MouseEvent.CLICK,onClick, false , 0 , true );
		}
		
		private function onClick($evt:MouseEvent):void {
			iStep++;
			var knValue1:int = int( Math.random() * 50 );
			var knValue2:int = int( Math.random() * 50 );
			var knResult:int = knValue1 + knValue2;
			
			txtMsg.appendText( '[' + iStep + '] ' + knValue1 + ' + ' +  knValue2 + ' = ' + knResult + '\r\n' );
			
		};
	}
	
}