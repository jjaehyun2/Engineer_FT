package GameObjects.Maps
{
	import flash.display.DisplayObject;
	import flash.display.Shape;
	import flash.display.Sprite;
	import GameObjects.Player;

	public class GrassMap extends Sprite
	{
		public function GrassMap()
		{
			var ground:Shape = new Shape();
			ground.graphics.beginFill(0x009900);
			ground.graphics.drawRect(100,200,300,5);
			ground.graphics.endFill();
			addChild(ground);
			
		}
		
		public function addPlayer(player:Player):void
		{
			addChild(player.fighter as DisplayObject);
		}
	}
}