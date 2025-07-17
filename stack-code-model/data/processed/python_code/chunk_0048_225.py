package  {
	
	import flash.display.MovieClip;
	import flash.utils.Timer;
	import flash.events.TimerEvent;
	import flash.events.MouseEvent;
	import fl.motion.MotionEvent;
	
	
	public class Enemy extends MovieClip {
		var timer:Timer = new Timer(1000 , 1);
		var Destroyed:Boolean = true;
		static var score:Number=0;
		static var scoretext:Score;
		public function Enemy(S:Score, GameTimer:Timer) {
			// constructor code
			var randomTime = Math.random() * 2000 + 1000;
			scoretext=S;
			timer.delay = randomTime;
			timer.addEventListener(TimerEvent.TIMER_COMPLETE , Destroy);
			this.addEventListener(MouseEvent.CLICK , AddScore);
			GameTimer.addEventListener(TimerEvent.TIMER_COMPLETE , END);
			timer.start();
		}
		function Destroy(e:TimerEvent)
		{
			if(Destroyed)
			{
				stage.removeChild(this);
				Destroyed = false;
			}
		}
		function AddScore(e:MouseEvent)
		{
			Destroyed=false;
			score++;
			scoretext.AddScore(score);	
			stage.removeChild(this);
		}
		function END(E:TimerEvent)
		{
			if(Destroyed)
			{
				stage.removeChild(this);
				Destroyed = false;
			}

		}
	}
	
}