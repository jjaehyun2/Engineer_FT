package com.tourism_in_lviv.air.utils
{
	import mx.collections.ArrayCollection;
	import mx.collections.Sort;
	import mx.collections.SortField;

	/**
	 * 
	 * @author Ihor Khomiak
	 */
	public class CollectionUtils
	{
		/**
		 * 
		 * @param collection
		 * @param byStringTag
		 * @return 
		 */
		public static function filterArrayCollectionByStringTag( collection:ArrayCollection, byStringTag:String ):ArrayCollection
		{
			var newCollection:ArrayCollection = new ArrayCollection();
			for each (var dto:* in collection) 
			{
				if( dto.categoryTags.indexOf( byStringTag ) >= 0 )
					newCollection.addItem( dto );
			}
			
			return newCollection;
		}
		
		/**
		 * 
		 * @param arrayCollection
		 * @param sortBy
		 * @param descending
		 * @param numeric
		 * @return 
		 */
		public static function sortByProperty( arrayCollection:ArrayCollection, sortBy:String, descending:Boolean = false, numeric:Object = null ):ArrayCollection
		{
			if ( !arrayCollection )
				return arrayCollection;

			var dataSortField:SortField = new SortField();
			dataSortField.name = sortBy;
			dataSortField.numeric = numeric;
			dataSortField.descending = descending;

			var dataSort:Sort = new Sort();
			dataSort.fields = [ dataSortField ];


			arrayCollection.sort = dataSort;
			arrayCollection.refresh();

			return arrayCollection;
		}
		
		/**
		 * 
		 * @param a
		 * @param b
		 * @return 
		 */
		public static function mixArray ( a : *, b : * ) : int 
		{
			return ( Math.random() > .5 ) ? 1 : -1;
		}
	}
}