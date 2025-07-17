package as3lib.helper
{
	import flash.system.Capabilities;

	/**
	 * @author gyb
	 * @date：2015-1-20 下午02:53:02
	 */
	public class CapabilitiesHelper
	{
		//事件类型========================================================================================================
		
		//属性及构造函数==================================================================================================
		public static var instance:CapabilitiesHelper = new CapabilitiesHelper();
		public function CapabilitiesHelper()
		{
		}
		//Getter/Setter===================================================================================================
		/**
		 * 获取屏幕最大水平分辨率
		 */
		public function get systemX():Number
		{
			return Capabilities.screenResolutionX;
		}
		/**
		 * 获取屏幕最大垂直分辨率
		 */
		public function get systemY():Number
		{
			return Capabilities.screenResolutionY;
		}
		//方法============================================================================================================
		public function isAirApplication():Boolean 
		{
			return Capabilities.playerType == "Desktop";
		}
		public function isIDE():Boolean 
		{
			return Capabilities.playerType == "External";
		}
		public function isMac():Boolean
		{
			return Capabilities.os.toLowerCase().indexOf("mac os") != -1;
		}
		public function isPC():Boolean
		{
			return Capabilities.os.toLowerCase().indexOf("mac os") == -1;
		}
		public function isPlugin():Boolean
		{
			return Capabilities.playerType == "PlugIn" || Capabilities.playerType == "ActiveX";
		}
		public function isStandAlone():Boolean
		{
			return Capabilities.playerType == "StandAlone";
		}
		//事件处理==========================================================================================================
		
		
	}
}