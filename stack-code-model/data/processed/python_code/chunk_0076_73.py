package  
{
	import flash.display.Sprite;
	import flash.text.TextField;
	import flash.text.TextFormat;
	/**
	 * ...
	 * @author Jake
	 */
	public class InkBar extends Sprite
	{
		private var bar:Sprite;
		private var color:uint;
		private var borderColor:uint = 0xbdbdbd;
		private var fill:int = 0;
		private var container:Sprite;
		private var inkPercent:TextField;
		private var large:Boolean;
		private var thickness:Number = 6;
		private var inkTextX:Number = 102.5;
		private var cartDisplay:TextField;
		private var displayText:TextFormat;
		private var cartType:String="null";
		
		public function InkBar(x:int,y:int,color:uint,large:Boolean=false,cartType:String="null") 
		{
			this.x = x;
			this.y = y;
			this.color = color;
			this.large = large;
			this.cartType = cartType;
			displayText= new TextFormat();
			displayText.size = 10;
			if (!large)
			{
				bar = new Sprite();
				container = new Sprite();
				container.graphics.lineStyle(1, borderColor);
				container.graphics.drawRect(0, 0, 100, 7);
				addChild(container);
				bar.graphics.beginFill(color);
				bar.graphics.drawRect(.5, .75, fill, 5.5);
				bar.graphics.endFill();
				addChild(bar);
			}
			else 
			{
				bar = new Sprite();
				container = new Sprite();
				container.graphics.lineStyle(2, borderColor);
				container.graphics.drawRect(0, 0, 150, 20);
				addChild(container);
				thickness = 18.75;
				displayText.size = 18;
				bar.graphics.beginFill(color);
				bar.graphics.drawRect(.5, .75, fill, 5.5);
				bar.graphics.endFill();
				addChild(bar);
			}
		}
		
		public function adjustInk(newValue:Number):void
		{
			var displayValue:Number = newValue;
			if (checkForError(newValue)) 
			{
				if (large) 
				{
					newValue *= 1.5;
				}
				removeChild(bar);
				bar.graphics.clear();
				bar.graphics.beginFill(color);
				bar.graphics.drawRect(.5, .85, newValue, thickness);
				bar.graphics.endFill();
				addChild(bar);
				inkDisplay(displayValue);
			}
			else 
			{
				if (large) 
				{
					newValue *= 1.5;
				}
				removeChild(bar);
				bar.graphics.clear();
				bar.graphics.beginFill(0xFF0000);
				bar.graphics.drawRect(.5, .85, 0, thickness);
				bar.graphics.endFill();
				addChild(bar);
				inkDisplay(-1);
			}
			
			
		}
		
		private function inkDisplay(value:int):void 
		{
			if (large)
			{
				inkTextX = 152.5;
				displayCartType();
			}
			inkPercent = new TextField();
			inkPercent.x = inkTextX;
			inkPercent.y = -3;
			inkPercent.defaultTextFormat = displayText;
			if (value >= 0)
			{ 
				inkPercent.text = value.toString() + "%" ; 
			}
			else
			{
				inkPercent.textColor = 0xFF0000
				inkPercent.text = "Error"; 
			}
			inkPercent.selectable = false;
			addChild(inkPercent);
		}
		
		private function displayCartType():void 
		{
			displayText.bold = true;
			cartDisplay = new TextField();
			cartDisplay.x = inkTextX+50;
			cartDisplay.y = -3;
			cartDisplay.width = 100;
			cartDisplay.text = cartType;
			cartDisplay.setTextFormat(displayText);
			displayText.bold = false;
			addChild(cartDisplay);
		}
		
		private function checkForError(value:int):Boolean
		{	
			if (value > 0) 
			{
				return true;
			}
			return false;
		}
	}

}