package devoron.data.core.serializer.serializers
{
	import org.aswing.tree.DefaultMutableTreeNode;
	
	/**
	 * TreeNodeSerializer
	 * @author Devoron
	 */
	public class TreeNodeSerializer
	{
		
		public function TreeNodeSerializer()
		{
		
		}
		
		public function isSupport(any:*):Boolean
		{
			if (any is DefaultMutableTreeNode)
				return true;
			return false;
		}
		
		public static function serializeNode(serializedData:String, node:DefaultMutableTreeNode):String
		{
			//var node:DefaultMutableTreeNode;
			var obj:Object = node.getUserObject();
			var childrenCount:int = node.getChildCount();
			var children:Array = [];
			
			if (!obj)
				return serializedData;
			
			serializedData += "{";
			serializedData += qutes("node") + ":" + qutes(obj.uid);
			
			if (childrenCount > 0)
			{
				
				serializedData += ",";
				serializedData += qutes("children") + ":" + "[";
				for (var i:int = 0; i < childrenCount; i++)
				{
					serializedData = serializeNode(serializedData, node.getChildAt(i) as DefaultMutableTreeNode) + ",";
						//children.push((node.getChildAt(i) as DefaultMutableTreeNode).getUserObject().uid);
				}
				serializedData = serializedData.substring(0, serializedData.length - 1);
				serializedData += "]";
			}
			
			//serializeArray("nodes", serializedData, children);
			//if ((value[prop] is Array))
			//serializedData = serializedData.substring(0, serializedData.length - 2) + "}";
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
		
	
	}

}