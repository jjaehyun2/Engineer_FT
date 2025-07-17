package lib 
{
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.media.SoundTransform;
	/**
	 * ...
	 */
	public class Application 
	{
		protected var sprite			: Sprite;
		protected var event				: Event;
		protected var mouse_event		: MouseEvent;
		public function Application() 
		{
			sprite			= new Sprite();
			event			= new Event();
			mouse_event		= new MouseEvent();
		}
		
	}

}