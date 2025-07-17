/*
 * Class: Loop Iterator
 * @author Ryan C. Knaggs
 * @date 09/18/2009
 * @since 1.0
 * @version 1.1 - Refactored the fade effect 10/08/2009
 * @version 1.2 - Refactored the fade effect 10/09/2009
 * @description: Interator for display objects
 */

package utils.displayObject
{
	
	import flash.events.*;
	
	import libs.vo.GlobalsVO;
	
	
	public class LoopIterator extends EventDispatcher
	{
		
		
		public function LoopIterator() {
		}
		
		private var _app:Object;
		private var _iterator:Number;
		private var _loop:Function;
		private var _effect:Object;
		
		
		/**
		 * Initialize to count up or down 
		 * @param effect
		 */
		 		
		public function init(effect:Object):void {
			this._effect = effect;
			this._iterator = effect.from;
			
			if(effect.from < effect._to) {
			
				_isCountUp = true;
				_loop = function():void {
					if(_iterator >= effect._to) {
						stop();
						dispatchEvent(new Event(Event.COMPLETE));
					}
					_iterator += effect.step;
					dispatchEvent(new Event(Event.CHANGE));
				}
				
			} else {
				
				_isCountUp = false;
				_loop = function():void {
					if(_iterator <= effect._to) {
						stop();
						dispatchEvent(new Event(Event.COMPLETE));
					}
					
					_iterator -=effect.step;
					dispatchEvent(new Event(Event.CHANGE));
				}					
			}
		}
		
		private var _isCountUp:Boolean;
		
		
		
		/*****************************
		 * API
		 *****************************/
		public function get isCountUp():Boolean {
			return _isCountUp;
		}
		
		
		
		/**
		 * Get the current value of the iteration
		 * @return _iterator:Number - Current Value
		 * of the iteration
		 */		
		 
		public function get value():Number {
			return _iterator;
		}
		
		
		
		/**
		 * Play the Effect 
		 */
		 		
		public function play():void {
			 enterFrame();
	    }
	    
	    
	   
	  	public function enterFrame():void {
	  		if(_app != null) {
	  			_app.removeEventListener(Event.ENTER_FRAME,onEnterFrame);
	  		}
	  		_app = GlobalsVO.getGlobal(GlobalsVO.APPLICATION);
			_app.addEventListener(Event.ENTER_FRAME,onEnterFrame); 
		}
		
		
		public function onEnterFrame(e:Event):void {
			_loop();
		}
	    
	    
	    
	    
	    public function stop():void {
	    	try {
	  			_app.removeEventListener(Event.ENTER_FRAME,onEnterFrame);
	    	} catch(e:Error) {}
	    	
	    }
		
	}
	
}