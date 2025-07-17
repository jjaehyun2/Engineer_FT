package metaswarm.subset    {
	import flash.display.DisplayObject;
	import flash.display.Sprite;
	import flash.display.Graphics;
    import flash.display.Shape;
	
	public class Subset extends Sprite{
		
		public var nodes:Array;
		public var tiler:SubsetTiler;
		//var count:uint;
		
		//constructor:	
		public function Subset(){
			nodes = new Array();
			tiler = new SubsetTiler(this);
		}
		
		public function tile():void {
			//trace("tile");
			tiler.grid();
		}
		
		public function restore():void {
			//trace("tile");
			tiler.restore();
		}
		
		public function disable():void {
			trace("disable");
			for(var i:uint=0; i<nodes.length; i++){
				nodes[i].visible = false;
			}
		}
		
	}//end class
}//end pkg