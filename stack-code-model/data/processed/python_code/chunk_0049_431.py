package com.macys.marketing.sema.command.tools
{
	import com.adobe.cairngorm.commands.Command;
	import com.adobe.cairngorm.control.CairngormEvent;
	import com.macys.marketing.sema.business.tools.GenerateKeywordsDelegate;
	import com.macys.marketing.sema.event.tools.GenerateKeywordsEvent;
	import com.macys.marketing.sema.model.SEMAModelLocator;
	
	import mx.rpc.IResponder;
	
	public class GenerateKeywordsCommand implements Command, IResponder
	{
		public function GenerateKeywordsCommand()
		{
		}
		
		private var model : SEMAModelLocator = SEMAModelLocator.getInstance();
	
		
		
		public function execute(event:CairngormEvent):void
		{
			var businessDelegate : GenerateKeywordsDelegate = new GenerateKeywordsDelegate;
			var keywordGeneratorEvent :GenerateKeywordsEvent = GenerateKeywordsEvent(event);	
			businessDelegate.execute(keywordGeneratorEvent.seedKeyword,keywordGeneratorEvent.matchType,keywordGeneratorEvent.negativeFlag,keywordGeneratorEvent.useSynonym);
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