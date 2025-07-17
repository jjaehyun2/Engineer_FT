package common.baseui
{
	import common.event.EventCenter;
	
	import laya.display.Sprite;
	import laya.net.Loader;
	import laya.utils.Handler;
	
	import manager.LoadingManager;
	import manager.UIManager;

	public class UIBase
	{
		
		protected var _isShow:Boolean = false;
		protected var container:Sprite;
		protected var skinRes:String = "";
		protected var _isLoaded:Boolean = false;
		
		public function UIBase(container:Sprite=null)
		{
			if(container==null)
			{
				this.container = UIManager.instance.uiLayer;
			}
			else
			{
				this.container = container;
			}
			
			EventCenter.instance.on(EventCenter.HALLVIEW_GOTOHOME,this,onGotoHome);
		
		}
		
		protected function onGotoHome(data:Object):void
		{
			hide();
		}
		
		public function show():void
		{
			_isShow = true;
			if(this.skinRes==""){
				if(!_isLoaded)
				{
					this.onLoaded();
				}
				return;
			}
			if(!_isLoaded)
			{
				LoadingManager.instance.showLoadPro(this);
				Laya.loader.load([{url: skinRes, type: Loader.ATLAS}],Handler.create(this, onLoaded),
					Handler.create(this,onProgress,null,false)//
				);
				
			}
		}
		
		private function onProgress(v):void
		{
			LoadingManager.totalProgress = v;
		}
		
		protected function onLoaded():void
		{
			LoadingManager.totalProgress = 1;
			_isLoaded = true;
		}
		
		public function hide():void
		{
			_isShow = false;
		}
		
		public function dispose():void
		{
			
		}
	}
}