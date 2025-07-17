package dom.tidesdk.network
{
	/**
	 * <p>An object representing an IRC client
	 * connection. [DEPRECATED]</p>
	 */
	public class TIRCClient
	{
		//
		// PROPERTIES
		//

		/**
		 * <p>The connected property of an IRCClient
		 * object</p>
		 */
		public var connected:Boolean;

		//
		// METHODS
		//

		/**
		 * <p>Connects an IRC to the host specified during
		 * creation of the IRCClient object</p>
		 * 
		 * @param hostname  the hostname 
		 * @param port  the port 
		 * @param nick  the users nickname 
		 * @param name  the users full name 
		 * @param user  the users login name 
		 * @param pass  the users password 
		 * @param callback  a callback function to recieve IRC events. 
		 */
		public function connect(hostname:String, port:int, nick:String, name:String, user:String, pass:String, callback:Function):void {}

		/**
		 * <p>Disconnects an IRC connection</p>
		 */
		public function disconnect():void {}

		/**
		 * <p>Returns the nick name for the connection</p>
		 */
		public function getNick():void {}

		/**
		 * <p>Returns a list of users for the channel</p>
		 * 
		 * @return Array   
		 */
		public function getUsers():Array { return null; }

		/**
		 * <p>Checks whether a user has OP status</p>
		 * 
		 * @return Boolean   
		 */
		public function isOp():Boolean { return false; }

		/**
		 * <p>Checks whether a user has VOICE status</p>
		 * 
		 * @return Boolean   
		 */
		public function isVoice():Boolean { return false; }

		/**
		 * <p>Joins a channel</p>
		 * 
		 * @param channel  channel to join to 
		 */
		public function join(channel:String):void {}

		/**
		 * <p>Sends data to the IRC connection</p>
		 * 
		 * @param channel  the channel to send the data to 
		 * @param message  message to send 
		 */
		public function send(channel:String, message:String):void {}

		/**
		 * <p>Sets the nick name for the connection</p>
		 * 
		 * @param nick  nickname to use 
		 */
		public function setNick(nick:String):void {}

		/**
		 * <p>Leaves a channel</p>
		 * 
		 * @param channel  channel to leave 
		 */
		public function unjoin(channel:String):void {}

		public function TIRCClient() {}
	}
}