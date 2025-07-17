// Generated from frameworks/libs/player/16.0/playerglobal.swc
// Breakpoints are not supported
package flash.events
{
import flash.net.drm.DRMContentData;
import flash.net.drm.DRMVoucher;


[API("661", "667")]
public class DRMStatusEvent extends Event
{
	public static const DRM_STATUS:String = "drmStatus";

	public function DRMStatusEvent(type      :String         = "drmStatus",
								   bubbles   :Boolean        = false,
								   cancelable:Boolean        = false,
								   inMetadata:DRMContentData = null,
								   inVoucher :DRMVoucher     = null,
								   inLocal   :Boolean        = false
								  ):void
	{
		super(type, bubbles, cancelable);
	}


	[API("663", "667")]
	public function get contentData():DRMContentData
	{
		return null;
	}


	[API("663", "667")]
	public function set contentData(value:DRMContentData):void
	{
	}


	[API("663", "667")]
	public function get isLocal():Boolean
	{
		return null;
	}


	[API("663", "667")]
	public function set isLocal(value:Boolean):void
	{
	}

	public function toString():String
	{
		return null;
	}


	[API("663", "667")]
	public function get voucher():DRMVoucher
	{
		return null;
	}


	[API("663", "667")]
	public function set voucher(value:DRMVoucher):void
	{
	}
}
}