package framework.core.net
{
	import flash.net.Socket;
	
	import mx.core.UIComponent;

	public class SocketUpdater extends UIComponent
	{
		// ================================================================= //
		//                           VARIABLES                               //
		// ================================================================= //
		protected var socket:Socket = new Socket();
		
		public function SocketUpdater()
		{
			super();
		}
		
		
		
	}
}