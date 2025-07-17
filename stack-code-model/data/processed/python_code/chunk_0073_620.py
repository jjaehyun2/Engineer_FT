package dom.tidesdk.network
{
	/**
	 * <p>An object representing a TCP client socket
	 * connection. A simple implementation of connecting
	 * to a host has been shown below.</p>
	 * 
	 *   <pre><code>//Create the connection. var socket =
	 * <a href="#!/api/Ti.Network-method-createTCPSocket"
	 * rel="Ti.Network-method-createTCPSocket"
	 * class="docClass">Ti.Network.createTCPSocket</a>("127.0.0.1",
	 * 8080); socket.connect();  //The onReadComplete
	 * function below ensures that the //read operation
	 * is completed and all bytes have been received. 
	 * socket.onReadComplete(function(data) {       
	 * alert(data);    }); </code></pre>
	 */
	public class TTCPSocket
	{
		//
		// METHODS
		//

		/**
		 * <p>Close this Network.TCPSocket connection. If
		 * there is no open connection then do nothing.
		 * Return true if the connection was closed and false
		 * otherwise.</p>
		 * 
		 * @return Boolean   
		 */
		public function close():Boolean { return false; }

		/**
		 * <p>Connect the Socket object to the host specified
		 * during creation. The connection will be made
		 * asynchronously. Use onError to detect
		 * failures.</p>
		 */
		public function connect():void {}

		/**
		 * <p>Check whether the Socket is closed.</p>
		 * 
		 * @return Boolean   
		 */
		public function isClosed():Boolean { return false; }

		/**
		 * <p>Set the callback that will be fired when the
		 * Socket encounters an error.</p>
		 * 
		 * @param onError  Function to be called when an error happens. 
		 */
		public function onError(onError:Function):void {}

		/**
		 * <p>Set a callback that will be fired when data is
		 * received on the Socket.</p>
		 * 
		 * @param onRead  Function to be called when data is received. 
		 */
		public function onRead(onRead:Function):void {}

		/**
		 * <p>Set the callback function that will be fired
		 * when a read finishes. A read is considered
		 * finished if some bytes have been read and a
		 * subsequent call to read returns zero bytes.</p>
		 * 
		 * @param onReadComplete  Function be called when a read completes. 
		 */
		public function onReadComplete(onReadComplete:Function):void {}

		/**
		 * <p>Set the callback that will be fired when an
		 * operation times out on the Socket.</p>
		 * 
		 * @param onTimeout  Function to be called when an operation times out. 
		 */
		public function onTimeout(onTimeout:Function):void {}

		/**
		 * <p>Set a callback that will be fired when data is
		 * written on the Socket.</p>
		 * 
		 * @param onWrite  Function to be called when data is written. 
		 */
		public function onWrite(onWrite:Function):void {}

		/**
		 * <p>Write data to the Socket's connection, if
		 * open.</p>
		 * 
		 * @param data  The data to write to the connection. 
		 */
		public function write(data:*):void {}

		public function TTCPSocket() {}
	}
}