package dom.tidesdk.network
{
	/**
	 * <p>No description provided.</p>
	 */
	public class TInterface
	{
		//
		// METHODS
		//

		/**
		 * <p>Return the display name of this interface.</p>
		 * 
		 * @return String   
		 */
		public function getDisplayName():String { return ""; }

		/**
		 * <p>Return the IP addresso of this interface.</p>
		 * 
		 * @return Ti.Network.IPAddress   
		 */
		public function getIPAddress():TIPAddress { return null; }

		/**
		 * <p>Get the name of this interface.</p>
		 * 
		 * @return String   
		 */
		public function getName():String { return ""; }

		/**
		 * <p>Return the subnet mask of this interface as a
		 * Network.IPAddress object.</p>
		 * 
		 * @return Ti.Network.IPAddress   
		 */
		public function getSubnetMask():TIPAddress { return null; }

		/**
		 * <p>Return true if this interface supports IPv4 and
		 * false otherwise.</p>
		 * 
		 * @return Boolean   
		 */
		public function supportsIPv4():Boolean { return false; }

		/**
		 * <p>Return true if this interface supports IPv6 and
		 * false otherwise.</p>
		 * 
		 * @return Boolean   
		 */
		public function supportsIPv6():Boolean { return false; }

		public function TInterface() {}
	}
}