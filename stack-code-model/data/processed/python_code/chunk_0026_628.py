// Generated from frameworks/libs/player/16.0/playerglobal.swc
// Breakpoints are not supported
package flash.events
{
[API("672")]
public class NetDataEvent extends Event
{
	public static const MEDIA_TYPE_DATA:String = "mediaTypeData";

	private var _timestamp:Number;

	private var _info:Object;

	public function NetDataEvent(type      :String,
								 bubbles   :Boolean = false,
								 cancelable:Boolean = false,
								 timestamp :Number  = 0,
								 info      :Object  = null
								):void
	{
		super(type, bubbles, cancelable);
		_info = info;
		_timestamp = timestamp;
	}

	override public function clone():Event
	{
		return new NetDataEvent(type, bubbles, cancelable, timestamp, info);
	}

	public function get info():Object
	{
		return _info;
	}

	public function get timestamp():Number
	{
		return _timestamp;
	}
}
}