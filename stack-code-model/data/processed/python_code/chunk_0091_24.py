package flash.net
{
    import flash.events.*;
    import flash.utils.*;

    public class URLLoader extends EventDispatcher
    {
        public var data:Object;
        public var dataFormat:String = "text";
        private var stream:URLStream;
        public var bytesLoaded:uint = 0;
        public var bytesTotal:uint = 0;

        public function URLLoader(param1:URLRequest = null)
        {
            this.stream = new URLStream();
            this.stream.addEventListener(Event.OPEN, this.redirectEvent);
            this.stream.addEventListener(IOErrorEvent.IO_ERROR, this.onComplete);
            this.stream.addEventListener(SecurityErrorEvent.SECURITY_ERROR, this.redirectEvent);
            this.stream.addEventListener(HTTPStatusEvent.HTTP_STATUS, this.redirectEvent);
            this.stream.addEventListener(ProgressEvent.PROGRESS, this.onProgress);
            this.stream.addEventListener(Event.COMPLETE, this.onComplete);
            if (param1 != null)
            {
                this.load(param1);
            }
            return;
        }// end function

        override public function addEventListener(param1:String, param2:Function, param3:Boolean = false, param4:int = 0, param5:Boolean = false) : void
        {
            super.addEventListener(param1, param2, param3, param4, param5);
            if (param1 == HTTPStatusEvent.HTTP_RESPONSE_STATUS)
            {
                this.stream.addEventListener(HTTPStatusEvent.HTTP_RESPONSE_STATUS, this.redirectEvent);
            }
            return;
        }// end function

        public function load(param1:URLRequest) : void
        {
            this.stream.load(param1);
            return;
        }// end function

        public function close() : void
        {
            this.stream.close();
            return;
        }// end function

        private function redirectEvent(event:Event) : void
        {
            dispatchEvent(event);
            return;
        }// end function

        private function onComplete(event:Event) : void
        {
            var _loc_2:* = new ByteArray();
            this.stream.readBytes(_loc_2);
            switch(this.dataFormat)
            {
                case "binary":
                {
                    this.data = _loc_2;
                    break;
                }
                case "variables":
                {
                    if (_loc_2.length > 0)
                    {
                        this.data = new URLVariables(_loc_2.toString());
                        break;
                    }
                }
                case "text":
                {
                }
                default:
                {
                    this.data = _loc_2.toString();
                    break;
                    break;
                }
            }
            dispatchEvent(event);
            return;
        }// end function

        private function onProgress(event:ProgressEvent) : void
        {
            this.bytesLoaded = event.bytesLoaded;
            this.bytesTotal = event.bytesTotal;
            dispatchEvent(event);
            return;
        }// end function

    }
}