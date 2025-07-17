/**
 * 创建：trg
 * 完善：gyb
 * 功能：模块加载队列工具类，实现模块的排队加载
 */
package as3lib.helper.module
{
	
	import as3lib.evt.ModuleEventEx;
	import as3lib.helper.module.core.ModuleCollection;
	import as3lib.helper.module.core.ModuleInfo;
	
	import flash.display.DisplayObject;
	import flash.events.Event;
	import flash.events.EventDispatcher;
	
	import mx.core.FlexGlobals;
	import mx.events.FlexEvent;
	import mx.events.ModuleEvent;
	import mx.modules.IModuleInfo;
	import mx.modules.Module;
	import mx.modules.ModuleManager;
	
	[Event(name = ModuleEventEx.PROGRESS, type = "ex.event.ModuleHelperEvent")]
	[Event(name = Event.COMPLETE, type = "flash.events.Event")]
	/**
	 * 应用模块加载和管理类
	 * @author trg
	 */
	public class ModuleHelper extends EventDispatcher
	{
		
		public static var Instance:ModuleHelper = new ModuleHelper();
		
		
		private var m_oQueue0:ModuleCollection = new ModuleCollection();	  //待加载的基础模块队列
		private var m_oQueue1:ModuleCollection = new ModuleCollection();	  //待加载的普通模块队列
		private var m_oProcessing:ModuleCollection = new ModuleCollection();//正在加载处理的模块队列
		private var m_oDone:ModuleCollection = new ModuleCollection();		  //已经完成加载和初始化的模块集合
		private var m_oEnterFrameSender:DisplayObject;
		
		//============================================== 构造函数 ==============================================
		public function ModuleHelper() 
		{
			
		}
		//============================================== 属性部分 ==============================================
		/**
		 * 同时进行加载的最大请求数量(可以理解为线程数)
		 */
		public var maxRequest:int = 1;
		
		//============================================== 方法部分 ==============================================
		/**
		 * 添加一个模块加载任务到加载队列，等待进行模块加载
		 * @param	key
		 * @param	url
		 * @param	type
		 * @param	vars
		 * @return	如果之前已经在加载队列中或已经加载，则返回0，否则添加到队列并返回1.不使用布尔值，是由于js调用时经常接收不成功。
		 */
		public function load(key:String, url:String, type:int = 1, vars:Object = null) : Boolean {
			if (get(key) != null) {
				return false;
			}
			var _oModuleInfo:ModuleInfo = new ModuleInfo(key, url, type, vars);
			_oModuleInfo.m_oOwner = this;
			if (type == 0) {
				m_oQueue0.add(_oModuleInfo.key, _oModuleInfo);
			}
			else {
				m_oQueue1.add(_oModuleInfo.key, _oModuleInfo);
			}
			ensureEnterFrameEvent();
			return true;
		}
		/**
		 * @param key：load时的key值
		 * @param methodName：方法名
		 * @param params：参数
		 */
		public function callModuleMethod(key:String, methodName:String, ...params):*
		{
			var _oModuleInfo:ModuleInfo = this.get(key);
			if (_oModuleInfo != null && _oModuleInfo.module != null && _oModuleInfo.module.hasOwnProperty(methodName)) 
			{
				return _oModuleInfo.module[methodName].apply(null, params);
			}
			return null;
		}
		/**
		 * 获取模块状态。供外部js调用
		 * @param	key
		 * @return	如果模块未加载，则返回-1；正等待加载或加载中，则返回0；加载完成，则返回1。
		 */
		public function getModuleState(key:String):int {
			var _oModuleInfo:ModuleInfo = this.get(key);
			if (_oModuleInfo == null) {
				return -1;
			}
			return (_oModuleInfo.completed ? 1 : 0);
		}
		/**
		 * 获取模块属性
		 * @param	key
		 * @param	propertyName
		 * @return
		 */
		public function getModuleProperty(key:String, propertyName:String):* {
			var _oModuleInfo:ModuleInfo = this.get(key);
			if (_oModuleInfo == null || _oModuleInfo.module == null || !_oModuleInfo.completed) {
				return null;
			}
			if (!_oModuleInfo.module.hasOwnProperty(propertyName)) {
				return null;
			}
			return _oModuleInfo.module[propertyName];
		}
		/**
		 * 确保注册了 ENTER_FRAME 事件，进行模块加载
		 */
		private function ensureEnterFrameEvent():void {
			if (m_oEnterFrameSender == null) {
				m_oEnterFrameSender = DisplayObject(FlexGlobals.topLevelApplication);
				if(m_oEnterFrameSender != null) 
				{
					//Event.ENTER_FRAME在结束监听前就是一个循环，不同的是，Event.ENTER_FRAME有周期，和帧频有关，周期性的运行方法体.播放器发布的事件，每过(1/帧频)秒向全部继承自DisplayObject的对象发送。在这个事件之前正好是屏幕的一次固定刷新。(即两次更新的时间间隔为(1/帧频)秒)
					m_oEnterFrameSender.addEventListener(Event.ENTER_FRAME, onEnterFrame);
				}
			}
		}
		
		/**
		 * 获取模块信息
		 * @param	key
		 * @return
		 */
		public function get(key:String):ModuleInfo {
			var rslt:ModuleInfo = m_oQueue0.get(key);
			if (rslt != null) {
				return rslt;
			}
			rslt = m_oQueue1.get(key);
			if (rslt != null) {
				return rslt;
			}
			rslt = m_oProcessing.get(key);
			if (rslt != null) {
				return rslt;
			}
			rslt = m_oDone.get(key);
			return rslt;
		}
		
		private function getModuleInfoByModuleInfo(moduleInfo:IModuleInfo):ModuleInfo {
			var _oModuleInfo:ModuleInfo;
			for (var k:int = 0; k < m_oProcessing.count ; k++) {
				_oModuleInfo = m_oProcessing.getAt(k) as ModuleInfo;
				if (_oModuleInfo.moduleInfo == moduleInfo) {
					return _oModuleInfo;
				}
			}
			return null;
		}
		
		/**
		 * 移除模块信息
		 * @param	key
		 * @return
		 */
		private function remove(key:String):ModuleInfo {
			var rslt:ModuleInfo = m_oQueue0.remove(key);
			if (rslt != null) {
				return rslt;
			}
			rslt = m_oQueue1.remove(key);
			if (rslt != null) {
				return rslt;
			}
			rslt = m_oProcessing.remove(key);
			if (rslt != null) {
				return rslt;
			}
			rslt = m_oDone.remove(key);
			return rslt;
		}
		
		/**
		 *  删除 ENTER_FRAME 事件
		 */
		private function removeEnterFrameEvent():void {
			if (m_oEnterFrameSender != null) {
				m_oEnterFrameSender.removeEventListener(Event.ENTER_FRAME, onEnterFrame);
				m_oEnterFrameSender = null;
			}
		}
		
		private function tryCallModuleError(moduleAppInfo:ModuleInfo, e:ModuleEvent):void {
			if (moduleAppInfo.vars && moduleAppInfo.vars.onError) {
				var args:Array = [moduleAppInfo, e];
				if (moduleAppInfo.vars.onErrorParams != null) {
					args = args.concat.apply(null, moduleAppInfo.vars.onErrorParams as Array);
				}
				moduleAppInfo.vars.onError.apply(null,  args);
			}
		}
		
		private function tryCallModuleProgress(moduleAppInfo:ModuleInfo, e:ModuleEvent):void {
			if (moduleAppInfo.vars && moduleAppInfo.vars.onProgress) {
				var args:Array = [moduleAppInfo, e];
				if (moduleAppInfo.vars.onProgressParams != null) {
					args = args.concat.apply(null, moduleAppInfo.vars.onProgressParams as Array);
				}
				moduleAppInfo.vars.onProgress.apply(null,  args);
			}
		}
		
		/**
		 * 初始化相关属性，并调用 onReady 参数指定的函数
		 * @param	moduleAppInfo
		 * @param	e
		 */
		private function tryCallModuleReady(moduleInfo:ModuleInfo, e:ModuleEvent):void {
			if (!moduleInfo.vars) {
				return;
			}
			for(var pName:String in moduleInfo.vars) {
				if (ModuleInfo.SPECIAL_PROPERTIES.indexOf(pName) < 0) {
					if(moduleInfo.module.hasOwnProperty(pName)) {
						moduleInfo.module[pName] = moduleInfo.vars[pName];
					}
					else {
						if(moduleInfo.module.setStyle) {
							moduleInfo.module.setStyle(pName, moduleInfo.vars[pName]);
						}
					}
				}
			}
			if (moduleInfo.vars.onReady) {
				var args:Array = [moduleInfo, e];
				if (moduleInfo.vars.onReadyParams != null) {
					args = args.concat.apply(null, moduleInfo.vars.onReadyParams as Array);
				}
				moduleInfo.vars.onReady.apply(null,  args);
			}
		}
		
		/**
		 * 尝试加载下一个模块
		 */
		private function tryLoadNextModule():void {
			if (m_oQueue0.count == 0 && m_oQueue1.count == 0) {
				removeEnterFrameEvent();
				dispatchEvent(new Event(Event.COMPLETE));
				return;
			}
			var o:* = null;
			if (m_oQueue0.count > 0) {	//如果有基础模块待加载，则先加载基础模块
				o = m_oQueue0.removeAt(0);
			}
			else {
				//遍历正在加载的模块，检查是否有基础模块尚未加载完成，如果有，则继续等待。
				for (var _k:int = 0; _k < m_oProcessing.count; _k++) {
					if (ModuleInfo(m_oProcessing.getAt(_k)).type == 0) {
						return;
					}
				}
				o = m_oQueue1.removeAt(0);	//此时基础模块已经全部加载完成，可以加载应用模块了
			}
			var _oInfo:ModuleInfo = o as ModuleInfo;
			
			var _oModuleInfo:IModuleInfo = ModuleManager.getModule(_oInfo.url);
			if(_oModuleInfo.loaded) {
				_oInfo.m_oModule = _oModuleInfo.factory.create();
				initModule(_oInfo,null);
			}
			_oModuleInfo.addEventListener(ModuleEvent.ERROR, onModuleError);
			_oModuleInfo.addEventListener(ModuleEvent.PROGRESS, onModuleProgress);
			_oModuleInfo.addEventListener(ModuleEvent.READY, onModuleReady);
			_oModuleInfo.load(_oInfo.vars ? _oInfo.vars.applicationDomain : null);
			
			m_oProcessing.add(_oInfo.key, _oInfo);
			
			_oInfo.moduleInfo = _oModuleInfo; //保持引用，否则会被回收，不会引发事件
		}
		
		/**
		 * 设置模块属性，检查和调用模块初始化方法
		 * @param	moduleAppInfo
		 */
		private function tryModuleInit(moduleInfo:ModuleInfo):void {
			if (!moduleInfo.vars) {
				return;
			}
			if(moduleInfo.vars.initMethod && moduleInfo.module.hasOwnProperty(moduleInfo.vars.initMethod)) {
				moduleInfo.module[moduleInfo.vars.initMethod].apply(moduleInfo.module,  moduleInfo.vars.initMethodParams);
			}
		}
		
		/**
		 * 卸载模块
		 * @param	key	模块关键字
		 * @return	如果未找到模块，则返回false，否则卸载并返回true。
		 */
		public function unload(key:String) : Boolean {
			var _oModuleInfo:ModuleInfo = remove(key);
			if (_oModuleInfo == null) {
				return false;
			}
			_oModuleInfo.moduleInfo.unload();
			return true;
		}
		//============================================== 事件处理 ==============================================
		/**
		 * ENTER_FRAME 事件处理
		 * @param	e	事件参数
		 */
		private function onEnterFrame(e:Event):void {
			if (m_oProcessing.count < maxRequest) 
			{
				tryLoadNextModule();
			}
		}
		
		private function onModuleError(e:ModuleEvent):void {
			var _oInfo:ModuleInfo = getModuleInfoByModuleInfo(e.currentTarget as IModuleInfo);
			tryCallModuleError(_oInfo, e);
			m_oDone.add(_oInfo.key, m_oProcessing.remove(_oInfo.key));	//添加到已完成队列。由于遇到的可能性很低，没有专门为“加载错误”创建一个队列
			dispatchEvent(new ModuleEventEx(ModuleEvent.ERROR, e.bubbles, e.cancelable, e.bytesLoaded, e.bytesTotal, e.errorText, e.module, _oInfo));
		}
		private function onModuleProgress(e:ModuleEvent):void {
			var _oModuleInfo:ModuleInfo = getModuleInfoByModuleInfo(e.currentTarget as IModuleInfo);
			tryCallModuleProgress(_oModuleInfo, e);
			dispatchEvent(new ModuleEventEx(ModuleEvent.PROGRESS, e.bubbles, e.cancelable, e.bytesLoaded, e.bytesTotal, e.errorText, e.module, _oModuleInfo));
		}
		private function onModuleReady(e:ModuleEvent):void {
			var _oModuleInfo:IModuleInfo = e.currentTarget as IModuleInfo;
			//移除事件
			_oModuleInfo.removeEventListener(ModuleEvent.ERROR, onModuleError);
			_oModuleInfo.removeEventListener(ModuleEvent.PROGRESS, onModuleProgress);
			_oModuleInfo.removeEventListener(ModuleEvent.READY, onModuleReady);
			
			//查找对应的ModuleInfo
			var _oInfo:ModuleInfo = getModuleInfoByModuleInfo(_oModuleInfo);
			if(_oInfo) {
				_oInfo.m_oModule = e.module.factory.create();
				initModule(_oInfo,e);
			}
		}
		
		private function initModule(_oInfo:ModuleInfo,e:ModuleEvent):void
		{
			tryCallModuleReady(_oInfo, e);	//引发onReady事件
			
			var _oModule:Module = _oInfo.module as Module;
			if (_oModule && !_oModule.initialized && _oModule.stage) {
				//注册事件，待初始化完成才能调用模块方法。
				_oModule.addEventListener(FlexEvent.CREATION_COMPLETE, function(ex:FlexEvent):void {
					tryModuleInit(_oInfo);
					var proModuleInfo:* = m_oProcessing.remove(_oInfo.key);
					if(proModuleInfo == null) proModuleInfo = _oInfo;
					m_oDone.add(_oInfo.key,proModuleInfo);
					_oInfo.m_bCompleted = true;
				});
			}
			else {
				//模块初始化方法
				tryModuleInit(_oInfo);
				//从正在加载队列移动模块到加载完成队列
				
				m_oDone.add(_oInfo.key, m_oProcessing.remove(_oInfo.key));
				_oInfo.m_bCompleted = true;
			}
		}
	}
	
}