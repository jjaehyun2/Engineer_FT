package com.macys.marketing.sema.event.adkeyword
{
	import com.adobe.cairngorm.control.CairngormEvent;
	import com.macys.marketing.sema.control.ServiceController;
	
	public class GetAllAdKeywordsEvent extends CairngormEvent
	{
		
		public var adGroupId:Number;
		
		public function GetAllAdKeywordsEvent(adGroupId:Number)
		{
			super (ServiceController.EVENT_GETALL_ADKEYWORDS);
			this.adGroupId = adGroupId;
		}

	}
}