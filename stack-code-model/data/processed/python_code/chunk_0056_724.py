package modules.game.majiangGame.view.animation
{
	import common.event.EventCenter;
	
	import laya.display.Animation;
	import laya.display.Sprite;

	public class HuAnimation extends Sprite
	{
		public static function get instance():HuAnimation
		{
			return new HuAnimation();;
		}
		
		//huoyandonghua
		protected var ani_shandian:Animation;
		protected var ani_huoyan:Animation;
		
		public function HuAnimation()
		{
			ani_shandian = new Animation();
			ani_shandian.loadAtlas("res/animations/huangseshandian.json");
			ani_shandian.stop();
			
			ani_huoyan = new Animation();
			ani_huoyan.loadAtlas("res/animations/huoyandonghua.json");
			ani_huoyan.stop();
			
			
			this.addChild(ani_shandian);
			this.addChild(ani_huoyan);
			
			ani_shandian.x = (this.width - ani_huoyan.width)/2;
			
			ani_huoyan.y = 300;
			this.y = -300;
			
			EventCenter.instance.on(EventCenter.MAJIANGPAGE_NOTICE_HUEFF_HIDE,this,hide);
			
			hide();
		}
		
		public function play():void
		{
			ani_shandian.play(0,false);
			ani_huoyan.play();
			show();
		}
		
		public function show():void
		{
			this.visible = true;
		}
		
		public function noticeHide():void
		{
			EventCenter.instance.event(EventCenter.MAJIANGPAGE_NOTICE_HUEFF_HIDE);
		}
		
		public function hide():void
		{
			ani_shandian.stop();
			ani_huoyan.stop();
			
			this.visible = false;
		}
	}
}