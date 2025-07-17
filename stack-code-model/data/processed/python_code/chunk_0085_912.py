package com.marioretana.checkersgame {
	import flash.external.ExternalInterface;
	
	/**
	 * @author Mario Retana
	 * This class has some utility functions that are handy during the development of the project.
	 */
	public class Utils {
		
		/**
		 * Logs a message in the browser's web console.
		 * @param info The message that must be logged in the web console.
		 */
		public static function logInfo(info:String):void
		{
			ExternalInterface.call('console.log', info);
		}
		
	}
}