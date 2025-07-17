package com.component.gt
{
	import starling.text.TextField;
	
	public class TextGame extends TextField
	{
		public var index:int;
		public function TextGame(text:String="",width:int=80, height:int=40)
		{
			super(width, height, text, "Verdana", 14, 0xFFFFFF);
			
			pivotX = width>>1;
			pivotY = height>>1;
		}
	}
}