package com.macys.marketing.sema.vo.tools
{
	
	import com.adobe.cairngorm.vo.ValueObject;

	[Bindable]
	public class GenerateKeywordsMatchTypeVO implements ValueObject
	{
		[Inspectable(enumeration="Broad,Phrase,Exact", type="String")]
		
		public var _MatchTypeVO:String;
		
		public function toString():String
		{
			return _MatchTypeVO.toString();
		}
	}
}