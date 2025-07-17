// Generated from frameworks/libs/player/27.0/playerglobal.swc
// Breakpoints are not supported
package flash.net
{
import flash.media.VideoStreamSettings;
import flash.media.Microphone;
import flash.events.EventDispatcher;
import flash.media.Camera;
import flash.utils.ByteArray;
import flash.media.SoundTransform;


[Event(name="mediaTypeData", type="flash.events.NetDataEvent")]
[Event(name="onSeekPoint")]
[Event(name="drmStatus", type="flash.events.DRMStatusEvent")]
[Event(name="drmError", type="flash.events.DRMErrorEvent")]
[Event(name="drmAuthenticate", type="flash.events.DRMAuthenticateEvent")]
[Event(name="onDRMContentData")]
[Event(name="onPlayStatus")]
[Event(name="onCuePoint")]
[Event(name="onTextData")]
[Event(name="onImageData")]
[Event(name="onMetaData")]
[Event(name="onXMPData")]
[Event(name="netStatus", type="flash.events.NetStatusEvent")]
[Event(name="ioError", type="flash.events.IOErrorEvent")]
[Event(name="asyncError", type="flash.events.AsyncErrorEvent")]
[Event(name="status", type="flash.events.StatusEvent")]
public class NetStream extends EventDispatcher
{
	public static const DIRECT_CONNECTIONS:String = "directConnections";
	public static const CONNECT_TO_FMS:String = "connectToFMS";

	public function NetStream(connection:NetConnection, peerID:String = "connectToFMS"):void
	{
	}

	[Version("10.1")]
	public function appendBytes(bytes:ByteArray):void
	{
	}

	[Version("10.1")]
	public function appendBytesAction(netStreamAppendBytesAction:String):void
	{
	}

	[Version("10.1")]
	public function attach(connection:NetConnection):void
	{
	}

	public function attachAudio(microphone:Microphone):void
	{
	}

	public function attachCamera(theCamera:Camera, snapshotMilliseconds:int = -1):void
	{
	}


	[Inspectable(environment="none")]
	public function get audioCodec():uint
	{
		return null;
	}


	[Version("10.1")]
	public function get audioReliable():Boolean
	{
		return null;
	}


	[Version("10.1")]
	public function set audioReliable(reliable:Boolean):void
	{
	}


	[Version("10.1")]
	public function get audioSampleAccess():Boolean
	{
		return null;
	}


	[Version("10.1")]
	public function set audioSampleAccess(reliable:Boolean):void
	{
	}


	[Version("10.1")]
	public function get backBufferLength():Number
	{
		return null;
	}


	[Version("10.1")]
	public function get backBufferTime():Number
	{
		return null;
	}


	[Version("10.1")]
	public function set backBufferTime(backBufferTime:Number):void
	{
	}

	public function get bufferLength():Number
	{
		return null;
	}

	public function get bufferTime():Number
	{
		return null;
	}

	public function set bufferTime(bufferTime:Number):void
	{
	}


	[Version("10.1")]
	public function get bufferTimeMax():Number
	{
		return null;
	}


	[Version("10.1")]
	public function set bufferTimeMax(bufferTimeMax:Number):void
	{
	}

	public function get bytesLoaded():uint
	{
		return null;
	}

	public function get bytesTotal():uint
	{
		return null;
	}

	public function get checkPolicyFile():Boolean
	{
		return null;
	}

	public function set checkPolicyFile(state:Boolean):void
	{
	}

	public function get client():Object
	{
		return null;
	}

	public function set client(object:Object):void
	{
	}

	public function close():void
	{
	}

	public function get currentFPS():Number
	{
		return null;
	}


	[Version("10.1")]
	public function get dataReliable():Boolean
	{
		return null;
	}


	[Version("10.1")]
	public function set dataReliable(reliable:Boolean):void
	{
	}


	[Inspectable(environment="none")]
	public function get decodedFrames():uint
	{
		return null;
	}

	[API("674")]
	public function dispose():void
	{
	}


	[Version("10")]
	public function get farID():String
	{
		return null;
	}


	[Version("10")]
	public function get farNonce():String
	{
		return null;
	}


	[Version("10.1")]
	public function get inBufferSeek():Boolean
	{
		return null;
	}


	[Version("10.1")]
	public function set inBufferSeek(value:Boolean):void
	{
	}


	[Version("10")]
	public function get info():NetStreamInfo
	{
		return null;
	}

	public function get liveDelay():Number
	{
		return null;
	}


	[Version("10")]
	public function get maxPauseBufferTime():Number
	{
		return null;
	}


	[Version("10")]
	public function set maxPauseBufferTime(pauseBufferTime:Number):void
	{
	}


	[Version("10.1")]
	public function get multicastAvailabilitySendToAll():Boolean
	{
		return null;
	}


	[Version("10.1")]
	public function set multicastAvailabilitySendToAll(value:Boolean):void
	{
	}


	[Version("10.1")]
	public function get multicastAvailabilityUpdatePeriod():Number
	{
		return null;
	}


	[Version("10.1")]
	public function set multicastAvailabilityUpdatePeriod(seconds:Number):void
	{
	}


	[Version("10.1")]
	public function get multicastFetchPeriod():Number
	{
		return null;
	}


	[Version("10.1")]
	public function set multicastFetchPeriod(seconds:Number):void
	{
	}


	[Version("10.1")]
	public function get multicastInfo():NetStreamMulticastInfo
	{
		return null;
	}


	[Version("10.1")]
	public function get multicastPushNeighborLimit():Number
	{
		return null;
	}


	[Version("10.1")]
	public function set multicastPushNeighborLimit(neighbors:Number):void
	{
	}


	[Version("10.1")]
	public function get multicastRelayMarginDuration():Number
	{
		return null;
	}


	[Version("10.1")]
	public function set multicastRelayMarginDuration(seconds:Number):void
	{
	}


	[Version("10.1")]
	public function get multicastWindowDuration():Number
	{
		return null;
	}


	[Version("10.1")]
	public function set multicastWindowDuration(seconds:Number):void
	{
	}


	[Version("10")]
	public function get nearNonce():String
	{
		return null;
	}

	public function get objectEncoding():uint
	{
		return null;
	}

	[Version("10")]
	public function onPeerConnect(subscriber:NetStream):Boolean
	{
		return null;
	}

	public function pause():void
	{
	}


	[Version("10")]
	public function get peerStreams():Array
	{
		return null;
	}

	public function play(...args:*):void
	{
	}

	[Version("10")]
	public function play2(param:NetStreamPlayOptions):void
	{
	}

	public function publish(name:String = null, type:String = null):void
	{
	}

	public function receiveAudio(flag:Boolean):void
	{
	}

	public function receiveVideo(flag:Boolean):void
	{
	}

	public function receiveVideoFPS(FPS:Number):void
	{
	}

	[API("661", "690")]
	public static function resetDRMVouchers():void
	{
	}

	public function resume():void
	{
	}

	[cppcall]
	public function seek(offset:Number):void
	{
	}

	public function send(handlerName:String, ...args:*):void
	{
	}

	public function get soundTransform():SoundTransform
	{
		return null;
	}

	public function set soundTransform(sndTransform:SoundTransform):void
	{
	}

	[Version("10.1")]
	public function step(frames:int):void
	{
	}

	public function get time():Number
	{
		return null;
	}

	public function togglePause():void
	{
	}

	public function get useHardwareDecoder():Boolean
	{
		return null;
	}

	public function set useHardwareDecoder(v:Boolean):void
	{
	}


	[API("680")]
	public function get useJitterBuffer():Boolean
	{
		return null;
	}


	[API("680")]
	public function set useJitterBuffer(value:Boolean):void
	{
	}


	[Inspectable(environment="none")]
	public function get videoCodec():uint
	{
		return null;
	}


	[Version("10.1")]
	public function get videoReliable():Boolean
	{
		return null;
	}


	[Version("10.1")]
	public function set videoReliable(reliable:Boolean):void
	{
	}


	[Version("10.1")]
	public function get videoSampleAccess():Boolean
	{
		return null;
	}


	[Version("10.1")]
	public function set videoSampleAccess(reliable:Boolean):void
	{
	}


	[API("674")]
	public function get videoStreamSettings():VideoStreamSettings
	{
		return null;
	}


	[API("674")]
	public function set videoStreamSettings(settings:VideoStreamSettings):void
	{
	}
}
}