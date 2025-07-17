package elements 
{
	import starling.display.Sprite;
	import starling.text.BitmapFont;
	import starling.text.TextField;
	import starling.utils.HAlign;
	/**
	 * ...
	 * @author LeleoSan
	 */
	public class Hud extends Sprite
	{
		/** statics */
		public static const WIN:String = "Win";
		public static const CREDITS:String = "Credits";
		public static const BET:String = "Bet";
		
		public function Hud() 
		{
			touchable = false;
			
			createField("default", "$", "fontWin", 40, 53, 30, 208, 0xFF9900);
			createField("default", "$", "fontCredits", 30, 30, 20, 602);
			createField("default", "$", "fontCredits", 30, 30, 306, 602);
			createField("Win", "0", "fontWin", 370, 53, 44, 208, 0xFF9900);
			createField("Credits", "0", "fontCredits", 167, 30, 33.3, 602);
			createField("Bet", "0", "fontCredits", 102, 30, 316, 602);
		}
		private function createField(_name:String, _text:String, _fontName:String, _width:Number, _height:Number, _x:Number, _y:Number, _color:Number = 0xFFFFFF):TextField
		{
			var field:TextField = new TextField(_width, _height, _text, _fontName, BitmapFont.NATIVE_SIZE, _color);
			field.name = _name; field.hAlign = HAlign.RIGHT; field.x = _x; field.y = _y;
			addChild(field);
			return field;
		}
		public function setText(_field:String, _value:String):void
		{
			TextField(getChildByName(_field)).text = _value;
		}
		public function getText(_field:String):String
		{
			return TextField(getChildByName(_field)).text;
		}
		public function destroy():void
		{
			removeChildren(0, -1, true);
			removeFromParent(true);
		}
	}

}