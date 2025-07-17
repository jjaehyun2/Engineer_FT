package com.wm.deal.cmd.core {
	import com.wm.net.py.ClientConnect;
	import flash.utils.Dictionary;
	/**
	 * ...
	 * @author wmTiger
	 */
	public class CmdFactory 
	{
		public static var handlers:Dictionary = new Dictionary(true);
		
		public function CmdFactory() 
		{
			
		}
		
		/**
		 * 添加一个cmd到池子中，准备复用
		 * @param	cmdId		命令id
		 * @param	conn		链接的客户端
		 * @param	cmdCls		具体的命令类
		 * @return
		 */
		public static function addCmd(cmdId:int, conn:ClientConnect, cmdCls:*):ICmdHandler
		{
			var cmdObj:Object = CmdFactory.handlers[conn];
			if (cmdObj == null) 
			{
				cmdObj = { };
			}
			if (!(cmdId in cmdObj)) 
			{
				cmdObj[cmdId] = null;
			}
			var handler:ICmdHandler = cmdObj[cmdId];
			if (handler == null) 
			{
				handler = new cmdCls();
			}
			handler.cmdId = cmdId;
			handler.clientConn = conn;
			
			cmdObj[cmdId] = handler;
			CmdFactory.handlers[conn] = cmdObj;
			return handler;
		}
		
		public static function removeConn(conn:ClientConnect):void
		{
			CmdFactory.handlers[conn] = null;
			delete CmdFactory.handlers[conn];
		}
		
	}

}