package com.smartfoxserver.redbox.exceptions
{
	/**
	 * A RedBox exception.
	 * 
	 * @author	The gotoAndPlay() Team
	 * 			{@link http://www.smartfoxserver.com}
	 * 			{@link http://www.gotoandplay.it}
	 */
	public class MyUserPropsNotSetException extends Error
	{
		/**
		 * Thrown when the "myUser" properties in the SmartFoxClient instance are not set.
		 * The RedBox classes make an extensive use of the <i>SmartFoxClient.myUserId</i> and <i>SmartFoxClient.myUserName</i> properties. In case of custom login, these two properties are not set automatically by the SmartFoxClient instance.
		 * In this case, when one of the main RedBox classes is instantiated, the exception is raised.
		 * 
		 * @example	The following example shows how to handle the "MyUserPropsNotSetException" exception.
		 * 			<code>
		 * 			try
		 * 			{
		 * 				var avChatMan:AVChatManager = new AVChatManager(smartFox, "127.0.0.1", true)
		 * 			}
		 * 			catch (err:MyUserPropertiesNotSetException)
		 * 			{
		 * 				trace (err.message)
		 * 			}
		 * 			</code>
		 */
		public function MyUserPropsNotSetException()
		{
			var message:String = "SmartFoxClient.myUserId and/or SmartFoxClient.myUserName properties not set: in case of custom login they must be set manually to the actual server values"
			super(message)
		}
	}
}