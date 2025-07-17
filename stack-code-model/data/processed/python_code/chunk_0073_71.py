package elements 
{
	import starling.display.Image;
	import starling.display.Sprite;
	/**
	 * ...
	 * @author LeleoSan
	 */
	public class Roulette extends Sprite
	{
		/** objects */
		public var items:Array;
		/** statics */
		public static const TYPES:Array = new Array({ name:"bar", prize:12 }, { name:"seven", prize:9 }, { name:"clover", prize:8 }, { name:"coin", prize:7 },
																		  { name:"bell", prize:6 }, { name:"lemon", prize:5 }, { name:"orange", prize:4 }, { name:"grape", prize:3 }, { name:"plum", prize:2 }, { name:"mulberry", prize:1 });
		public static const MULBERRY_PRIZE:int = 10;
		public static const MULBERRY_PRIZE2:int = 20;
		
		public function Roulette() 
		{
			items = new Array();
			
			var item:Image;
			for (var i:int = 0; i < Roulette.TYPES.length; i++) {
				item = new Image(Root.assets.getTextureAtlas("spriteAll").getTexture(Roulette.TYPES[i].name + "Big.png"));
				item.alignPivot();
				item.name = Roulette.TYPES[i].name;
				item.y = -100 * i;
				addChild(item);
				items.push(item);
			}
		}
		public static function getPrize(_name:String):int
		{
			for (var i:int = 0; i < Roulette.TYPES.length; i++) {
				if (Roulette.TYPES[i].name == _name) {
					return Roulette.TYPES[i].prize;
				}
			}
			return 0;
		}
		public function destroy():void
		{
			removeChildren(0, -1, true);
			removeFromParent(true);
		}
	}

}