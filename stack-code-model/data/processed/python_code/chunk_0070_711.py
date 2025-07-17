package hud {
	
	import hud.ProceduralMessage;
	import net.flashpunk.FP;
	
	public class FailureMessage extends ProceduralMessage {
		
		public function FailureMessage():void {
			super(new Array("FOOL", "DUDE", "AIRHEAD", "N00B"),
			      new Array("DEAD", "TERMINATE", "FAIL", "BLOW"),
				  new Array("YOU", "EASY THING", "WALL IN YOUR HEAD", "I WANNA MOMMY"),
				  0xFF1493);
		}
		
	}

}