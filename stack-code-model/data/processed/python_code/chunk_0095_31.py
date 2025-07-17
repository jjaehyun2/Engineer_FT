package com.macys.marketing.sema.event.adcopy
{
	import com.adobe.cairngorm.control.CairngormEvent;
	import com.macys.marketing.sema.control.ServiceController;

	public class ReplicateAdCopyEvent extends CairngormEvent
	{
		
		public var sourceEntityId:Number;
		public var parentDestinationEntityId:Number;
		
		public function ReplicateAdCopyEvent(sourceEntityId:Number,parentDestinationEntityId:Number) 
		{
			super( ServiceController.EVENT_REPLICATE_ADCOPY );
			this.sourceEntityId = sourceEntityId;
			this.parentDestinationEntityId = parentDestinationEntityId;
		}
	}
}