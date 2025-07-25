package com.game.framework.data
{
	import com.game.framework.error.OperateError;
	import com.game.framework.ifaces.IURL;
	
	/**
	 *
	 *@author sixf
	 */
	public class ConfigData
	{
		private static var dialogView:IURL;
		private static var _delayTime:uint = 100;
		private static var _dialogContentBoundName:String="dialogBound";
		private static var _MaxRecodePage:int = 10;
		private static var _InvalidDialogAlert:Boolean = false;
		private static var _MaxLoadCount:int = 5;
			
		private static var _ReSizeRepeatCount:uint = 6;
		public function ConfigData()
		{
			
		}		
		public static function getReSizeRepeatCount():uint
		{
			return _ReSizeRepeatCount;
		}

		public static function setReSizeRepeatCount(value:uint):void
		{
			if(value==0){
				throw new OperateError("ReSizeRepeatCount 不能少等于 0，请设置大于 0 的值！ ",setReSizeRepeatCount);
			}
			
			_ReSizeRepeatCount = value;
		}

		public static function get MaxLoadCount():int
		{
			return _MaxLoadCount;
		}

		public static function getInvalidDialogAlert():Boolean
		{
			return _InvalidDialogAlert;
		}

		public static function setInvalidDialogAlert(value:Boolean):void
		{
			_InvalidDialogAlert = value;
		}

		public static function getMaxRecodePage():int
		{
			return _MaxRecodePage;
		}

		public static function setMaxRecodePage(value:int):void
		{
			_MaxRecodePage = value;
		}

		public static function getDialogContentBoundName():String
		{
			return _dialogContentBoundName;
		}

		public static function getDelayTime():uint
		{
			return _delayTime;
		}

		public static function setDelayTime(value:uint):void
		{
			_delayTime = value;
		}

		/**
		 *  valur 要实现 IDialog 接口
		 * @return 
		 * 
		 */		
		public static function getDialogView():IURL{
			return dialogView;
		}
		public static function setDialogView(valur:IURL):void{
			dialogView = valur;
		}
	}
}