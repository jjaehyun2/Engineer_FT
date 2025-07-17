package h2olib.services 
{	
   
    import flash.events.IOErrorEvent;
    
    import mx.rpc.Fault;
    import mx.rpc.events.FaultEvent;
    import mx.rpc.events.ResultEvent;
    import mx.rpc.http.mxml.HTTPService;
    import mx.utils.StringUtil;

    /**
     *  HTTPXmlService class
     *
     *  This class allows to make an HTTP request with specified
     *  result and error handler functions.
     *
     *  @author Anton Kirzyk / Ramada
     *  @version $Revision 1.0 $ $Date: 2009/06/19
     */
    [Event(name="responseError", type="flash.events.Event")]
    public class HTTPXmlService extends HTTPService {

        public static const HTTP_RESULT_ERROR:String = "Can't obtain data from the host url ";

        /**
         *  Constructor
         */
        public function HTTPXmlService(resultHandler:Function=null, errorHandler:Function=null) 
        {
            super();

            useProxy = false;
            
            method = "POST";
            resultFormat = "object";
            contentType = "application/xml";

            addResultHandler(resultHandler);
            addErrorHandler(errorHandler);
            addEventListener(IOErrorEvent.IO_ERROR, ioErrorHandler)
            
            //addEventListener(FaultEvent.FAULT, faultHandler);
        }

        /**
         *  Internal Fault Handler
         *
         *  If event handler for <code>ServiceErrorEvent.FAULT_ERROR</code>
         *  was specified dispatches ServiceErrorEvent.
         *  Otherwise throws an exception.
         */
        protected function ioErrorHandler(event:IOErrorEvent):void 
        {
            if (hasEventListener(FaultEvent.FAULT)) 
            {
            	var fault:Fault = new Fault("0000","IOError",event.text);
            	var faultEvent:FaultEvent = new FaultEvent(FaultEvent.FAULT,false,true,fault);
                dispatchEvent(faultEvent);
            } 
            
        }

        public function addResultHandler(handler:Function):void 
        {
            if (handler != null) 
            {
                addEventListener(ResultEvent.RESULT, handler);
            }
        }

        public function addErrorHandler(handler:Function):void 
        {
        	if (handler != null) 
            {
        		addEventListener(FaultEvent.FAULT, handler);
            }
        }

        override public function toString():String 
        {
            return StringUtil.substitute("Url: {1}\n{0}", url, super.toString());
        }
    }
}