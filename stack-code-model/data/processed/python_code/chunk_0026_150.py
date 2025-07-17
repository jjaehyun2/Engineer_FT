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

package {

	import systems.*;

	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.text.TextField;

	import org.gimmick.core.Gimmick;

	import systems.InitialSystem;

	/**
	 * Launcher of simple example
	 */
	[SWF(width=1024, height=768, frameRate=60)]
	public class Launcher extends Sprite
	{
		public function Launcher()
		{
			super ();
			this.addEventListener(Event.ADDED_TO_STAGE, this.initialHandler);
		}

		private function initialHandler(event:Event):void
		{
			this.removeEventListener(event.type, this.initialHandler);
			//prepare application stage
			this.stage.align = StageAlign.TOP_LEFT;
			this.stage.scaleMode = StageScaleMode.NO_SCALE;
			//create and initialize Gimmick framework
			Gimmick.initialize(null);
			Gimmick.addSystem(new InitialSystem(this));
			Gimmick.addSystem(new GUISystem());
			Gimmick.addSystem(new MovementSystem());
			Gimmick.addSystem(new DisplaySystem());
			//activate systems
			Gimmick.activateSystem(InitialSystem);
			Gimmick.activateSystem(GUISystem);
			Gimmick.activateSystem(MovementSystem);
			Gimmick.activateSystem(DisplaySystem);
			//start application loop
			this.addEventListener(Event.ENTER_FRAME, this.enterFrameHandler);
		}

		/**
		 * Application loop handler
		 * @param event
		 */
		private function enterFrameHandler(event:Event):void
		{
			Gimmick.tick();
		}
	}
}