package com.tourism_in_lviv.air.interfaces
{
	import mx.collections.ArrayCollection;

	/**
	 * 
	 * @author Ihor Khomiak
	 */
	public interface ICategoryDTO
	{
		function get categoryName():String;
		
		function set categoryName( value:String ):void;

		function get label():String;
		
		function set label( value:String ):void;

		function get items():ArrayCollection;
		
		function set items( value:ArrayCollection ):void;
	}
}