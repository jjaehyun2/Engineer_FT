package
{
	import as3isolib.display.scene.IsoGrid;
	
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.filters.GlowFilter;

	import masputih.isometric.Tile;

	public class TileTest extends Tile
	{
		public function TileTest(iso:IsoGrid)
		{
			super(iso);
			var plot:MovieClip = new PlotClear();
			//this.addChild(plot);
			this.sprites = [plot];
			mainContainer.addEventListener(MouseEvent.MOUSE_OVER, addStroke);
			mainContainer.addEventListener(MouseEvent.MOUSE_OUT, removeStroke);
		}
		
		public function addStroke(event:Event):void{
			var filt:Array = new Array();
			var g:GlowFilter = new GlowFilter(0xFFFF00, 1, 4, 4, 100);
			filt.push(g);
			mainContainer.filters = filt;
		}
		
		public function removeStroke(event:Event):void{
			var filt:Array = new Array();
			mainContainer.filters = new Array()	
		}
	}
}