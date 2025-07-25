package com.akamai.events
{
	import flash.events.Event;

	/**
	 * The AkamaiNotificationEvent class provides notification that the AkamaiConnection class
	 * has reached certain states or conditions. These conditions are characterized by the
	 * common attribute that the event itself carries no parameters. Typically, once the notification
	 * has been received, other properties on the AkamaiConnection class are then queried for
	 * additional information. 
	 * 
	 * @see com.akamai.AkamaiConnection
	 */
	public class AkamaiNotificationEvent extends Event
	{

		/** 
		 * The AkamaiNotificationEvent.BANDWIDTH constant defines the value of the AkamaiNotificationEvent's
		 * <code>type</code> property, which indicates the class
		 * has completed a bandwidth estimate and that the <code>bandwidth</code> and <code>latency</code>
		 * properties of the AkamaiConnection will now hold the measured values.
		 * 
		 * @see com.akamai.AkamaiConnection#bandwidth
		 * @see com.akamai.AkamaiConnection#latency
		 * 
		 */
		public static const BANDWIDTH:String = "bandwidth";

		/** 
		 * The AkamaiNotificationEvent.CONNECTED constant defines the value of the AkamaiNotificationEvent's
		 * <code>type</code> property, which indicates the class
		 * has successfully connected to the Akamai Flash Video Streaming Service. Note that if
		 * <code>createStream</code> was set true on the class, then this event will be delayed until the 
		 * NetStream has been created.
		 * 
		 * @see com.akamai.AkamaiConnection#createStream
		 * @see com.akamai.AkamaiConnection#netConnection
		 */
		public static const CONNECTED:String = "connected";

		/** 
		 * The AkamaiNotificationEvent.END_OF_STREAM constant defines the value of the AkamaiNotificationEvent's
		 * <code>type</code> property, which indicates that the end of the stream has been reached. Note that determination
		 * of this end is based upon an analysis of the NetStream events  (specifically NetStream.Play.Stop
		 * followed by NetStream.Buffer.Empty). This method is used, and this event provided, in order for the class
		 * to be compatible with FCS 1.7x servers, which do not issue the NetStream.onPlayStatus.Complete event. This 
		 * event is a more robust indicator that end of stream has been reached, and it can be accessed via listening to the 
		 * AkamaiStatusEvent.NETSTREAM_PLAYSTATUS event. Always use AkamaiStatusEvent.NETSTREAM_PLAYSTATUS as an indicator 
		 * that the end of stream has been reached if you know that you are connecting to FMS 2.x servers.
		 * 
		 * @see com.akamai.events.AkamaiStatusEvent
		 */
		public static const END_OF_STREAM:String = "end";

		/** 
		 * The AkamaiNotificationEvent.STREAM_LENGTH constant defines the value of the AkamaiNotificationEvent's
		 * <code>type</code> property, which indicates the class
		 * has completed a stream length request and that the <code>streamLength</code> and <code>streamLengthAsTimeCode</code>
		 * properties of the AkamaiConnection will now hold valid values.
		 * 
		 * @see com.akamai.AkamaiConnection#getStreamLength
		 * @see com.akamai.AkamaiConnection#streamLength
		 * @see com.akamai.AkamaiConnection#streamLengthAsTimeCode
		 * 
		 */
		public static const STREAM_LENGTH:String = "streamlength";

		/** 
		 * The AkamaiNotificationEvent.SUBSCRIBED constant  defines the value of the AkamaiNotificationEvent's
		 * <code>type</code> property, which indicates the class has successfully subscribed to a live stream.
		 * 
		 * @see com.akamai.AkamaiConnection#isLive
		 * @see com.akamai.AkamaiConnection#play
		 */
		public static const SUBSCRIBED:String = "subscribed";

		/** 
		 * The AkamaiNotificationEvent.UNSUBSCRIBED constant defines the value of the AkamaiNotificationEvent's
		 * <code>type</code> property, which indicates the class has unsubscribed from a live stream.
		 * This may happen because the <code>unsubscribe</code> method was called by the parent or because the 
		 * publisher of the stream ceased publication. In the latter case, the AkamaiConnection class will automatically
		 * attempt to resubscribe to the live stream. It will do this until the <code>liveStreamMasterTimeout</code> period
		 * has been exceeded, after which it will dispatch an error event.
		 * 
		 * @see com.akamai.AkamaiConnection#isLive
		 * @see com.akamai.AkamaiConnection#play
		 * @see com.akamai.AkamaiConnection#unsubscribe
		 * @see com.akamai.AkamaiConnection#liveStreamMasterTimeout
		 */
		public static const UNSUBSCRIBED:String = "unsubscribed";

		/** 
		 * The AkamaiNotificationEvent.SUBSCRIBE_ATTEMPT constant defines the value of the AkamaiNotificationEvent's
		 * <code>type</code> property, which indicates the class is making a new attempt to subscribe to a live stream.
		 * This will occur immediately after the first <code>play</code> request for a live stream, as well as after
		 * an AkamaiNotificationEvent.UNSUBSCRIBED event has been issued while the stream was still active.
		 * These resubscription attempts will occur roughly every 30 seconds until the <code>liveStreamMasterTimeout</code> period
		 * has been exceeded, after which an error event will be dispatched.
		 * 
		 * @see com.akamai.AkamaiConnection#isLive
		 * @see com.akamai.AkamaiConnection#play
		 * @see com.akamai.AkamaiConnection#unsubscribe
		 * @see com.akamai.AkamaiConnection#liveStreamMasterTimeout
		 */
		public static const SUBSCRIBE_ATTEMPT:String = "subscribeattempt";

		/**
		 * Constructor. Normally called by the AkamaiConnection class, not used in application code.
		 * 
		 * @param type The event type; indicates the action that caused the event. 
		 */
		public function AkamaiNotificationEvent(type:String) 
		{
			super(type);
		}

		/** 
		 * @private 
		 * Override the inherited clone() method.
		 */
		override public function clone():Event 
		{
			return new AkamaiNotificationEvent(type);
		}
	}
}