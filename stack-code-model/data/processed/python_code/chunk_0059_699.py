package utils.loader{
    import flash.display.Loader;
    import flash.display.Sprite;
    import flash.events.*;
    import flash.net.URLRequest;

    public class BinLoader extends Sprite {
       
       
        private var _url:String = "";
        private var _onStatus:Function=null;

        public function BinLoader() {
        }
        
        
        public function getData(url:String,onStatus:Function=null):Loader {
        	_url = url;
        	this._onStatus = onStatus;
        	
        	var loader:Loader = new Loader();
			loader.contentLoaderInfo.addEventListener(Event.COMPLETE, completeHandler);
            loader.contentLoaderInfo.addEventListener(IOErrorEvent.IO_ERROR, ioErrorHandler);
           
            var request:URLRequest = new URLRequest(url);
            loader.load(request);
           
            return loader;
        }
        

        private function completeHandler(e:Event):void {
            if(this._onStatus!=null) 
            	this._onStatus(true);
        }


        private function ioErrorHandler(e:IOErrorEvent):void {
        	if(this._onStatus!=null) 
        		this._onStatus(false);
        }
    }
}