package flash.net
{
import flash.events.EventDispatcher;

[Event(name="netStatus", type="flash.events.NetStatusEvent")]
[Event(name="securityError", type="flash.events.SecurityErrorEvent")]
[Event(name="ioError", type="flash.events.IOErrorEvent")]
[Event(name="asyncError", type="flash.events.AsyncErrorEvent")]
public class NetConnection extends EventDispatcher
{
	[Inspectable(environment="none")]
	public function addHeader(operation:String, mustUnderstand:Boolean = false, param:Object = null):void
	{
	}

	public function call(command:String, responder:Responder, ...args:*):void
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

	public function connect(command:String, ...args:*):void
	{
	}

	public function get connected():Boolean
	{
		return null;
	}

	public function get connectedProxyType():String
	{
		return null;
	}

	public static function get defaultObjectEncoding():uint
	{
		return null;
	}

	public static function set defaultObjectEncoding(version:uint):void
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


	[Version("10")]
	public function get maxPeerConnections():uint
	{
		return null;
	}


	[Version("10")]
	public function set maxPeerConnections(maxPeers:uint):void
	{
	}


	[Version("10")]
	public function get nearID():String
	{
		return null;
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

	public function set objectEncoding(version:uint):void
	{
	}


	[Version("10")]
	public function get protocol():String
	{
		return null;
	}

	public function get proxyType():String
	{
		return null;
	}

	public function set proxyType(ptype:String):void
	{
	}


	[Version("10")]
	public function get unconnectedPeerStreams():Array
	{
		return null;
	}

	public function get uri():String
	{
		return null;
	}

	public function get usingTLS():Boolean
	{
		return null;
	}
}
}