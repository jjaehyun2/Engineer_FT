package com.macys.marketing.sema.business.adcopy
{
	import com.macys.marketing.sema.business.SEMAWebService;
	import com.macys.marketing.sema.model.SEMAModelLocator;
	import com.macys.marketing.sema.view.event.ReplicateEvent;
	import com.macys.marketing.sema.view.event.ViewEventDispatcher;
	
	import mx.core.Application;
	import mx.rpc.events.FaultEvent;
	import mx.rpc.events.ResultEvent;
	import mx.rpc.soap.WebService;

	
	public class ReplicateAdCopyDelegate {
 
		private var model : SEMAModelLocator = SEMAModelLocator.getInstance();
	
  
	    public function execute(entityId:Number,destinationParentId:Number):void {
	       
	        var ws:WebService = new SEMAWebService("ReplicateEntityService");
	   
	        ws.ReplicateAdCopyList.addEventListener("result", resultHandler);
	        ws.addEventListener("fault", faultHandler);
	       
	          
	        
	        ws.ReplicateAdCopyList.send({EntityId:entityId, DestinationParentId:destinationParentId});
	  	       
	    }
    

	    public function resultHandler(event:ResultEvent):void {
	  
	        model.replicateAdCopyVO.id = event.result.Id;
	       	model.replicateAdCopyVO.groupId = event.result.GroupId;
	       	model.replicateAdCopyVO.status = event.result.Status;
	       	model.replicateAdCopyVO.state = event.result.State;
	       	model.replicateAdCopyVO.headline = event.result.Headline;
	       	model.replicateAdCopyVO.description1 = event.result.Description1;
	       	model.replicateAdCopyVO.description2 = event.result.Description2;
	       	model.replicateAdCopyVO.displayUrl = event.result.DisplayUrl;
	       	model.replicateAdCopyVO.destinationUrl = event.result.DestinationUrl;
	       	model.replicateAdCopyVO.vendorPolicyExemptionRequest = event.result.VendorPolicyExemptionRequest;
	       	model.replicateAdCopyVO.expirationDate = event.result.ExpirationDate;
	       	model.replicateAdCopyVO.effectiveDate = event.result.EffectiveDate;
	       	model.replicateAdCopyVO.createdDate = event.result.CreatedDate;
	       	model.replicateAdCopyVO.modifiedDate = event.result.ModifiedDate;
	       	model.replicateAdCopyVO.createdBy = event.result.CreatedBy;
	       	model.replicateAdCopyVO.modifiedBy = event.result.ModifiedBy;
	       	
	       	var evt:ReplicateEvent = new ReplicateEvent(ReplicateEvent.AD_COPY_CHANGED);
			evt.value = event;
			ViewEventDispatcher.dispatchViewEvent(evt);
	      
	    }

	    public function faultHandler(event:FaultEvent):void {
	  		Application.application.handleSoapFault(event);
	    }
		

	}
}