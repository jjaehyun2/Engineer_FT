package com.tourism_in_lviv.air.utils
{
	import flash.utils.getTimer;

	/**
	 * 
	 * @author Ihor Khomiak
	 */
	public class GeneralUtils
	{
		/**
		 * 
		 * @param ms
		 */
		public static function sleep( ms:int ):void 
		{
			var init:int = getTimer();
			while( true ) 
			{
				if(getTimer() - init >= ms) 
				{
					break;
				}
			}
		}
	}
}