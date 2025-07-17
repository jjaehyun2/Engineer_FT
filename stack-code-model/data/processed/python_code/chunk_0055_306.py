package dom.tidesdk.notification
{
	/**
	 * <p>A module for displaying desktop notifications.
	 * TideSDK allows you to display notifications from
	 * your desktop apps using Growl on OS X, Snarl on
	 * Windows and libnotify on Linux. In the event of a
	 * notification provider being absent, notifications
	 * are shown using HTML/CSS.</p>
	 * 
	 *   <p>Please refer to the code example below</p>
	 * 
	 *   <pre><code>//Create a callback function for the
	 * notification var doSomething = function() {    
	 * //Do something! }  //Creating a notification and
	 * displaying it. var notification = <a
	 * href="#!/api/Ti.Notification-method-createNotification"
	 * rel="Ti.Notification-method-createNotification"
	 * class="docClass">Ti.Notification.createNotification</a>({
	 *     'title' : 'Notification from App',    
	 * 'message' : 'Click here for updates!',    
	 * 'timeout' : 10,     'callback' : doSomething,    
	 * 'icon' : 'app://images/notificationIcon.png'      
	 *   });  notification.show(); </code></pre>
	 * 
	 *   <p>Not all platforms support a callback function
	 * or specifying a custom timeout.  <br/> The
	 * notification icon should be always be referenced
	 * by an absolute app://, ti:// or file:// URL.</p>
	 */
	public class TNotificationBase
	{
		//
		// METHODS
		//

		/**
		 * <p>Create a new Notification object.</p>
		 * 
		 * @return Ti.UI.Notification   
		 */
		public function createNotification():TNotificationBase { return null; }

		public function TNotificationBase() {}
	}
}