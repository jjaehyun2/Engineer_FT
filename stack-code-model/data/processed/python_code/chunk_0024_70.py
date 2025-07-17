package com.macys.marketing.sema.command.adcopy
{
	import com.adobe.cairngorm.commands.Command;
	import com.adobe.cairngorm.control.CairngormEvent;
	import com.macys.marketing.sema.business.adcopy.ReplicateAdCopyDelegate;
	import com.macys.marketing.sema.event.adcopy.ReplicateAdCopyEvent;
	import com.macys.marketing.sema.model.SEMAModelLocator;
	
	import mx.rpc.IResponder;
	
	public class ReplicateAdCopyCommand implements Command, IResponder
	{
		public function ReplicateAdCopyCommand()
		{
		}
		
		private var model : SEMAModelLocator = SEMAModelLocator.getInstance();
	
		
		
		public function execute(event:CairngormEvent):void
		{
			var businessDelegate : ReplicateAdCopyDelegate = new ReplicateAdCopyDelegate;
			var replicateAdCopyEvent : ReplicateAdCopyEvent = ReplicateAdCopyEvent(event);	
			businessDelegate.execute(replicateAdCopyEvent.sourceEntityId,replicateAdCopyEvent.parentDestinationEntityId);
		}
		
		public function fault(info:Object):void
		{
			trace("We have a fault");
		}
		
		public function result(data:Object):void
		{
			
		}

	}

}