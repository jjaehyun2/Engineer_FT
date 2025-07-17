package services.vo
{
	import flash.utils.getQualifiedClassName;
	
	import mx.utils.ObjectUtil;
	import mx.utils.StringUtil;
	
	public class MapValueObject
	{
		/**
		 *  Duplicates an instance of an ValueObject subclass.
		 *  
		 *  Returns a new ValueObject that is a copy of the original
		 *  instance of the ValueObject object.
		 *  
		 *  The new ValueObject object includes all the properties
		 *  of the original.
		 */
		public function clone():Object
		{
			return ObjectUtil.copy(this);
		}
		/**
		 *  Collect all properties to string as <i>property</i> = <i>value</i>.
		 */
		public function toString():String
		{
			// get type of map class
			var type:String = getQualifiedClassName(this);
			// collect all properties to string
			var classInfo:Object = ObjectUtil.getClassInfo(this);
			var values:String = "";
			var props:Array = classInfo["properties"];
			for(var i:int = 0; i < props.length; i++)
			{
				var prop:String = (props[i] as QName).localName;
				values += StringUtil.substitute("{0}: {1}\n", prop, this[prop]);
			}
			
			return StringUtil.substitute("name: {0} ({1})", type, values)
		}
	}
}