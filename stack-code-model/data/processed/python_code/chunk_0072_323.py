package com.macys.marketing.sema.event.tools
{
	import com.adobe.cairngorm.control.CairngormEvent;
	import com.macys.marketing.sema.control.ServiceController;

	public class GenerateKeywordsEvent extends CairngormEvent
	{
		
		public var seedKeyword : String;
		public var matchType : String;
		public var negativeFlag : Boolean;
		public var useSynonym : Boolean;
		
		public function GenerateKeywordsEvent(seedKeyword:String,matchType:String,negativeFlag:Boolean,useSynonym:Boolean) 
		{
			super( ServiceController.EVENT_GET_KEYWORD_VARIATIONS );
			this.seedKeyword = seedKeyword;
			this.matchType = matchType;
			this.negativeFlag = negativeFlag;
			this.useSynonym = useSynonym;
			

		}
	}
}