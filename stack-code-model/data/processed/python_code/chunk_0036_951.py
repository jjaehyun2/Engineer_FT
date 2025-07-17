package display {
	
	import constants.ResourceType;
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Graphics;
	import flash.display.Sprite;
	import flash.events.MouseEvent;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class House extends Sprite {
		
		private static var graphicsList:Object = { };
		
		private var _wSize:uint;
		private var _hSize:uint;
		private var _xPosition:uint;
		private var _yPosition:uint;
		private var gName:String;
		
		public function House(wSize:uint = 1, hSize:uint = 1) {
			this._hSize = hSize;
			this._wSize = wSize;
			draw();
			addEventListener(MouseEvent.CLICK, onClick);
		}
		
		private function draw():void {
			gName = "gr"+String(wSize) + String(hSize);
			if (!graphicsList.hasOwnProperty(gName)) {
				var gr:Graphics = this.graphics;
				gr.lineStyle(1, 0x0);
				gr.beginFill(0x008000);
				gr.moveTo(0, 15);
				gr.lineTo(25 * _wSize, getY(_wSize, 1));
				gr.lineTo(getX(_wSize, _hSize), getY(_wSize, _hSize+1));
				gr.lineTo(25 * _hSize, 15 * _hSize+15);
				gr.lineTo(0, 15);
				gr.endFill();
				
				var bdata:BitmapData = new BitmapData(this.width, this.height, true, 0x0);
				bdata.draw(this);
				graphicsList[gName] = bdata
			}
			
			addChild(new Bitmap(graphicsList[gName]));
		}
		
		public function setPosinion(xPosition:uint, yPosition:uint):void {
			this._yPosition = yPosition;
			this._xPosition = xPosition;
			this.x = getX(xPosition, yPosition);
			this.y = getY(xPosition, yPosition);
		}
		
		private function getX(xCount:uint, yCount:uint):int {
			return xCount * 25 + yCount * 25;
		}
		
		private function getY(xCount:uint, yCount:uint):int {
			return xCount * -15 + yCount * 15;
		}
		
		private function onClick(e:MouseEvent):void {
			explode();
		}
		
		public function explode():void {
			var ground:Bitmap = new Bitmap(ResourceManager.getBitmapData(ResourceType.GROUND), "auto", true);
			addChild(ground);
			ground.width = this.width;
			ground.height = this.height;
			ground.y = -ground.height / 2;
			var gmask:Bitmap = new Bitmap(graphicsList[gName]);
			addChild(gmask);
			ground.mask = gmask;
		}
		
		public function get wSize():uint {
			return _wSize;
		}
		
		public function get hSize():uint {
			return _hSize;
		}
		
		public function get xPosition():uint {
			return _xPosition;
		}
		
		public function get yPosition():uint {
			return _yPosition;
		}
	}
}