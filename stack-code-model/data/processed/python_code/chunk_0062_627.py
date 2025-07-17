package Beetle.NetPackage
{
	/**
	 * Copyright © henryfan 2013
	 * Created by henryfan on 13-7-30.
	 * homepage:www.ikende.com
	 * email:henryfan@msn.com
	 */
	public class NetClientHandler implements INetClientHandler
	{
		public function NetClientHandler(receive:Function,error:Function,disposed:Function,connected:Function)
		{
			OnReceive = receive;
			OnError = error;
			OnDisposed = disposed;
			OnConnected = connected;
		}
		
		public var OnReceive:Function;
		
		public var OnError:Function;
		
		public var OnDisposed:Function;
		
		private var OnConnected:Function;
		
		public function ClientReceive(client:NetClient, msg:Object):void
		{
			if(OnReceive!=null)
				OnReceive(client,msg);
		}
		
		public function ClientError(client:NetClient, err:Error):void
		{
			if(OnError!=null)
				OnError(client,err);
		}
		
		public function ClientDisposed(client:NetClient):void
		{
			if(OnDisposed!=null)
				OnDisposed(client);
				
		}
		public function  ClientConnected(client:NetClient):void
		{
			if(OnConnected!=null)
				OnConnected(client);
		}
	}
}