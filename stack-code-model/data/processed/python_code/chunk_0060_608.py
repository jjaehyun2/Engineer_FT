class mx.managers.OverlappedWindows
{
	function OverlappedWindows () {
	}
	static function checkIdle(Void) {
		if (mx.managers.SystemManager.idleFrames > 10) {
			mx.managers.SystemManager.dispatchEvent({type:"idle"});
		} else {
			mx.managers.SystemManager.idleFrames++;
		}
	}
	static function __addEventListener(e, o, l) {
		if (e == "idle") {
			if (mx.managers.SystemManager.interval == undefined) {
				mx.managers.SystemManager.interval = setInterval(mx.managers.SystemManager.checkIdle, 100);
			}
		}
		mx.managers.SystemManager._xAddEventListener(e, o, l);
	}
	static function __removeEventListener(e, o, l) {
		if (e == "idle") {
			if (mx.managers.SystemManager._xRemoveEventListener(e, o, l) == 0) {
				clearInterval(mx.managers.SystemManager.interval);
			}
		} else {
			mx.managers.SystemManager._xRemoveEventListener(e, o, l);
		}
	}
	static function onMouseDown(Void) {
		mx.managers.SystemManager.idleFrames = 0;
		mx.managers.SystemManager.isMouseDown = true;
		var _local5 = _root;
		var _local3;
		var _local8 = _root._xmouse;
		var _local7 = _root._ymouse;
		if (mx.managers.SystemManager.form.modalWindow == undefined) {
			if (mx.managers.SystemManager.forms.length > 1) {
				var _local6 = mx.managers.SystemManager.forms.length;
				var _local4;
				_local4 = 0;
				while (_local4 < _local6) {
					var _local2 = mx.managers.SystemManager.forms[_local4];
					if (_local2._visible) {
						if (_local2.hitTest(_local8, _local7)) {
							if (_local3 == undefined) {
								_local3 = _local2.getDepth();
								_local5 = _local2;
							} else if (_local3 < _local2.getDepth()) {
								_local3 = _local2.getDepth();
								_local5 = _local2;
							}
						}
					}
					_local4++;
				}
				if (_local5 != mx.managers.SystemManager.form) {
					mx.managers.SystemManager.activate(_local5);
				}
			}
		}
		var _local9 = mx.managers.SystemManager.form;
		_local9.focusManager._onMouseDown();
	}
	static function onMouseMove(Void) {
		mx.managers.SystemManager.idleFrames = 0;
	}
	static function onMouseUp(Void) {
		mx.managers.SystemManager.isMouseDown = false;
		mx.managers.SystemManager.idleFrames = 0;
	}
	static function activate(f) {
		if (mx.managers.SystemManager.form != undefined) {
			if ((mx.managers.SystemManager.form != f) && (mx.managers.SystemManager.forms.length > 1)) {
				var _local1 = mx.managers.SystemManager.form;
				_local1.focusManager.deactivate();
			}
		}
		mx.managers.SystemManager.form = f;
		f.focusManager.activate();
	}
	static function deactivate(f) {
		if (mx.managers.SystemManager.form != undefined) {
			if ((mx.managers.SystemManager.form == f) && (mx.managers.SystemManager.forms.length > 1)) {
				var _local5 = mx.managers.SystemManager.form;
				_local5.focusManager.deactivate();
				var _local3 = mx.managers.SystemManager.forms.length;
				var _local1;
				var _local2;
				_local1 = 0;
				while (_local1 < _local3) {
					if (mx.managers.SystemManager.forms[_local1] == f) {
						_local1 = _local1 + 1;
						while (_local1 < _local3) {
							if (mx.managers.SystemManager.forms[_local1]._visible == true) {
								_local2 = mx.managers.SystemManager.forms[_local1];
							}
							_local1++;
						}
						mx.managers.SystemManager.form = _local2;
						break;
					}
					if (mx.managers.SystemManager.forms[_local1]._visible == true) {
						_local2 = mx.managers.SystemManager.forms[_local1];
					}
					_local1++;
				}
				_local5 = mx.managers.SystemManager.form;
				_local5.focusManager.activate();
			}
		}
	}
	static function addFocusManager(f) {
		mx.managers.SystemManager.forms.push(f);
		mx.managers.SystemManager.activate(f);
	}
	static function removeFocusManager(f) {
		var _local3 = mx.managers.SystemManager.forms.length;
		var _local1;
		_local1 = 0;
		while (_local1 < _local3) {
			if (mx.managers.SystemManager.forms[_local1] == f) {
				if (mx.managers.SystemManager.form == f) {
					mx.managers.SystemManager.deactivate(f);
				}
				mx.managers.SystemManager.forms.splice(_local1, 1);
				return(undefined);
			}
			_local1++;
		}
	}
	static function enableOverlappedWindows() {
		if (!initialized) {
			initialized = true;
			mx.managers.SystemManager.checkIdle = checkIdle;
			mx.managers.SystemManager.__addEventListener = __addEventListener;
			mx.managers.SystemManager.__removeEventListener = __removeEventListener;
			mx.managers.SystemManager.onMouseDown = onMouseDown;
			mx.managers.SystemManager.onMouseMove = onMouseMove;
			mx.managers.SystemManager.onMouseUp = onMouseUp;
			mx.managers.SystemManager.activate = activate;
			mx.managers.SystemManager.deactivate = deactivate;
			mx.managers.SystemManager.addFocusManager = addFocusManager;
			mx.managers.SystemManager.removeFocusManager = removeFocusManager;
		}
	}
	static var initialized = false;
	static var SystemManagerDependency = mx.managers.SystemManager;
}