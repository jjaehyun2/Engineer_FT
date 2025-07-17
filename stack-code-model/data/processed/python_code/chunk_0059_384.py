/*Author: Akram Taghavi-Burris
  Project: Case Statements
  Created: March 1, 2013
  Updated: March 4, 2013 */
 
package 
{
  import flash.display.MovieClip;
	import flash.events.Event; //imports stage events
	import flash.events.TimerEvent;
	import flash.utils.Timer;
 
	public class CharDance extends MovieClip
	{
		private var _timerInterval:Number = 200; //How long the timer is, in milliseconds
		private var _randomFrameTimer:Timer; //New timer
		private var _numFrames:Number = 5; //Total number of sweetie frames
		private var _stageWidth: Number; //Width of stage
		private var _Width:Number; //The objects width
		private var _Scale:Number; //The objects scale
		private var _origX:Number; //The objects orignial X positon
		private var _maxX:Number ; //The maximum X position 
		private var _minX:Number ; //The minimum X position
		private var _xChange:Number = 15; //The amount of change in the X position
		private var _maxScale:Number = 1.2; //The maximum amount of scale
		private var _minScale:Number = .7; //the minimum amount of scale
		private var _scaleChange:Number = .05; //The amount of change in the scale
 
 
		public function CharDance()
		{// constructor function runs an init() function
		
			this.addEventListener(Event.ADDED_TO_STAGE, _init);
			/*because we want to set the stage widht,, and we can't the stage until the object is on the stage, 
			  we will at this point check to see if our character has been ADDED_TO_STAGE, if so it will run 
			  the next function */
			
			
			
 
		}
		//end constructor function;
		
		private function _init(e:Event):void{
 
			_randomFrameTimer = new Timer(_timerInterval); //creates a timer
			_randomFrameTimer.addEventListener(TimerEvent.TIMER,_danceMoves);
			//calls the danceMoves functions;
			//listens for the timer;
			_randomFrameTimer.start();
			
			_origX = this.x; // find the objects X postion (this value is set after the objec is added to the stage)
			_Width = this.width; // finds the width of the object
			
		}
		
		
		private function _doMath():void{
			_stageWidth = stage.stageWidth/2; //finds half the size of the stage, so the character remains on one side of the stage
			_Scale = this.scaleX; //this sets the current objects scale
			_maxX = (_stageWidth + _origX) - (_Width * _Scale); //determines the maximum X value by subtracting 1/2 the objects width from the stage width
			_minX = _origX; //determines the minimum X value by adding 1/2 the objects width to the 0 point of the stage
			
		}
 
 
		private function _danceMoves(e:TimerEvent):void
		{
			_doMath();
 
			var randomFrame = Math.round(Math.random() * _numFrames); //moves to a random number based on the number of frames possible.
 
			switch (randomFrame)
			{
				case 1 :
					//try to get her to move forward
					if (this.scaleX <= _maxScale)
					{
						this.scaleX +=  _scaleChange;
						this.scaleY +=  _scaleChange;
					}
					else
					{
						this.scaleX -=  _scaleChange;
						this.scaleY -=  _scaleChange;
					}
					break;
 
				case 2 :
					//try to get her to move right
					if (this.x <= _maxX)
					{
						this.x +=  _xChange;
					}
					else
					{
						this.x -=  _xChange;
					}
					break;
 
				case 3 :
					//try to get her to move backwards
					if (this.scaleX >= _minScale)
					{
						this.scaleX -=  _scaleChange;
						this.scaleY -=  _scaleChange;
					}
					else
					{
						this.scaleX +=  _scaleChange;
						this.scaleY +=  _scaleChange;
					}
					break;
 
 
				case 4 :
					//try to get him to move left
					if (this.x >= _minX)
					{
						this.x -=  _xChange;
					}
					else
					{
						this.x +=  _xChange;
					}
					break;
 
				default :
					break;
			}//end switch
 
			this.gotoAndStop(randomFrame);
 
		}//end danceMoves();
 
	}//end class
 
}//end package