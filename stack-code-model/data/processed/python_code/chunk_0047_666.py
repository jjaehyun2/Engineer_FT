
// ScrollBar Class
// by Valentino Tombesi 
// http://www.fuoridalcerchio.net

import mx.transitions.Tween; 
import mx.transitions.easing.*; 

class ScrollBarD extends MovieClip {

	private var scrollbar:MovieClip;
	private var scrollobj:MovieClip;
	private var minY:Number, maxY:Number, endY:Number, diffY:Number;
	private var percentuale:Number = 0;
	private var obj_minY:Number, obj_maxY:Number, obj_endY:Number, obj_diffY:Number, content_starty:Number;
	private var clip_ruler:MovieClip, clip_sfondo:MovieClip, clip_dragged:MovieClip, clip_mask:MovieClip;
	
	private var b_FirstExceed:Boolean	= false;//k

	private var scrollWheelSpeed:Number, tweenSpeed:Number; 

	function ScrollBarD() {
	}
	function setMinY(val:Number) {
		minY = val;
	}

	function setMaxY(val:Number) {
		maxY = val;
	}
	function getMaxY():Number {
		return maxY;
	}
	function getMinY():Number {
		return minY;
	}
	function setDragged(mc:MovieClip) {
		clip_dragged = mc;
	}
	function setRuler(mc:MovieClip) {
		clip_ruler = mc;
	}
	function setBackground(mc:MovieClip) {
		clip_sfondo = mc;
	}
	function setMaschera(mc:MovieClip) {
		clip_mask = mc; 
	}
	function setTweenSpeed(speed:Number) {
		tweenSpeed = speed; 
	}
	function setMouseWheelAdd(number:Number) {
		scrollWheelSpeed = number; 
	}
	function init() {
		setMinY(0);
		setMaxY(clip_sfondo._height - clip_ruler._height);

		var mouseListener:Object = new Object();
		
		content_starty = clip_dragged._y; 

		mouseListener.target = this;

		var mc:MovieClip = this;

		mouseListener.onMouseWheel = function(delta:Number) {
			if (mc.clip_dragged.hitTest(_root._xmouse, _root._ymouse, false)) {
				this.target.scrollData(delta);
			}
		};

		Mouse.addListener(mouseListener);

		clip_ruler.onPress = function() {
			this.startDrag(false,0,this._parent.getMinY(),0,this._parent.getMaxY());
		};

		clip_ruler.onRelease = clip_ruler.onReleaseOutside = function () {
			this.stopDrag();
		};
		this.onEnterFrame = function() {
			updateContentPos();
		};
	}
	function scrollData(delta:Number) {
		var d:Number;

		if (delta > 1) {
			delta = 1;
		}
		if (delta < -1) {
			delta = -1;
		}
		d = -delta * scrollWheelSpeed;

		if (d > 0) {
			var rulerY:Number = Math.min(getMaxY(), clip_ruler._y + d);
		}
		if (d < 0) {
			var rulerY:Number = Math.max(getMinY(), clip_ruler._y + d);
		}
		
		var ruler_mov:Tween = new Tween(clip_ruler, "_y", Strong.easeOut, clip_ruler._y, rulerY, this.tweenSpeed, false); 

		updateContentPos();
	}
	function updateContentPos() {
		var minY:Number, maxY:Number, curY:Number;

		percentuale = (100 / getMaxY()) * clip_ruler._y;

		minY = 0;
		maxY = clip_dragged._height - (clip_mask._height / 2);
		
		if (clip_dragged._height > clip_mask._height) {
			
						
			clip_ruler._visible = true;
			clip_sfondo._visible = true; //k


			curY = content_starty; 
			var halfMaskHeight:Number = (clip_mask._height / 2); 
			
			var finalX:Number = curY - (((maxY - halfMaskHeight) / 100) * percentuale)
			
			var dragged_mov:Tween = new Tween(clip_dragged, "_y", Strong.easeOut, clip_dragged._y, finalX, this.tweenSpeed, false); 
			
		} else {
			var dragged_mov:Tween = new Tween(clip_dragged, "_y", Strong.easeOut, clip_mask._y, finalX, this.tweenSpeed, false);//k
			clip_ruler._visible = false;
			clip_sfondo._visible = false; 
		}
	}

}