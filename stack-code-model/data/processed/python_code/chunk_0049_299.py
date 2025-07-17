package com.tourism_in_lviv.air.model
{	
	import com.tourism_in_lviv.air.model.dto.CategoryDTO;
	
	import org.robotlegs.mvcs.Actor;

	/**
	 * 
	 * @author Ihor Khomiak
	 */
	public class ModelLocator extends Actor
	{

		private static var _instance:ModelLocator;
		
		private var _selectedPlaceCategory:CategoryDTO;

		private var _selectedFactCategory:CategoryDTO;

		/**
		 * 
		 * @return 
		 */
		public function get selectedFactCategory():CategoryDTO
		{
			return _selectedFactCategory;
		}

		/**
		 * 
		 * @param value
		 */
		public function set selectedFactCategory(value:CategoryDTO):void
		{
			_selectedFactCategory = value;
		}

		/**
		 * 
		 * @return 
		 */
		public function get selectedPlaceCategory():CategoryDTO
		{
			return _selectedPlaceCategory;
		}

		/**
		 * 
		 * @param value
		 */
		public function set selectedPlaceCategory(value:CategoryDTO):void
		{
			_selectedPlaceCategory = value;
		}

		/**
		 * 
		 * @return 
		 */
		public static function getInstance():ModelLocator
		{
			if ( _instance == null )
			{
				_instance = new ModelLocator();
			}
			return _instance;
		}

		/**
		 * 
		 */
		public function ModelLocator()
		{
			super();
		}
	}
}