package game
{
	import flash.geom.Point;
	
	import system.loader.ResPath;
	import system.ui.Panel;

	public class PlayPanel extends Panel
	{
		public static var PANELNAME:String = "PlayPanel";
		
		override public function onCreate():void
		{
			MapManager.instance().loadMapConfig(1).createMap().showMap();
		}
		
		override public function getResUrl():Array{
			return [ResPath.ROOT+"config/level1.json"];
		}
		
		override public function reLayout():void{
			var point:Point = Game.instance().getPosition();
			this.x = point.x;
			this.y = point.y;
		}
	}
}