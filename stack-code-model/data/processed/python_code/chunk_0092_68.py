package com.wm.deal.cmd 
{
	import com.wm.deal.cmd.core.BaseCmdHandler;
	import com.wm.net.py.ClientConnect;
	import com.wm.net.py.Packet;
	/**
	 * ...
	 * @author wmTiger
	 */
	public class CmdWelcome extends BaseCmdHandler
	{
		
		public function CmdWelcome() 
		{
			
		}
		
		override public function cmdHandler(p:Packet = null):void
		{
			//Log.info("===>pk.cmdId: "+pk.cmdId+"pk.data: "+ pk.data);
		}
		
		override public function sendCmd(params:Array = null):void
		{
			// 这里的_cmdId 可以手动设置，不过不要覆盖_cmdId
			var p:Packet = new Packet(_cmdId);// s
			if (params == null) 
			{
				p.data = ['hello'];
			}
			else
			{
				p.data = params;
			}
			
			_clientConn.send(p);
		}
		
	}

}