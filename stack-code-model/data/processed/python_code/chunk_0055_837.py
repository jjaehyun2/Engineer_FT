package com.HAL.sockets {
    import com.HAL.sockets.events.CloseHandlerEvent;
    import com.HAL.sockets.events.ConnectHandlerEvent;
    import com.HAL.sockets.events.DataHandlerEvent;
    import com.HAL.sockets.events.ErrorHandlerEvent;
    import com.HAL.sockets.events.IOErrorHandlerEvent;
    import com.HAL.sockets.events.ProgressHandlerEvent;
    import com.HAL.sockets.events.SecurityErrorHandlerEvent;
    import com.HAL.utils.StringUtils;
    
    import flash.display.Sprite;
    import flash.events.Event;
    import flash.events.IEventDispatcher;
    import flash.events.IOErrorEvent;
    import flash.events.ProgressEvent;
    import flash.events.SecurityErrorEvent;
    import flash.net.Socket;
    import flash.utils.ByteArray;

    public class JSONSocketConnector extends Sprite {
        private var hostName:String = "127.0.0.1";
        private var port:uint = 7800;
        private var socket:Socket;
        
        public static const none_encryptionMethod:String = '';
        public static const custom_encryptionMethod:String = 'custom';
        
        private var _encryptionMethod:String = JSONSocketConnector.none_encryptionMethod;

		[Event(name="connectHandler", type="com.HAL.sockets.events.ConnectHandlerEvent")]
		[Event(name="closeHandler", type="com.HAL.sockets.events.CloseHandlerEvent")]
		[Event(name="dataHandler", type="com.HAL.sockets.events.DataHandlerEvent")]
		[Event(name="ioErrorHandler", type="com.HAL.sockets.events.IOErrorHandlerEvent")]
		[Event(name="progressHandler", type="com.HAL.sockets.events.ProgressHandlerEvent")]
		[Event(name="securityErrorHandler", type="com.HAL.sockets.events.SecurityErrorHandlerEvent")]
		[Event(name="errorHandler", type="com.HAL.sockets.events.ErrorHandlerEvent")]

        public function JSONSocketConnector(hostName:String = 'localhost', port:uint = 7800) {
            this.socket = new Socket();
            this.hostName = hostName;
            this.port = port;
            configureListeners(this.socket);
            this.socket.connect(this.hostName, this.port);
        }
        
        public function set useEncryptionNone(bool:Boolean):void {
        	this.encryptionMethod = JSONSocketConnector.none_encryptionMethod;
        }
        
        public function get useEncryptionNone():Boolean {
        	return this.isEncryptionNone;
        }
        
        public function set useEncryptionCustom(bool:Boolean):void {
			trace('JSONSocketConnector.useEncryptionCustom.1 --> bool='+bool);
        	this.encryptionMethod = ((bool) ? JSONSocketConnector.custom_encryptionMethod : JSONSocketConnector.none_encryptionMethod);
			trace('JSONSocketConnector.useEncryptionCustom.2 --> this.encryptionMethod='+this.encryptionMethod);
        }
        
        public function get useEncryptionCustom():Boolean {
        	return this.isEncryptionCustom;
        }
        
        public function set encryptionMethod(encryptionMethod:String):void {
        	var isMethodValid:Boolean = false;
        	switch (encryptionMethod) {
        		case JSONSocketConnector.custom_encryptionMethod:
        			isMethodValid = true;
        		break;
        	}
        	if (isMethodValid) {
        		this._encryptionMethod = encryptionMethod;
        	}
        }
        
        public function get encryptionMethod():String {
        	return this._encryptionMethod;
        }

        public function get isEncryptionCustom():Boolean {
			trace('JSONSocketConnector.isEncryptionCustom.1 --> this._encryptionMethod='+this._encryptionMethod);
			trace('JSONSocketConnector.isEncryptionCustom.2 --> JSONSocketConnector.custom_encryptionMethod='+JSONSocketConnector.custom_encryptionMethod);
        	return (this._encryptionMethod == JSONSocketConnector.custom_encryptionMethod);
        }

        public function get isEncryptionNone():Boolean {
        	return (this._encryptionMethod == JSONSocketConnector.none_encryptionMethod);
        }

		private function send_bytes_to_socket(data:String):void { 
			var ba:ByteArray = new ByteArray(); 
			ba.writeMultiByte(data + String.fromCharCode(0), "UTF-8");
			try {
				this.socket.writeBytes(ba,0,ba.length);
			} catch(err:Error) {
				trace('JSONSocketConnector.send_bytes_to_socket().ERROR.1 --> '+err.toString());
				this.dispatchEvent(new ErrorHandlerEvent(ErrorHandlerEvent.TYPE_ERROR_HANDLER, data));
			} finally {
				this.socket.flush();
			}
			trace('JSONSocketConnector.send_bytes_to_socket().1 --> ba='+ba.toString());
		}
		
		public function send(data:String):void {
        	var x:String = data;
			trace('JSONSocketConnector.send().1 --> this.isEncryptionCustom='+this.isEncryptionCustom);
        	if (this.isEncryptionCustom) {
        		if (data is String) {
	        		data = StringUtils.obscure(data,StringUtils.mode_OBSCURE_ALL_SWAPPER);
        		}
				x = StringUtils.dumpAsHexBytesString(data);
        	}
			trace('JSONSocketConnector.send().2 --> x='+x);
			this.send_bytes_to_socket(x);
        }

        private function configureListeners(dispatcher:IEventDispatcher):void {
            dispatcher.addEventListener(Event.CLOSE, closeHandler);
			dispatcher.addEventListener(Event.CONNECT, connectHandler);
			dispatcher.addEventListener(ProgressEvent.SOCKET_DATA, dataHandler);
			dispatcher.addEventListener(IOErrorEvent.IO_ERROR, ioErrorHandler);
            dispatcher.addEventListener(ProgressEvent.PROGRESS, progressHandler);
            dispatcher.addEventListener(SecurityErrorEvent.SECURITY_ERROR, securityErrorHandler);
        }

        private function closeHandler(event:Event):void {
			trace('JSONSocketConnector.closeHandler().1 --> event='+event.toString());
        	this.dispatchEvent(new CloseHandlerEvent(CloseHandlerEvent.TYPE_CLOSE_HANDLER, event));
        }

        private function connectHandler(event:Event):void {
			trace('JSONSocketConnector.connectHandler().1 --> event='+event.toString());
        	this.dispatchEvent(new ConnectHandlerEvent(ConnectHandlerEvent.TYPE_CONNECT_HANDLER, event));
        }

        private function dataHandler(event:ProgressEvent):void {
			var data:* = this.socket.readUTFBytes(this.socket.bytesAvailable);
			trace('JSONSocketConnector.dataHandler().1 --> event='+event.toString());
        	if ( (this.useEncryptionCustom) || (StringUtils.isHexDigits(data)) ) {
        		//this.useEncryptionCustom = true;
				data = StringUtils.deobscure(StringUtils.fromHexBytesString(data),StringUtils.mode_OBSCURE_ALL_SWAPPER);
        	}
        	this.dispatchEvent(new DataHandlerEvent(DataHandlerEvent.TYPE_DATA_HANDLER, data));
        }

        private function ioErrorHandler(event:IOErrorEvent):void {
			trace('JSONSocketConnector.ioErrorHandler().1 --> event='+event.toString());
        	this.dispatchEvent(new IOErrorHandlerEvent(IOErrorHandlerEvent.TYPE_IOERROR_HANDLER, event));
        }

        private function progressHandler(event:ProgressEvent):void {
			trace('JSONSocketConnector.progressHandler().1 --> event='+event.toString());
        	this.dispatchEvent(new ProgressHandlerEvent(ProgressHandlerEvent.TYPE_PROGRESS_HANDLER, event));
        }

        private function securityErrorHandler(event:SecurityErrorEvent):void {
        	this.dispatchEvent(new SecurityErrorHandlerEvent(SecurityErrorHandlerEvent.TYPE_SECURITY_ERROR_HANDLER, event));
        }
    }
}