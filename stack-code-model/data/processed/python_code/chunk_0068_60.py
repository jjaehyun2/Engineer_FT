package com.unhurdle
{
	import com.unhurdle.utils.GeneralUtils;

	public class OMVMethod
	{
		public function OMVMethod(method:XML)
		{
			structure = method;
		}
		public var static:Boolean;
		public var structure:XML;
		public var name:String;
		public var shortDescription:String;
		public var longDescription:String;
		public var parameters:Vector.<OMVParameter> = new Vector.<OMVParameter>();
		public var returnType:String = "void";
		
		public function requiresCore():Boolean{
			var i:int;
			var len:int = parameters.length;
			for(i=0;i<len;i++){
				if(parameters[i].requiresCore()){
					return true;
				}
			}
			return GeneralUtils.isCore(returnType);
		}


	}
}