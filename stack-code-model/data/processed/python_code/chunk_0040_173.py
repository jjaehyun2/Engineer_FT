class caurina.transitions.properties.ColorShortcuts
{
	function ColorShortcuts () {
		trace("This is an static class and should not be instantiated.");
	}
	static function init() {
		caurina.transitions.Tweener.registerSpecialProperty("_color_ra", _oldColor_property_get, _oldColor_property_set, ["ra"]);
		caurina.transitions.Tweener.registerSpecialProperty("_color_rb", _oldColor_property_get, _oldColor_property_set, ["rb"]);
		caurina.transitions.Tweener.registerSpecialProperty("_color_ga", _oldColor_property_get, _oldColor_property_set, ["ga"]);
		caurina.transitions.Tweener.registerSpecialProperty("_color_gb", _oldColor_property_get, _oldColor_property_set, ["gb"]);
		caurina.transitions.Tweener.registerSpecialProperty("_color_ba", _oldColor_property_get, _oldColor_property_set, ["ba"]);
		caurina.transitions.Tweener.registerSpecialProperty("_color_bb", _oldColor_property_get, _oldColor_property_set, ["bb"]);
		caurina.transitions.Tweener.registerSpecialProperty("_color_aa", _oldColor_property_get, _oldColor_property_set, ["aa"]);
		caurina.transitions.Tweener.registerSpecialProperty("_color_ab", _oldColor_property_get, _oldColor_property_set, ["ab"]);
		caurina.transitions.Tweener.registerSpecialProperty("_color_redMultiplier", _color_property_get, _color_property_set, ["redMultiplier"]);
		caurina.transitions.Tweener.registerSpecialProperty("_color_redOffset", _color_property_get, _color_property_set, ["redOffset"]);
		caurina.transitions.Tweener.registerSpecialProperty("_color_greenMultiplier", _color_property_get, _color_property_set, ["greenMultiplier"]);
		caurina.transitions.Tweener.registerSpecialProperty("_color_greenOffset", _color_property_get, _color_property_set, ["greenOffset"]);
		caurina.transitions.Tweener.registerSpecialProperty("_color_blueMultiplier", _color_property_get, _color_property_set, ["blueMultiplier"]);
		caurina.transitions.Tweener.registerSpecialProperty("_color_blueOffset", _color_property_get, _color_property_set, ["blueOffset"]);
		caurina.transitions.Tweener.registerSpecialProperty("_color_alphaMultiplier", _color_property_get, _color_property_set, ["alphaMultiplier"]);
		caurina.transitions.Tweener.registerSpecialProperty("_color_alphaOffset", _color_property_get, _color_property_set, ["alphaOffset"]);
		caurina.transitions.Tweener.registerSpecialPropertySplitter("_color", _color_splitter);
		caurina.transitions.Tweener.registerSpecialPropertySplitter("_colorTransform", _colorTransform_splitter);
		caurina.transitions.Tweener.registerSpecialProperty("_brightness", _brightness_get, _brightness_set, [false]);
		caurina.transitions.Tweener.registerSpecialProperty("_tintBrightness", _brightness_get, _brightness_set, [true]);
		caurina.transitions.Tweener.registerSpecialProperty("_contrast", _contrast_get, _contrast_set);
		caurina.transitions.Tweener.registerSpecialProperty("_hue", _hue_get, _hue_set);
		caurina.transitions.Tweener.registerSpecialProperty("_saturation", _saturation_get, _saturation_set, [false]);
		caurina.transitions.Tweener.registerSpecialProperty("_dumbSaturation", _saturation_get, _saturation_set, [true]);
	}
	static function _color_splitter(p_value, p_parameters) {
		var _local1 = new Array();
		if (p_value == null) {
			_local1.push({name:"_color_redMultiplier", value:1});
			_local1.push({name:"_color_redOffset", value:0});
			_local1.push({name:"_color_greenMultiplier", value:1});
			_local1.push({name:"_color_greenOffset", value:0});
			_local1.push({name:"_color_blueMultiplier", value:1});
			_local1.push({name:"_color_blueOffset", value:0});
		} else {
			_local1.push({name:"_color_redMultiplier", value:0});
			_local1.push({name:"_color_redOffset", value:caurina.transitions.AuxFunctions.numberToR(p_value)});
			_local1.push({name:"_color_greenMultiplier", value:0});
			_local1.push({name:"_color_greenOffset", value:caurina.transitions.AuxFunctions.numberToG(p_value)});
			_local1.push({name:"_color_blueMultiplier", value:0});
			_local1.push({name:"_color_blueOffset", value:caurina.transitions.AuxFunctions.numberToB(p_value)});
		}
		return(_local1);
	}
	static function _colorTransform_splitter(p_value, p_parameters) {
		var _local2 = new Array();
		if (p_value == null) {
			_local2.push({name:"_color_redMultiplier", value:1});
			_local2.push({name:"_color_redOffset", value:0});
			_local2.push({name:"_color_greenMultiplier", value:1});
			_local2.push({name:"_color_greenOffset", value:0});
			_local2.push({name:"_color_blueMultiplier", value:1});
			_local2.push({name:"_color_blueOffset", value:0});
		} else {
			if (p_value.ra != undefined) {
				_local2.push({name:"_color_ra", value:p_value.ra});
			}
			if (p_value.rb != undefined) {
				_local2.push({name:"_color_rb", value:p_value.rb});
			}
			if (p_value.ga != undefined) {
				_local2.push({name:"_color_ba", value:p_value.ba});
			}
			if (p_value.gb != undefined) {
				_local2.push({name:"_color_bb", value:p_value.bb});
			}
			if (p_value.ba != undefined) {
				_local2.push({name:"_color_ga", value:p_value.ga});
			}
			if (p_value.bb != undefined) {
				_local2.push({name:"_color_gb", value:p_value.gb});
			}
			if (p_value.aa != undefined) {
				_local2.push({name:"_color_aa", value:p_value.aa});
			}
			if (p_value.ab != undefined) {
				_local2.push({name:"_color_ab", value:p_value.ab});
			}
			if (p_value.redMultiplier != undefined) {
				_local2.push({name:"_color_redMultiplier", value:p_value.redMultiplier});
			}
			if (p_value.redOffset != undefined) {
				_local2.push({name:"_color_redOffset", value:p_value.redOffset});
			}
			if (p_value.blueMultiplier != undefined) {
				_local2.push({name:"_color_blueMultiplier", value:p_value.blueMultiplier});
			}
			if (p_value.blueOffset != undefined) {
				_local2.push({name:"_color_blueOffset", value:p_value.blueOffset});
			}
			if (p_value.greenMultiplier != undefined) {
				_local2.push({name:"_color_greenMultiplier", value:p_value.greenMultiplier});
			}
			if (p_value.greenOffset != undefined) {
				_local2.push({name:"_color_greenOffset", value:p_value.greenOffset});
			}
			if (p_value.alphaMultiplier != undefined) {
				_local2.push({name:"_color_alphaMultiplier", value:p_value.alphaMultiplier});
			}
			if (p_value.alphaOffset != undefined) {
				_local2.push({name:"_color_alphaOffset", value:p_value.alphaOffset});
			}
		}
		return(_local2);
	}
	static function _oldColor_property_get(p_obj, p_parameters) {
		return(new Color(p_obj).getTransform()[p_parameters[0]]);
	}
	static function _oldColor_property_set(p_obj, p_value, p_parameters) {
		var _local1 = new Object();
		_local1[p_parameters[0]] = p_value;
		new Color(p_obj).setTransform(_local1);
	}
	static function _color_property_get(p_obj, p_parameters) {
		return(p_obj.transform.colorTransform[p_parameters[0]]);
	}
	static function _color_property_set(p_obj, p_value, p_parameters) {
		var _local1 = p_obj.transform.colorTransform;
		_local1[p_parameters[0]] = p_value;
		p_obj.transform.colorTransform = _local1;
	}
	static function _brightness_get(p_obj, p_parameters) {
		var _local3 = p_parameters[0];
		var _local1 = new Color(p_obj).getTransform();
		var _local4 = 1 - (((_local1.ra + _local1.ga) + _local1.ba) / 300);
		var _local2 = ((_local1.rb + _local1.gb) + _local1.bb) / 3;
		if (_local3) {
			return(((_local2 > 0) ? (_local2 / 255) : (-_local4)));
		}
		return(_local2 / 100);
	}
	static function _brightness_set(p_obj, p_value, p_parameters) {
		var _local4 = p_parameters[0];
		var _local1;
		var _local2;
		if (_local4) {
			_local1 = 1 - Math.abs(p_value);
			_local2 = ((p_value > 0) ? (Math.round(p_value * 255)) : 0);
		} else {
			_local1 = 1;
			_local2 = Math.round(p_value * 100);
		}
		var _local5 = {ra:_local1 * 100, rb:_local2, ga:_local1 * 100, gb:_local2, ba:_local1 * 100, bb:_local2};
		new Color(p_obj).setTransform(_local5);
	}
	static function _saturation_get(p_obj, p_parameters) {
		var _local1 = getObjectMatrix(p_obj);
		var _local5 = p_parameters[0];
		var _local4 = (_local5 ? 0.3333333 : (LUMINANCE_R));
		var _local2 = (_local5 ? 0.3333333 : (LUMINANCE_G));
		var _local3 = (_local5 ? 0.3333333 : (LUMINANCE_B));
		var _local7 = ((((_local1[0] - _local4) / (1 - _local4)) + ((_local1[6] - _local2) / (1 - _local2))) + ((_local1[12] - _local3) / (1 - _local3))) / 3;
		var _local6 = 1 - (((((((_local1[1] / _local2) + (_local1[2] / _local3)) + (_local1[5] / _local4)) + (_local1[7] / _local3)) + (_local1[10] / _local4)) + (_local1[11] / _local2)) / 6);
		return((_local7 + _local6) / 2);
	}
	static function _saturation_set(p_obj, p_value, p_parameters) {
		var _local5 = p_parameters[0];
		var _local10 = (_local5 ? 0.3333333 : (LUMINANCE_R));
		var _local7 = (_local5 ? 0.3333333 : (LUMINANCE_G));
		var _local9 = (_local5 ? 0.3333333 : (LUMINANCE_B));
		var _local1 = p_value;
		var _local3 = 1 - _local1;
		var _local6 = _local10 * _local3;
		var _local4 = _local7 * _local3;
		var _local2 = _local9 * _local3;
		var _local8 = [_local6 + _local1, _local4, _local2, 0, 0, _local6, _local4 + _local1, _local2, 0, 0, _local6, _local4, _local2 + _local1, 0, 0, 0, 0, 0, 1, 0];
		setObjectMatrix(p_obj, _local8);
	}
	static function _contrast_get(p_obj, p_parameters) {
		var _local1 = new Color(p_obj).getTransform();
		var _local2;
		var _local3;
		_local2 = (((_local1.ra + _local1.ga) + _local1.ba) / 300) - 1;
		_local3 = (((_local1.rb + _local1.gb) + _local1.bb) / 3) / -128;
		return((_local2 + _local3) / 2);
	}
	static function _contrast_set(p_obj, p_value, p_parameters) {
		var _local1;
		var _local2;
		_local1 = p_value + 1;
		_local2 = Math.round(p_value * -128);
		var _local3 = {ra:_local1 * 100, rb:_local2, ga:_local1 * 100, gb:_local2, ba:_local1 * 100, bb:_local2};
		new Color(p_obj).setTransform(_local3);
	}
	static function _hue_get(p_obj, p_parameters) {
		var _local4 = getObjectMatrix(p_obj);
		var _local1 = [];
		_local1[0] = {angle:-179.9, matrix:getHueMatrix(-179.9)};
		_local1[1] = {angle:180, matrix:getHueMatrix(180)};
		var _local3 = 0;
		while (_local3 < _local1.length) {
			_local1[_local3].distance = getHueDistance(_local4, _local1[_local3].matrix);
			_local3++;
		}
		var _local5 = 15;
		var _local2;
		_local3 = 0;
		while (_local3 < _local5) {
			if (_local1[0].distance < _local1[1].distance) {
				_local2 = 1;
			} else {
				_local2 = 0;
			}
			_local1[_local2].angle = (_local1[0].angle + _local1[1].angle) / 2;
			_local1[_local2].matrix = getHueMatrix(_local1[_local2].angle);
			_local1[_local2].distance = getHueDistance(_local4, _local1[_local2].matrix);
			_local3++;
		}
		return(_local1[_local2].angle);
	}
	static function _hue_set(p_obj, p_value, p_parameters) {
		setObjectMatrix(p_obj, getHueMatrix(p_value));
	}
	static function getHueDistance(mtx1, mtx2) {
		return((Math.abs(mtx1[0] - mtx2[0]) + Math.abs(mtx1[1] - mtx2[1])) + Math.abs(mtx1[2] - mtx2[2]));
	}
	static function getHueMatrix(hue) {
		var _local6 = (hue * 3.141593) / 180;
		var _local5 = LUMINANCE_R;
		var _local3 = LUMINANCE_G;
		var _local4 = LUMINANCE_B;
		var _local2 = Math.cos(_local6);
		var _local1 = Math.sin(_local6);
		var _local7 = [(_local5 + (_local2 * (1 - _local5))) + (_local1 * (-_local5)), (_local3 + (_local2 * (-_local3))) + (_local1 * (-_local3)), (_local4 + (_local2 * (-_local4))) + (_local1 * (1 - _local4)), 0, 0, (_local5 + (_local2 * (-_local5))) + (_local1 * 0.143), (_local3 + (_local2 * (1 - _local3))) + (_local1 * 0.14), (_local4 + (_local2 * (-_local4))) + (_local1 * -0.283), 0, 0, (_local5 + (_local2 * (-_local5))) + (_local1 * (-(1 - _local5))), (_local3 + (_local2 * (-_local3))) + (_local1 * _local3), (_local4 + (_local2 * (1 - _local4))) + (_local1 * _local4), 0, 0, 0, 0, 0, 1, 0];
		return(_local7);
	}
	static function getObjectMatrix(p_obj) {
		var _local1 = 0;
		while (_local1 < p_obj.filters.length) {
			if (p_obj.filters[_local1] instanceof flash.filters.ColorMatrixFilter) {
				return(p_obj.filters[_local1].matrix.concat());
			}
			_local1++;
		}
		return([1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0]);
	}
	static function setObjectMatrix(p_obj, p_matrix) {
		var _local2 = p_obj.filters.concat();
		var _local3 = false;
		var _local1 = 0;
		while (_local1 < _local2.length) {
			if (_local2[_local1] instanceof flash.filters.ColorMatrixFilter) {
				_local2[_local1].matrix = p_matrix.concat();
				_local3 = true;
			}
			_local1++;
		}
		if (!_local3) {
			var _local5 = new flash.filters.ColorMatrixFilter(p_matrix);
			_local2[_local2.length] = _local5;
		}
		p_obj.filters = _local2;
	}
	static var LUMINANCE_R = 0.212671;
	static var LUMINANCE_G = 0.71516;
	static var LUMINANCE_B = 0.072169;
}