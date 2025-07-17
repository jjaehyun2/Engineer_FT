/**
 * BasePortfolioGroupServiceService.as
 * This file was auto-generated from WSDL by the Apache Axis2 generator modified by Adobe
 * Any change made to this file will be overwritten when the code is re-generated.
 */
package com.macys.marketing.sema{
	import flash.events.Event;
	import flash.events.EventDispatcher;
	import flash.net.URLLoader;
	import flash.net.URLRequest;
	import flash.utils.getDefinitionByName;
	import flash.utils.getQualifiedClassName;
	import mx.controls.treeClasses.DefaultDataDescriptor;
	import mx.utils.ObjectUtil;
	import mx.utils.ObjectProxy;
	import mx.messaging.events.MessageFaultEvent;
	import mx.messaging.MessageResponder;
	import mx.messaging.messages.SOAPMessage;
	import mx.messaging.messages.ErrorMessage;
   	import mx.messaging.ChannelSet;
	import mx.messaging.channels.DirectHTTPChannel;
	import mx.rpc.*;
	import mx.rpc.events.*;
	import mx.rpc.soap.*;
	import mx.rpc.wsdl.*;
	import mx.rpc.xml.*;
	import mx.rpc.soap.types.*;
	import mx.collections.ArrayCollection;
	
	/**
	 * Base service implementation, extends the AbstractWebService and adds specific functionality for the selected WSDL
	 * It defines the options and properties for each of the WSDL's operations
	 */ 
	public class BasePortfolioGroupService extends AbstractWebService
    {
		private var results:Object;
		private var schemaMgr:SchemaManager;
		private var BasePortfolioGroupServiceService:WSDLService;
		private var BasePortfolioGroupServicePortType:WSDLPortType;
		private var BasePortfolioGroupServiceBinding:WSDLBinding;
		private var BasePortfolioGroupServicePort:WSDLPort;
		private var currentOperation:WSDLOperation;
		private var internal_schema:BasePortfolioGroupServiceSchema;
	
		/**
		 * Constructor for the base service, initializes all of the WSDL's properties
		 * @param [Optional] The LCDS destination (if available) to use to contact the server
		 * @param [Optional] The URL to the WSDL end-point
		 */
		public function BasePortfolioGroupService(destination:String=null, rootURL:String=null)
		{
			super(destination, rootURL);
			if(destination == null)
			{
				//no destination available; must set it to go directly to the target
				this.useProxy = false;
			}
			else
			{
				//specific destination requested; must set proxying to true
				this.useProxy = true;
			}
			
			if(rootURL != null)
			{
				this.endpointURI = rootURL;
			} 
			else 
			{
				this.endpointURI = null;
			}
			internal_schema = new BasePortfolioGroupServiceSchema();
			schemaMgr = new SchemaManager();
			for(var i:int;i<internal_schema.schemas.length;i++)
			{
				internal_schema.schemas[i].targetNamespace=internal_schema.targetNamespaces[i];
				schemaMgr.addSchema(internal_schema.schemas[i]);
			}
BasePortfolioGroupServiceService = new WSDLService("BasePortfolioGroupServiceService");
			BasePortfolioGroupServicePort = new WSDLPort("BasePortfolioGroupServicePort",BasePortfolioGroupServiceService);
        	BasePortfolioGroupServiceBinding = new WSDLBinding("BasePortfolioGroupServiceBinding");
	        BasePortfolioGroupServicePortType = new WSDLPortType("BasePortfolioGroupServicePortType");
       		BasePortfolioGroupServiceBinding.portType = BasePortfolioGroupServicePortType;
       		BasePortfolioGroupServicePort.binding = BasePortfolioGroupServiceBinding;
       		BasePortfolioGroupServiceService.addPort(BasePortfolioGroupServicePort);
       		BasePortfolioGroupServicePort.endpointURI = "http://192.168.1.27:8081/SEMAServices/services/v1/PortfolioGroupService";
       		if(this.endpointURI == null)
       		{
       			this.endpointURI = BasePortfolioGroupServicePort.endpointURI; 
       		} 
       		
			var requestMessage:WSDLMessage;
	        var responseMessage:WSDLMessage;
//define the WSDLOperation: new WSDLOperation(methodName)
            var putPortfolioGroups:WSDLOperation = new WSDLOperation("putPortfolioGroups");
				//input message for the operation
    	        requestMessage = new WSDLMessage("putPortfolioGroups");
            				requestMessage.addPart(new WSDLMessagePart(new QName("http://schemas.macys.com/api/ad/v1","putPortfolioGroups"),null,new QName("http://schemas.macys.com/api/ad/v1","putPortfolioGroups")));
                requestMessage.encoding = new WSDLEncoding();
                requestMessage.encoding.namespaceURI="http://schemas.macys.com/api/ad/v1";
			requestMessage.encoding.useStyle="literal";
	            requestMessage.isWrapped = true;
	            requestMessage.wrappedQName = new QName("http://schemas.macys.com/api/ad/v1","putPortfolioGroups");
                
                responseMessage = new WSDLMessage("putPortfolioGroupsResponse");
            				responseMessage.addPart(new WSDLMessagePart(new QName("http://schemas.macys.com/api/ad/v1","putPortfolioGroupsResponse"),null,new QName("http://schemas.macys.com/api/ad/v1","putPortfolioGroupsResponse")));
                responseMessage.encoding = new WSDLEncoding();
                responseMessage.encoding.namespaceURI="http://schemas.macys.com/api/ad/v1";
                responseMessage.encoding.useStyle="literal";				
				
	            responseMessage.isWrapped = true;
	            responseMessage.wrappedQName = new QName("http://schemas.macys.com/api/ad/v1","putPortfolioGroups");putPortfolioGroups.inputMessage = requestMessage;
	        putPortfolioGroups.outputMessage = responseMessage;
            putPortfolioGroups.schemaManager = this.schemaMgr;
            putPortfolioGroups.soapAction = "\"\"";
            putPortfolioGroups.style = "document";
            BasePortfolioGroupServiceService.getPort("BasePortfolioGroupServicePort").binding.portType.addOperation(putPortfolioGroups);//define the WSDLOperation: new WSDLOperation(methodName)
            var getPortfolioGroupList:WSDLOperation = new WSDLOperation("getPortfolioGroupList");
				//input message for the operation
    	        requestMessage = new WSDLMessage("getPortfolioGroupList");
            				requestMessage.addPart(new WSDLMessagePart(new QName("http://schemas.macys.com/api/ad/v1","getPortfolioGroupList"),null,new QName("http://schemas.macys.com/api/ad/v1","getPortfolioGroupList")));
                requestMessage.encoding = new WSDLEncoding();
                requestMessage.encoding.namespaceURI="http://schemas.macys.com/api/ad/v1";
			requestMessage.encoding.useStyle="literal";
	            requestMessage.isWrapped = true;
	            requestMessage.wrappedQName = new QName("http://schemas.macys.com/api/ad/v1","getPortfolioGroupList");
                
                responseMessage = new WSDLMessage("getPortfolioGroupListResponse");
            				responseMessage.addPart(new WSDLMessagePart(new QName("http://schemas.macys.com/api/ad/v1","getPortfolioGroupListResponse"),null,new QName("http://schemas.macys.com/api/ad/v1","getPortfolioGroupListResponse")));
                responseMessage.encoding = new WSDLEncoding();
                responseMessage.encoding.namespaceURI="http://schemas.macys.com/api/ad/v1";
                responseMessage.encoding.useStyle="literal";				
				
	            responseMessage.isWrapped = true;
	            responseMessage.wrappedQName = new QName("http://schemas.macys.com/api/ad/v1","getPortfolioGroupList");getPortfolioGroupList.inputMessage = requestMessage;
	        getPortfolioGroupList.outputMessage = responseMessage;
            getPortfolioGroupList.schemaManager = this.schemaMgr;
            getPortfolioGroupList.soapAction = "\"\"";
            getPortfolioGroupList.style = "document";
            BasePortfolioGroupServiceService.getPort("BasePortfolioGroupServicePort").binding.portType.addOperation(getPortfolioGroupList);//define the WSDLOperation: new WSDLOperation(methodName)
            var getAllPortfolioGroups:WSDLOperation = new WSDLOperation("getAllPortfolioGroups");
				//input message for the operation
    	        requestMessage = new WSDLMessage("getAllPortfolioGroups");
            				requestMessage.addPart(new WSDLMessagePart(new QName("http://schemas.macys.com/api/ad/v1","getAllPortfolioGroups"),null,new QName("http://schemas.macys.com/api/ad/v1","getAllPortfolioGroups")));
                requestMessage.encoding = new WSDLEncoding();
                requestMessage.encoding.namespaceURI="http://schemas.macys.com/api/ad/v1";
			requestMessage.encoding.useStyle="literal";
	            requestMessage.isWrapped = true;
	            requestMessage.wrappedQName = new QName("http://schemas.macys.com/api/ad/v1","getAllPortfolioGroups");
                
                responseMessage = new WSDLMessage("getAllPortfolioGroupsResponse");
            				responseMessage.addPart(new WSDLMessagePart(new QName("http://schemas.macys.com/api/ad/v1","getAllPortfolioGroupsResponse"),null,new QName("http://schemas.macys.com/api/ad/v1","getAllPortfolioGroupsResponse")));
                responseMessage.encoding = new WSDLEncoding();
                responseMessage.encoding.namespaceURI="http://schemas.macys.com/api/ad/v1";
                responseMessage.encoding.useStyle="literal";				
				
	            responseMessage.isWrapped = true;
	            responseMessage.wrappedQName = new QName("http://schemas.macys.com/api/ad/v1","getAllPortfolioGroups");getAllPortfolioGroups.inputMessage = requestMessage;
	        getAllPortfolioGroups.outputMessage = responseMessage;
            getAllPortfolioGroups.schemaManager = this.schemaMgr;
            getAllPortfolioGroups.soapAction = "\"\"";
            getAllPortfolioGroups.style = "document";
            BasePortfolioGroupServiceService.getPort("BasePortfolioGroupServicePort").binding.portType.addOperation(getAllPortfolioGroups);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","PortfolioGroup"),com.macys.marketing.sema.PortfolioGroup);
							SchemaTypeRegistry.getInstance().registerCollectionClass(new QName("http://schemas.macys.com/api/ad/v1","getPortfolioGroupListResponse"),com.macys.marketing.sema.GetPortfolioGroupListResponse);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","ServiceException"),com.macys.marketing.sema.ServiceException);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","SemaStatusType"),com.macys.marketing.sema.SemaStatusType);
							SchemaTypeRegistry.getInstance().registerCollectionClass(new QName("http://schemas.macys.com/api/ad/v1","getPortfolioGroupList"),com.macys.marketing.sema.GetPortfolioGroupList);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","getAllPortfolioGroups"),com.macys.marketing.sema.GetAllPortfolioGroups);
							SchemaTypeRegistry.getInstance().registerCollectionClass(new QName("http://schemas.macys.com/api/ad/v1","putPortfolioGroups"),com.macys.marketing.sema.PutPortfolioGroups);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","ExceptionInfoDetail"),com.macys.marketing.sema.ExceptionInfoDetail);
							SchemaTypeRegistry.getInstance().registerCollectionClass(new QName("http://schemas.macys.com/api/ad/v1","getAllPortfolioGroupsResponse"),com.macys.marketing.sema.GetAllPortfolioGroupsResponse);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","exceptionInfo"),com.macys.marketing.sema.ExceptionInfo);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","SemaStateType"),com.macys.marketing.sema.SemaStateType);
							SchemaTypeRegistry.getInstance().registerCollectionClass(new QName("http://schemas.macys.com/api/ad/v1","putPortfolioGroupsResponse"),com.macys.marketing.sema.PutPortfolioGroupsResponse);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","SchemaValidationException"),com.macys.marketing.sema.SchemaValidationException);}
		/**
		 * Performs the low level call to the server for the operation
		 * It passes along the headers and the operation arguments
		 * @param userName1* @param putPortfolioGroups
		 * @return Asynchronous token
		 */
		public function putPortfolioGroups(userName1:com.macys.marketing.sema.UserName,putPortfolioGroups:PutPortfolioGroups):AsyncToken
		{
			var headerArray:Array = new Array();
            var out:Object = new Object();
            out["putPortfolioGroups"] = putPortfolioGroups;
	            currentOperation = BasePortfolioGroupServiceService.getPort("BasePortfolioGroupServicePort").binding.portType.getOperation("putPortfolioGroups");//add each header value here 
				headerArray.push(new SOAPHeader(new QName("http://schemas.macys.com/definitions/ad/v1","userName"),userName1));
            var pc:PendingCall = new PendingCall(out,headerArray);
            call(currentOperation,out,pc.token,pc.headers);
            return pc.token;
		}
		/**
		 * Performs the low level call to the server for the operation
		 * It passes along the headers and the operation arguments
		 * @param getPortfolioGroupList
		 * @return Asynchronous token
		 */
		public function getPortfolioGroupList(getPortfolioGroupList:GetPortfolioGroupList):AsyncToken
		{
			var headerArray:Array = new Array();
            var out:Object = new Object();
            out["getPortfolioGroupList"] = getPortfolioGroupList;
	            currentOperation = BasePortfolioGroupServiceService.getPort("BasePortfolioGroupServicePort").binding.portType.getOperation("getPortfolioGroupList");
            var pc:PendingCall = new PendingCall(out,headerArray);
            call(currentOperation,out,pc.token,pc.headers);
            return pc.token;
		}
		/**
		 * Performs the low level call to the server for the operation
		 * It passes along the headers and the operation arguments
		 * @param getAllPortfolioGroups
		 * @return Asynchronous token
		 */
		public function getAllPortfolioGroups(getAllPortfolioGroups:GetAllPortfolioGroups):AsyncToken
		{
			var headerArray:Array = new Array();
            var out:Object = new Object();
            out["getAllPortfolioGroups"] = getAllPortfolioGroups;
	            currentOperation = BasePortfolioGroupServiceService.getPort("BasePortfolioGroupServicePort").binding.portType.getOperation("getAllPortfolioGroups");
            var pc:PendingCall = new PendingCall(out,headerArray);
            call(currentOperation,out,pc.token,pc.headers);
            return pc.token;
		}
        /**
         * Performs the actual call to the remove server
         * It SOAP-encodes the message using the schema and WSDL operation options set above and then calls the server using 
         * an async invoker
         * It also registers internal event handlers for the result / fault cases
         * @private
         */
        private function call(operation:WSDLOperation,args:Object,token:AsyncToken,headers:Array=null):void
        {
	    	var enc:SOAPEncoder = new SOAPEncoder();
	        var soap:Object = new Object;
	        var message:SOAPMessage = new SOAPMessage();
	        enc.wsdlOperation = operation;
	        soap = enc.encodeRequest(args,headers);
	        message.setSOAPAction(operation.soapAction);
	        message.body = soap.toString();
	        message.url=endpointURI;
            var inv:AsyncRequest = new AsyncRequest();
            inv.destination = super.destination;
            //we need this to handle multiple asynchronous calls 
            var wrappedData:Object = new Object();
            wrappedData.operation = currentOperation;
            wrappedData.returnToken = token;
            if(!this.useProxy)
            {
            	var dcs:ChannelSet = new ChannelSet();	
	        	dcs.addChannel(new DirectHTTPChannel("direct_http_channel"));
            	inv.channelSet = dcs;
            }                
            var processRes:AsyncResponder = new AsyncResponder(processResult,faultResult,wrappedData);
            inv.invoke(message,processRes);
		}
        
        /**
         * Internal event handler to process a successful operation call from the server
         * The result is decoded using the schema and operation settings and then the events get passed on to the actual facade that the user employs in the application 
         * @private
         */
		private function processResult(result:Object,wrappedData:Object):void
           {
           		var headers:Object;
           		var token:AsyncToken = wrappedData.returnToken;
                var currentOperation:WSDLOperation = wrappedData.operation;
                var decoder:SOAPDecoder = new SOAPDecoder();
                decoder.resultFormat = "object";
                decoder.headerFormat = "object";
                decoder.multiplePartsFormat = "object";
                decoder.ignoreWhitespace = true;
                decoder.makeObjectsBindable=false;
                decoder.wsdlOperation = currentOperation;
                decoder.schemaManager = currentOperation.schemaManager;
                var body:Object = result.message.body;
                var stringResult:String = String(body);
                if(stringResult == null  || stringResult == "")
                	return;
                var soapResult:SOAPResult = decoder.decodeResponse(result.message.body);
                if(soapResult.isFault)
                {
	                var faults:Array = soapResult.result as Array;
	                for each (var soapFault:Fault in faults)
	                {
		                var soapFaultEvent:FaultEvent = FaultEvent.createEvent(soapFault,token,null);
		                token.dispatchEvent(soapFaultEvent);
	                }
                } else {
	                result = soapResult.result;
	                headers = soapResult.headers;
	                var event:ResultEvent = ResultEvent.createEvent(result,token,null);
	                event.headers = headers;
	                token.dispatchEvent(event);
                }
           }
           	/**
           	 * Handles the cases when there are errors calling the operation on the server
           	 * This is not the case for SOAP faults, which is handled by the SOAP decoder in the result handler
           	 * but more critical errors, like network outage or the impossibility to connect to the server
           	 * The fault is dispatched upwards to the facade so that the user can do something meaningful 
           	 * @private
           	 */
			private function faultResult(error:MessageFaultEvent,token:Object):void
			{
				//when there is a network error the token is actually the wrappedData object from above	
				if(!(token is AsyncToken))
					token = token.returnToken;
				token.dispatchEvent(new FaultEvent(FaultEvent.FAULT,true,true,new Fault(error.faultCode,error.faultString,error.faultDetail)));
			}
		}
	}

	import mx.rpc.AsyncToken;
	import mx.rpc.AsyncResponder;
	import mx.rpc.wsdl.WSDLBinding;
                
    /**
     * Internal class to handle multiple operation call scheduling
     * It allows us to pass data about the operation being encoded / decoded to and from the SOAP encoder / decoder units. 
     * @private
     */
    class PendingCall
    {
		public var args:*;
		public var headers:Array;
		public var token:AsyncToken;
		
		public function PendingCall(args:Object, headers:Array=null)
		{
			this.args = args;
			this.headers = headers;
			this.token = new AsyncToken(null);
		}
	}