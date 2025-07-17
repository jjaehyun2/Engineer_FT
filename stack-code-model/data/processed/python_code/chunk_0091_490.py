package com.component.hpbar
{
	import com.game.unit.core.Properties;
	
	import starling.display.Canvas;
	import starling.display.Sprite;
	
	public class HpBar extends Sprite
	{
//		private var rect:Sprite;
		private var barWidth:Number;
		
		private var red:Canvas;
		
		public function HpBar()
		{
//			rect = new Sprite();
//			addChild(rect);
			
			red = new Canvas();
			addChild(red);
			
			visible = false;
		}
		
		public function draw(barWidth:Number):void{
			this.barWidth = barWidth;
			
//			graphics.lineStyle(1);
//			graphics.drawRect(-barWidth/2,-3,barWidth+1,4);
//			graphics.endFill();
//			drawGraphics();
			
			red.beginFill(0xff0000);
			red.drawRectangle(0,0,barWidth,3);
			red.endFill();
			red.x = -red.width>>1;
			red.pivotY = red.height>>1;
		}
		
		public function percent(value:Number,color:uint=0xff0000):void{
			if(value < 0) value = 0;
			
			red.scaleX = value;
			
			if(value<1){
				visible = true;
			}
//			graphics.clear();
//			
//			graphics.lineStyle();
//			graphics.beginFill(color);
//			graphics.drawRect(-barWidth/2,-3,barWidth * value,4);
//			graphics.endFill();
//			
//			graphics.lineStyle(1);
//			graphics.drawRect(-barWidth/2,-3,barWidth,4);
//			graphics.endFill();
		}
		
		public function percentFromProperty(p:Properties):void{
			percent(p.hp/p.hpMax);
		}
	}
}