package 
{
	import flash.display.MovieClip;
	
	/**
	 * ...
	 * @author Ben Mason
	 */
	public class Screen extends MovieClip implements IScreen
	{
		public function Screen() { }
		
		public function add(... movieClips:Array):void {
			for each (var movieClip:MovieClip in movieClips) {
				addChild(movieClip);
			}
		}
		
		public function remove(... movieClips:Array):void {
			for each (var movieClip:MovieClip in movieClips) {
				if (this.contains(movieClip)) this.removeChild(movieClip);
			}
		}
	}
}