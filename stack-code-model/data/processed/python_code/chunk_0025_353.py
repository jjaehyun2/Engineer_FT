package as3lib.core.valid
{
	import flash.display.DisplayObject;
	/**
	 * @param
	 * @return
	 */
	public function isWeb(location:DisplayObject):Boolean {
		return location.loaderInfo.url.substr(0, 4) == "http";
	}
}