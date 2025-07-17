package com.tourism_in_lviv.air.interfaces
{
	import com.tourism_in_lviv.air.model.dto.ImagePathDTO;

	/**
	 * 
	 * @author Ihor Khomiak
	 */
	public interface IPlaceDTO
	{
		function get name():String;
		
		function set name( value:String ):void;

		function get shortDescription():String;
		
		function set shortDescription( value:String ):void;

		function get longDescription():String;
		
		function set longDescription( value:String ):void;
		
		function get address():String;
		
		function set address( value:String ):void;
		
		function get pathToImage():ImagePathDTO;
		
		function set pathToImage( value:ImagePathDTO ):void;
	}
}