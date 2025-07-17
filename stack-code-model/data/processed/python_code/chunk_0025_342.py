package org.pong.mvcs.view.component 
{
	import org.pong.mvcs.view.AbstractSpriteView;
	import starling.core.Starling;
	import starling.display.Image;
	import starling.events.KeyboardEvent;
	
	/**
	 * 
	 * General behavior of paddle object, abstract class that contains shared paddle functionality.
	 * 
	 * @author mc
	 */
	public class AbstractPaddleView extends AbstractSpriteView 
	{		
		/**
		 * Paddle speed of movment.
		 */
		private var _velocity:uint = 500;
		
		/**
		 * x coordinate paddle position. Never changes.
		 */
		private var _xPosition:uint = 75;
		
		/**
		 * Flag that upward indicates movement in next update.
		 */
		private var _moveUpFlag:Boolean = false;
		
		/**
		 * Flag that downward indicates movement in next update.
		 */
		private var _moveDownFlag:Boolean = false;
		
		/**
		 * Key code to initiate move up. Defined in derived classes.
		 * 
		 * @see setKeyCodeUp()
		 */
		private var _keyCodeUp:uint;
		
		/**
		 * Key code to initiate move down. Defined in derived classes.
		 * 
		 * @see setKeyCodeDown()
		 */
		private var _keyCodeDown:uint;
		
		/**
		 * x coordinate position getter. Read only.
		 */
		public function get xPosition():uint 
		{
			return _xPosition;
		}
		
		/**
		 * const
		 */
		public function AbstractPaddleView() 
		{
			super();
			
			setKeyCode();
		}
		
		/**
		 * Key codes setter.
		 * 
		 * @private
		 */
		private function setKeyCode():void
		{
			_keyCodeUp = setKeyCodeUp();
			_keyCodeDown = setKeyCodeDown();
		}
		
		/**
		 * 
		 * Abstract function to define upward movement initiator. Which keyboard button to move up.
		 * 
		 * @return Key code <code>uint</code> value.
		 */
		protected function setKeyCodeUp():uint
		{
			throw("setKeyCodeUp() must be override as it is an abstract method.");
			return 0;
		}
		
		/**
		 * 
		 * Abstract function to define upward movement initiator.  Which keyboard button to move down.
		 * 
		 * @return Key code <code>uint</code> value.
		 */
		protected function setKeyCodeDown():uint
		{
			throw("setKeyCodeDown() must be override as it is an abstract method.");
			return 0;
		}
		
		/**
		 * Called when component added to stage. Sets graphic, initial values, and listeners.
		 */
		override public function added():void
		{
			super.added();
	
			setGraphic();
			setInitaialValues();
			setKeyListeners();
		}
		
		/**
		 * Sets paddle graphic image. It will also set the view with and height to the same values as graphic.
		 */
		private function setGraphic():void
		{
			graphic = graphicUtils.paddle;
			this.addChild(graphic);
			
			this.width = graphic.width;
			this.height = graphic.height;
		}
		
		/**
		 * Abstract method - used by derived classes to define initial values. For example position.
		 */
		public function setInitaialValues():void
		{
			throw("setInitaialValues() must be override as it is an abstract method.");
		}
		
		/**
		 * Key listener setter.
		 * 
		 * @private
		 */
		private function setKeyListeners():void
		{			
			Starling.current.stage.addEventListener(KeyboardEvent.KEY_DOWN, onKeyDown);
			Starling.current.stage.addEventListener(KeyboardEvent.KEY_UP, onKeyUp);
		}
		
		/**
		 * 
		 * Key down key pressed handler. Will set key down flag to <code>true</code>.
		 * 
		 * @param	event Keyboard event
		 */
		protected function onKeyDown(event:KeyboardEvent):void
		{
			if (event.keyCode == _keyCodeUp)
				_moveUpFlag = true;
			else if (event.keyCode == _keyCodeDown)
				_moveDownFlag = true;
		}
		
		/**
		 * 
		 * Key up key pressed handler. Will set key up flag to <code>true</code>.
		 * 
		 * @param	event Keyboard event
		 */
		protected function onKeyUp(event:KeyboardEvent):void
		{
			if (event.keyCode == _keyCodeUp)
				_moveUpFlag = false;
			else if (event.keyCode == _keyCodeDown)
				_moveDownFlag = false;
		}
		
		/**
		 * destructor
		 */
		override public function removed():void
		{
			removeKeyListeners();
			
			super.removed();
		}
		
		/**
		 * 
		 * Key listener destructor.
		 * 
		 * @private
		 */
		private function removeKeyListeners():void
		{
			trace(this + " removeKeyListeners()");
			
			Starling.current.stage.removeEventListener(KeyboardEvent.KEY_DOWN, onKeyDown);
			Starling.current.stage.removeEventListener(KeyboardEvent.KEY_UP, onKeyUp);
		}
		
		/**
		 * 
		 * Calculates next moment position by using movement flags.
		 * 
		 * @private
		 */
		private function updatePaddleMovement(passedTime:Number):void
		{
			if (_moveUpFlag && this.y > 0)
				this.y -= _velocity * passedTime;
			else if (_moveDownFlag && this.y + this.height < stage.height)
				this.y += _velocity * passedTime;
		}
		
		/**
		 * View tick updater. Called every frame.
		 * 
		 * @param	passedTime Time passed since the last frame/signal.
		 */
		override public function update(passedTime:Number):void
		{
			super.update(passedTime);
			
			updatePaddleMovement(passedTime);
		}
	}

}