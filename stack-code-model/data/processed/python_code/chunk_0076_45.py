package com.arxterra.utils
{
	import com.arxterra.controllers.CameraManager;
	import com.arxterra.controllers.SessionManager;
	import com.arxterra.interfaces.IPermissionsChecker;
	import com.smartfoxserver.v2.SmartFox;
	import com.smartfoxserver.v2.core.SFSEvent;
	import com.smartfoxserver.v2.entities.Room;
	import com.smartfoxserver.v2.entities.User;
	import com.smartfoxserver.v2.entities.variables.SFSUserVariable;
	import com.smartfoxserver.v2.entities.variables.UserVariable;
	import com.smartfoxserver.v2.redbox.BaseAVManager;
	import com.smartfoxserver.v2.redbox.data.LiveCast;
	import com.smartfoxserver.v2.redbox.events.RedBoxCastEvent;
	import com.smartfoxserver.v2.redbox.exceptions.InvalidParamsException;
	import com.smartfoxserver.v2.redbox.exceptions.NoAVConnectionException;
	import com.smartfoxserver.v2.redbox.exceptions.NoRoomJoinedException;
	import com.smartfoxserver.v2.redbox.utils.Constants;
	import com.smartfoxserver.v2.redbox.utils.Logger;
	import com.smartfoxserver.v2.requests.SetUserVariablesRequest;
	
	import flash.net.NetStream;
	
	/**
	 * SmartFoxServer 2X RedBox Audio/Video Broadcast Manager.
	 * This class is responsible for managing audio/video live casts inside the SmartFoxServer Room joined by the user, making it possible to create live web events or a/v conferences.
	 * The AVCastManager handles the live cast publishing/playing to/from the Red5 server.
	 * Unlike the other RedBox classes, the AVCastManager works on a Room basis to leverage the access control and moderation features of SmartFoxServer rooms.
	 * 
	 * <b>NOTE</b>: in the provided examples, <b>avCastMan</b> always indicates an AVCastManager instance.
	 * 
	 * @usage	The most common usages for the <b>AVCastManager</b> class are video conference applications and live webcast applications (for example live online seminars).
	 * 			
	 * 			<i>Video conference</i>
	 * 			In this kind of application, each user publishes his own live stream and subscribes the streams coming from the other users in the same SmartFoxServer Room. The following workflow is suggested.
	 * 			<ol>
	 * 				<li>The current user joins the room where the video conference takes place.</li>
	 * 				<li>The list of currently available streams (or "live casts") is retrieved by means of the <b>getAvailableCasts</b> method (in case the conference is already in progress).
	 * 				Calling this method also enables the reception of the <b>RedBoxCastEvent.LIVE_CAST_PUBLISHED</b> and <b>RedBoxCastEvent.LIVE_CAST_UNPUBLISHED</b> events which notify if another user started or stopped his own stream.</li>
	 * 				<li>Each live cast is subscribed by means of the <b>subscribeLiveCast</b> method and a Video object is displayed on the stage to attach the stream to.
	 * 				When a live cast is published (a new user joins the conference) or stopped (a user leaves the conference), a notification is received by means of the above mentioned events: the stream is subscribed / unsubscribed and displayed on / removed from the stage.</li>
	 * 				<li>The a/v stream for the current user is published by means of the <b>publishLiveCast</b> method and an additional Video object showing the user own camera stream is added on the stage; when the current user publishes his own stream, the other users receive the above mentioned events.</li>
	 * 				<li>To make the current user leave the conference, the <b>unpublishLiveCast</b> method is called. Also changing Room causes the user to leave the conference and the other users to be notified.</li>
	 * 			</ol>
	 * 			<hr />
	 * 			<i>Live webcast</i>
	 * 			In this kind of application, a single user publishes his own live stream and all the other users in the same room subscribe it. The following workflow is suggested.
	 * 			<ol>
	 * 				<li>The publisher joins the Room where the live webcast takes place.</li>
	 * 				<li>The a/v stream for the user is published by means of the <b>publishLiveCast</b> method and a Video object showing the user own camera stream is added on the stage; when the current user publishes his own stream, the other users already in the room receive the <b>RedBoxCastEvent.LIVE_CAST_PUBLISHED</b> event and the stream can be subscribed (see step 4).</li>
	 * 				<li>The webcast spectators join the room and retrieve the list of available streams (one item only if the publisher is already streaming, otherwise the list will be empty).</li>
	 * 				<li>If the live webcast is already started, it can be subscribed by means of the <b>subscribeLiveCast</b> method; otherwise the <b>RedBoxCastEvent.LIVE_CAST_UNPUBLISHED</b> event must be waited for before calling this method.</li>
	 * 				<li>On all the subscribers clients a Video object is displayed on the stage to attach the stream to.</li>
	 * 			</ol>
	 * 
	 * @version	1.0.0 for SmartFoxServer 2X
	 * 
	 * @author	The gotoAndPlay() Team
	 * 			<b>http://www.smartfoxserver.com</b>
	 */
	public class AVCastManagerArx extends BaseAVManager
	{
		//--------------------------------------
		// CLASS CONSTANTS
		//--------------------------------------
		
		private const CAST_USER_VAR:String = "$RB_castId"
		
		//--------------------------------------
		//  PRIVATE VARIABLES
		//--------------------------------------
		
		private var castList:Array;
		private var castListByUser:Array;
		private var myLiveCast:NetStream;
		private var castListRequested:Boolean;
		
		//--------------------------------------
		//  COSTRUCTOR
		//--------------------------------------
		
		/**
		 * AVCastManager contructor.
		 * 
		 * @param	sfs:		the SmartFox API main class instance.
		 * @param	red5Ip:		the Red5 server IP address (include the port number if the default one is not used).
		 * @param	useRTMPT:	connect to Red5 server using the HTTP-tunnelled RTMP protocol (optional, default is <b>false</b>); Red5 must be configured accordingly.
		 * @param	debug:		turn on the debug messages (optional, default is <b>false</b>).
		 *
		 * @example	The following example shows how to instantiate the AVCastManager class.
		 * 			<code>
		 * 			var smartFox:SmartFox = new SmartFox();
		 * 			var red5IpAddress:String = "127.0.0.1";
		 * 			
		 * 			var avCastMan:AVCastManager = new AVCastManager(smartFox, red5IpAddress);
		 * 			</code>
		 */
		public function AVCastManagerArx ( sfs:SmartFox, red5Ip:String, useRTMPT:Boolean = false, debug:Boolean = false )
		{
			super(sfs, red5Ip, useRTMPT, debug);
			
			// Initialize casts list for the current Room
			if (smartFox.lastJoinedRoom != null)
				initCastList();
			
			// Add SmartFoxServer event listeners
			smartFox.addEventListener(SFSEvent.ROOM_JOIN, onRoomJoin);
			smartFox.addEventListener(SFSEvent.USER_VARIABLES_UPDATE, onUserVariablesUpdate);
			smartFox.addEventListener(SFSEvent.USER_EXIT_ROOM, onUserExitRoom);
		}
		
		// -------------------------------------------------------
		// PUBLIC METHODS
		// -------------------------------------------------------
		
		/**
		 * Destroy the AVCastManager instance.
		 * Calling this method causes the interruption of all the playing streams (if any) and the disconnection from Red5.
		 * This method should always be called before deleting the AVCastManager instance.
		 * 
		 * @example	The following example shows how to destroy the AVCastManager instance.
		 * 			<code>
		 * 			avCastMan.destroy();
		 * 			avCastMan = null;
		 * 			</code>
		 */
		override public function destroy():void
		{
			super.destroy();
			
			// Remove SmartFoxServer event listeners
			smartFox.removeEventListener(SFSEvent.ROOM_JOIN, onRoomJoin);
			smartFox.removeEventListener(SFSEvent.USER_VARIABLES_UPDATE, onUserVariablesUpdate);
			smartFox.removeEventListener(SFSEvent.USER_EXIT_ROOM, onUserExitRoom);
			
			// Unpublish outgoing stream
			unpublishLiveCast();
			
			// Unsubscribe all incoming streams
			unsubscribeAllLiveCasts();
			
			castListRequested = false;
			castList = null;
			castListByUser = null;
			
			// Disconnect from Red5 server
			if (netConn.connected)
				netConn.close();
			
			Logger.log("AVCastManager instance destroyed");
		}
		
		/**
		 * Retrieve the list of available live broadcasts for the current Room.
		 * The list is populated by the <b>AVCastManager</b> class as soon as it is instantiated and each time a new Room is joined.
		 * When this method is called, the <b>RedBoxCastEvent.LIVE_CAST_PUBLISHED</b> and <b>RedBoxCastEvent.LIVE_CAST_UNPUBLISHED</b> events dispatching is enabled, in order to be notified when users in the current Room start/stop streaming.
		 * In order to turn off events notification, the <b>stopPublishNotification</b> method should be called.
		 * 
		 * @return	An array of <b>LiveCast</b> objects.
		 * 
		 * @example	The following example shows how to loop through the list of live casts available for the current Room.
		 * 			<code>
		 * 			for each (var liveCast:LiveCast in avCastMan.getAvailableCasts())
		 * 			{
		 * 				// Subscribe live cast
		 * 				var stream:NetStream = avCastMan.subscribeLiveCast(liveCast.id);
		 * 				
		 * 				// Display a/v stream on stage
		 * 				...
		 * 			}
		 * 			</code>
		 * 
		 * @see		LiveCast
		 * @see		#stopPublishNotification
		 */
		public function getAvailableCasts():Array
		{
			castListRequested = true;
			
			return castList;
		}
		
		/**
		 * Stop receiving live cast published/unpublished events.
		 * 
		 * @see		#getAvailableCasts
		 */
		public function stopPublishNotification():void
		{
			castListRequested = false;
		}
		
		/**
		 * Subscribe a live cast to receive its audio/video stream.
		 * 
		 * @param	castId:	(<b>String</b>) the id of the <b>LiveCast</b> object to be subscribed.
		 * 
		 * @return	A flash.net.NetStream object.
		 * 
		 * @throws	NoAVConnectionException if the connection to Red5 is not available.
		 * 
		 * @example	The following example shows how to subscribe a live cast when a publishing notification is received.
		 * 			<code>
		 * 			avCastMan.addEventListener(RedBoxCastEvent.LIVE_CAST_PUBLISHED, onLiveCastPublished);
		 * 			
		 * 			// A user publishes his own live cast...
		 * 			
		 * 			function onLiveCastPublished(evt:RedBoxCastEvent):void
		 * 			{
		 * 				var liveCast:LiveCast = evt.params.liveCast;
		 * 				
		 * 				// Subscribe live cast
		 * 				var stream:NetStream = avCastMan.subscribeLiveCast(liveCast.id);
		 * 				
		 * 				// Display a/v stream on stage
		 * 				...
		 * 			}
		 * 			</code>
		 * 
		 * @see		#unsubscribeLiveCast
		 * @see		NoAVConnectionException
		 * @see		flash.net.NetStream
		 */
		public function subscribeLiveCast(castId:String):NetStream
		{
			// Check Red5 connection availability
			if (!netConn.connected)
				throw new NoAVConnectionException(Constants.ERROR_NO_CONNECTION + " [subscribeLiveCast method]");
			
			//------------------------------
			
			if (castList != null && castList[castId] != null)
			{
				var liveCast:LiveCast = castList[castId];
				
				var stream:NetStream = new NetStream(netConn);
				stream.play(liveCast.id);
				
				liveCast.setStream(stream);
				
				return liveCast.stream;
			}
			
			return null;
		}
		
		/**
		 * Unsubscribe a live cast to stop receiving its audio/video stream.
		 * <b>NOTE</b>: when a user stops his own stream or leaves the current Room / disconnects from SmartFoxServer while his stream is in progress, the <b>AVCastManager</b> class automatically unsubscribes the live cast before dispatching the <b>RedBoxCastEvent.LIVE_CAST_UNPUBLISHED</b> event.
		 * 
		 * @param	castId:	(<b>String</b>) the id of the <b>LiveCast</b> object to be unsubscribed.
		 * 
		 * @example	The following example shows how to unsubscribe a live cast.
		 * 			<code>
		 * 			avCastMan.unsubscribeLiveCast(liveCast.id);
		 * 			</code>
		 * 
		 * @see		#subscribeLiveCast
		 */
		public function unsubscribeLiveCast(castId:String):void
		{
			if (castList != null && castList[castId] != null)
			{
				var liveCast:LiveCast = castList[castId];
				
				// Close incoming stream
				if (liveCast.stream != null)
				{
					liveCast.stream.close();
					liveCast.setStream(null);
				}
			}
		}
		
		/**
		 * Unsubscribe all currently subscribed live casts.
		 * 
		 * @see		#unsubscribeLiveCast
		 */
		public function unsubscribeAllLiveCasts():void
		{
			if (castList != null)
			{
				for each (var liveCast:LiveCast in castList)
				unsubscribeLiveCast(liveCast.id);
			}
		}
		
		/**
		 * Start broadcasting the current user's live stream.
		 * Calling this method causes the <b>RedBoxCastEvent.LIVE_CAST_PUBLISHED</b> event to be fired on the other users clients.
		 * Audio and video recording mode/quality should be set before calling this method. In order to alter these settings, please refer to the flash.media.Microphone and flash.media.Camera classes documentation.
		 * Also, the user must join a Room before calling this method.
		 * 
		 * @param	enableCamera:		enable video live streaming; default value is <b>true</b>.
		 * @param	enableMicrophone:	enable audio live streaming; default value is <b>true</b>.
		 * 
		 * @return	The flash.net.NetStream object representing the user's outgoing stream.
		 * 
		 * @sends	RedBoxCastEvent#LIVE_CAST_PUBLISHED
		 * 
		 * @throws	NoAVConnectionException if the connection to Red5 is not available.
		 * @throws	InvalidParamsException if both <i>enableCamera</i> and <i>enableMicrophone</i> parameters are set to <b>false</b>.
		 * @throws	NoRoomJoinedException if the current user didn't join a Room before calling this method.
		 * 
		 * @example	The following example shows how to publish the current user's live stream.
		 * 			<code>
		 * 			avCastman.publishLiveCast(true, true);
		 * 			</code>
		 * 
		 * @see		#unpublishLiveCast
		 * @see		RedBoxCastEvent#LIVE_CAST_PUBLISHED
		 * @see		NoAVConnectionException
		 * @see		InvalidParamsException
		 * @see		NoRoomJoinedException
		 * @see		flash.media.Camera
		 * @see		flash.media.Microphone
		 * @see		flash.net.NetStream
		 */
		public function publishLiveCast ( enableCamera:Boolean = true, enableMicrophone:Boolean = true ) : NetStream
		{
			// If cam & mic are both null, why sending this type of request?
			if (!enableCamera && !enableMicrophone)
				throw new InvalidParamsException(Constants.ERROR_INVALID_PARAMS);
			
			// Check Red5 connection availability
			if (!netConn.connected)
				throw new NoAVConnectionException(Constants.ERROR_NO_CONNECTION + " [publishLiveCast method]");
			
			// Check if a room is joined
			if (smartFox.lastJoinedRoom == null)
				throw new NoRoomJoinedException(Constants.ERROR_NO_ROOM_JOINED);
			
			//------------------------------
			
			if (myLiveCast == null)
			{
				myLiveCast = new NetStream(netConn);
				var bHaveMedia:Boolean = false;
				var camMgr:CameraManager = CameraManager.instance;
				var prmsChkr:IPermissionsChecker = SessionManager.instance.permissionsChecker; // 2019-10-10
				
				// Attach cam and mic to the stream
				if (enableCamera)
				{
					if ( prmsChkr.cameraPermitted ) // 2019-10-10
					{
						bHaveMedia = true;
						myLiveCast.attachCamera ( camMgr.camera );
					}
				}
				
				if (enableMicrophone)
				{
					if ( prmsChkr.microphonePermitted ) // 2019-10-10
					{
						bHaveMedia = true;
						myLiveCast.attachAudio ( camMgr.microphone );
					}
				}
				
				if ( !bHaveMedia )
				{
					myLiveCast.close();
					myLiveCast = null;
					return null; // return
				}
				
				// Generate stream id
				var now:Date = new Date();
				var month:int = now.getUTCMonth() + 1;
				var dateString:String = now.getUTCFullYear().toString() + (month < 10 ? "0" : "") + month.toString() + now.getUTCDate().toString();
				var timeString:String = now.getUTCHours().toString() + now.getUTCMinutes().toString() + now.getUTCSeconds().toString() + now.getUTCMilliseconds().toString();
				var roomId:int = smartFox.lastJoinedRoom.id;
				var userId:int = smartFox.mySelf.id;
				
				var liveCastId:String = roomId + "_" + dateString + timeString + "_" + userId;
				
				// Publish live stream
				myLiveCast.publish(liveCastId, Constants.BROADCAST_TYPE_LIVE);
				
				// Set user variable
				var userVar:SFSUserVariable = new SFSUserVariable(CAST_USER_VAR, liveCastId);
				smartFox.send(new SetUserVariablesRequest([userVar]));
				
				Logger.log("User own live cast published; id:", liveCastId);
				
				return myLiveCast;
			}
			
			return null;
		}
		
		/**
		 * Stop broadcasting the current user's live stream.
		 * Calling this method causes the <b>RedBoxCastEvent.LIVE_CAST_UNPUBLISHED</b> event to be fired on the other users clients.
		 * 
		 * @sends	RedBoxCastEvent#LIVE_CAST_UNPUBLISHED
		 * 
		 * @example	The following example shows how to unpublish a live cast.
		 * 			<code>
		 * 			avCastMan.unpublishLiveCast();
		 * 			</code>
		 * 
		 * @see		#publishLiveCast
		 * @see		RedBoxCastEvent#LIVE_CAST_UNPUBLISHED
		 */
		public function unpublishLiveCast():void
		{
			// Stop outgoing stream
			if (myLiveCast != null)
			{
				myLiveCast.close();
				myLiveCast = null;
				
				// Reset user variable
				if (smartFox.isConnected)
				{
					var userVar:SFSUserVariable = new SFSUserVariable(CAST_USER_VAR, null);
					smartFox.send(new SetUserVariablesRequest([userVar]));
				}
				
				Logger.log("User own live cast unpublished");
			}
		}
		
		// -------------------------------------------------------
		// SMARTFOXSERVER & RED5 EVENT HANDLERS
		// -------------------------------------------------------
		
		/**
		 * Handle room joined event.
		 * 
		 * @exclude
		 */
		public function onRoomJoin(evt:SFSEvent):void
		{
			// Unpublish outgoing stream
			unpublishLiveCast();
			
			// Unsubscribe all incoming streams
			unsubscribeAllLiveCasts();
			
			// Re-initialize live casts list
			initCastList();
		}
		
		/**
		 * Handle user variables update event.
		 * 
		 * @exclude
		 */
		public function onUserVariablesUpdate(evt:SFSEvent):void
		{
			// Check if the proper variable has changed
			// Current user is skipped
			if (evt.params.user != smartFox.mySelf && evt.params.changedVars.indexOf(CAST_USER_VAR) > -1 && castList != null)
			{
				var castIdVar:UserVariable = evt.params.user.getVariable(CAST_USER_VAR);
				var user:User = evt.params.user;
				
				if (castIdVar != null && !castIdVar.isNull())
				{
					var castId:String = castIdVar.getStringValue();
					Logger.log("User '" + user.name + "' published his live cast:", castId);
					
					// Add new live cast to list
					addLiveCast(castId, user.id, user.name, true);
				}
				else
				{
					Logger.log("User '" + user.name + "' unpublished his live cast");
					
					// Remove live cast from list
					removeLiveCast(user.id);
				}
			}
		}
		
		/**
		 * Handle user leaving current room.
		 * 
		 * @exclude
		 */
		public function onUserExitRoom(evt:SFSEvent):void
		{
			var user:User = evt.params.user;
			
			if (!user.isItMe)
			{
				// Remove live cast from list
				var removed:Boolean = removeLiveCast(user.id);
				
				if (removed)
					Logger.log("User '" + user.name + "' left the room; live cast removed");
			}
		}
		
		// -------------------------------------------------------
		// PRIVATE METHODS
		// -------------------------------------------------------
		
		override protected function handleRed5ConnectionError(errorCode:String):void
		{
			// Unpublish outgoing stream
			unpublishLiveCast();
			
			// Unsubscribe all incoming streams
			unsubscribeAllLiveCasts();
		}
		
		/**
		 * Dispatch AVCastManager events.
		 */
		private function dispatchAVCastEvent(type:String, params:Object = null):void
		{
			var event:RedBoxCastEvent = new RedBoxCastEvent(type, params);
			dispatchEvent(event);
		}
		
		/**
		 * Initialize the available live casts list for the current room.
		 */
		private function initCastList():void
		{
			Logger.log("Initializing Live Casts list for current room...");
			
			castListRequested = false;
			
			castList = new Array();
			castListByUser = new Array();
			
			var currRoom:Room = smartFox.lastJoinedRoom;
			
			for each (var user:User in currRoom.userList)
			{
				// Exclude my own cast
				if (!user.isItMe)
				{
					var castIdVar:UserVariable = user.getVariable(CAST_USER_VAR);
					var castId:String = ((castIdVar != null && !castIdVar.isNull()) ? castIdVar.getStringValue() : null);
					
					if (castId != null && castId != "")
					{
						Logger.log("Live cast found for user", user.name);
						
						// Add live cast to list
						addLiveCast(castId, user.id, user.name, false);
					}
				}
			}
		}
		
		/**
		 * Add live cast to list.
		 */
		private function addLiveCast(id:String, userId:int, userName:String, fireEvent:Boolean = true):void
		{
			// Create new live cast
			var params:Object = {};
			params.id = id;
			params.uId = userId;
			params.uName = userName;
			
			var liveCast:LiveCast = new LiveCast(params);
			
			// Add cast to list
			castList[id] = liveCast;
			castListByUser[userId] = liveCast;
			
			// Dispatch event (only if the cast list has already been requested)
			if (fireEvent && castListRequested)
			{
				params = {};
				params.liveCast = liveCast;
				
				dispatchAVCastEvent(RedBoxCastEvent.LIVE_CAST_PUBLISHED, params);
			}
		}
		
		/**
		 * Remove live cast from list.
		 */
		private function removeLiveCast(userId:int):Boolean
		{
			if (castListByUser != null && castListByUser[userId] != null)
			{
				var liveCast:LiveCast = castListByUser[userId];
				
				// Unsubscribe live cast
				unsubscribeLiveCast(liveCast.id);
				
				// Dispatch event (only if the cast list has already been requested)
				if (castListRequested)
				{
					var params:Object = {};
					params.liveCast = liveCast;
					
					dispatchAVCastEvent(RedBoxCastEvent.LIVE_CAST_UNPUBLISHED, params);
				}
				
				// Remove cast from casts list
				delete castList[liveCast.id];
				delete castListByUser[userId];
				
				return true;
			}
			
			return false;
		}
	}
}