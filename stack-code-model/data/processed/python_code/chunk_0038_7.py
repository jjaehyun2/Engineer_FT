package utils
{
	import mx.collections.ArrayCollection;

	public class CollectionUtils
	{	
		public static function getObjectByKey(source:ArrayCollection, key:String, value:*):Object
		{
			for each(var item:Object in source)
			{
				if(item.hasOwnProperty(key) && item[key] == value)
				{
					return item;
				}
			}
			return null;
		}
	}
}