package system.loader
{


	public class Res
	{
		public var url:String;
		public var data:* = null;
		private var _listenerList:Vector.<LoaderListener>;
		
		public function Res(url:String)
		{
			this.url = url;
		}
		
		/**
		 * 添加回调事件
		 * */
		public function addListener(listener:LoaderListener):void
		{
			if(!_listenerList)
				_listenerList = new Vector.<LoaderListener>();
			if(null != listener && _listenerList.indexOf(listener) < 0)
			{
				_listenerList.push(listener);
			}
		}
		
		public function completeNotify():void{
			if(!_listenerList) return;
			while(_listenerList.length){
				var listener:LoaderListener = _listenerList.pop();
				listener.onComplete(this);
			}
			_listenerList = null;
		}
		
		public function isReady():Boolean{
			return !(null==data);
		}
	}
}