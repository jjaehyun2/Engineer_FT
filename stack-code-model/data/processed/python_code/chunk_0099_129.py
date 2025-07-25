/*
Feathers
Copyright 2012-2013 Joshua Tynjala. All Rights Reserved.

This program is free software. You can redistribute and/or modify it in
accordance with the terms of the accompanying license agreement.
*/
package feathers.motion.transitions
{
	import feathers.controls.IScreen;
	import feathers.controls.ScreenNavigator;

	import flash.utils.getQualifiedClassName;

	import starling.animation.Transitions;
	import starling.animation.Tween;
	import starling.core.Starling;
	import starling.display.DisplayObject;

	/**
	 * A transition for <code>ScreenNavigator</code> that fades in or out
	 * the top-most screen, depending on if the manager determines that the
	 * transition is a push or a pop. (Just mimic the transition used by
	 * Android version's WhatsApp)
	 *
	 * <p>Whether a screen change is supposed to be a push or a pop is
	 * determined automatically. The manager generates an identifier from the
	 * fully-qualified class name of the screen, and if present, the
	 * <code>screenID</code> defined by <code>IScreen</code> instances. If the
	 * generated identifier is present on the stack, a screen change is
	 * considered a pop. If the token is not present, it's a push. Screen IDs
	 * should be tailored to this behavior to avoid false positives.</p>
	 *
	 * <p>If your navigation structure requires explicit pushing and popping, a
	 * custom transition manager is probably better.</p>
	 *
	 * @see feathers.controls.ScreenNavigator
	 */
	public class ShrinkAndFadeStackTransitionManager
	{
		/**
		 * Constructor.
		 */
		public function ShrinkAndFadeStackTransitionManager(navigator:ScreenNavigator, quickStackScreenClass:Class = null, quickStackScreenID:String = null)
		{
			if(!navigator)
			{
				throw new ArgumentError("ScreenNavigator cannot be null.");
			}
			this.navigator = navigator;
			var quickStack:String;
			if(quickStackScreenClass)
			{
				quickStack = getQualifiedClassName(quickStackScreenClass);
			}
			if(quickStack && quickStackScreenID)
			{
				quickStack += "~" + quickStackScreenID;
			}
			if(quickStack)
			{
				this._stack.push(quickStack);
			}
			this.navigator.transition = this.onTransition;
		}

		/**
		 * The <code>ScreenNavigator</code> being managed.
		 */
		protected var navigator:ScreenNavigator;

		/**
		 * @private
		 */
		protected var _stack:Vector.<String> = new <String>[];

		/**
		 * @private
		 */
		protected var _activeTransition:Tween;

		/**
		 * @private
		 */
		protected var _savedCompleteHandler:Function;

		/**
		 * The duration of the transition, in seconds.
		 *
		 * @default 0.25
		 */
		public var duration:Number = 0.25;

		/**
		 * A delay before the transition starts, measured in seconds. This may
		 * be required on low-end systems that will slow down for a short time
		 * after heavy texture uploads.
		 *
		 * @default 0.1
		 */
		public var delay:Number = 0.1;

		/**
		 * The easing function to use.
		 *
		 * @default starling.animation.Transitions.EASE_OUT
		 */
		public var ease:Object = Transitions.EASE_OUT;

		/**
		 * Determines if the next transition should be skipped. After the
		 * transition, this value returns to <code>false</code>.
		 *
		 * @default false
		 */
		public var skipNextTransition:Boolean = false;
	
		/**
		 * The scale the screen will expand
		 *
		 * @default 0.1
		 */
		public var tweenScale:Number = 0.1;
		
		/**
		 * The x position the screen will shift
		 *
		 * @default 0.05
		 */
		public var tweenX:Number = 0.05;
		
		/**
		 * The y position the screen will shift
		 *
		 * @default 0.02
		 */
		public var tweenY:Number = 0.02;
		
		/**
		 * Removes all saved classes from the stack that are used to determine
		 * which side of the <code>ScreenNavigator</code> the new screen will
		 * slide in from.
		 */
		public function clearStack():void
		{
			this._stack.length = 0;
		}

		/**
		 * The function passed to the <code>transition</code> property of the
		 * <code>ScreenNavigator</code>.
		 */
		protected function onTransition(oldScreen:DisplayObject, newScreen:DisplayObject, onComplete:Function):void
		{
			if(this._activeTransition)
			{
				Starling.juggler.remove(this._activeTransition);
				this._activeTransition = null;
			}

			if(!oldScreen || !newScreen || this.skipNextTransition)
			{
				this.skipNextTransition = false;
				this._savedCompleteHandler = null;
				if(newScreen)
				{
					newScreen.x = newScreen.y = 0;
					newScreen.scaleX = newScreen.scaleY = 1;
					newScreen.alpha = 1;
				}
				if(oldScreen)
				{
					oldScreen.x = oldScreen.y = 0;
					oldScreen.scaleX = oldScreen.scaleY = 1;
					oldScreen.alpha = 1;
				}
				if(onComplete != null)
				{
					onComplete();
				}
				return;
			}

			this._savedCompleteHandler = onComplete;

			var newScreenClassAndID:String = getQualifiedClassName(newScreen);
			if(newScreen is IScreen)
			{
				newScreenClassAndID += "~" + IScreen(newScreen).screenID;
			}
			var stackIndex:int = this._stack.indexOf(newScreenClassAndID);
			
			if(stackIndex < 0) //push
			{
				var oldScreenClassAndID:String = getQualifiedClassName(oldScreen);
				if(oldScreen is IScreen)
				{
					oldScreenClassAndID += "~" + IScreen(oldScreen).screenID;
				}
				this._stack.push(oldScreenClassAndID);
				oldScreen.x = oldScreen.y = 0;
				oldScreen.scaleX = oldScreen.scaleY = 1;
				oldScreen.alpha = 1;
				newScreen.x = -this.navigator.width * tweenX;
				newScreen.y = -this.navigator.height * tweenY;
				newScreen.scaleX = newScreen.scaleY = 1 + tweenScale;
				newScreen.alpha = 0;
				this._activeTransition = new Tween(newScreen, this.duration, this.ease);
				this._activeTransition.animate("scaleX", 1);
				this._activeTransition.animate("scaleY", 1);
				this._activeTransition.animate("x", 0);
				this._activeTransition.animate("y", 0);
				this._activeTransition.animate("alpha", 1);
			}
			else //pop
			{
				this._stack.length = stackIndex;
				newScreen.x = newScreen.y = oldScreen.x = oldScreen.y = 0;
				newScreen.scaleX = newScreen.scaleY = oldScreen.scaleX = oldScreen.scaleY = 1;
				newScreen.alpha = oldScreen.alpha = 1;
				this.navigator.addChild(oldScreen);
				this._activeTransition = new Tween(oldScreen, this.duration, this.ease);
				this._activeTransition.animate("scaleX", 1 + tweenScale);
				this._activeTransition.animate("scaleX", 1 + tweenScale);
				this._activeTransition.animate("x", -this.navigator.width * tweenX);
				this._activeTransition.animate("y", -this.navigator.height * tweenY);
				this._activeTransition.animate("alpha", 0);
			}
			this._activeTransition.delay = this.delay;
			this._activeTransition.onComplete = activeTransition_onComplete;
			Starling.juggler.add(this._activeTransition);
		}

		/**
		 * @private
		 */
		protected function activeTransition_onComplete():void
		{
			this._activeTransition = null;
			if(this._savedCompleteHandler != null)
			{
				this._savedCompleteHandler();
			}
		}
	}
}