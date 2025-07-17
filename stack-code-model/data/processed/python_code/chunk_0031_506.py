package com.as3long.node.native.http 
{
	/**
	 * ...
	 * @author lonnyhuang
	 */
	public class Server 
	{
		private var nativeServer:*;
		/**
		 * 最大请求头数目限制, 默认 1000 个. 如果设置为0, 则代表不做任何限制.
		 */
		public var maxHeadersCount:Number = 1000;
		
		/**
		 * 默认2分钟
		 */
		public var timeout:Number = 1200000;
		
		public function Server(nativeServer:*)
		{
			this.nativeServer = nativeServer;
		}
		
		public function setTimeout(msecs:Number, callback:Function):*
		{
			return nativeServer.setTimeout(msecs, callback);
		}
		
		public function listen(...args):*
		{
			return nativeServer.listen.apply(nativeServer, args);
		}
		
		public function close(callback):*
		{
			return nativeServer.close(callback);
		}
		
	}

}