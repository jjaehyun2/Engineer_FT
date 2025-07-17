package  
{
	import flash.display.MovieClip;
	import flash.events.TimerEvent;
	import flash.geom.Point;
	import flash.utils.Timer;
	import org.libspark.betweenas3.BetweenAS3;
	import org.libspark.betweenas3.tweens.IObjectTween;
	import org.libspark.betweenas3.easing.Sine;
	import org.libspark.betweenas3.events.TweenEvent;
	import org.libspark.betweenas3.tweens.IObjectTween;
	
	/**
	 * ...
	 * @author sere
	 */
	public class Boss extends MovieClip 
	{
		public var spd:Number = 5;
		public var escapefg = false;
		
		public static const MOTION_TOJO:int = 1;
		public static const MOTION_BATTLE1:int = 2;
		public var motion:int = 0;
		public var life:int = 100 / 2;
		public var muteki_fg:Boolean = true;
		
		public var wait_fg:Boolean = false;
		public function Boss() 
		{
			x = 240;
			y = -250;
			setMotion( MOTION_TOJO );
		}
		public function setMotion(m:int):void 
		{
			motion = m;
			wait_fg = false;
		}
		public function move():void 
		{
			if ( wait_fg ) return;
			if ( escapefg ) return;
			
			switch (motion) 
			{
				case MOTION_TOJO:
					var ot:IObjectTween = BetweenAS3.tween(this, { y:150 }, { y: -250 }, 3, Sine.easeOut );
					ot.addEventListener(TweenEvent.COMPLETE, otcomp_handler );					
					ot.play();
					wait_fg = true;
				break;
				case MOTION_BATTLE1:
					var mp:Point = new Point( this.x -120, this.y + 220 );
					var tama:Tama2 = new Tama2(Math2.getAngle(mp, BattleStage.ins.player));
					tama.x = mp.x;
					tama.y = mp.y;
					BattleStage.ins.setEnetama(tama);
					
					mp = new Point( this.x +120, this.y + 220 );
					tama = new Tama2(Math2.getAngle(mp, BattleStage.ins.player));
					tama.x = mp.x;
					tama.y = mp.y;
					BattleStage.ins.setEnetama(tama);
					
					mp = new Point( this.x +120, this.y + 220 );
					tama = new Tama2(Math2.getAngle(mp, BattleStage.ins.player));
					tama.x = mp.x;
					tama.y = mp.y;
					BattleStage.ins.setEnetama(tama);
					
					
					var tim:Timer = new Timer( 1500, 1 );
					tim.addEventListener(TimerEvent.TIMER_COMPLETE, tim_handler );
					tim.start();
					wait_fg = true;
				break;
				default:
					
				break;
			}
		}
		public function tim_handler(e:TimerEvent):void 
		{
			setMotion( MOTION_BATTLE1 );
			trace( "tim" );
		}
		public function otcomp_handler(e:TweenEvent):void 
		{
			setMotion( MOTION_BATTLE1 );
			muteki_fg = false;
		}
	}

}