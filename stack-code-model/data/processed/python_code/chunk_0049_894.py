package org.pong.mvcs.view.component.paddle 
{
	import flash.ui.Keyboard;
	import org.pong.mvcs.view.component.AbstractPaddleView;
	
	/**
	 * More specialized child of AbstractPaddleView object.
	 * 
	 * @see org.pong.mvcs.view.component.AbstractPaddleView
	 * 
	 * @author mc
	 */
	public class LeftPaddleView extends AbstractPaddleView 
	{	
		/**
		 * 
		 */
		public function LeftPaddleView() 
		{
			super();
		}
		
		/**
		 * 
		 * Definition of upward movement key.
		 * 
		 * @return KeyCode that will initiate upward movment of paddle object. Abstract method. Define to move up.
		 */
		override protected function setKeyCodeUp():uint
		{
			return Keyboard.W;
		}
		
		/**
		 * 
		 *  Definition of downward movement key.
		 * 
		 * @return KeyCode that will initiate downward movment of paddle object. Abstract Method. Define to move down.
		 */
		override protected function setKeyCodeDown():uint
		{
			return Keyboard.S;
		}
		
		/**
		 * Called to set inital view values - like position. 
		 */
		override public function setInitaialValues():void
		{
			this.x = xPosition - this.width;
			this.y = stage.height / 2 - this.height / 2;
		}
	}

}