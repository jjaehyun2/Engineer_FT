/*
 * The MIT License (MIT)
 *
 * Copyright (c) 2015 Andrew Salomatin (MerlinDS)
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

package systems
{

	import components.Display;
	import components.Label;

	import flash.events.MouseEvent;

	import org.gimmick.collections.IEntities;
	import org.gimmick.core.Gimmick;
	import org.gimmick.core.IEntity;
	import org.gimmick.core.IIdleSystem;

	/**
	 * This system controls pause button.
	 */
	public class GUISystem implements IIdleSystem
	{

		private var _onPause:Boolean;
		private var _entities:IEntities;
		//======================================================================================================================
//{region											PUBLIC METHODS
		public function GUISystem()
		{
		}

		public function initialize():void
		{
			_entities = Gimmick.getEntities(Label);//only button has label component
		}

		public function dispose():void
		{
			_entities.dispose();
			_entities = null;
		}

		public function activate():void
		{
			_onPause = true;
			_entities.begin();//in over case collection has only one entity
			var button:IEntity = _entities.current;
			var display:Display = button.get(Display);
			//add click listener and initialize label
			display.view.addEventListener(MouseEvent.CLICK, this.clickHandler);
			this.clickHandler();
		}

		public function deactivate():void
		{
			//remove listener from button
			_entities.begin();//in over case collection has only one entity
			var button:IEntity = _entities.current;
			var display:Display = button.get(Display);
			display.view.removeEventListener(MouseEvent.CLICK, this.clickHandler);
		}

//} endregion PUBLIC METHODS ===========================================================================================
//======================================================================================================================
//{region										PRIVATE\PROTECTED METHODS
		private function clickHandler(event:MouseEvent = null):void
		{
			_entities.begin();//in over case collection has only one entity
			var button:IEntity = _entities.current;
			var label:Label = button.get(Label);
			_onPause = !_onPause;
			label.textField.text = !_onPause ? 'pause' : 'resume';
			if(event != null)//change app state, only if button was clicked
			{
				if(_onPause)
				{
					Gimmick.deactivateSystem(MovementSystem);
					Gimmick.deactivateSystem(DisplaySystem);
				}
				else
				{
					Gimmick.activateSystem(MovementSystem);
					Gimmick.activateSystem(DisplaySystem);
				}
			}
		}
//} endregion PRIVATE\PROTECTED METHODS ================================================================================
//======================================================================================================================
//{region											GETTERS/SETTERS

//} endregion GETTERS/SETTERS ==========================================================================================
	}
}