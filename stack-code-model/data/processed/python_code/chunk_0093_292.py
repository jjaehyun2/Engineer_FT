class FlashScripts.TweenColorTransform extends mx.transitions.Tween
{
	var obj, prop, func, __set__duration, useSeconds, _listeners, addListener, start, broadcastMessage, _time, changeCT, beginCT, _duration, finishCT;
	function TweenColorTransform (obj, prop, func, begin, finish, duration, useSeconds) {
		super();
		mx.transitions.OnEnterFrameBeacon.init();
		if (!arguments.length) {
			return;
		}
		this.obj = obj;
		this.prop = prop;
		this.begin = (begin);
		if (func) {
			this.func = func;
		}
		this.finish = (finish);
		position = (begin);
		__set__duration(duration);
		this.useSeconds = useSeconds;
		_listeners = [];
		this.addListener(this);
		this.start();
	}
	function set position(p) {
		setPosition(p);
		//return(position);
	}
	function setPosition(ct) {
		if (typeof(obj) == "movieclip") {
			obj.transform.colorTransform = ct;
		} else {
			var _local2 = 0;
			while (_local2 < rgba.length) {
				var _local3 = rgba[_local2];
				obj[_local3] = ct[_local3];
				_local2++;
			}
		}
		this.broadcastMessage("onMotionChanged", this, ct);
		updateAfterEvent();
	}
	function get position() {
		return(getPosition());
	}
	function getPosition(t) {
		if (t == undefined) {
			t = _time;
		}
		var _local6 = changeCT[changeProp];
		var _local8 = func(t, beginCT[changeProp], _local6, _duration);
		var _local5 = ((_local6 != 0) ? ((_local8 - beginCT[changeProp]) / _local6) : 0);
		var _local4 = new flash.geom.ColorTransform();
		var _local3 = 0;
		while (_local3 < rgba.length) {
			var _local2 = rgba[_local3];
			_local4[_local2] = beginCT[_local2] + (changeCT[_local2] * _local5);
			_local3++;
		}
		return(_local4);
	}
	function set begin(b) {
		beginCT = new flash.geom.ColorTransform();
		var _local2 = 0;
		while (_local2 < rgba.length) {
			var _local3 = rgba[_local2];
			beginCT[_local3] = b[_local3];
			_local2++;
		}
		//return(begin);
	}
	function get begin() {
		return(beginCT);
	}
	function set finish(f) {
		finishCT = f;
		changeCT = new flash.geom.ColorTransform();
		var _local4 = 0;
		var _local3 = 0;
		while (_local3 < rgba.length) {
			var _local2 = rgba[_local3];
			changeCT[_local2] = f[_local2] - beginCT[_local2];
			if (Math.abs(changeCT[_local2]) > _local4) {
				changeProp = _local2;
			}
			_local3++;
		}
		//return(finish);
	}
	function get finish() {
		return(finishCT);
	}
	function continueTo(finish, duration) {
		begin = (position);
		this.finish = (finish);
		if (duration != undefined) {
			__set__duration(duration);
		}
		this.start();
	}
	function toString() {
		return("[TweenColorTransform]");
	}
	var changeProp = "redOffset";
	var rgba = ["redOffset", "greenOffset", "blueOffset", "alphaOffset", "redMultiplier", "greenMultiplier", "blueMultiplier", "alphaMultiplier"];
}