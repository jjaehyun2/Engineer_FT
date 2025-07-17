package com.syamgot.as3.util.logging
{
	import com.syamgot.as3.util.DateUtil;
	
	public class SimpleFormatter extends Formatter
	{
		public function SimpleFormatter()
		{
			super();
		}
		
		override public function format(record:LogRecord):String
		{
			
			var buf:String = '';
			
			buf += DateUtil.format(new Date(record.time));
			buf += ' ';
			
			switch (record.level){
				case Level.FINEST :
					buf += 'FINEST ';
					break;
				case Level.FINER :
					buf += 'FINER ';
					break;
				case Level.FINE :
					buf += 'FINE ';
					break;
				case Level.CONFIG :
					buf += 'CONFIG ';
					break;
				case Level.INFO :
					buf += 'INFO ';
					break;
				case Level.WARNING :
					buf += 'WARNING ';
					break;
				case Level.SEVERE :
					buf += 'SEVERE ';
					break;
				default :
					buf += record.level.toString();
					break;
			}
			
			buf += record.loggerName;
			buf += ' - ';
			buf += record.message;
			buf += "\n";
			
			return buf;
		}
	}
}