package devoron.data.core.serializer 
{
	import devoron.data.core.serializer.serializers.ASColorSerializer;
	import devoron.data.core.serializer.serializers.IntDimensionSerializer;
	import devoron.data.core.serializer.serializers.SimpleTypesSerializer;
	import devoron.data.core.serializer.serializers.TreeModelSerializer;
	import devoron.data.core.serializer.serializers.TreeNodeSerializer;
	import devoron.data.core.serializer.serializers.VectorListModelSerializer;
	import org.aswing.ASColor;
	import org.aswing.ASFont;
	import org.aswing.geom.IntDimension;
	import org.aswing.tree.DefaultMutableTreeNode;
	import org.aswing.tree.DefaultTreeModel;
	import org.aswing.tree.TreeModel;
	import org.aswing.tree.TreeNode;
	import org.aswing.VectorListModel;
	/**
	 * SerializerShema
	 * @author Devoron
	 */
	public class SerializerShema implements ISerializerShema
	{
		
		public function SerializerShema() 
		{
			
			// согласно схеме сериализаторов должна быть сформирована схема парсеров
			//registerSerializer(DefaultMutableTreeNode, new TreeNodeSerializer);
			registerSerializer(/*DefaultMutableTreeNode,*/ new SimpleTypesSerializer);
			registerSerializer(/*DefaultMutableTreeNode,*/ new TreeNodeSerializer);
			registerSerializer(/*IntDimension, */new TreeNodeSerializer);
			registerSerializer(/*DefaultTreeModel,*/ new TreeModelSerializer);
			registerSerializer(/*DefaultMutableTreeNode, */new TreeNodeSerializer);
			registerSerializer(/*VectorListModel,*/ new VectorListModelSerializer);
			registerSerializer(/*IntDimension,*/ new IntDimensionSerializer);
			registerSerializer(/*ASColor,*/ new ASColorSerializer);
		}
		
		public static function serializeObject(serializedData:String):String {
							else if (value is DefaultMutableTreeNode)
				{
					serializedData += serializeNode(serializedData, value as DefaultMutableTreeNode);
						//gtrace(serializedData);
						//serializedData = serializedData.substring(0, serializedData.length - 2) + "}" + ",";
				}
				
				/*if (value is ASColor)
				{
					serializedData += qutes(item) + " : " + qutes(String((value as ASColor).getARGB())) + ",";
				}*/
				
				else if (value is ASFont)
				{
					//serializedData += serializeNode(serializedData, value as DefaultMutableTreeNode);
					//gtrace("Надо быть сериализовать шрифт");
					//gtrace(serializedData);
					//serializedData = serializedData.substring(0, serializedData.length - 2) + "}" + ",";
				}
				
				else if (value is Object)
				{
					serializedData = serializeObject(serializedData, value) + ",";
					
					// удаление запятой после последнего элемента сериализованного массива
					
					//if (i == arr.length - 1){
					var lastId:int = serializedData.length - 2;
					while (serializedData.charAt(lastId) == "}")
					{
						lastId--;
					}
					
					//serializedData = serializedData.substring(0, lastId) + serializedData.substring(lastId + 1, serializedData.length);
						//}
					
				}
			return serializedData;
		}
		
				public static function serializeObject(serializedData:String, value:Object):String
		{
			
			// если у объекта есть собственная реализация приведения к строковому значению,
			// то вызывать функцию toString
			/*if ((!(value is DataObject)) && (value as Object).hasOwnProperty("toString"))
			   {
			   serializedData += value.toString();
			   }
			   else
			 {*/
			serializedData += "{";
			for (var prop:String in value)
			{
				// есть свойство prop и для него необходимо определить все подходящие сериализаторы
				// по цепочке наследований
				
				if (value[prop] is String)
					serializedData += qutes(prop) + ":" + qutes(value[prop]);
				else if ((value[prop] is Number) || (value[prop] is int) || (value[prop] is uint) || (value[prop] is Boolean) || (value[prop] is TextValue) || (value[prop] is ThreeDValue) || (value[prop] is OneDValue) || (value[prop] is FourDCompositeWithOneDValue) || (value[prop] is FourDCompositeWithThreeDValue))
				{
					serializedData += qutes(prop) + ":" + String(value[prop]);
				}
				else if (value[prop] is DefaultTreeModel)
				{
					serializedData = serializeTreeModel(prop, serializedData, value[prop]);
						//gtrace(serializedData);
						//serializedData = serializedData.substring(0, serializedData.length - 2) + "}" + ",";
				}
				else if (value[prop] is Array)
				{
					serializedData = serializeArray(prop, serializedData, value[prop]);
					serializedData = serializedData.substring(0, serializedData.length - 2) + "}";
				}
				else if (value[prop] is VectorListModel)
				{
					serializedData = serializeVectorListModel(prop, serializedData, value[prop]);
					serializedData = serializedData.substring(0, serializedData.length - 2) + "}";
				}
				else if (value[prop] is ASColor)
				{
					//serializedData += qutes(prop) + ":";
					//serializedData = serializeObject(serializedData, value[prop]);
					
					//serializedData += qutes(prop) + " : " + qutes(String((value[prop] as ASColor).getARGB()));
					serializedData += qutes(prop) + " : " + qutes(String((value[prop] as ASColor).getARGB()));
				}
				else if (value[prop] is ASFontValue)
				{
					//serializedData += qutes(prop) + ":" + qutes(String("DSJK")) + ",";
					
					//serializedData += qutes(value[prop]) + ":";
					//serializedData = serializeObject(serializedData, value[prop]);
					
					//serializedData = serializeObject(serializedData, value[prop]);
					
					//serializedData += qutes(prop) + ":";
					//serializedData += qutes(prop) + " : " + qutes(String((value[prop] as ASFont).toString())) + ",";
					//serializedData += qutes(prop) + " : " + qutes(String((value[prop] as ASFont).toString())) + ",";
				}
				
				else if (value[prop] is Object)
				{
					serializedData += qutes(prop) + ":";
					serializedData = serializeObject(serializedData, value[prop]);
				}
				
				
				/*else
				 serializedData += qutes(prop) + ":" + value[prop] + ",";*/
					 //}
					 // удаление последней запятой
				
					 serializedData += ",";
					 
			}
			
			if (serializedData.charAt(serializedData.length - 1) == ",")
			 serializedData = serializedData.substr(0, serializedData.length - 1);
			
			//if ((value[prop] is Array))
			//serializedData = serializedData.substring(0, serializedData.length - 2) /*+ "}"*/;
			//else
			//serializedData = serializedData.substring(0, serializedData.length - 1);
			//serializedData += "}";
			serializedData += "}" /*+ ","*/;
			
			return serializedData;
		}
		
		public static function qutes(str:String):String
		{
			return '"' + str + '"';
		}
		
		static public function serializeValue(serializedData:String, value:*):String 
		{
			if (value is String || value is Number || value is int || value is uint || value is Boolean)
				{
					serializedData += String(value) + ",";
				}
			return serializedData;
				
		}
		
		
		public function serialize(any:*):void {
			//getSupportedSerializer();
			/*if (any is String || any is Number || any is int || any is uint || any is Boolean)
				{
					serializedData += String(value) + ",";
				}*/
				
				var serializedData:String;
				/*var simpleTypesSerializer:SimpleTypesSerializer = new SimpleTypesSerializer();
				if (simpleTypesSerializer.isSupport(any))
					serializedData = simpleTypesSerializer.serialize(value);*/
					
					// пройти циклом по всем сериализатором и воспользоваться тем, который поддерживается
					
			
		}
		
		/* INTERFACE devoron.data.core.serializer.ISerializerShema */
		
		public function registerSerializer(cls:Class, serializer:ISerializer) 
		{
			
		}
		
		public function unregisterSerializer(cls:Class, serializer:ISerializer) 
		{
			
		}
		
		
	}

}