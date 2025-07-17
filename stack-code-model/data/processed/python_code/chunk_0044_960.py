package metaswarm.node.components.dot    {
	import flash.display.DisplayObject;
    import flash.display.Graphics;
    import flash.display.Shape;
	import flash.display.Sprite;
	
	public class DotMaker extends Sprite{
		
		private var _dot:Dot;
		
		public function DotMaker(dot:Dot):void{
			_dot = dot;
			init();
		}
		public function init():void{
			//
		}
		public function make():void{
			_dot.dotButton = new DotButton();
			_dot.addChild(_dot.dotButton);
		}
	}
}