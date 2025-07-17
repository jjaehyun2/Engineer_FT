/**
 * BaseAdGroupStatsServiceService.as
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
	public class BaseAdGroupStatsService extends AbstractWebService
    {
		private var results:Object;
		private var schemaMgr:SchemaManager;
		private var BaseAdGroupStatsServiceService:WSDLService;
		private var BaseAdGroupStatsServicePortType:WSDLPortType;
		private var BaseAdGroupStatsServiceBinding:WSDLBinding;
		private var BaseAdGroupStatsServicePort:WSDLPort;
		private var currentOperation:WSDLOperation;
		private var internal_schema:BaseAdGroupStatsServiceSchema;
	
		/**
		 * Constructor for the base service, initializes all of the WSDL's properties
		 * @param [Optional] The LCDS destination (if available) to use to contact the server
		 * @param [Optional] The URL to the WSDL end-point
		 */
		public function BaseAdGroupStatsService(destination:String=null, rootURL:String=null)
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
			internal_schema = new BaseAdGroupStatsServiceSchema();
			schemaMgr = new SchemaManager();
			for(var i:int;i<internal_schema.schemas.length;i++)
			{
				internal_schema.schemas[i].targetNamespace=internal_schema.targetNamespaces[i];
				schemaMgr.addSchema(internal_schema.schemas[i]);
			}
BaseAdGroupStatsServiceService = new WSDLService("BaseAdGroupStatsServiceService");
			BaseAdGroupStatsServicePort = new WSDLPort("BaseAdGroupStatsServicePort",BaseAdGroupStatsServiceService);
        	BaseAdGroupStatsServiceBinding = new WSDLBinding("BaseAdGroupStatsServiceBinding");
	        BaseAdGroupStatsServicePortType = new WSDLPortType("BaseAdGroupStatsServicePortType");
       		BaseAdGroupStatsServiceBinding.portType = BaseAdGroupStatsServicePortType;
       		BaseAdGroupStatsServicePort.binding = BaseAdGroupStatsServiceBinding;
       		BaseAdGroupStatsServiceService.addPort(BaseAdGroupStatsServicePort);
       		BaseAdGroupStatsServicePort.endpointURI = "http://192.168.1.27:8081/SEMAServices/services/v1/AdGroupStatsService";
       		if(this.endpointURI == null)
       		{
       			this.endpointURI = BaseAdGroupStatsServicePort.endpointURI; 
       		} 
       		
			var requestMessage:WSDLMessage;
	        var responseMessage:WSDLMessage;
//define the WSDLOperation: new WSDLOperation(methodName)
            var getAdGroupStats:WSDLOperation = new WSDLOperation("getAdGroupStats");
				//input message for the operation
    	        requestMessage = new WSDLMessage("getAdGroupStats");
            				requestMessage.addPart(new WSDLMessagePart(new QName("http://schemas.macys.com/api/ad/v1","getAdGroupStats"),null,new QName("http://schemas.macys.com/api/ad/v1","getAdGroupStats")));
                requestMessage.encoding = new WSDLEncoding();
                requestMessage.encoding.namespaceURI="http://schemas.macys.com/api/ad/v1";
			requestMessage.encoding.useStyle="literal";
	            requestMessage.isWrapped = true;
	            requestMessage.wrappedQName = new QName("http://schemas.macys.com/api/ad/v1","getAdGroupStats");
                
                responseMessage = new WSDLMessage("getAdGroupStatsResponse");
            				responseMessage.addPart(new WSDLMessagePart(new QName("http://schemas.macys.com/api/ad/v1","getAdGroupStatsResponse"),null,new QName("http://schemas.macys.com/api/ad/v1","getAdGroupStatsResponse")));
                responseMessage.encoding = new WSDLEncoding();
                responseMessage.encoding.namespaceURI="http://schemas.macys.com/api/ad/v1";
                responseMessage.encoding.useStyle="literal";				
				
	            responseMessage.isWrapped = true;
	            responseMessage.wrappedQName = new QName("http://schemas.macys.com/api/ad/v1","getAdGroupStats");getAdGroupStats.inputMessage = requestMessage;
	        getAdGroupStats.outputMessage = responseMessage;
            getAdGroupStats.schemaManager = this.schemaMgr;
            getAdGroupStats.soapAction = "\"\"";
            getAdGroupStats.style = "document";
            BaseAdGroupStatsServiceService.getPort("BaseAdGroupStatsServicePort").binding.portType.addOperation(getAdGroupStats);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","AdGroupStats"),com.macys.marketing.sema.AdGroupStats);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","adGroupStatsPK"),com.macys.marketing.sema.AdGroupStatsPK);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","ServiceException"),com.macys.marketing.sema.ServiceException);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","SemaStatsType"),com.macys.marketing.sema.SemaStatsType);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","getAdGroupStats"),com.macys.marketing.sema.GetAdGroupStats);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","ExceptionInfoDetail"),com.macys.marketing.sema.ExceptionInfoDetail);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","exceptionInfo"),com.macys.marketing.sema.ExceptionInfo);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","SemaStateType"),com.macys.marketing.sema.SemaStateType);
							SchemaTypeRegistry.getInstance().registerCollectionClass(new QName("http://schemas.macys.com/api/ad/v1","getAdGroupStatsResponse"),com.macys.marketing.sema.GetAdGroupStatsResponse);
							SchemaTypeRegistry.getInstance().registerClass(new QName("http://schemas.macys.com/api/ad/v1","SchemaValidationException"),com.macys.marketing.sema.SchemaValidationException);}
		/**
		 * Performs the low level call to the server for the operation
		 * It passes along the headers and the operation arguments
		 * @param getAdGroupStats
		 * @return Asynchronous token
		 */
		public function getAdGroupStats(getAdGroupStats:GetAdGroupStats):AsyncToken
		{
			var headerArray:Array = new Array();
            var out:Object = new Object();
            out["getAdGroupStats"] = getAdGroupStats;
	            currentOperation = BaseAdGroupStatsServiceService.getPort("BaseAdGroupStatsServicePort").binding.portType.getOperation("getAdGroupStats");
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