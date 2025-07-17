package Ed 
{
	import flash.display.MovieClip;
	import flash.events.*;
	import flash.utils.Timer;
	
	public class Kretanje 
	{       
		var stvar;


		public function Kretanje() 
		{
				
		}

		public function pravac(stvar, cilj):void
		{
			this.stvar = stvar;
			
			var dijagonala:Number = Math.sqrt(Math.pow((stvar.x - cilj.x), 2) + Math.pow((stvar.y - cilj.y), 2));
			var razX:Number = (cilj.x-stvar.x);
			var razY:Number = (cilj.y-stvar.y);
			stvar.brzX=razX/dijagonala;
			stvar.brzY=razY/dijagonala;
		}
		
		public function rotacija(stvar, cilj):Number
		{
			return(Math.round(Math.atan2((stvar.y-cilj.y),(stvar.x-cilj.x)) * 57.2957795) - 90);
		}
	}
}