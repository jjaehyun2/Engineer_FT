package metaswarm.node.components.dot    {
	import flash.display.DisplayObject;
    import flash.display.Graphics;
    import flash.display.Shape;
	import flash.display.Sprite;
	import metaswarm.node.components.Particle;
	
	public class Dot extends Particle{
		
		public var dotMaker:DotMaker;
		public var dotButton:DotButton;
		
		public function Dot():void{
			dotMaker = new DotMaker(this);
			init();
		}
		public function init():void {
			//visible = true;
			//focusRect = true;
			//tabEnabled = true;
		}
		
		public function load():void{
			//
		}
		//might dep on load later, so leave here!
		public function make():void{
			dotMaker.make();
		}
		
	}
}