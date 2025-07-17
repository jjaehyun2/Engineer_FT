import it.gotoandplay.smartfoxbits.events.SFSEvent;	

/**
 * RedBoxClipEvent is the class representing all events dispatched by the RedBox's {@link AVClipManager} instance.
 * The RedBoxClipEvent extends the it.gotoandplay.smartfoxbits.events.SFSEvent class, which in turn extends the it.gotoandplay.smartfoxbits.events.BaseEvent.
 * RedBoxClipEvent also provides a public property called {@code params} of type {@code Object} that can contain any number of parameters.
 * 
 * @usage	Please refer to the specific events for usage examples and {@code params} object content.
 * 
 * @author	The gotoAndPlay() Team
 * 			{@link http://www.smartfoxserver.com}
 * 			{@link http://www.gotoandplay.it}
 */
class com.smartfoxserver.redbox.events.RedBoxClipEvent extends SFSEvent
{
	/**
	 * Dispatched when the connection to Red5 server has been established.
	 * This event is dispatched after the {@link AVClipManager} is instantiated or when the {@link AVClipManager#initAVConnection} method is called.
	 * The connection to Red5 must be available before any method related to a/v streaming is called.
	 * 
	 * No parameters are provided.
	 * 
	 * @example	The following example shows how to handle the "onAVConnectionInited" event.
	 * 			<code>
	 * 			var red5IpAddress:String = "127.0.0.1"
	 * 			var avClipMan:AVClipManager = new AVClipManager(red5IpAddress)
	 * 			
	 * 			avClipMan.addEventListener(RedBoxClipEvent.onAVConnectionInited, Delegate.create(this, onAVConnectionInited))
	 * 			
	 * 			function onAVConnectionInited(evt:RedBoxClipEvent):Void
	 * 			{
	 * 				trace("Red5 connection established")
	 * 			}
	 * 			</code>
	 * 
	 * @see		AVClipManager#initAVConnection
	 */
	public static var onAVConnectionInited:String = "onAVConnectionInited"
	
	
	/**
	 * Dispatched when the connection to Red5 server can't be established.
	 * This event is dispatched when an error or special condition (like "connection closed") occurred in the NetConnection object used internally by the {@link AVClipManager} to handle the connection to Red5.
	 * This kind of error is always related to the Red5 server connection, so you should check if the server is running and reachable.
	 * Also check the Red5 logs or console output for more details.
	 * 
	 * The {@code params} object contains the following parameters.
	 * @param	errorCode:	(<b>String</b>) the description of the error condition; check the "code" property of the infoObject param of the NetConnection.onStatus handler in the <a href="http://livedocs.adobe.com/flashmediaserver/3.0/hpdocs/help.html?content=00000168.html#228975">Adobe Flash Media Server ActionScript 2.0 Language Reference</a>.
	 * 
	 * @example	The following example shows how to handle a Red5 connection error.
	 * 			<code>
	 * 			avClipMan.addEventListener(RedBoxClipEvent.onAVConnectionError, Delegate.create(this, onAVConnectionError))
	 * 			
	 * 			function onAVConnectionError(evt:RedBoxClipEvent):Void
	 * 			{
	 * 				trace("A connection error occurred: " + evt.params.errorCode)
	 * 			}
	 * 			</code>
	 */
	public static var onAVConnectionError:String = "onAVConnectionError"
	
	
	/**
	 * Dispatched when clips list is returned, in response to a {@link AVClipManager#getClipList} request.
	 * 
	 * The {@code params} object contains the following parameters.
	 * @param	clipList:	(<b>Array</b>) a list of {@link Clip} objects for the zone logged in by the user.
	 * 
	 * @example	The following example shows how to request the available clips list.
	 * 			<code>
	 * 			avClipMan.addEventListener(RedBoxClipEvent.onClipList, Delegate.create(this, onClipList))
	 * 			
	 * 			avClipMan.getClipList()
	 * 			
	 * 			function onClipList(evt:RedBoxClipEvent):Void
	 * 			{
	 * 				for(var i in evt.params.clipList)
	 *				{
	 *					var clip:Clip = evt.params.clipList[i]
	 * 					trace ("Clip id:", clip.id)
	 * 					trace ("Clip submitter:", clip.username)
	 * 					trace ("Clip size:", clip.size + " bytes")
	 * 					trace ("Clip last modified date:", clip.lastModified)
	 * 					trace ("Clip properties:")
	 * 					for (var s:String in clip.properties)
	 * 						trace (s + " --> " + clip.properties[s])
	 * 				}
	 * 			}
	 * 			</code>
	 * 
	 * @see		AVClipManager#getClipList
	 * @see		#onClipAdded
	 * @see		#onClipDeleted
	 * @see		#onClipUpdated
	 * @see		Clip
	 */
	public static var onClipList:String = "onClipList"
	
	
	/**
	 * Dispatched when the recording of an a/v clip starts, in response to a {@link AVClipManager#startClipRecording} request.
	 * 
	 * No parameters are provided.
	 * 
	 * @example	The following example shows how to handle the "onClipRecordingStarted" event.
	 * 			<code>
	 * 			avClipMan.addEventListener(RedBoxClipEvent.onClipRecordingStarted, Delegate.create(this, onClipRecordingStarted))
	 * 			
	 * 			avClipMan.startClipRecording(true, true)
	 * 			
	 * 			function onClipRecordingStarted(evt:RedBoxClipEvent):Void
	 * 			{
	 * 				// Attach camera output to video instance on stage to see what I'm recording
	 * 				video.attachVideo(Camera.get())
	 * 			}
	 * 			</code>
	 * 
	 * @see		AVClipManager#startClipRecording
	 */
	public static var onClipRecordingStarted:String = "onClipRecordingStarted"
	
	
	/**
	 * Dispatched when an error occurs in the RedBox server-side extension after submitting an a/v clip.
	 * This event is used when either a recorded or an uploaded clip is submitted.
	 * 
	 * The {@code params} object contains the following parameters.
	 * @param	error:	(<b>String</b>) the error message sent by the RedBox extension.
	 * 
	 * @example	The following example shows how to handle a clip submission error.
	 * 			<code>
	 * 			avClipMan.addEventListener(RedBoxClipEvent.onClipSubmissionFailed, Delegate.create(this, onClipSubmissionFailed))
	 * 			
	 * 			var clipProperties:Object = {}
	 * 			clipProperties.author = "jack"
	 * 			
	 * 			avClipMan.submitRecordedClip(clipProperties)
	 * 			
	 * 			function onClipSubmissionFailed(evt:RedBoxClipEvent):Void
	 * 			{
	 * 				trace("An error occurred during clip submission:" + evt.params.error)
	 * 			}
	 * 			</code>
	 * 
	 * @see		AVClipManager#submitRecordedClip
	 */
	public static var onClipSubmissionFailed:String = "onClipSubmissionFailed"
	
	
	/**
	 * Dispatched when a new a/v clip has been submitted by one of the users in the current zone.
	 * 
	 * The {@code params} object contains the following parameters.
	 * @param	clip:	(<b>Clip</b>) the Clip instance representing the added a/v clip.
	 * 
	 * @example	The following example shows how to handle a clip added event.
	 * 			<code>
	 * 			avClipMan.addEventListener(RedBoxClipEvent.onClipAdded, Delegate.create(this, onClipAdded))
	 * 			
	 * 			function onClipAdded(evt:RedBoxClipEvent):Void
	 * 			{
	 * 				var clip:Clip = evt.params.clip
	 * 				
	 * 				trace("A new clip was submitted")
	 * 				trace ("Clip id:", clip.id)
	 * 				trace ("Clip submitter:", clip.username)
	 * 				trace ("Clip size:", clip.size + " bytes")
	 * 				trace ("Clip last modified date:", clip.lastModified)
	 * 				trace ("Clip properties:")
	 * 				for (var s:String in clip.properties)
	 * 					trace (s + " --> " + clip.properties[s])
	 * 			}
	 * 			</code>
	 * 
	 * @see		AVClipManager#submitRecordedClip
	 * @see		AVClipManager#submitUploadedClip
	 * @see		Clip
	 */
	public static var onClipAdded:String = "onClipAdded"
	
	
	/**
	 * Dispatched when an a/v clip has been deleted by one of the users in the current zone.
	 * 
	 * The {@code params} object contains the following parameters.
	 * @param	clip:	(<b>Clip</b>) the Clip instance representing the deleted a/v clip.
	 * 
	 * @example	The following example shows how to handle a clip deletion event.
	 * 			<code>
	 * 			avClipMan.addEventListener(RedBoxClipEvent.onClipDeleted, Delegate.create(this, onClipDeleted))
	 * 			
	 * 			avClipMan.deleteClip(clipId)
	 * 			
	 * 			function onClipDeleted(evt:RedBoxClipEvent):Void
	 * 			{
	 * 				trace("The clip " + evt.params.clip.id + " was deleted")
	 * 			}
	 * 			</code>
	 * 
	 * @see		AVClipManager#deleteClip
	 * @see		Clip
	 */
	public static var onClipDeleted:String = "onClipDeleted"
	
	
	/**
	 * Dispatched when the properties of an a/v clip have been updated by one of the users in the current zone.
	 * 
	 * The {@code params} object contains the following parameters.
	 * @param	clip:	(<b>Clip</b>) the Clip instance representing the updated a/v clip.
	 * 
	 * @example	The following example shows how to handle an update in clip properties.
	 * 			<code>
	 * 			avClipMan.addEventListener(RedBoxClipEvent.onClipUpdated, Delegate.create(this, onClipUpdated))
	 * 			
	 * 			var newClipProperties:Object = {}
	 * 			newClipProperties.title = "Batman - The Dark Knight"
	 * 			newClipProperties.author = "Warner Bros."
	 * 			
	 * 			avClipMan.updateClipProperties(clipId, newClipProperties)
	 * 			
	 * 			function onClipUpdated(evt:RedBoxClipEvent):Void
	 * 			{
	 * 				trace("Clip properties have been updated")
	 * 				var clip:Clip = evt.params.clip
	 * 				
	 * 				// Update the clip list
	 * 				...
	 * 			}
	 * 			</code>
	 * 
	 * @see		AVClipManager#updateClipProperties
	 * @see		Clip
	 */
	public static var onClipUpdated:String = "onClipUpdated"
	
	
	//-----------------------------------------------------------------------------------------------------
	
	/**
	 * The parameters for this event.
	 *
	 * @exclude
	 */
	var params:Object;
	
	/**
	 *	RedBoxChatEvent class constructor.
	 *
	 *	@param target: the event's target.
	 *	@param type: the event's type.
	 *	@param params: an object containing the event's parameters.
	 *	
	 *	@exclude
	 */
	public function RedBoxClipEvent(target:Object, type:String, params:Object)
	{
		super(target, type)
		this.params = params;
	}
}