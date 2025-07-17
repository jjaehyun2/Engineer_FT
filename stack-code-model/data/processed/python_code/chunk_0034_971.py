package com.illuzor.bitmap {
	
	import com.bit101.components.ColorChooser;
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.events.TimerEvent;
	import flash.filters.BlurFilter;
	import flash.filters.ConvolutionFilter;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import flash.text.TextField;
	import flash.utils.Timer;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	
	/**
	 * ...
	 * @author illuzor // illuzor@gmail.com // illuzor.com
	 */
	
	public class MainBitmapData extends Sprite{
		
		private var bitmapdata:BitmapData;
		private var bitmap:Bitmap;
		
		private var currentEffect:String = "EFFECT 1";
		private var counter:Number = 1;
		private var blurCounter:uint;
		private var forward:Boolean = false;
		private var color1:uint = 0xFFFFFF;
		private var color2:uint = 0xFF00FF;
		private var plaing:Boolean = true;
		
		private var speed:uint = 1;
		private var waveLength:Number = 30;
		private var amplitude:uint = 100;

		private var bitmapContainer:Sprite;
		private var controlPanel:Panel;
		
		
		public function MainBitmapData():void{
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void{
			removeEventListener(Event.ADDED_TO_STAGE, init);
			stage.align = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.NO_SCALE;
			
			bitmapContainer = new Sprite();
			addChild(bitmapContainer)
			bitmapdata = new BitmapData(800, 600, false, 0x000000);
			bitmap = new Bitmap(bitmapdata);
			bitmapContainer.addChild(bitmap);
			
			controlPanel = new Panel();
			controlPanel.x = controlPanel.y = 8;
			addChild(controlPanel);
			controlPanel.effects.addEventListener(Event.SELECT, changeEffect);
			controlPanel.addEventListener(MouseEvent.CLICK, onPanelClick);
			controlPanel.color1.addEventListener(Event.CHANGE, changeColor);
			controlPanel.color2.addEventListener(Event.CHANGE, changeColor);
			controlPanel.singleColor.addEventListener(Event.CHANGE, changeSingleColor);
			controlPanel.length.addEventListener(Event.CHANGE, changeLength);
			controlPanel.speed.addEventListener(Event.CHANGE, changeSpeed);
			controlPanel.amplitude.addEventListener(Event.CHANGE, changeAmplitude);
			
			addEventListener(Event.ENTER_FRAME, draw);
		}
		
		private function changeAmplitude(e:Event):void {
			amplitude = controlPanel.amplitude.value;
		}
		
		private function changeLength(e:Event):void {
			waveLength = controlPanel.length.value;
		}
		
		private function changeSpeed(e:Event):void {
			speed = controlPanel.speed.value;
		}
		
		private function changeSingleColor(e:Event):void {
			if (controlPanel.singleColor.selected) {
				controlPanel.color2.value = controlPanel.color1.value;
				color2 = color1;
			}
		}
		
		private function changeColor(e:Event):void {
			if (controlPanel.singleColor.selected) {
				color1 = color2 = e.target.value;
				controlPanel.color1.value = controlPanel.color2.value = e.target.value;
			} else {
				if (e.target == controlPanel.color1) {
					color1 = controlPanel.color1.value;
				} else if (e.target == controlPanel.color2) {
					color2 = controlPanel.color2.value;
				}
			}
		}

		private function changeEffect(e:Event):void {
			if (currentEffect != e.target.selectedItem) {
				currentEffect = e.target.selectedItem;
				if (controlPanel.autoclear.selected) clearBitmap();
			}
		}
		
		private function onPanelClick(e:MouseEvent):void {
			switch(e.target) {
				case controlPanel.clearBackground:
					clearBitmap();
				break;
				
				case controlPanel.randomize:
					randomize();
				break;
				
				case controlPanel.play:
					if (!plaing) {
						plaing = true;
						addEventListener(Event.ENTER_FRAME, draw);
					}
				break;
				
				case controlPanel.pause:
					if (plaing) {
						plaing = false;
						removeEventListener(Event.ENTER_FRAME, draw);
					}
				break;
			}
		}
		
		private function randomize():void {
			controlPanel.color1.value = color1 = randomColor();
			
			if (controlPanel.singleColor.selected) {
				controlPanel.color2.value = color2 = color1
			} else {
				controlPanel.color2.value = color2 = randomColor();
			}
			controlPanel.speed.value = speed = Math.round(Math.random() * 9) + 1;
			controlPanel.length.value = waveLength =  Math.round(Math.random() * 299) +1;
			controlPanel.amplitude.value = amplitude = Math.round(Math.random() * 250);
		}
		
		private function clearBitmap():void {
			bitmapContainer.removeChild(bitmap);
				bitmapdata = new BitmapData(800, 600, false, 0x000000);
				bitmap = new Bitmap(bitmapdata);
				bitmapContainer.addChild(bitmap);
		}
		
		private function draw(e:Event):void{
			if (!forward){
				counter += speed;
			}
			else{
				counter -= speed;
			}
			
			if (counter >= 1200 || counter <= 0){
				forward = !forward;
			}
			
			if (currentEffect == "EFFECT 2") {
				blurCounter++;
				if (blurCounter > 8) blurCounter = 0;
			}
			
			if (currentEffect == "EFFECT 1" || currentEffect == "EFFECT 2") {
				if (currentEffect == "EFFECT 2" && blurCounter == 8) bitmapdata.applyFilter(bitmapdata, bitmap.getRect(this), new Point(), new BlurFilter(2, 2));
				bitmapdata.setPixel32(Math.sin(counter / waveLength) * amplitude + 400, counter / 2, color1);
				bitmapdata.setPixel32( -Math.sin(counter  / waveLength) * amplitude + 400, counter / 2, color2);
			} else {
				if (currentEffect == "EFFECT 4") bitmapdata.applyFilter(bitmapdata, bitmap.getRect(this), new Point(), new BlurFilter(2, 2));
				for (var i:int = 0; i < amplitude*.4; i++) {
					bitmapdata.setPixel32(Math.sin(counter  / waveLength) * (amplitude * Math.random()) + (400), counter / 2, color1);
					bitmapdata.setPixel32( -Math.sin(counter  / waveLength) * (amplitude * Math.random()) + (400), (counter) / 2, color2);
				}
			}
		}
		
		private function randomColor():uint{
			var color:uint = Math.random() * 0x1000000;
			return color;
		}
	
	}
}