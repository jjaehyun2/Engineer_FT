package com.as3long.node.native.http 
{
	/**
	 * ...
	 * @author lonnyhuang
	 */
	public class Http 
	{
		
		public function Http() 
		{
			
		}
		
		/**
		 * Node维护几个连接每个服务器的HTTP请求。 这个函数允许后台发布请求。
		 * @param	options 
		 *  host：请求发送到的服务器的域名或IP地址。默认为'localhost'。
		 *	hostname：用于支持url.parse()。hostname比host更好一些
		 *	port：远程服务器的端口。默认值为80。
		 *	localAddress：用于绑定网络连接的本地接口。
		 *	socketPath：Unix域套接字（使用host:port或socketPath）
		 *	method：指定HTTP请求方法的字符串。默认为'GET'。
		 *	path：请求路径。默认为'/'。如果有查询字符串，则需要包含。例如'/index.html?page=12'。请求路径包含非法字符时抛出异常。目前，只否决空格，不过在未来可能改变。
		 *	headers：包含请求头的对象。
		 *	auth：用于计算认证头的基本认证，即'user:password'
		 *	agent：控制Agent的行为。当使用了一个Agent的时候，请求将默认为Connection: keep-alive。可能的值为：
		 *	undefined（默认）：在这个主机和端口上使用[全局Agent][]。
		 *	Agent对象：在Agent中显式使用passed。
		 *	false：在对Agent进行资源池的时候，选择停用连接，默认请求为：Connection: close。
		 *	keepAlive：{Boolean} 保持资源池周围的套接字在未来被用于其它请求。默认值为false
		 *	keepAliveMsecs：{Integer} 当使用HTTP KeepAlive的时候，通过正在保持活动的套接字发送TCP KeepAlive包的频繁程度。默认值为1000。仅当keepAlive被设置为true时才相关。
		 * @param	callback
		 * @return
		 */
		public static function request(options:*, callback:Function):ClientRequest
		{
			var clientRequest:ClientRequest = new ClientRequest(nativeHttp.request(options, callback));
			
			return clientRequest;
		}
		
		public static function get(options, callback):ClientRequest
		{
			var clientRequest:ClientRequest = new ClientRequest(nativeHttp.get(options, callback));
			
			return clientRequest;
		}
		
		public static function createServer(requestListener:Function):Server
		{
			var server:Server = new Server(nativeHttp.createServer(function(req:*, res:*):void {
				$Debug.outObject(req);
				requestListener(req, new ServerResponse(res));
			}));
			return server;
		}
		
	}

}

var nativeHttp:* = require("http");