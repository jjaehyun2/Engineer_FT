package common.view
{
	import laya.display.Sprite;
	import laya.display.Text;
	import laya.ui.Image;
	import laya.utils.Handler;
	import laya.utils.Tween;
	
	import manager.UIManager;

	public class PopMessageBox extends Sprite
	{
		protected var tf:Text;
		protected var bg:Image;
		
		public function PopMessageBox()
		{
			bg = new Image("common/commonTitBg.png");
			bg.sizeGrid = "20,20,20,20";
			bg.y = -12;
			tf = new Text();
			tf.x = 10;
			tf.fontSize = 25;
			tf.color = "#ffffff";
			this.addChild(bg);
			this.addChild(tf);
		}
		
		override public function get width():Number
		{
			return tf.width+20;
		}
		
		override public function get height():Number
		{
			return tf.height+30;
		}
		
		public function show():void//因为没有使用dialog的
		{
			QuickUtils.AddCenter(this,UIManager.instance.popLayer,0,-150);
		}
		
		public function hide():void
		{
			if(this.parent)
			{
				this.parent.removeChild(this);
			}	
		}
		
		public function pop(msg:String):void
		{
			tf.text = msg;
			tf.width = tf.textWidth+5;
			bg.width = this.width;
			bg.height = this.height;
			this.alpha = 1;
			show();
			Tween.clearTween(this);
			Laya.timer.once(2000,this,tweenHide);
		}
		
		protected function tweenHide():void
		{
			Tween.to(this,{alpha:0},1000,null,Handler.create(this,hide));
		}
	}
}