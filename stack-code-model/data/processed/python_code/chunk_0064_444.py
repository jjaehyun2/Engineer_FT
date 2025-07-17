package common.view
{
	import laya.events.Event;
	import laya.html.dom.HTMLDivElement;
	import laya.maths.Rectangle;
	
	import manager.UIManager;
	
	import ui.common.NoticeInfoViewUI;

	public class NoticeInfoView
	{
		protected var _skin:NoticeInfoViewUI;
		
		protected var infoTf:HTMLDivElement;
		
		protected var caller:*;
		protected var callBack:Function;
		
		public function NoticeInfoView()
		{
			_skin = new NoticeInfoViewUI();
			
			init();
		}
		
		protected function init():void
		{
			infoTf = _skin.infoTf;
			infoTf.style.color="#ffffff";
			infoTf.style.fontSize = 25;
			infoTf.style.lineHeight = 40;
			infoTf.scrollRect = new Rectangle(0,0,infoTf.width,infoTf.height);
			QuickUtils.addHTextScroll(infoTf);  
			_skin.confirmBtn.on(Event.CLICK,this,onClickConfirm);
			
		}
		
		public function showInfo(info:String,caller:*=null,callBack:Function=null):void
		{
			this.caller = caller;
			this.callBack = callBack;
			info = QuickUtils.html_decode(info);
			infoTf.innerHTML = info;
			
			show();
		}
		
		
		
		public function show():void
		{
			QuickUtils.AddCenter(_skin,UIManager.instance.popLayer);
		}
		
		public function hide():void
		{
			_skin && _skin.removeSelf();
		}
		
		protected function onClickConfirm(e:Event):void
		{
			if(this.callBack != null  && caller)
			{
				callBack.apply(caller,[0]);
				
			}
			
			hide();
		}
	}
}