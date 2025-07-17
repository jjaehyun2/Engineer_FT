package com.lowoui_as.events 
{
    import flash.display.InteractiveObject;
    import flash.events.Event;
    import flash.events.MouseEvent;
    
    public class GameOptionEvent extends Event 
	{
        public static const SETTINGS:String  = "gameSettings";
        public static const PREVSCENE:String = "prevScene";
        public static const QUITGAME:String  = "quitGame";
        
        public function GameOptionEvent(type:String, bubbles:Boolean = true, cancelable:Boolean = false) {
            super(type, bubbles, cancelable);
        }
        override public function clone():Event {
            return new ButtonEvent(type, bubbles, cancelable);
        }
        
        override public function toString():String {
            return formatToString("GameOptionEvent", "type", "bubbles", "cancelable");
        }
    }
}