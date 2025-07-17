package devoron.data.core.base
{
	import ascb.util.DateFormat;
	import org.aswing.util.HashMap;
	
	/**
	 * ...
	 * @author Devoron
	 */
	public class DataObjectUtil
	{
		
		public static const LOW_TO_HIGH:String = "lh";
		public static const HIGH_TO_LOW:String = "hl";
		
		public function DataObjectUtil()
		{
		
		}
		
		public static function changeKeyByProperty(datas:HashMap, property:String):void
		{
			var keys:Array = datas.keys();
			var l:uint = keys.length;
			for (var i:int = 0; i < l; i++)
			{
				var dso:DataStructurObject = datas.remove(keys[i]) as DataStructurObject;
				datas.put(dso[property], dso);
			}
		}
		
		//*****
		//*****
		//*****
		//***** БЕЗУМНО НУЖНА ФУНКЦИЯ СОРТИРОВКИ DSO по свойствам
		/**
		 * sortBy(datas, property, type, propertyAsKey, resultType, sortFunction:Function
		 * @param	datas
		 * @param	type
		 * @param	resultAsKeys
		 * @param	timestampAsKey
		 * @return
		 */
		//*****
		//*****
		//*****
		
		public static const KEYS:String = "keys";
		public static const DSOs:String = "dsos";
		
		
		public static function sortBy(datas:HashMap, property:String, type:String = "lh", resultType:String = "keys", sortFunction:Function = null, propertyAsKey:Boolean = false):Array {
			var properties:Array = [];
			var keys:Array = datas.keys();
			var keysL:uint = keys.length;
			var dso:DataStructurObject;
			var propAndKey:HashMap = new HashMap();
			var property:*;
			// занести все свойства из каждого dso c полем property в массив
			// заполнить HashMap {dso[property] : dso}
			for (var i:int = 0; i < keysL; i++) 
			{
				dso = datas.get(keys[i]);
				property = dso[property];
				properties.push(property);
				propAndKey.put(dso[property], dso);
			}
			
			// отсортировать массив properties
			if (sortFunction!=null) {
				// отсортировать все даты по убыванию
				properties.sort(sortFunction);
				if (type == DataObjectUtil.HIGH_TO_LOW)
				{
					properties.reverse();
				}
			}
			else {
				//properties.sort();	
			}
			
			// если нужно, то заменить прежние ключи для dso на значение property для каждого dso
			if (propertyAsKey)
				changeKeyByProperty(datas, dso[property]);
			
			// если результат - отсортированные properties, то вернуть их
			if (resultType == DataObjectUtil.KEYS) {
				return properties
			}
			// если результат - отсортированные по property DSO, то создать такой массив и вернуть
			else if (resultType == DataObjectUtil.DSOs) {
				var sortedDSOs:Array = new Array();
				for (var j:int = 0; j < keysL; j++) 
				{
					sortedDSOs.push(propAndKey.get(properties[i]));
				}
				return sortedDSOs;
			}
			
		return null;	
		}
		
		public static function orderDate(date1:String, date2:String):int
		{
			var formatter:DateFormat = new DateFormat("h:i:s m.d.Y");
			var dateD1:Date = formatter.parse(date1);
			var dateD2:Date = formatter.parse(date2);
			if (dateD1 < dateD2)
				return -1;
			else if (dateD1 > dateD2)
				return 1;
			else
				return 0;
		}
		
		public static function sortByName(datas:HashMap, resultAsKeys:Boolean = false):Array
		{
			return null;
		}
		
		public static function sortByType(datas:HashMap, resultAsKeys:Boolean = false):Array
		{
			return null;
		}
	
	}

}