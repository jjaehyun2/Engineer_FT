package {
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;
	import flash.geom.Point;
	
	[SWF(frameRate="60")]
    public class Main extends Sprite {
        private var drawing:Boolean;
		private var forceMode:Boolean;
        private var prevPoint:Point;
        private var sketch:BitmapData;
        private var sketchBitmap:Bitmap;
		private var canvas:Shape;
		private var lines:Vector.<Vector.<Point>>;
		private var nowPoint:Point;
		private var nowId:int;
		private var minPos:Point;
		private var maxPos:Point;
        public function Main() {
			stage.align = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.NO_SCALE;
            this.stage.addEventListener(MouseEvent.MOUSE_DOWN, begin);
            this.stage.addEventListener(Event.ENTER_FRAME, loop);
			this.stage.addEventListener(MouseEvent.RIGHT_MOUSE_DOWN, rightMouseDown);
			this.stage.addEventListener(MouseEvent.RIGHT_MOUSE_UP, rightMouseUp);
			this.stage.addEventListener(KeyboardEvent.KEY_DOWN, showData);
			var s:Sketch = new Sketch();
			var ss:Sprite = new Sprite();
			s.scaleX = s.scaleY = 2;
			ss.addChild(s);
			drawing = false;
            prevPoint = new Point(0, 0);
			nowPoint = new Point(0, 0);
            sketch = new BitmapData(ss.width*1.5, ss.height*1.5, false, 0xffffff);
            sketchBitmap = new Bitmap(sketch);
			canvas = new Shape();
			sketch.draw(ss);
			this.addChild(sketchBitmap);
			this.addChild(canvas);
			stage.stageWidth = sketch.width;
			stage.stageHeight = sketch.height;
			lines = new Vector.<Vector.<Point>>();
			minPos = new Point();
			maxPos = new Point();
			nowId = -1;
        }
        private function begin(e:MouseEvent):void{
            this.drawing = !drawing;
			if(this.drawing && nowPoint) {
				lines.push(new Vector.<Point>());
				nowId++;
				lines[nowId].push(nowPoint.clone());
				prevPoint = nowPoint.clone();
			}
        }
        private function loop(e:Event):void{
			canvas.graphics.clear();
			canvas.graphics.lineStyle(1, drawing?0x0000ff:0x00ff00);
			canvas.graphics.drawCircle(mouseX, mouseY, 30);
			canvas.graphics.lineStyle(1, 0xff0000);
			if(!drawing) {
				nowPoint = findFit(new Point(mouseX, mouseY), 30);
				if (nowPoint) {
					canvas.graphics.drawCircle(nowPoint.x, nowPoint.y, 5);
				}
			}else{
				if(forceMode){
					nowPoint.x = mouseX;
					nowPoint.y = mouseY;
					canvas.graphics.lineStyle(1, 0x00ff00);
					canvas.graphics.drawCircle(nowPoint.x, nowPoint.y, 2);
				}else {
					var r:Number = Math.atan2(mouseY - prevPoint.y, mouseX - prevPoint.x);
					var br:Number = r - Math.PI / 4;
					var er:Number = r + Math.PI / 4;
					var p:Point = findFitByRadius(prevPoint, 5, br, er);
					if (p) {
						var tx:Number = p.x - mouseX;
						var ty:Number = p.y - mouseY;
						if (p) {
							canvas.graphics.lineStyle(1, 0x00ff00);
							canvas.graphics.drawCircle(p.x, p.y, 2);
							if (Math.sqrt(tx * tx + ty * ty) < 2) {
								lines[nowId].push(p.clone());
								prevPoint = p.clone();
							}
						}
					}
				}
			}
			minPos.x = minPos.y = Number.MAX_VALUE;
			maxPos.x = maxPos.y = Number.MIN_VALUE;
			for(var i:int = 0; i < lines.length; i ++){
				canvas.graphics.lineStyle(3, 0xff0000);
				for(var ii:int = 0; ii < lines[i].length; ii++){
					var x:Number = lines[i][ii].x;
					var y:Number = lines[i][ii].y;
					if(ii == 0){
						canvas.graphics.moveTo(x, y);
					}else{
						canvas.graphics.lineTo(x, y);
					}
					if(minPos.x > x) minPos.x = x;
					if(minPos.y > y) minPos.y = y;
					if(maxPos.x < x) maxPos.x = x;
					if(maxPos.y < y) maxPos.y = y;
				}
			}
			canvas.graphics.lineStyle(1, 0x00ff00);
			canvas.graphics.drawRect(minPos.x, minPos.y, maxPos.x - minPos.x, maxPos.y - minPos.y);
        }
		private function showData(e:*):void{
			var w:Number = maxPos.x - minPos.x;
			var h:Number = maxPos.y - minPos.y;
			w = int(w*100)/100;
			h = int(h*100)/100;
			var data:Object = {
				lines:[],
				width:w,
				height:h
			};
			for(var i:int = 0; i < lines.length; i ++){
				var d:Array = [];
				for(var ii:int = 0; ii < lines[i].length; ii++){
					var x:Number = lines[i][ii].x - minPos.x;
					var y:Number = lines[i][ii].y - minPos.y;
					x = int(x*100)/100;
					y = int(y*100)/100;
					d.push({
						x:x,
						y:y
					});
				}
				data.lines.push(d);
			}
			trace(JSON.stringify(data));
		}
		private function rightMouseDown(e:MouseEvent):void{
			if(!drawing){
				return;
			}
			forceMode = true;
		}
		private function rightMouseUp(e:MouseEvent):void{
			if(!drawing){
				return;
			}
			forceMode = false;
			lines[nowId].push(nowPoint.clone());
			prevPoint = nowPoint.clone();
		}
		private function findFit(basePoint:Point, maxR:Number):Point{
			for(var r:Number = 1; r < maxR; r++){
                var p:Point = findFitByRadius(basePoint, r);
                if(p) return p;
			}
            return null;
		}
        private function findFitByRadius(basePoint:Point, r:Number, br:Number = 0, er:Number = Math.PI*2):Point{
            var res:Number = 1;
            var rres:Number = res/(r*2*Math.PI)*Math.PI*2;
            var pColor:int = -1;
            for(var i:Number = br; i < er; i += rres){
                var x:Number = basePoint.x + Math.cos(i)*r;
                var y:Number = basePoint.y + Math.sin(i)*r;
				var color:uint = sketch.getPixel(x, y);
                if(color == 0xffff00) return new Point(x, y);
            }
            return null;
        }
    }
}