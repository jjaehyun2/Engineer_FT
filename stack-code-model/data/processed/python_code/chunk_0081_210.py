package com.smartfoxserver.redbox.events
{
	import it.gotoandplay.smartfoxserver.SFSEvent;
	
	/**
	 * RedBoxChatEvent is the class representing all events dispatched by the RedBox's {@link AVChatManager} instance.
	 * The RedBoxChatEvent extends the SFSEvent class, which in turn extends the flash.events.Event class.
	 * SFSEvent also provides a public property called {@code params} of type {@code Object} that can contain any number of parameters.
	 * 
	 * @usage	Please refer to the specific events for usage examples and {@code params} object content.
	 * 
	 * @author	The gotoAndPlay() Team
	 * 			{@link http://www.smartfoxserver.com}
	 * 			{@link http://www.gotoandplay.it}
	 */
	public class RedBoxChatEvent extends SFSEvent
	{
		/**
		 * Dispatched when the connection to Red5 server has been established.
		 * This event is dispatched after the {@link AVChatManager} is instantiated or when the {@link AVChatManager#initAVConnection} method is called.
		 * The connection to Red5 must be available before any method related to a/v streaming is called.
		 * 
		 * No parameters are provided.
		 * 
		 * @example	The following example shows how to handle the "onAVConnectionInited" event.
		 * 			<code>
		 * 			var red5IpAddress:String = "127.0.0.1"
		 * 			var avChatMan:AVChatManager = new AVChatManager(smartFox, red5IpAddress)
		 * 			
		 * 			avChatMan.addEventListener(RedBoxChatEvent.onAVConnectionInited, onAVConnectionInited)
		 * 			
		 * 			function onAVConnectionInited(evt:RedBoxChatEvent):void
		 * 			{
		 * 				trace("Red5 connection established")
		 * 			}
		 * 			</code>
		 * 
		 * @see		AVChatManager#initAVConnection
		 */
		public static const onAVConnectionInited:String = "onAVConnectionInited"
		
		
		/**
		 * Dispatched when the connection to Red5 server can't be established.
		 * This event is dispatched when an error or special condition (like "connection closed") occurred in the flash.net.NetConnection object used internally by the {@link AVChatManager} to handle the connection to Red5.
		 * This kind of error is always related to the Red5 server connection, so you should check if the server is running and reachable.
		 * Also check the Red5 logs or console output for more details.
		 * NOTE: when a connection error occurs, all the existing chat sessions (whatever their status is) are stopped.
		 * 
		 * The {@code params} object contains the following parameters.
		 * @param	errorCode:	(<b>String</b>) the description of the error condition; check the "code" property of the NetStatusEvent.info object in the Actionscript 3 Language Reference.
		 * 
		 * @example	The following example shows how to handle a Red5 connection error.
		 * 			<code>
		 * 			avChatMan.addEventListener(RedBoxChatEvent.onAVConnectionError, onAVConnectionError)
		 * 			
		 * 			function onAVConnectionError(evt:RedBoxChatEvent):void
		 * 			{
		 * 				trace("A connection error occurred: " + evt.params.errorCode)
		 * 			}
		 * 			</code>
		 */
		public static const onAVConnectionError:String = "onAVConnectionError"
		
		
		/**
		 * Dispatched when a chat request is sent, but the recipient is not available.
		 * 
		 * The {@code params} object contains the following parameters.
		 * @param	chatSession:	(<b>ChatSession</b>) the same {@link ChatSession} object returned by the AVChatManager instance when the {@link AVChatManager#sendChatRequest} method was called.
		 * 
		 * @example	The following example shows how to handle the "onRecipientMissing" event.
		 * 			<code>
		 * 			avChatMan.addEventListener(RedBoxChatEvent.onRecipientMissing, onRecipientMissing)
		 * 			
		 * 			avChatMan.sendChatRequest(AVChatManager.REQ_TYPE_SEND_RECEIVE, buddyId, true, true)
		 * 			
		 * 			function onRecipientMissing(evt:RedBoxChatEvent):void
		 * 			{
		 * 				trace ("Request '" + evt.params.chatSession.id + "' error: the recipient is not available!")
		 * 			}
		 * 			</code>
		 * 
		 * @see		ChatSession
		 * @see		AVChatManager#sendChatRequest
		 */
		public static const onRecipientMissing:String = "onRecipientMissing"
		
		
		/**
		 * Dispatched when a chat request is sent, but a mutual request has already been sent by the recipient.
		 * 
		 * The {@code params} object contains the following parameters.
		 * @param	chatSession:	(<b>ChatSession</b>) the same {@link ChatSession} object returned by the AVChatManager instance when the {@link AVChatManager#sendChatRequest} method was called.
		 * 
		 * @example	The following example shows how to handle the "onDuplicateRequest" event.
		 * 			<code>
		 * 			avChatMan.addEventListener(RedBoxChatEvent.onDuplicateRequest, onDuplicateRequest)
		 * 			
		 * 			avChatMan.sendChatRequest(AVChatManager.REQ_TYPE_SEND_RECEIVE, buddyId, true, true)
		 * 			
		 * 			function onDuplicateRequest(evt:RedBoxChatEvent):void
		 * 			{
		 * 				trace ("Request '" + evt.params.chatSession.id + "' error: a mutual request has already been sent by the recipient!")
		 * 			}
		 * 			</code>
		 * 
		 * @see		ChatSession
		 * @see		AVChatManager#sendChatRequest
		 */
		public static const onDuplicateRequest:String = "onDuplicateRequest"
		
		
		/**
		 * Dispatched when an a/v chat request is received.
		 * 
		 * The {@code params} object contains the following parameters.
		 * @param	chatSession:	(<b>ChatSession</b>) the {@link ChatSession} object created by the AVChatManager instance when the request is received.
		 * 
		 * @example	The following example shows how to handle an incoming chat request.
		 * 			<code>
		 * 			avChatMan.addEventListener(RedBoxChatEvent.onChatRequest, onChatRequest)
		 * 			
		 * 			// Another user sends a chat request...
		 * 			
		 * 			function onChatRequest(evt:RedBoxChatEvent):void
		 * 			{
		 * 				var chatData:ChatSession = evt.params.chatSession
		 * 				
		 * 				trace ("Chat request received ->", chatData.toString())
		 * 				
		 * 				// Enable "accept" and "decline" buttons
		 * 				...
		 * 			}
		 * 			</code>
		 * 
		 * @see		ChatSession
		 * @see		AVChatManager#sendChatRequest
		 */
		public static const onChatRequest:String = "onChatRequest"
		
		
		/**
		 * Dispatched when an a/v chat request has been refused by the recipient.
		 * 
		 * The {@code params} object contains the following parameters.
		 * @param	chatSession:	(<b>ChatSession</b>) the {@link ChatSession} object created by the AVChatManager instance when the request was sent.
		 * 
		 * @example	The following example shows how to handle a chat request refusal.
		 * 			<code>
		 * 			avChatMan.addEventListener(RedBoxChatEvent.onChatRefused, onChatRefused)
		 * 			
		 * 			// The recipient refuses the chat request...
		 * 			
		 * 			function onChatRefused(evt:RedBoxChatEvent):void
		 * 			{
		 * 				var chatData:ChatSession = evt.params.chatSession
		 * 				
		 * 				trace ("Chat request refused by user", chatData.mateName)
		 * 				
		 * 				// Show message and reset start/stop chat buttons states
		 * 				...
		 * 			}
		 * 			</code>
		 * 
		 * @see		ChatSession
		 * @see		AVChatManager#refuseChatRequest
		 */
		public static const onChatRefused:String = "onChatRefused"
		
		
		/**
		 * Dispatched when an a/v chat session is started, after the recipient accepted the requester's invitation.
		 * This event is fired on both the requester and the recipient clients.
		 * In order to display the connected users' a/v streams, the {@link ChatSession#myStream} and {@link ChatSession#mateStream} properties should be used. These two properties are set depending on the request type and on who is the requester.
		 * Check the following table:
		 * <img src="../img/img1.jpg"/>
		 * 
		 * 
		 * The {@code params} object contains the following parameters.
		 * @param	chatSession:	(<b>ChatSession</b>) the {@link ChatSession} object created by the AVChatManager instance when the request was sent/received.
		 * 
		 * @example	The following example shows how to handle a chat starting.
		 * 			<code>
		 * 			avChatMan.addEventListener(RedBoxChatEvent.onChatStarted, onChatStarted)
		 * 			
		 * 			// I'm the recipient accepting the chat request...
		 * 			avChatMan.acceptChatRequest(chatSessionId)
		 * 			
		 * 			function onChatStarted(evt:RedBoxChatEvent):void
		 * 			{
		 * 				var chatData:ChatSession = evt.params.chatSession
		 * 				
		 * 				var myStream:NetStream = chatData.myStream
		 * 				var mateStream:NetStream = chatData.mateStream
		 * 				
		 * 				// Attach streams to Video objects on stage
		 * 				...
		 * 			}
		 * 			</code>
		 * 
		 * @see		ChatSession
		 * @see		AVChatManager#acceptChatRequest
		 */
		public static const onChatStarted:String = "onChatStarted"
		
		
		/**
		 * Dispatched when an a/v chat session is stopped.
		 * This event is not fired on the client of the user who stopped the chat session, but only on his/her mate's client.
		 * 
		 * The {@code params} object contains the following parameters.
		 * @param	chatSession:	(<b>ChatSession</b>) the {@link ChatSession} object created by the AVChatManager instance when the request was sent/received.
		 * 
		 * @example	The following example shows how to handle a chat being stopped.
		 * 			<code>
		 * 			avChatMan.addEventListener(RedBoxChatEvent.onChatStopped, onChatStopped)
		 * 			
		 * 			avChatMan.stopChat(chatSessionId)
		 * 			
		 * 			function onChatStopped(evt:RedBoxChatEvent):void
		 * 			{
		 * 				var chatData:ChatSession = evt.params.chatSession
		 * 				
		 * 				// Detach streams from Video objects on stage
		 * 				...
		 * 			}
		 * 			</code>
		 * 
		 * @see		ChatSession
		 * @see		AVChatManager#stopChat
		 */
		public static const onChatStopped:String = "onChatStopped"
		
		//-----------------------------------------------------------------------------------------------------
		
		
		/**
		 *	RedBoxChatEvent class constructor.
		 *
		 *	@param type: the event's type.
		 *	@param params: an object containing the event's parameters.
		 *	
		 *	@exclude
		 */
		public function RedBoxChatEvent(type:String, params:Object = null)
		{
			super(type, params)
		}
	}
}