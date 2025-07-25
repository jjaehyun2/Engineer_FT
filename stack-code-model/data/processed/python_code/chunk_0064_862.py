package com.game.framework.base {
	import com.asvital.dev.Log;
	import com.game.framework.FW;
	import com.game.framework.Launcher;
	import com.game.framework.error.OperateError;
	import com.game.framework.ifaces.INotify;
	import com.game.framework.ifaces.INotifyData;
	import com.game.framework.models.NotifyData;
	
	import flash.events.EventDispatcher;
	import flash.system.Capabilities;
	import flash.utils.getQualifiedClassName;
	
	/**
	 *实现了 INotify 接口
	 *@see com.game.framework.interfaces.INotify
	 *@author sixf
	 */
	public class BaseNotify extends EventDispatcher implements INotify {
		
		private static var _name:String;
		
		protected var launcher:Launcher;
		
		public function BaseNotify() {
			_name = getQualifiedClassName(this);
			
			launcher = Launcher.launcher;
		}		
		
		/**
		 *  name == Mediator.NONE 将不被注册到 MVC 框架中。 
		 * @return 
		 * 
		 */
		public function get name():String {
			//throw new OperateError("重写 name, 或为 Mediator.NONE 值 目标： " + this);
			
			return _name;
		}
		/*public function set name(value:String):void{
			this._name =value;
		}*/
		public function sendNotify(type:String, notifyData:INotifyData):Boolean {
			
			if (notifyData == null) {
				notifyData = new NotifyData();
			}		
			notifyData.FW::target = _name;
			
			if (launcher.sendNotify(type, notifyData)) {
				return true;
			} else {
				return false;
			}
			
			
		}		
		public function registerNotify():Array {
			//Log.out(this+"该Mediator没有订阅消息，将不会收到任何的消息。如果想接收消息请重写 registerNotify 方法！");
			return [];
		}
		
		public function sendNotifyTarget(name:String, type:String, notifyData:INotifyData):void {
			notifyData.FW::target = _name;
			launcher.sendNotifyTarget(name, type, notifyData);
		}
		
		public function handerNotify(type:String, notifyData:INotifyData):void {
			if (Capabilities.isDebugger) {
				Log.out(new OperateError("未处理的消息：" + type, this));
			}
		}
	}
}