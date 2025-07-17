package classes 
{
	import com.greensock.TweenLite;
	import flash.display.Sprite;
	/**
	 * ...
	 * @author Lucas Moyano
	 */
	public class Flash extends Sprite
	{
		
		public function Flash() 
		{
			visible = false;
		}
		
		public function play():void
		{
			Sounds.play(Sounds.audioFlash);
			visible = true;
			alpha = 1;
			TweenLite.to(this, 2, { alpha:0, onComplete:function() { visible = false; } } );
		}
		
	}

}