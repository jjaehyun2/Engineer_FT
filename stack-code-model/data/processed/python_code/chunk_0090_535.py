////////////////////////////////////////////////////////////////////////////////
//
//  CODE11.COM
//  Copyright 2011
//  licenced under GPU
//
//  @author		Romeo Copaciu romeo.copaciu@code11.com
//  @date		24 May 2011
//  @version	1.0
//  @site		code11.com
//
////////////////////////////////////////////////////////////////////////////////

package com.code11.util {
	import flash.utils.getQualifiedClassName;
	
	import mx.logging.ILogger;
	import mx.logging.Log;
	
	final public class LogUtil {
		
		public static function getLogger(c:*):ILogger {
			var className:String = getQualifiedClassName(c).replace("::", ".");
			return Log.getLogger(className);
		}
	}
}