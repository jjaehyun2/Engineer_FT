package com.unhurdle
{
	import com.unhurdle.utils.GeneralUtils;

	public class OMVParameter
	{
		public function OMVParameter(xml:XML)
		{
			structure = xml;
		}
		public var structure:XML;
		public var name:String;
		public var optional:Boolean = false;
		public var description:String;
		public var type:String;
		public var value:String;
		public function requiresCore():Boolean{
			return GeneralUtils.isCore(type);
		}
	}
}