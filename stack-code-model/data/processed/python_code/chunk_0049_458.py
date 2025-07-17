package utils
{
	import mx.collections.ArrayCollection;

	public class KeepOnly
	{
		/**
		 * Reserved unique value
		 * Not processing the meta array, return an array only contains unique values
		 * @param source
		 * @return 
		 * 
		 */                
		public static function keepOnly(source:Array):Array
		{
			var array:Array=source.slice(0,source.length)
			for(var i:int=0;i<array.length-1;i++)
			{
				for(var j:int=i+1;j<array.length;j++)
				{
					if(array[i]==array[j])
					{
						array.splice(j,1);
						i--;
						j--;
					}        
				}
			}
			return array;
		}
	}
}