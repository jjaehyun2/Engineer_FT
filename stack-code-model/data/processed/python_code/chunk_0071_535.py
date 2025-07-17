package com.syamgot.as3.util.logging
{
	import flash.errors.IllegalOperationError;

	public class Logger
	{

		private static var _isInternallyCalled:Boolean;

		private var _loggerName:String;	

		public function get loggerName():String
		{
			return _loggerName;
		}

		public function set loggerName(value:String):void
		{
			_loggerName = value;
		}
		
		public function Logger(name:String)
		{
			if (_isInternallyCalled)
			{
				_loggerName = name;
				_isInternallyCalled = false;
				_handlers = new Vector.<Handler>;
				_handlers.push(new TraceHandler());
				_level = Level.INFO;
			}
			else
			{
				throw new IllegalOperationError('#2012: Logger class cannot be instantiated.');
			}
		}

		public static function getLogger(name:String):Logger
		{
			_isInternallyCalled = true;
			return new Logger(name);
		}
		
		private var _handlers:Vector.<Handler>;
		
		public function addHandler(handler:Handler):void 
		{
			_handlers.push(handler);
		}
		
		public function removeHandler(handler:Handler):void
		{
			var i:uint, n:uint = _handlers.length;
			for (i = 0; i < n; i++) 
			{
				if (_handlers[i] == handler) 
				{
					_handlers.splice(i, 1);
					break;
				}
			}
		}
		
		private var _level:int;

		public function get level():int
		{
			return _level;
		}

		public function set level(value:int):void
		{
			_level = value;
		}
		
		public function log(level:int, msg:String):void 
		{
			if (level < _level) 
			{
				return;
			}
			
			var record:LogRecord = new LogRecord(level, msg);
			record.loggerName = _loggerName;
			
			var i:uint, n:uint = _handlers.length;
			for (i = 0; i < n; i++) 
			{
				_handlers[i].publish(record);
			}
		}
		
		public function severe(msg:String):void 
		{
			log(Level.SEVERE, msg);
		}
		
		public function warning(msg:String):void 
		{
			log(Level.WARNING, msg);
		}
		
		public function info(msg:String):void 
		{
			log(Level.INFO, msg);
		}
		
		public function config(msg:String):void 
		{
			log(Level.CONFIG, msg);
		}
		
		public function fine(msg:String):void 
		{
			log(Level.FINE, msg);
		}
		
		public function finer(msg:String):void 
		{
			log(Level.FINER, msg);
		}
		
		public function finest(msg:String):void 
		{
			log(Level.FINEST, msg);
		}
		
	}
}