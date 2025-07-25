/**
* Copyright (c) 2013 Wesley Luyten
**/

package coverflow {

	import flash.system.*;
	import flash.utils.*;
	import flash.display.*;
	import flash.geom.*;
	import flash.events.*;
	import flash.ui.Keyboard;
	import flash.text.TextField;
	
	import aze.motion.EazeTween;
		
	public class CoverFlow extends Sprite {
	

		private var config:Object;
	
		private var canvas:Sprite;
		private var covers:Vector.<Cover>;
		private var tweenValues:Vector.<TypedObject>;
		private var oldTweenValues:Vector.<TypedObject>;
		private var coverIndexes:Vector.<int>;
		
		private var coversLength:int;
		private var completeLength:int = 0;
		private var maxCoverHeight:Number = 0;
		public var current:int = 0;

		private var time:Number;
		private var duration:Number;
		private var oldIndex:int;
		
		private var focalLength:Number;
		
		private var focusCallbacks:Array = [];
		private var clickCallbacks:Array = [];
		

		public function CoverFlow(playlist:Array, config:Object) {
			
			this.config = config;
			coversLength = playlist.length;
			covers = new Vector.<Cover>(coversLength, true);
			tweenValues = new Vector.<TypedObject>(coversLength * 2 - 1, true);
			oldTweenValues = new Vector.<TypedObject>(coversLength * 2 - 1, true);
			coverIndexes = new Vector.<int>(coversLength * 2 - 1, true);
			
			this.duration = config.tweentime * 1000;
			this.focalLength = config.focallength;
						
			canvas = new Sprite();
			addChild(canvas);
			
			for (var i:int = 0; i < coversLength; i++) {

				var cover:Cover = new Cover(this, i, playlist[i].image, config);
				canvas.addChild(cover);
				cover.addEventListener(MouseEvent.MOUSE_DOWN, clickHandler);
				covers[coversLength-i-1] = cover;
			}
			
			var index:int = coversLength - 1;		
			var len:int = coversLength * 2 - 1;
			for (i = 0; i < len; i++) {
				if (i == index) {
					tweenValues[i] = new TypedObject(0, 0, 0, 1);
					coverIndexes[i] = coversLength - 1;
				} else if (i < index) {
					tweenValues[i] = new TypedObject((index-i+1)*config.covergap+config.coveroffset, config.coverdepth, config.coverangle, 1-(index-i+1)*config.opacitydecrease);
					coverIndexes[i] = i;
				} else {
					tweenValues[i] = new TypedObject((i-index+1)*-config.covergap-config.coveroffset, config.coverdepth, -config.coverangle, 1-(i-index+1)*config.opacitydecrease);
					coverIndexes[i] = coversLength-i+index-1;
				}
				oldTweenValues[i] = new TypedObject();
			}
	
			addEventListener(Event.ADDED_TO_STAGE, perspective);	
			addEventListener(Event.ENTER_FRAME, staticTick);
		}
		
		public function destroy():void {
			removeEventListener(Event.ENTER_FRAME, staticTick);
			if (parent && parent.contains(this)) parent.removeChild(this);
		}
		
		public function fadeOut(callback:Function=null):void {
			if (visible == true) {
				for (var i:int = 0; i < coversLength; i++) {
					var tween:EazeTween = new EazeTween(covers[i].bitmap).to(0.7, { alpha:0 });
				}
				tween.onComplete(function():void {
					visible = false;
					if (parent && callback is Function) callback();
				});
			} else if (parent && callback is Function) {
				callback();
			}
		}
		
		public function fadeIn(callback:Function=null):void {
			if (visible == false) {
				visible = true;
				for (var i:int = 0; i < coversLength; i++) {
					covers[i].bitmap.alpha = 0; // force alpha back to zero
					var brightness:Number = covers[i]._brightness > 0 ? covers[i]._brightness : 0.005;
					var tween:EazeTween = new EazeTween(covers[i].bitmap).to(0.7, { alpha:brightness });
				}
				tween.onComplete(function():void {
					if (parent && callback is Function) callback();
				});
			} else if (parent && callback is Function) {
				callback();
			}
		}
		
		public function itemComplete(h:Number):void {
			maxCoverHeight = maxCoverHeight < h ? h : maxCoverHeight;
			completeLength += 1;
			if (completeLength == coversLength) {
				to(config.item);
				for (var i:int = 0; i < coversLength; i++) {
					covers[i].setY(maxCoverHeight);
				}
			}
		}
		
		private function clickHandler(e:MouseEvent):void {
			var cover:Cover = e.currentTarget as Cover;
			if (cover.mouseY < cover.halfHeight) {
				e.stopImmediatePropagation();
				if (cover.index != current) to(cover.index);
				else clicked(cover.index);
			}
		}
		
		private function perspective(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, perspective);
			
			var p:PerspectiveProjection = new PerspectiveProjection();
			p.focalLength = focalLength;
			p.projectionCenter = new Point(0, 0);
			transform.perspectiveProjection = p;
			
			stage.addEventListener(KeyboardEvent.KEY_DOWN, keyboard, false, 0, true);
		}
		
		private function keyboard(e:KeyboardEvent):void {
		
			if (stage && stage.focus is TextField) return;
		
			switch (e.keyCode) {
				case Keyboard.LEFT: left(); break;
				case Keyboard.RIGHT: right(); break;
				case Keyboard.UP:
				case Keyboard.PAGE_UP: to(0); break;
				case Keyboard.DOWN:					
				case Keyboard.PAGE_DOWN:
					if (coversLength) to(coversLength - 1);
					break;
				case Keyboard.SPACE:
					clicked(current);
					break;
			}
		}
		
		private function staticTick(e:Event):void {
			
			var ratio:Number = 1;
			var t:Number = new Date().getTime();
			t = (t - time) / duration;
			t = t > 1 ? 1 : t;
			ratio = (t == 1) ? 1 : -Math.pow(2, -10 * t) + 1;
			
			var i:int = coversLength;
			while (i--) {
				var cover:Cover = covers[i];
				var values:TypedObject = tweenValues[current+i];
				var oldValues:TypedObject = oldTweenValues[oldIndex+i];
				cover.x = oldValues.x + (values.x - oldValues.x) * ratio;
				cover.z = oldValues.z + (values.z - oldValues.z) * ratio;
				cover.rotationY = oldValues.rotationY + (values.rotationY - oldValues.rotationY) * ratio;
				cover.brightness = oldValues.brightness + (values.brightness - oldValues.brightness) * ratio;
			}			
		}
		
		public function left():void {
			if (current > 0) to(current - 1);
		}
			
		public function right():void {
			if (current < coversLength - 1) to(current + 1);
		}
		
		public function prev():void {
			if (current > 0) to(current - 1);
			else to(coversLength - 1);
		}
		
		public function next():void {
			if (current < coversLength - 1) to(current + 1);
			else to(0);
		}

		public function to(index:int):void {
			if (index > coversLength - 1) index = coversLength - 1;
			else if (index < 0) index = 0;
			
			focused(index);
			
			oldIndex = current;
			current = index;
			
			time = new Date().getTime();
			
			var i:int = coversLength;
			while (i--) {
				var cover:Cover = covers[i];
				var typedObject:TypedObject = oldTweenValues[oldIndex+i];
				typedObject.x = cover.x;
				typedObject.z = cover.z;
				typedObject.rotationY = cover.rotationY;
				typedObject.brightness = cover.brightness;
				canvas.setChildIndex(cover, coverIndexes[current+i]);
			}
		}
		
		public function onFocus(c:Function):void {
			focusCallbacks.push(c);
		}
		
		public function onClick(c:Function):void {
			clickCallbacks.push(c);
		}
		
		public function focused(index:int):void {
			for (var i:int = 0; i < focusCallbacks.length; i++) {
    			focusCallbacks[i](index);
			}
		}
		
		public function clicked(index:int):void {
			for (var i:int = 0; i < clickCallbacks.length; i++) {
				clickCallbacks[i](index);
			}
		}
	}
}