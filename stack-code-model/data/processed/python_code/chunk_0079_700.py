package com.syamgot.as3.util.logging
{
	
	/**
	 * Loggerのハンドラの抽象クラスです.
	 * 
	 * @author syamgot
	 */
	public class Handler
	{
		
		/**
		 * 新しい Handler インスタンスを生成します.
		 * 
		 */
		public function Handler()
		{
			formatter = new SimpleFormatter();
		}
		
		private var _formatter:Formatter;
		
		public function get formatter():Formatter
		{
			return _formatter;
		}

		public function set formatter(value:Formatter):void
		{
			_formatter = value;
		}
		
		public function publish(record:LogRecord):void 
		{
			throw new Error('');
		}
		
		public function close():void 
		{
			throw new Error('');
		}

	}
}