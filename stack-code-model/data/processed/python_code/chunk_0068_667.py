package com.freshplanet.ane.AirAlert {
	import flash.events.EventDispatcher;
	import flash.events.IEventDispatcher;
	import flash.events.StatusEvent;
	import flash.external.ExtensionContext;
	import flash.geom.Rectangle;

	public class AirPicker extends EventDispatcher {


		private var _context:ExtensionContext = null;
		private var _frame:Rectangle = null;
		private var _items:Array = null;
		private var _doneLabel:String = null;
		private var _cancelLabel:String = null;
		private var _selectedCallback:Function;
		private var _cancelCallback:Function;

		public function AirPicker(context:ExtensionContext, frame:Rectangle, items:Array, doneLabel:String, cancelLabel:String, selectedCallback:Function, cancelCallback:Function) {
			super();
			_context = context;
			_frame = frame;
			_items = items;
			_doneLabel = doneLabel;
			_cancelLabel = cancelLabel;
			_selectedCallback = selectedCallback;
			_cancelCallback = cancelCallback;
			_context.addEventListener(StatusEvent.STATUS, handleStatusEvent);
		}

		public function dispose():void {

			this._context.removeEventListener(StatusEvent.STATUS, handleStatusEvent);
			_context.dispose();
			_context = null;
			_frame = null;
			_selectedCallback = null;
			_cancelCallback = null;
			_doneLabel = null;
			_cancelLabel = null;
			_items = null;
		}

		public function show():void {
			var ret:Object = _context.call("picker_show");
			if (ret is Error)
				throw ret;
		}

		public function hide():void {
			var ret:Object = _context.call("picker_hide");
			if (ret is Error)
				throw ret;
		}


		private function handleStatusEvent(event:StatusEvent):void {

			if (event.code == "PICKER_SELECTED") {
				if(_selectedCallback)
					_selectedCallback(event.level);
			}
			else if (event.code == "PICKER_CANCELED") {
				if(_cancelCallback)
					_cancelCallback();
			}
		}
		

		public function get frame():Rectangle {
			return _frame;
		}

		public function get items():Array {
			return _items;
		}

		public function get doneLabel():String {
			return _doneLabel;
		}

		public function get cancelLabel():String {
			return _cancelLabel;
		}

		public function get selectedCallback():Function {
			return _selectedCallback;
		}

		public function get cancelCallback():Function {
			return _cancelCallback;
		}
	}
}