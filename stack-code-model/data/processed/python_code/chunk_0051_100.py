﻿/*
This class get initialized in the Constructor of the Game class.
This class manages basic key presses, user input.
You can just use this class by calling: Key.isDown(Keyboard.LEFT) from other classes like in AS2.0.
*/

package 
{
    
    import flash.display.Stage;
    import flash.events.Event;
    import flash.events.KeyboardEvent;

    public class Key {
        
        private static var initialized:Boolean = false;
        public static var keysDown:Object = new Object();  // stores key codes of all keys pressed

        public static function initialize(stage:Stage) {
            if (!initialized) {
                // assign listeners for key presses and deactivation of the player
                stage.addEventListener(KeyboardEvent.KEY_DOWN, keyPressed);
                stage.addEventListener(KeyboardEvent.KEY_UP, keyReleased);
                stage.addEventListener(Event.DEACTIVATE, clearKeys);
                
                // mark initialization as true so redundant
                // calls do not reassign the event handlers
                initialized = true;
            }
        }
        
		
        public static function isDown(keyCode:uint):Boolean 
		{
			
            return Boolean(keyCode in keysDown);
        }
        
		
        private static function keyPressed(event:KeyboardEvent):void {
            keysDown[event.keyCode] = true;
        }
        

        private static function keyReleased(event:KeyboardEvent):void {
            if (event.keyCode in keysDown) {
                delete keysDown[event.keyCode];
            }
        }
        

        public static function clearKeys(event:Event):void {
            // clear all keys in keysDown since the player cannot detect keys being pressed or released when not focused
            keysDown = new Object();
        }
    }
}