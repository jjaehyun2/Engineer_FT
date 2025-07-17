class gs.dataTransfer.XMLParser
{
	static var _parsers_array;
	var parse, _results_obj, _url_str, _onComplete_func, _xml;
	function XMLParser () {
		parse = initLoad;
		if (_parsers_array == undefined) {
			_parsers_array = [];
		}
		_parsers_array.push(this);
	}
	static function load(url_str, onComplete_func, results_obj) {
		var _local1 = new gs.dataTransfer.XMLParser();
		_local1.initLoad(url_str, onComplete_func, results_obj);
		return(_local1);
	}
	static function sendAndLoad(toSend_obj, url_str, onComplete_func, results_obj) {
		var _local1 = new gs.dataTransfer.XMLParser();
		_local1.initSendAndLoad(toSend_obj, url_str, onComplete_func, results_obj);
		return(_local1);
	}
	function initLoad(url_str, onComplete_func, results_obj) {
		if (results_obj == undefined) {
			results_obj = {};
		}
		_results_obj = results_obj;
		_url_str = url_str;
		_onComplete_func = onComplete_func;
		_xml = new XML();
		_xml.ignoreWhite = true;
		_xml.onLoad = mx.utils.Delegate.create(this, parseLoadedXML);
		_xml.load(_url_str);
	}
	function initSendAndLoad(toSend_obj, url_str, onComplete_func, results_obj) {
		if (results_obj == undefined) {
			results_obj = {};
		}
		_results_obj = results_obj;
		_url_str = url_str;
		_onComplete_func = onComplete_func;
		if (toSend_obj instanceof XML) {
			var _local2 = toSend_obj;
		} else {
			var _local2 = objectToXML(toSend_obj);
		}
		_xml = new XML();
		_xml.ignoreWhite = true;
		_xml.onLoad = mx.utils.Delegate.create(this, parseLoadedXML);
		_local2.sendAndLoad(_url_str, _xml);
	}
	function searchAndReplace(holder, searchfor, replacement) {
		var _local1 = holder.split(searchfor);
		holder = _local1.join(replacement);
		return(holder);
	}
	function parseLoadedXML(success_boolean) {
		if (success_boolean == false) {
			trace(("XML FAILED TO LOAD! (" + _url_str) + ")");
			_onComplete_func(false);
			return(undefined);
		}
		var _local8 = _xml;
		var _local2 = _local8.firstChild.firstChild;
		var _local7 = _local8.firstChild.lastChild;
		_local8.firstChild.obj = _results_obj;
		while (_local2 != undefined) {
			if ((_local2.nodeName == null) && (_local2.nodeType == 3)) {
				_local2.parentNode.obj.value = searchAndReplace(_local2.nodeValue, "\r\n", "");
			} else {
				var _local4 = {};
				for (var _local6 in _local2.attributes) {
					_local4[_local6] = _local2.attributes[_local6];
				}
				var _local5 = _local2.parentNode.obj;
				if (_local5[_local2.nodeName] == undefined) {
					_local5[_local2.nodeName] = [];
				}
				_local2.obj = _local4;
				_local5[_local2.nodeName].push(_local4);
			}
			if (_local2.childNodes.length > 0) {
				_local2 = _local2.childNodes[0];
			} else {
				var _local3 = _local2;
				while ((_local3.nextSibling == undefined) && (_local3.parentNode != undefined)) {
					_local3 = _local3.parentNode;
				}
				_local2 = _local3.nextSibling;
				if (_local3 == _local7) {
					_local2 = undefined;
				}
			}
		}
		_onComplete_func(true, _results_obj, _local8);
	}
	static function objectToXML(o, rootNodeName_str) {
		if (rootNodeName_str == undefined) {
			rootNodeName_str = "XML";
		}
		var _local7 = new XML();
		var _local4 = _local7.createElement(rootNodeName_str);
		var _local5 = [];
		var _local1;
		for (var _local3 in o) {
			_local5.push(_local3);
		}
		var _local3 = _local5.length - 1;
		while (_local3 >= 0) {
			_local1 = _local5[_local3];
			if ((typeof(o[_local1]) == "object") && (o[_local1].length > 0)) {
				arrayToNodes(o[_local1], _local4, _local7, _local1);
			} else if (_local1 == "value") {
				var _local6 = _local7.createTextNode(o.value);
				_local4.appendChild(_local6);
			} else {
				_local4.attributes[_local1] = o[_local1];
			}
			_local3--;
		}
		_local7.appendChild(_local4);
		return(_local7);
	}
	static function arrayToNodes(ar, parentNode, xml, nodeName_str) {
		var _local9 = [];
		var _local5;
		var _local1;
		var _local4;
		var _local2;
		var _local8 = ar.length - 1;
		while (_local8 >= 0) {
			_local4 = xml.createElement(nodeName_str);
			_local2 = ar[_local8];
			_local5 = [];
			for (var _local3 in _local2) {
				_local5.push(_local3);
			}
			var _local3 = _local5.length - 1;
			while (_local3 >= 0) {
				_local1 = _local5[_local3];
				if ((typeof(_local2[_local1]) == "object") && (_local2[_local1].length > 0)) {
					arrayToNodes(_local2[_local1], _local4, xml, _local1);
				} else if (_local1 != "value") {
					_local4.attributes[_local1] = _local2[_local1];
				} else {
					var _local6 = xml.createTextNode(_local2.value);
					_local4.appendChild(_local6);
				}
				_local3--;
			}
			_local9.push(_local4);
			_local8--;
		}
		_local8 = _local9.length - 1;
		while (_local8 >= 0) {
			parentNode.appendChild(_local9[_local8]);
			_local8--;
		}
	}
	function destroy() {
		delete _xml;
		var _local2 = 0;
		while (_local2 < _parsers_array.length) {
			if (this == _parsers_array[_local2]) {
				_parsers_array.splice(_local2, 1);
			}
			_local2++;
		}
		destroyInstance(this);
	}
	static function destroyInstance(i) {
	}
	static function get active_boolean() {
		if (_parsers_array.length > 0) {
			return(true);
		}
		return(false);
	}
	static var CLASS_REF = gs.dataTransfer.XMLParser;
}