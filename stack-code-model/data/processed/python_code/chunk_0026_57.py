package local.display
{
	import flash.display.MovieClip;
	
	import elemental.display.Rotator;
	
	public class ActivityIndicator extends MovieClip
	{
		// makes a new rotator, to edit the color of it,
		// put a new hex code in as the argument
		private var rotator: Rotator = new Rotator(0x000000);
		
		public function ActivityIndicator() : void
		{
			// starts the rotator spinning
			rotator.start();
			// adds it to the display list
			addChild(rotator);
			
			// cut down the scale a bit, their big,
			// full scale is 1, change the number to
			// change the scaling
			rotator.scaleX = rotator.scaleY = .3;
			// put it where it needs to be, above the text
			// the higher the number, the lower the placement
			rotator.y = -180;
			
			// this makes it not interfere with the mouse
			mouseEnabled = false;
			mouseChildren = false;
			
			hide();
		}
		
		// call this function to show the activity indicator
		public function show() : void
		{
			if (rotator == null)
				return void;
			
			visible = true;
			rotator.start();
		}
		
		// call this function to hide the activity indicator
		public function hide() : void
		{
			if (rotator == null)
				return void;
			
			visible = false;
			rotator.stop();
		}
	}
}