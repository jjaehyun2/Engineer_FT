package devoron.data.core.serializer.serializers
{
	
	/**
	 * ...
	 * @author Devoron
	 */
	public class DataStructurSerializer
	{
		
		public function DataStructurSerializer()
		{
		
		}
		
		public function serializePart():String
		{
			//gtrace("ЧАСТИЧНАЯ СЕРИАЛИЗАЦИЯ");
			
			// В СЛУЧАЕ ЧАСТИЧНОЙ СЕРЕАЛИЗАЦИИ МЫ СОБИРАЕМ ВСЕ ДАННЫЕ ИЗ
			// ТОГО КОНТЕЙНЕРА, КОТОРЫЙ БЫЛ ИНЦИАТОРОМ СЕРИАЛИЗАЦИИ
			// ЗНАЧИТ, ЭТО ГДЕ-ТО ДОЛЖНО БЫТЬ ОТМЕЧЕНО, А ПОТОМ СТЁРТО
			// СОБРАННЫЕ ДАННЫЕ В ВИДЕ СТРОКИ МЫ ЗАМЕНЯЕМ В СТРУКТУРЕ ДАННЫХ
			// И СООБЩАЕМ, ЧТО СТРУКТУРА ДАННЫХ ГОТОВА К ПАРСИНГУ
			
			if (!_serializable || _serializeObservers.length == 0)
				return "";
			
			// сериализованные данные
			var serializedData:String = "";
			// имя контейнера данных
			var dataContainerName:String;
			// данные в контейнере данных
			var dso:DataStructurObject;
			
			serializedData += "{"
			//serializedData += qutes(dataType) + ":" + "{";
			
			// выделить группы - объекты с одинаковым dataType
			var groupsDataType:HashMap = new HashMap();
			var group:Array;
			
			for each (dataContainerName in dataContainers.keys())
			{
				dso = DataStructurObject(dataContainers.get(dataContainerName));
				group = groupsDataType.get(dso.dataType);
				
				if (!group)
					groupsDataType.put(dso.dataType, [dso]);
				else
					group.push(dso);
			}
			
			var type:String;
			
			for each (type in groupsDataType.keys())
			{
				group = groupsDataType.get(type);
				
				// если количество контейнеров одного типа в группе больше чем один
				// то нужно открыть массив, иначе - это один отдельный контейнер
				if (group.length > 1)
					serializedData += qutes(type) + ":" + "[";
				else
					serializedData += qutes(type) + ":" + "{";
				
				for (var i:int = 0; i < group.length; i++)
				{
					dso = group[i];
					
					if (group.length > 1)
						serializedData += "{";
					
					serializedData += qutes("id") + ":" + qutes(dso.dataName) + ",";
					serializedData += qutes("data") + ":" + "{";
					
					var dataIsEmpty:Boolean = true;
					
					// запись свойства
					for (var item:String in dso)
					{
						dataIsEmpty = false;
						
						if (dso[item] is String)
							serializedData += qutes(item) + " : " + qutes(dso[item]) + ",";
						
						else if (dso[item] is Array)
						{
							serializedData = serializeArray(item, serializedData, dso[item]);
							/*var arr:Array = dso[item];
							   serializedData += qutes(item) + " : " + "[";
							   for each (var value:*in arr)
							   {
							
							   if (value is String || value is Number || value is int || value is uint || value is Boolean)
							   {
							   serializedData += String(value) + ",";
							   }
							
							   else if (value is Object)
							   {
							   serializedData = serializeObject(serializedData, value);
							   }
							
							   }
							   // удаление последней запятой
							   if (arr.length > 0)
							   serializedData = serializedData.substring(0, serializedData.length - 1);
							 serializedData += "]" + ","*/
						}
						
						else
							serializedData += qutes(item) + " : " + dso[item] + ",";
					}
					
					// удаление последней запятой
					if (!dataIsEmpty)
						serializedData = serializedData.substring(0, serializedData.length - 1);
					
					serializedData += "}";
					
					if (group.length > 1)
					{
						serializedData += "}";
						if (i != (group.length - 1))
							serializedData += ","
					}
					
				}
				
				// если количество контейнеров в группе больше чем один
				// то нужно закрыть массив, иначе - это один отдельный контейнер
				if (group.length > 1)
				{
					serializedData += "]";
					serializedData += ",";
				}
				else
				{
					serializedData += "}";
					serializedData += ",";
				}
				
			}
			
			// удаление последней запятой
			serializedData = serializedData.substring(0, serializedData.length - 1);
			//serializedData += "}";
			
			serializedData += "}";
			
			dataCode = serializedData;
			
			for each (var so:ISerializeObserver in _serializeObservers)
				so.setSerializedData(this, serializedData);
			
			return serializedData;
		}
	
	}

}