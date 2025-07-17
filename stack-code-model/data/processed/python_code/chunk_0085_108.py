package com.macys.marketing.sema.command.adcopy
{
	import com.adobe.cairngorm.commands.Command;
	import com.adobe.cairngorm.control.CairngormEvent;
	import com.macys.marketing.sema.business.adcopy.GetAllAdCopyDelegate;
	import com.macys.marketing.sema.event.adcopy.GetAllAdCopyEvent;
	import com.macys.marketing.sema.model.SEMAModelLocator;
	
	import mx.rpc.IResponder;
	
	public class GetAllAdCopyCommand implements Command, IResponder
	{
		public function GetAllAdCopyCommand()
		{
			trace("GetAllAdCopyCommand: GetAllAdCopyCommand()");
		}
		
		private var model : SEMAModelLocator = SEMAModelLocator.getInstance();
	
		
		
		public function execute(event:CairngormEvent):void
		{
			trace("GetAllAdCopyCommand: execute()");
			
			var businessDelegate : GetAllAdCopyDelegate = new GetAllAdCopyDelegate();
			var getAllAdCopyEvent : GetAllAdCopyEvent = GetAllAdCopyEvent(event);	
			businessDelegate.execute(getAllAdCopyEvent.groupId);
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