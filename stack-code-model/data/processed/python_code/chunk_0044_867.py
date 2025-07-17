class mx.skins.halo.FocusRect extends mx.skins.SkinElement
{
	var boundingBox_mc, _xscale, _yscale, clear, beginFill, drawRoundRect, endFill, _visible;
	function FocusRect () {
		super();
		boundingBox_mc._visible = false;
		boundingBox_mc._width = (boundingBox_mc._height = 0);
	}
	function draw(o) {
		o.adjustFocusRect();
	}
	function setSize(w, h, r, a, rectCol) {
		_xscale = (_yscale = 100);
		this.clear();
		if (typeof(r) == "object") {
			r.br = ((r.br > 2) ? (r.br - 2) : 0);
			r.bl = ((r.bl > 2) ? (r.bl - 2) : 0);
			r.tr = ((r.tr > 2) ? (r.tr - 2) : 0);
			r.tl = ((r.tl > 2) ? (r.tl - 2) : 0);
			this.beginFill(rectCol, a * 0.3);
			drawRoundRect(0, 0, w, h, r);
			drawRoundRect(2, 2, w - 4, h - 4, r);
			this.endFill();
			r.br = ((r.br > 1) ? (r.br + 1) : 0);
			r.bl = ((r.bl > 1) ? (r.bl + 1) : 0);
			r.tr = ((r.tr > 1) ? (r.tr + 1) : 0);
			r.tl = ((r.tl > 1) ? (r.tl + 1) : 0);
			this.beginFill(rectCol, a * 0.3);
			drawRoundRect(1, 1, w - 2, h - 2, r);
			r.br = ((r.br > 1) ? (r.br - 1) : 0);
			r.bl = ((r.bl > 1) ? (r.bl - 1) : 0);
			r.tr = ((r.tr > 1) ? (r.tr - 1) : 0);
			r.tl = ((r.tl > 1) ? (r.tl - 1) : 0);
			drawRoundRect(2, 2, w - 4, h - 4, r);
			this.endFill();
		} else {
			var _local5;
			if (r != 0) {
				_local5 = r - 2;
			} else {
				_local5 = 0;
			}
			this.beginFill(rectCol, a * 0.3);
			drawRoundRect(0, 0, w, h, r);
			drawRoundRect(2, 2, w - 4, h - 4, _local5);
			this.endFill();
			this.beginFill(rectCol, a * 0.3);
			if (r != 0) {
				_local5 = r - 2;
				r = r - 1;
			} else {
				_local5 = 0;
				r = 0;
			}
			drawRoundRect(1, 1, w - 2, h - 2, r);
			drawRoundRect(2, 2, w - 4, h - 4, _local5);
			this.endFill();
		}
	}
	function handleEvent(e) {
		if (e.type == "unload") {
			_visible = true;
		} else if (e.type == "resize") {
			e.target.adjustFocusRect();
		} else if (e.type == "move") {
			e.target.adjustFocusRect();
		}
	}
	static function classConstruct() {
		mx.core.UIComponent.prototype.drawFocus = function (focused) {
			var _local2 = this._parent.focus_mc;
			if (!focused) {
				_local2._visible = false;
				this.removeEventListener("unload", _local2);
				this.removeEventListener("move", _local2);
				this.removeEventListener("resize", _local2);
			} else {
				if (_local2 == undefined) {
					_local2 = this._parent.createChildAtDepth("FocusRect", mx.managers.DepthManager.kTop);
					_local2.tabEnabled = false;
					this._parent.focus_mc = _local2;
				} else {
					_local2._visible = true;
				}
				_local2.draw(this);
				if (_local2.getDepth() < this.getDepth()) {
					_local2.setDepthAbove(this);
				}
				this.addEventListener("unload", _local2);
				this.addEventListener("move", _local2);
				this.addEventListener("resize", _local2);
			}
		};
		mx.core.UIComponent.prototype.adjustFocusRect = function () {
			var _local2 = this.getStyle("themeColor");
			if (_local2 == undefined) {
				_local2 = 8453965;
			}
			var _local3 = this._parent.focus_mc;
			_local3.setSize(this.width + 4, this.height + 4, 0, 100, _local2);
			_local3.move(this.x - 2, this.y - 2);
		};
		TextField.prototype.drawFocus = mx.core.UIComponent.prototype.drawFocus;
		TextField.prototype.adjustFocusRect = mx.core.UIComponent.prototype.adjustFocusRect;
		mx.skins.halo.FocusRect.prototype.drawRoundRect = mx.skins.halo.Defaults.prototype.drawRoundRect;
		return(true);
	}
	static var classConstructed = classConstruct();
	static var DefaultsDependency = mx.skins.halo.Defaults;
	static var UIComponentDependency = mx.core.UIComponent;
}