package com.tourism_in_lviv.air.model.dto
{
	import com.tourism_in_lviv.air.interfaces.IFactDTO;

	/**
	 * 
	 * @author Ihor Khomiak
	 */
	public class FactDTO implements IFactDTO
	{
		private var _name:String='';
		private var _description:String='';
		private var _categoryTags:String='';
		private var _pathToImage:ImagePathDTO;

		/**
		 * 
		 * @return 
		 */
		public function get categoryTags():String
		{
			return _categoryTags;
		}

		/**
		 * 
		 * @param value
		 */
		public function set categoryTags(value:String):void
		{
			_categoryTags = value;
		}

		/**
		 * 
		 * @return 
		 */
		public function get pathToImage():ImagePathDTO
		{
			return _pathToImage;
		}

		/**
		 * 
		 * @param value
		 */
		public function set pathToImage(value:ImagePathDTO):void
		{
			_pathToImage = value;
		}

		/**
		 * 
		 * @return 
		 */
		public function get description():String
		{
			return _description;
		}

		/**
		 * 
		 * @param value
		 */
		public function set description(value:String):void
		{
			_description = value;
		}

		/**
		 * 
		 * @return 
		 */
		public function get name():String
		{
			return _name;
		}

		/**
		 * 
		 * @param value
		 */
		public function set name(value:String):void
		{
			_name = value;
		}

	}
}