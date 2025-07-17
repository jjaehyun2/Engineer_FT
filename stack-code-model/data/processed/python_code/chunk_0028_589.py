/*Author: Akram Taghavi-Burris
  Project: If-Else
  Created: March 1, 2013
  Updated: March 4, 2013 */

package 
{
  import flash.display.MovieClip;
	import flash.events.KeyboardEvent;
	import flash.events.Event; //imports stage events

	public class CharMove extends MovieClip
	{
		private var _stageWidth: Number; //Width of stage
		private var _maxX:Number //The maximum X position 
		private var _minX:Number //The minimum X position
		private var _Xpos:Number; //X position of object
		private var _Ypos:Number; //Y postiion of object
		private var _Width:Number; //Width of obect
		private var _myKey:uint; //Key code (used to determine what key is pressed)

		public function CharMove()
		{
			// constructor code

			this.addEventListener(Event.ADDED_TO_STAGE, _init);
			/*because we have to listen to the stage for the keyboard press, and we can't 
			  listen until the object is on the stage, we will at this point check to see
			  if our character has been ADDED_TO_STAGE, if so it will run the next function */

		}//end constructor function

		private function _init(e:Event):void
		{
			
			_stageWidth = stage.stageWidth; //finds the size of the stage (this has to be done after the object is added to the stage
			_Width = this.width; // finds the width of the object
			_maxX = _stageWidth - (_Width/2); //determines the maximum X value by subtracting 1/2 the objects width from the stage width
			_minX = 0 + (_Width/2); //determines the minimum X value by adding 1/2 the objects width to the 0 point of the stage
			
			this.stage.addEventListener(KeyboardEvent.KEY_DOWN,_myKeyDown);
			/*here we can listen for the stage, keyboard press*/
		}

		private function _myKeyDown(e:KeyboardEvent):void
		{

			trace(this.x);
			trace(e.keyCode);
			
			_Xpos = this.x;
			_Ypos = this.y;
			_myKey = e.keyCode;
			
			_checkKey();

		}//end _myKeyDown()
		
		private function _checkKey():void
		{
			if (_myKey == 39 && _Xpos < _maxX)
			{//If the keycode is equal to 39 (right)
				_Xpos +=  5;
				this.x = _Xpos;

			}//end if
			
			else if (_myKey == 37 && _Xpos > _minX){
				_Xpos -=  5;
				this.x = _Xpos;
			}
			else
			{
				this.x = _Xpos;

			}//end else
		}//end _checkKey

	}//end class

}//end package