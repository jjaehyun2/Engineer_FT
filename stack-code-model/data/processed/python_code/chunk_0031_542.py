package hall.view
{
	import common.baseui.UIBase;
	
	import laya.display.Sprite;
	
	import ui.hall.FeedbackViewUI;

	public class FeedbackView extends UIBase
	{
		protected var _skin:FeedbackViewUI;
		public function FeedbackView(container:Sprite=null)
		{
			super(container);
			skinRes = "res/atlas/hall/feedbackView.atlas";
		}
		
		protected override function onLoaded():void
		{
			trace('rechargeView.atlas')
			super.onLoaded();
			_skin = new FeedbackViewUI();
			_skin.mouseEnabled = true;
			if(_isShow)
			{
				container.addChild(_skin);
			}
			
			init();
			
			if(ModuleDef.CurGameModule && ModuleDef.CurGameModule.inGame)
			{
				hide();
				//HallModule.instance.goEmpty();
			}
		}
		
		protected function init():void
		{
//			this._skin.homeBtn.on(Event.CLICK,this,function():void{
//				this.hide();
//			});//返回大厅
//			_skin.chongzhiBtn.on(Event.CLICK,this,function():void{
//				this.hide();
//				EventCenter.instance.event(HallMainView.HALLVIEW_GOTORECHARGE);
//			});//充值
//			_skin.share.on(Event.CLICK,this,function():void{
////				this.hide();
//				EventCenter.instance.event(HallMainView.HALLVIEW_GOTOSHARE);
//			});//分享
//			_skin.feedback.on(Event.CLICK,this,function():void{
//				EventCenter.instance.event(HallMainView.HALLVIEW_GOTOFEEDBACK);
////				this.hide();
//			});//反馈
//			_skin.recordBtn.on(Event.CLICK,this,function():void{
//				this.hide();
//				EventCenter.instance.event(HallMainView.HALLVIEW_GOTORECORD);
//			});//战绩	
		}
		
		public override function show():void
		{
			super.show();
			if(_skin)
			{
				container.addChild(_skin);
			}
		}
		
		public override function hide():void
		{
			super.hide();
			if(_skin && _skin.parent)
			{
				_skin.parent.removeChild(_skin);
			}
		}
	}
}