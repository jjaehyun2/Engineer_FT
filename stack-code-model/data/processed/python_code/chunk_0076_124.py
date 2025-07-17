/**
 * BaseAdGroupServiceService.as
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
	public class BaseAdGroupService extends AbstractWebService
    {
		private var results:Object;
		private var schemaMgr:SchemaManager;
		private var BaseAdGroupServiceService:WSDLService;
		private var BaseAdGroupServicePortType:WSDLPortType;
		private var BaseAdGroupServiceBinding:WSDLBinding;
		private var BaseAdGroupServicePort:WSDLPort;
		private var currentOperation:WSDLOperation;
		private var internal_schema:BaseAdGroupServiceSchema;
	
		/**
		 * Constructor for the base service, initializes all of the WSDL's properties
		 * @param [Optional] The LCDS destination (if available) to use to contact the server
		 * @param [Optional] The URL to the WSDL end-point
		 */
		public function BaseAdGroupService(destination:String=null, rootURL:String=null)
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
			internal_schema = new BaseAdGroupServiceSchema();
			schemaMgr = new SchemaManager();
			for(var i:int;i<internal_schema.schemas.length;i++)
			{
				internal_schema.schemas[i].targetNamespace=internal_schema.targetNamespaces[i];
				schemaMgr.addSchema(internal_schema.schemas[i]);
			}
BaseAdGroupServiceService = new WSDLService("BaseAdGroupServiceService");
			BaseAdGroupServicePort = new WSDLPort("BaseAdGroupServicePort",BaseAdGroupServiceService);
        	BaseAdGroupServiceBinding = new WSDLBinding("BaseAdGroupServiceBinding");
	        BaseAdGroupServicePortType = new WSDLPortType("BaseAdGroupServicePortType");
       		BaseAdGroupServiceBinding.portType = BaseAdGroupServicePortType;
       		BaseAdGroupServicePort.binding = BaseAdGroupServiceBinding;
       		BaseAdGroupServiceService.addPort(BaseAdGroupServicePort);
       		BaseAdGroupServicePort.endpointURI = "http://192.168.1.27:8081/SEMAServices/services/v1/AdGroupService";
       		if(this.endpointURI == null)
       		{
       			this.endpointURI = BaseAdGroupServicePort.endpointURI; 
       		} 
       		
			var requestMessage:WSDLMessage;
	        var responseMessage:WSDLMessage;
