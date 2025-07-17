package com.macys.marketing.sema.business.adkeyword
{
	import com.macys.marketing.sema.business.SEMAWebService;
	
	import mx.collections.ArrayCollection;
	import mx.rpc.IResponder;
	import mx.rpc.events.FaultEvent;
	import mx.rpc.events.ResultEvent;
	import mx.rpc.soap.WebService;

	
	public class AdKeywordService
	{
 
			
		/**
		 * GetAllAdKeywords
		 * 
		 * This method calls the AdKeyword.getAllAdKeywords webservice and sets the handler on the
		 * given IResponder.
		 * 
		 * @param IResponder  Typically the command that will initiate and handle the result, like GetAllAdKeywordsCommand
		 * @param Number adGroupId.  Used as input to the web service
		 *  
		 */
		public function getAllAdKeywords(responder : IResponder,adGroupId : Number) : void
		{
			
			var ws : WebService = new SEMAWebService("AdKeyWordService");
			
			ws.getAllAdKeywords.addEventListener(ResultEvent.RESULT, responder.result);
        	ws.getAllAdKeywords.addEventListener(FaultEvent.FAULT, responder.fault);
          	ws.getAllAdKeywords.send(adGroupId);
			
		}//end getAllAdKeywords()
		
		

		/**
		 * PutAdKeywordList
		 * 
		 * This method calls the AdKeyword.putAdKeywords webservice and sets the handler on the
		 * given IResponder.
		 * 
		 * @param IResponder  Typically the command that will initiate and handle the result, like PutAdKeywordsCommand
		 * @param ArrayCollection of AdKeywordVO's.  Used as input to the web service
		 *  
		 */
		public function putAdKeywords(responder : IResponder,adKeywords : ArrayCollection) : void
		{
			
			var ws : WebService = new SEMAWebService("AdKeyWordService");
			
			ws.putAdKeywords.addEventListener(ResultEvent.RESULT, responder.result);
        	ws.putAdKeywords.addEventListener(FaultEvent.FAULT, responder.fault);
          	ws.putAdKeywords.send(adKeywords);
			
		}//end putAdKeywords()
		
		
	}   
    

}