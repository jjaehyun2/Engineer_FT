import core.ArrayUtil;
import core.TPArrayUtil;

class core.CustomEvent {
	
	private var listeners : Array = [];
	
	function CustomEvent() {
		listeners = [];
	}
	
	function listen(_scope, _handler : Function) : Object {
		var handler : Function;
		
		if (arguments.length > 2) {
			var listenArgs : Array = arguments.slice(2);
			handler = function(_emitArgs : Array) {
				var allArguments : Array = listenArgs.concat(_emitArgs);
				_handler.apply(_scope, allArguments);
			}
		} else {
			handler = function(_emitArgs : Array) {
				_handler.apply(_scope, _emitArgs);
			}
		}
		
		var listener : Object = {handler: handler, scope: _scope, once: false}
		listeners.push(listener);
		return listener;
	}
	
	function listenOnce(_scope, _handler : Function) : Object {
		var listener : Object = {handler: _handler, scope: _scope, once: true}
		listeners.push(listener);
		return listener;
	}
	
	function stopListening(_listener : Object) : Boolean {
		var index : Number = TPArrayUtil.indexOf(listeners, _listener);
		if (index >= 0) {
			listeners.splice(index, 1);
			return true;
		}
		return false;
	}
	
	function emit() : Void {
		for (var i : Number = 0; i < listeners.length; i++) {
			this.listeners[i].handler(arguments);
			if (this.listeners[i].once == true) {
				this.listeners.splice(i, 1);
				i--;
			}
		}
	}
}