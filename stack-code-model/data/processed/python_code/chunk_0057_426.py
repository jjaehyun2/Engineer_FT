package metaswarm.ui.hoverlabel {
	import flash.display.*;
	import flash.text.*;
	
	public class HoverLabel extends Sprite{
		
		//add formatting constants here
		public var labelMaker:LabelMaker;
		public var _output:TextField;
		public var _text:String;
		
		public function HoverLabel():void
		{
			_output = new TextField();
			_text = new String();
			labelMaker = new LabelMaker(this);
			
			init();
		}
		public function init():void {
			visible = true;
			focusRect = false;
			tabEnabled = false;
			mouseEnabled = false;
		}
		
		/*public function load():void{
			//
		}
		public function make():void{
			labelMaker.make();
		}
		public function go():void{
			labelMaker.go();
		}*/
		
		public function get text():String {
            return _text;
        }
        public function set text(newText:String):void {
        	_text = newText; 
		}
		
		public function update():void{
			_output.x = mouseX + 15;
			_output.y = mouseY + 5;
			_output.text = _text;
		}
		
		public function show():void{
			_output.visible = true;
		}
		
		public function hide():void{
			_output.visible = false;
		}
			
		
	}//end class
}//end pkg