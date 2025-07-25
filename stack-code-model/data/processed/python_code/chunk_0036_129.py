package com.game.framework.net {
	import com.asvital.dev.Log;
	import com.game.framework.FW;
	import com.game.framework.Launcher;
	import com.game.framework.error.OperateError;
	import com.game.framework.events.AssetsEvent;
	import com.game.framework.events.DissolveEvent;
	import com.game.framework.events.FrameWorkEvent;
	import com.game.framework.ifaces.IAssetItem;
	import com.game.framework.ifaces.INotifyData;
	import com.game.framework.ifaces.ISwfFile;
	import com.game.framework.ifaces.IURL;
	import com.game.framework.logic.AssetsData;
	import com.game.framework.models.NotifyData;
	import com.game.framework.views.CreateView;
	import com.game.framework.views.Mediator;
	
	import flash.display.MovieClip;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.net.getClassByAlias;
	import flash.utils.ByteArray;
	import flash.utils.getTimer;
	
	import avmplus.getQualifiedClassName;
	
	/**
	 * 
	 * 消息事件，当 Mediator 层，被告知要消失。
	 * 
	 */	
	[Event(name="dissolve", type="com.game.framework.events.DissolveEvent")]
	
	[Event(name="init_over", type="com.game.framework.events.FrameWorkEvent")]
	
	/**
	 * 仅用于模块的加载
	 * 使用 MediaAssetItem 对象方法:<br/>
	 * 1, addMediaView 先加到显示列表中，此时就可以得到父级，同时去判断父级中是否有相同名字（name）的对象，如果有，直接返回。<br/>
	 * 2，initView 初始化<br/>
	 * var login:MediaAssetItem = new MediaAssetItem(MediaURL.fromUIView(MediaURL.SKIN.LoginViewSkin));<br/>
	 * uimanager.addMediaView(login);<br/>
	 * login.initView();<br/>
	 * @author sixf
	 */
	public class MediaAssetItem extends AssetItem {
		
		protected var mediator:Mediator;
		protected var createView:CreateView;
		private var notify:NotifyData = null;
		private var notifyType:String = null;
		private var _isLoadSuccess:Boolean = false;
		private var skinLoader:SkinLoader;
		private var swfFile:ISwfFile;
		private var isINType:Boolean =false;
		protected var _isinitView:Boolean = false;
		private var _serial:int=0;
		
		/**
		 * 
		 * 建设使用 uimanager.addMediaView(new MediaAssetItem(MediaURL.fromUIView(MediaURL.SKIN.HUDViewSkin)));    而不直接进行实例化
		 * @param url
		 *
		 */
		public function MediaAssetItem(url:IURL,_serial:int =0,loadType:String = LoadType.ChildApplicationDomain) {
			super(url, loadType);
			
			this.addEventListener(Event.ADDED_TO_STAGE,onAddStageHandler);
			this.addEventListener(Event.REMOVED_FROM_STAGE,onRemovedStageHandler);	
			
			this._serial = _serial;
			
		}		
		
		public function get serial():int
		{
			return _serial;
		}
		
		public function set serial(value:int):void
		{
			_serial = value;
		}
		
		protected function onAddStageHandler(event:Event):void
		{
			
			if(mediator){
				//mediator.handerNotify(Mediator.IN_TYPE,null);
				mediator.push(Mediator.IN_TYPE,null);
				mediator.isOutStage = false;
			}else{
				isINType =true;
			}
		}
		protected function onRemovedStageHandler(event:Event):void
		{
			
			if(mediator){
				
				mediator.push(Mediator.OUT_TYPE,null);
				mediator.isOutStage = true;
			}			
			
		}
		/**
		 * 用于修改 Mediator 
		 * @param mediator
		 * @return 
		 * 
		 */
		protected function newMediator(mediator:Mediator):Mediator{
			
			
			return mediator;
		}
		
		/**
		 *内部的资源是否加载完成,不统计其内部其它线程的加载
		 */
		public function get isLoadSuccess():Boolean {
			return _isLoadSuccess;
		}
		
		override public function onCompleteHandler(event:Event):void {
			swfFile = content as ISwfFile;
			if (swfFile == null) {
				throw new OperateError("loader.content 不是 ISwfFile 对象，这可能是加载的路径出错，请查看 MediaAssetItem 传入的 IURL 对象！地址：" + contentLoaderInfo.url, this);
			}
			var url:IURL = swfFile.getSkinURL;
			
			if(skinLoader!=null){
				return;
			}
			var assite:AssetsData;
			
			if(swfFile.getSkinClass){
				var SkinClass:Class = swfFile.getSkinClass;
				var SkinByteArray:ByteArray = new SkinClass();
				if(SkinByteArray){
					skinLoader = new SkinLoader(url,this._loaderContext,LoadType.NoneApplicationDomain,LoadContentType.MEDIA_CONTENT_BY_BYTEARRAY);	
					skinLoader.data = SkinByteArray;
					
					assite = new AssetsData();		
					assite.asssetCompleteFunc = onSkinloaderOver;			
					assite.netErrorFunc = function (event:IOErrorEvent,data:IAssetItem):void{
						getDatainterface.netError(event,data);
					}
					skinLoader.setDatainterface = assite;
					skinLoader.initView();	
					
				}else{
					throw new OperateError("采用编译的 Skin 资源，Embed 的 mimeType 值必须为 application/octet-stream,请检查 "+swfFile+"是否成功指定！");
				}
				
			}else{
				throw new OperateError("请采用 Embed 嵌入 XXXSkin.swf 文件"+swfFile);
				skinLoader = new SkinLoader(url,this._loaderContext,LoadType.NoneApplicationDomain);		
				
				assite = new AssetsData();		
				assite.asssetCompleteFunc = onSkinloaderOver;
				assite.netErrorFunc = function (event:IOErrorEvent,data:IAssetItem):void{
					getDatainterface.netError(event,data);
				}
				skinLoader.setDatainterface = assite;
				skinLoader.initView();			
			}
			
		}
		
		
		private function initModel(skin:MovieClip):void{
			
			
			_isinitView = true;
			_isLoadSuccess = true;
			
			
			createView = swfFile.getCreateView;			
			mediator = swfFile.getMediator;
			
			mediator.addEventListener(DissolveEvent.DISSOLVE,onDissolveHandler);
			mediator.addEventListener(AssetsEvent.COMPLETE_LOAD, onSkinLoadCompleteHandler);
			mediator.FW::view = createView;			
			
			launcher.registerMediator(_loaderContext.applicationDomain.getDefinition(getQualifiedClassName(mediator)) as Class);
			
			
			createView.FW::setContentContainer(swfFile as Sprite,this,skin,mediator,this);
			
			this.addChild(swfFile as Sprite);
			
			if(getDatainterface){
				this.getDatainterface.asssetComplete(this);					
			}		
			
			
			//-----------start----解决多必加载的问题。------
			if (this.notify == null) {
				notify = Mediator.INIT_NOTIFY;
				//Log.out("-dsfdsf----------------ss------------------");
			}		
			//mediator.handerNotify(Mediator.INIT_TYPE,notify);
			mediator.push(Mediator.INIT_TYPE,notify);
			//-------------end----------
			
			this.dispatchEvent(new FrameWorkEvent(FrameWorkEvent.INIT_OVER));	
			
			Log.out("加载用时："+(getTimer()-t));
		}
		private function onSkinloaderOver(data:IAssetItem):void {			
			
			initModel(MovieClip(data.contentLoaderInfo.content));
			
		}
		
		/**
		 * 反注册 
		 * @return 
		 * 
		 */
		public function unregisterMediator():Boolean{
			if(mediator){				
				launcher.unregisterMediator(_loaderContext.applicationDomain.getDefinition(getQualifiedClassName(mediator)) as Class);
				return true;
			}else{
				return false;
			}
		}
		
		protected function onDissolveHandler(event:DissolveEvent):void
		{
			
			this.dispatchEvent(new DissolveEvent(DissolveEvent.DISSOLVE,this));
		}		
		
		
		private function onSkinLoadCompleteHandler(e:AssetsEvent):void {
			mediator.removeEventListener(AssetsEvent.COMPLETE_LOAD, onSkinLoadCompleteHandler);
			this.addEventListener(Event.ENTER_FRAME,onEnterFrameHandler);		
			
		}	
		
		protected function onEnterFrameHandler(event:Event):void
		{
			//Log.out("ENTER_FRAME",this);
			this.removeEventListener(Event.ENTER_FRAME,onEnterFrameHandler);
			notifyMediator();			
			
		}
		protected function notifyMediator():void{
			if(getDatainterface){				
				this.getDatainterface.asssetAllComplete(this);			
			}
			
			if(isINType){
				onAddStageHandler(null);
				isINType =false;
			}
			
			this.notifyType = null;
			this.notify = null;
		}
		/**
		 * 是否正在初始化视图
		 * @return
		 *
		 */
		public function get isinitView():Boolean {
			return _isinitView;
		}
		private var t:Number =0;
		/**
		 * 初始时，也就是执行一个资源的加载，此时可以向  Mediator 层发信息,加载到共享域中</br>
		 * 有可能在 Mediator.INIT_TYPE 类型的之后，可能还有一个 为  Mediator.RE_INIT_TYPE 类型的消息。也会发送。默认情况下，Mediator.RE_INIT_TYPE  消息数据为  Mediator.RE_INIT_NOTIFY，如果不相等的，就满足发送的条件。</br>
		 * 
		 * @param type 如果为 null 将使用 Mediator 中的 Mediator.DEFAULT_TYPE
		 * @param notify
		 * @see com.game.framework.view.Mediator.DEFAULT_TYPE
		 * @see com.game.framework.view.Mediator.DEFAULT_NOTIFY
		 * @see com.game.framework.interfaces.INotifyData
		 * @see com.game.framework.model.NotifyData
		 * @see com.game.framework.view.Mediator
		 */
		override public function initView(notify:INotifyData = null):void {
			t = getTimer();
			
			this.notifyType = type;
			this.notify = notify as NotifyData;	
			
			if (_isinitView) {			
				if (this.notify == null) {
					notify = Mediator.RE_INIT_NOTIFY;
				}
				mediator.FW::isdissolve = false;
				//mediator.handerNotify(Mediator.RE_INIT_TYPE, notify);	
				mediator.push(Mediator.RE_INIT_TYPE,notify);
				
				
				this.notifyType = null;
				this.notify = null;	
				this.getDatainterface.asssetComplete(this);
				this.getDatainterface.asssetAllComplete(this);		
				
				this.dispatchEvent(new FrameWorkEvent(FrameWorkEvent.INIT_OVER));
				return;
			}
			
			if (this.parent == null) {
				throw new OperateError("先添加到显示列表中，UIManager.addMediaView(MediaAssetItem) 加载的地址：" + this.url.url, this);
				return;
			}			
			
			//如果资源没有衩释放，将不重新加载
			if (_isLoadSuccess == true) {
				return;
			}
			if (this.getDatainterface == null) {
				this.setDatainterface = new AssetsData();
			}
			super.initView();
			
			
		}
		
		/**
		 * 释放资源并移除 事件
		 *
		 */
		override public function dispose():void
		{
			//Log.out("释放之前："+this.loaderContext.applicationDomain.domainMemory.length);			
			this.removeEventListener(Event.ADDED_TO_STAGE,onAddStageHandler);
			this.removeEventListener(Event.REMOVED_FROM_STAGE,onRemovedStageHandler);
			
			if(swfFile){
				
				(swfFile as Sprite).removeChildren();
				
			}
			
			if(mediator){
				mediator.removeEventListener(DissolveEvent.DISSOLVE,onDissolveHandler);
				mediator.dispose();				
				launcher.unregisterMediator(_loaderContext.applicationDomain.getDefinition(getQualifiedClassName(mediator)) as Class);				
				mediator=null;
			}		
			if(createView){
				
				createView.dispose();
				createView=null;
			}
			if(skinLoader){
				skinLoader.setDatainterface = null;
				skinLoader.dispose();
				skinLoader = null;
			}
			
			super.dispose();
			
			_isLoadSuccess = false;
			_isinitView = false;
			
			mediator=null;
			skinLoader =null;
			swfFile=null;
			createView=null;
			
			//Log.out("释放之后："+this.loaderContext.applicationDomain.domainMemory.length);
		}
		
		
	}
}