package common.view
{
	import laya.events.Event;
	
	import manager.UIManager;
	
	import ui.common.PopBoxUI;
	
	
	public class PopBox extends PopBoxUI
	{
		
		public static const BTN_QUEREN:String = "BTN_QUEREN";
		public static const BTN_MATCH:String = "BTN_MATCH";
		
		/**不显示按钮*/
		public static const BTN_NONE:String = "BTN_NONE";
		
		/**同意拒绝*/
		public static const BTN_LABEL_TONGYIJUJUE:String = "BTN_LABEL_TONGYIJUJUE";
		
		/**确定取消*/
		public static const BTN_LABEL_QUEDINGQUXIAO:String = "BTN_LABEL_QUEDINGQUXIAO";
		
		public static const BTN_ENDGAME:String = "BTN_ENDGAME";
		
		protected var _labels:String = BTN_NONE;
		
		public var caller:*;
		public var callback:Function;
		
		protected var _params:Array;
		
		public function PopBox(content:String,labels:String,caller:*,callback:Function ,
							   title:String="提示",align:String="left",params:Array=null,fontSize:int=30)
		{
			super();
		
			this._labels = labels;
			
			this.caller = caller;
			this.callback = callback;
			this._params = params;
			
			this.txtTitle.text=title;
			this.txtBody.fontSize = fontSize;
			this.txtBody.text=content;
			this.txtBody.align=align;
			
			QuickUtils.AddTextScroll(this.txtBody.textField);
			
			agreeBtn.on(Event.CLICK,this,onClickAgree);
			refuseBtn.on(Event.CLICK,this,onClickRefuse);
			btnCLose.on(Event.CLICK,this,onClickClose);
			confirmBtn.on(Event.CLICK,this,onClickAgree);
			
			endViewReportBtn.on(Event.CLICK,this,onClickAgree);
			endToHallBtn.on(Event.CLICK,this,onClickRefuse);
			
			swicthLabels();
			
		}
		
		protected function onClickAgree(e:Event):void
		{
			trace("dianjile onClickAgree:: "+this.callback);
			
			if(this.callback != null  && caller)
			{
				if(_params)
				{
					trace("dianjile onClickAgree");
					callback.apply(caller,[0,_params]);
				}
				else
				{
					callback.apply(caller,[0]);
				}
				
			}
			onhide();
		}
		
		protected function onClickRefuse(e:Event):void
		{
			if(this.callback != null && caller)
			{
				if(_params)
				{
					callback.apply(caller,[1,_params]);
				}
				else
				{
					callback.apply(caller,[1]);
				}
				
			}
			onhide();
		}
		
		protected function onClickClose(e:Event):void
		{
			if(callback && caller)
			{
				callback.apply(caller);
			}
			
			onhide();
		}
		
		protected function swicthLabels():void
		{
			switch(this._labels)
			{
				case BTN_NONE:
					btnCLose.visible = true;
					agreeBtn.visible = false;
					refuseBtn.visible = false;
					confirmBtn.visible = false;
					endViewReportBtn.visible = false;
					endToHallBtn.visible = false;
					break;
				case BTN_LABEL_TONGYIJUJUE:
					btnCLose.visible = false;
					agreeBtn.visible = true;
					refuseBtn.visible = true;
					confirmBtn.visible = false;
					endViewReportBtn.visible = false;
					endToHallBtn.visible = false;
					
					agreeBtn.label = "同意";
					refuseBtn.label = "拒绝";
					
//					agreeBtn.skin = "gametable/同意.png";
//					refuseBtn.skin = "gametable/拒绝.png";
					break;
				case BTN_LABEL_QUEDINGQUXIAO:
					btnCLose.visible = false;
					agreeBtn.visible = true;
					refuseBtn.visible = true;
					confirmBtn.visible = false;
					endViewReportBtn.visible = false;
					endToHallBtn.visible = false;
					
//					agreeBtn.skin = "gametable/确定.png";
//					refuseBtn.skin = "gametable/取消.png";
					break;
				case BTN_QUEREN:
					btnCLose.visible = false;
					agreeBtn.visible = false;
					refuseBtn.visible = false;
					confirmBtn.visible = true;
					endViewReportBtn.visible = false;
					endToHallBtn.visible = false;
					
					confirmBtn.label = "确定";
					break;
				case BTN_MATCH:
					btnCLose.visible = false;
					agreeBtn.visible = false;
					refuseBtn.visible = false;
					confirmBtn.visible = true;
					endViewReportBtn.visible = false;
					endToHallBtn.visible = false;
					
					confirmBtn.label = "取消匹配";
					break;
				
				
				case BTN_ENDGAME:
					btnCLose.visible = false;
					agreeBtn.visible = false;
					refuseBtn.visible = false;
					confirmBtn.visible = false;
					
					endViewReportBtn.visible = true;
					endToHallBtn.visible = true;
					
					
					break;
				
				default:
					
					
					
					
					break;
			}
		}
		
		public function onshow():void//因为没有使用dialog的
		{
			QuickUtils.AddCenter(this,UIManager.instance.popLayer);
		}
		
		public function onhide():void
		{
			this.removeSelf();
		}
	}
}