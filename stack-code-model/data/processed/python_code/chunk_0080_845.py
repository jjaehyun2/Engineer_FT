package metaswarm.node.components.databox   {
	import flash.display.*;
	import flash.text.*;
	
	class DataBoxButtonState extends Sprite {
		private var typeOfButton:String;
		private var bgColor:uint;
		private var lineColor:uint;
		private var size:uint;
	
		public function DataBoxButtonState(typeOfButton:String, lineColor:uint, bgColor:uint, size:uint) {
			this.typeOfButton = typeOfButton;
			this.bgColor = bgColor;
			this.lineColor = lineColor;
			this.size = size;
			draw();
		}
	
		private function draw():void {
			graphics.beginFill(bgColor);
			graphics.drawRect(0, 0, size, size);
			graphics.endFill();
			graphics.lineStyle(0, lineColor);
			//graphics.beginFill(lineColor);
			
			//. . . . .
			//. a . b .
			//. . . . .
			//. c . d .
			//. . . . .
			var ax:Number = size*(1/4);
			var ay:Number = size*(1/4);
			var bx:Number = size*(3/4);
			var by:Number = size*(1/4);
			var cx:Number = size*(1/4);
			var cy:Number = size*(3/4);
			var dx:Number = size*(3/4);
			var dy:Number = size*(3/4);
			
			
			switch (typeOfButton) {
				case "close"://x
					//trace(0);
					graphics.moveTo(ax, ay);
					graphics.lineTo(dx, dy);
					graphics.moveTo(bx, by);
					graphics.lineTo(cx, cy);
					break;
				case "popout"://>
					//trace(1);
					graphics.moveTo(ax, ay);
					graphics.lineTo(dx, dy);
					graphics.moveTo(bx, by);
					graphics.lineTo(dx, dy);
					graphics.lineTo(cx, cy);
					break;
				case "popin"://<
					//trace(2);
					graphics.moveTo(ax, ay);
					graphics.lineTo(dx, dy);
					graphics.moveTo(bx, by);
					graphics.lineTo(ax, ay);
					graphics.lineTo(cx, cy);
					break;
				default:
					trace("Not a valid type of button");
			}
			
			//graphics.endFill();
			
			/*var label:TextField = new TextField();
			var fmt:TextFormat = new TextFormat(txt, size/2, 0xCCCCCC);
			//label.x = dbx.closeButton.x;
			//label.y = dbx.closeButton.y;
			label.autoSize = TextFieldAutoSize.LEFT;
			//label.width = size;
			//label.height = size;
			label.setTextFormat(fmt);
			label.text = txt;
			addChild(label);
			label.mouseEnabled = false;*/
		}
	}
}