//define the WSDLOperation: new WSDLOperation(methodName)
            var getAllAdGroups:WSDLOperation = new WSDLOperation("getAllAdGroups");
				//input message for the operation
    	        requestMessage = new WSDLMessage("getAllAdGroups");
            				requestMessage.addPart(new WSDLMessagePart(new QName("http://schemas.macys.com/api/ad/v1","getAllAdGroups"),null,new QName("http://schemas.macys.com/api/ad/v1","getAllAdGroups")));
                requestMessage.encoding = new WSDLEncoding();
                requestMessage.encoding.namespaceURI="http://schemas.macys.com/api/ad/v1";
			requestMessage.encoding.useStyle="literal";
	            requestMessage.isWrapped = true;
	            requestMessage.wrappedQName = new QName("http://schemas.macys.com/api/ad/v1","getAllAdGroups");
                
                responseMessage = new WSDLMessage("getAllAdGroupsResponse");
            				responseMessage.addPart(new WSDLMessagePart(new QName("http://schemas.macys.com/api/ad/v1","getAllAdGroupsResponse"),null,new QName("http://schemas.macys.com/api/ad/v1","getAllAdGroupsResponse")));
                responseMessage.encoding = new WSDLEncoding();
                responseMessage.encoding.namespaceURI="http://schemas.macys.com/api/ad/v1";
                responseMessage.encoding.useStyle="literal";				
				
	            responseMessage.isWrapped = true;
	            responseMessage.wrappedQName = new QName("http://schemas.macys.com/api/ad/v1","getAllAdGroups");getAllAdGroups.inputMessage = requestMessage;
	        getAllAdGroups.outputMessage = responseMessage;
            getAllAdGroups.schemaManager = this.schemaMgr;
            getAllAdGroups.soapAction = "\"\"";
            getAllAdGroups.style = "document";
            BaseAdGroupServiceService.getPort("BaseAdGroupServicePort").binding.portType.addOperation(getAllAdGroups);//define the WSDLOperation: new WSDLOperation(methodName)
            var putAdGroup:WSDLOperation = new WSDLOperation("putAdGroup");
				//input message for the operation
    	        requestMessage = new WSDLMessage("putAdGroup");
            				requestMessage.addPart(new WSDLMessagePart(new QName("http://schemas.macys.com/api/ad/v1","putAdGroup"),null,new QName("http://schemas.macys.com/api/ad/v1","putAdGroup")));
                requestMessage.encoding = new WSDLEncoding();
                requestMessage.encoding.namespaceURI="http://schemas.macys.com/api/ad/v1";
			requestMessage.encoding.useStyle="literal";
	            requestMessage.isWrapped = true;
	            requestMessage.wrappedQName = new QName("http://schemas.macys.com/api/ad/v1","putAdGroup");
                
                responseMessage = new WSDLMessage("putAdGroupResponse");
            				responseMessage.addPart(new WSDLMessagePart(new QName("http://schemas.macys.com/api/ad/v1","putAdGroupResponse"),null,new QName("http://schemas.macys.com/api/ad/v1","putAdGroupResponse")));
                responseMessage.encoding = new WSDLEncoding();
                responseMessage.encoding.namespaceURI="http://schemas.macys.com/api/ad/v1";
                responseMessage.encoding.useStyle="literal";				
				
	            responseMessage.isWrapped = true;
	            responseMessage.wrappedQName = new QName("http://schemas.macys.com/api/ad/v1","putAdGroup");putAdGroup.inputMessage = requestMessage;
	        putAdGroup.outputMessage = responseMessage;
            putAdGroup.schemaManager = this.schemaMgr;
            putAdGroup.soapAction = "\"\"";
            putAdGroup.style = "document";
            BaseAdGroupServiceService.getPort("BaseAdGroupServicePort").binding.portType.addOperation(putAdGroup);//define the WSDLOperation: new WSDLOperation(methodName)
            var getAdGroupList:WSDLOperation = new WSDLOperation("getAdGroupList");
				//input message for the operation
    	        requestMessage = new WSDLMessage("getAdGroupList");
            				requestMessage.addPart(new WSDLMessagePart(new QName("http://schemas.macys.com/api/ad/v1","getAdGroupList"),null,new QName("http://schemas.macys.com/api/ad/v1","getAdGroupList")));
                requestMessage.encoding = new WSDLEncoding();
                requestMessage.encoding.namespaceURI="http://schemas.macys.com/api/ad/v1";
			requestMessage.encoding.useStyle="literal";
	            requestMessage.isWrapped = true;
	            requestMessage.wrappedQName = new QName("http://schemas.macys.com/api/ad/v1","getAdGroupList");
                
                responseMessage = new WSDLMessage("getAdGroupListResponse");
            				responseMessage.addPart(new WSDLMessagePart(new QName("http://schemas.macys.com/api/ad/v1","getAdGroupListResponse"),null,new QName("http://schemas.macys.com/api/ad/v1","getAdGroupListResponse")));
                responseMessage.encoding = new WSDLEncoding();
                responseMessage.encoding.namespaceURI="http://schemas.macys.com/api/ad/v1";
                responseMessage.encoding.useStyle="literal";				
				
	            responseMessage.isWrapped = true;
	            responseMessage.wrappedQName = new QName("http://schemas.macys.com/api/ad/v1","getAdGroupList");getAdGroupList.inputMessage = requestMessage;
	        getAdGroupList.outputMessage = responseMessage;
            getAdGroupList.schemaManager = this.schemaMgr;
            getAdGroupList.soapAction = "\"\"";
            getAdGroupList.style = "document";
            BaseAdGroupServiceService.getPort("BaseAdGroupServicePort").binding.portType.addOperation(getAdGroupList);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","AdGroup"),com.macys.marketing.sema.AdGroup);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","ServiceException"),com.macys.marketing.sema.ServiceException);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","SemaStatusType"),com.macys.marketing.sema.SemaStatusType);
							SchemaTypeRegistry.getInstance().registerCollectionClass(new QName("http://schemas.macys.com/api/ad/v1","getAdGroupList"),com.macys.marketing.sema.GetAdGroupList);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","getAllAdGroups"),com.macys.marketing.sema.GetAllAdGroups);
							SchemaTypeRegistry.getInstance().registerCollectionClass(new QName("http://schemas.macys.com/api/ad/v1","putAdGroupResponse"),com.macys.marketing.sema.PutAdGroupResponse);
							SchemaTypeRegistry.getInstance().registerCollectionClass(new QName("http://schemas.macys.com/api/ad/v1","putAdGroup"),com.macys.marketing.sema.PutAdGroup);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","ExceptionInfoDetail"),com.macys.marketing.sema.ExceptionInfoDetail);
							SchemaTypeRegistry.getInstance().registerCollectionClass(new QName("http://schemas.macys.com/api/ad/v1","getAllAdGroupsResponse"),com.macys.marketing.sema.GetAllAdGroupsResponse);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","exceptionInfo"),com.macys.marketing.sema.ExceptionInfo);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","SemaStateType"),com.macys.marketing.sema.SemaStateType);
							SchemaTypeRegistry.getInstance().registerCollectionClass(new QName("http://schemas.macys.com/api/ad/v1","getAdGroupListResponse"),com.macys.marketing.sema.GetAdGroupListResponse);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","SchemaValidationException"),com.macys.marketing.sema.SchemaValidationException);}
		/**
		 * Performs the low level call to the server for the operation
		 * It passes along the headers and the operation arguments
		 * @param getAllAdGroups
		 * @return Asynchronous token
		 */
		public function getAllAdGroups(getAllAdGroups:GetAllAdGroups):AsyncToken
		{
			var headerArray:Array = new Array();
            var out:Object = new Object();
            out["getAllAdGroups"] = getAllAdGroups;
	            currentOperation = BaseAdGroupServiceService.getPort("BaseAdGroupServicePort").binding.portType.getOperation("getAllAdGroups");
            var pc:PendingCall = new PendingCall(out,headerArray);
            call(currentOperation,out,pc.token,pc.headers);
            return pc.token;
		}
		/**
		 * Performs the low level call to the server for the operation
		 * It passes along the headers and the operation arguments
		 * @param userName3* @param putAdGroup
		 * @return Asynchronous token
		 */
		public function putAdGroup(userName3:com.macys.marketing.sema.UserName,putAdGroup:PutAdGroup):AsyncToken
		{
			var headerArray:Array = new Array();
            var out:Object = new Object();
            out["putAdGroup"] = putAdGroup;
	            currentOperation = BaseAdGroupServiceService.getPort("BaseAdGroupServicePort").binding.portType.getOperation("putAdGroup");//add each header value here 
				headerArray.push(new SOAPHeader(new QName("http://schemas.macys.com/definitions/ad/v1","userName"),userName3));
            var pc:PendingCall = new PendingCall(out,headerArray);
            call(currentOperation,out,pc.token,pc.headers);
            return pc.token;
		}
		/**
		 * Performs the low level call to the server for the operation
		 * It passes along the headers and the operation arguments
		 * @param getAdGroupList
		 * @return Asynchronous token
		 */
		public function getAdGroupList(getAdGroupList:GetAdGroupList):AsyncToken
		{
			var headerArray:Array = new Array();
            var out:Object = new Object();
            out["getAdGroupList"] = getAdGroupList;
	            currentOperation = BaseAdGroupServiceService.getPort("BaseAdGroupServicePort").binding.portType.getOperation("getAdGroupList");
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