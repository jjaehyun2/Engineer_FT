/*
 *	Temple Library for ActionScript 3.0
 *	Copyright © MediaMonks B.V.
 *	All rights reserved.
 *	
 *	Redistribution and use in source and binary forms, with or without
 *	modification, are permitted provided that the following conditions are met:
 *	1. Redistributions of source code must retain the above copyright
 *	   notice, this list of conditions and the following disclaimer.
 *	2. Redistributions in binary form must reproduce the above copyright
 *	   notice, this list of conditions and the following disclaimer in the
 *	   documentation and/or other materials provided with the distribution.
 *	3. All advertising materials mentioning features or use of this software
 *	   must display the following acknowledgement:
 *	   This product includes software developed by MediaMonks B.V.
 *	4. Neither the name of MediaMonks B.V. nor the
 *	   names of its contributors may be used to endorse or promote products
 *	   derived from this software without specific prior written permission.
 *	
 *	THIS SOFTWARE IS PROVIDED BY MEDIAMONKS B.V. ''AS IS'' AND ANY
 *	EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 *	WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 *	DISCLAIMED. IN NO EVENT SHALL MEDIAMONKS B.V. BE LIABLE FOR ANY
 *	DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 *	(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *	LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 *	ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 *	(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 *	SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *	
 *	
 *	Note: This license does not apply to 3rd party classes inside the Temple
 *	repository with their own license!
 */

package temple.core.display 
{
	import flash.events.IEventDispatcher;
	import temple.core.debug.Registry;
	import temple.core.debug.log.Log;
	import temple.core.debug.log.LogLevel;
	import temple.core.debug.objectToString;
	import temple.core.destruction.DestructEvent;
	import temple.core.destruction.Destructor;
	import temple.core.errors.TempleArgumentError;
	import temple.core.errors.throwError;
	import temple.core.events.EventListenerManager;
	import temple.core.templelibrary;
	import flash.display.DisplayObject;
	import flash.display.FrameLabel;
	import flash.display.Loader;
	import flash.display.MovieClip;
	import flash.display.Stage;
	import flash.events.Event;
	import flash.geom.Point;


	/**
	 * @eventType temple.core.destruction.DestructEvent.DESTRUCT
	 */
	[Event(name = "DestructEvent.destruct", type = "temple.core.destruction.DestructEvent")]
	
	/**
	 * Base class for all MovieClips in the Temple. The CoreMovieClip handles some core features of the Temple:
	 * <ul>
	 * 	<li>Registration to the Registry class.</li>
	 * 	<li>Global reference to the stage trough the StageProvider.</li>
	 * 	<li>Corrects a timeline bug in Flash (see <a href="http://www.tyz.nl/2009/06/23/weird-parent-thing-bug-in-flash/" target="_blank">http://www.tyz.nl/2009/06/23/weird-parent-thing-bug-in-flash/</a>).</li>
	 * 	<li>Event dispatch optimization.</li>
	 * 	<li>Easy remove of all EventListeners.</li>
	 * 	<li>Wrapper for Log class for easy logging.</li>
	 * 	<li>Completely destructible.</li>
	 * 	<li>Automatic removes and destruct children, grandchildren etc. on destruction.</li>
	 * 	<li>Tracked in Memory (of this feature is enabled).</li>
	 * 	<li>Some useful extra properties like autoAlpha, position and scale.</li>
	 * </ul>
	 * 
	 * <p>You should always use and/or extend the CoreMovieClip instead of MovieClip if you want to make use of the Temple features.</p>
	 * 
	 * @see temple.core.Temple#registerObjectsInMemory
	 * 
	 * @includeExample CoreDisplayObjectsExample.as
	 * 
	 * @author Thijs Broerse
	 */
	public class CoreMovieClip extends MovieClip implements ICoreMovieClip
	{
		/**
		 * @private
		 * 
		 * Protected namespace for construct method. This makes overriding of constructor possible.
		 */
		protected namespace construct;
		
		private const _toStringProps:Vector.<String> = Vector.<String>(['name']);
		private var _eventListenerManager:EventListenerManager;
		private var _isDestructed:Boolean;
		private var _onStage:Boolean;
		private var _onParent:Boolean;
		private var _registryId:uint;
		private var _destructOnUnload:Boolean = true;
		private var _emptyPropsInToString:Boolean = true;
		private var _frameScripts:Vector.<Function>;
		private var _frameLabels:Object;
		private var _debug:Boolean;

		public function CoreMovieClip()
		{
			construct::coreMovieClip();
		}
		
		/**
		 * @private
		 */
		construct function coreMovieClip():void
		{
			if (loaderInfo) loaderInfo.addEventListener(Event.UNLOAD, handleUnload, false, 0, true);
			
			_registryId = Registry.add(this);
			if (super.stage) StageProvider.stage ||= super.stage;
			
			// Set listeners to keep track of object is on stage, since we can't trust the .parent property
			super.addEventListener(Event.ADDED, handleAdded);
			super.addEventListener(Event.ADDED_TO_STAGE, handleAddedToStage);
			super.addEventListener(Event.REMOVED, handleRemoved);
			super.addEventListener(Event.REMOVED_FROM_STAGE, handleRemovedFromStage);
		}
		
		/**
		 * @inheritDoc
		 */
		override public function addFrameScript(...args):void
		{
			_frameScripts ||= new Vector.<Function>(totalFrames, true);
			
			for (var i:int = 0, leni:int = args.length; i < leni; i += 2)
			{
				if (!(args[i] is int))
				{
					args[i] = getFrame(args[i]);
					if (args[i])
					{
						args[i]--;
					}
					else
					{
						continue;
					}
				}
				
				_frameScripts[args[i]] = args[i+1];
				
				if (_debug) logDebug("FrameScript " + (args[i+1] == null ? "cleared" : "set") + " on frame " + (args[i] + 1));
			}
			super.addFrameScript.apply(null, args);
		}
		
		/**
		 * @inheritDoc
		 */
		public function hasFrameScript(frame:Object):Boolean
		{
			return _frameScripts && (frame = getFrame(frame)) &&  _frameScripts[int(frame) - 1] != null;
		}

		/**
		 * @inheritDoc
		 */
		public function get hasFrameScripts():Boolean
		{
			return _frameScripts != null;
		}

		/**
		 * @inheritDoc
		 */
		public function getFrameScript(frame:Object):Function
		{
			return (frame = getFrame(frame)) && _frameScripts ? _frameScripts[int(frame) - 1] : null;
		}

		/**
		 * @inheritDoc
		 */
		public function setFrameScript(frame:Object, script:Function):void
		{
			frame = getFrame(frame);
			if (frame) addFrameScript(int(frame) - 1, script);
		}
		
		/**
		 * @inheritDoc
		 */
		public function clearFrameScript(frame:Object):void
		{
			frame = getFrame(frame);
			if (frame) addFrameScript(int(frame) - 1, null);
		}

		/**
		 * @inheritDoc
		 */
		public function clearFrameScripts():void
		{
			if (_frameScripts)
			{
				for (var i:int = 0, leni:int = _frameScripts.length; i < leni; i++)
				{
					if (_frameScripts[i] != null) addFrameScript(i, null);
				}
			}
		}

		/**
		 * Returns a list of all Frame Scripts. Modifying this list does not have effect on the actual scripts on the
		 * frames.
		 */
		templelibrary function get frameScripts():Vector.<Function>
		{
			return _frameScripts;
		}
		
		/**
		 * Returns a hash with all the FrameLabels with the name and frame as index
		 */
		public function get frameLabels():Object
		{
			if (!_frameLabels)
			{
				_frameLabels = {};
				for each (var frameLabel:FrameLabel in currentLabels)
				{
					if (frameLabel.name in _frameLabels) logWarn("Duplicate label '" + frameLabel.name + "' on frame " + frameLabel.frame);
					_frameLabels[frameLabel.frame] = _frameLabels[frameLabel.name] = frameLabel;
				}
			}
			return _frameLabels;
		}
		
		/**
		 * @inheritDoc
		 */
		public function getFrameLabel(frame:Object):FrameLabel
		{
			return frameLabels[frame is int ? frame : String(frame)];
		}
		
		/**
		 * @inheritDoc
		 */
		public function getFrame(frame:Object):int
		{
			if (frame is int)
			{
				if (frame < 1)
				{
					throwError(new TempleArgumentError(this, "frame cannot lower then 1"));
					return 0;
				}
				else if (frame > totalFrames)
				{
					throwError(new TempleArgumentError(this, "frame " + frame + " doesn't exists, totalFrame is " + totalFrames));
					return 0;
				}
				else
				{
					return int(frame);
				}
			}
			else
			{
				if (hasFrameLabel(frame))
				{
					return getFrameLabel(frame).frame;
				}
				else
				{
					throwError(new TempleArgumentError(this, "frame '" + frame + "' not found"));
				}
			}
			return 0;
		}
		
		/**
		 * @inheritDoc
		 */
		public function hasFrameLabel(frame:Object):Boolean
		{
			if (!(frame is int)) frame = String(frame);
			
			return frame in frameLabels;
		}

		[Temple]
		/**
		 * @inheritDoc
		 */
		public final function get registryId():uint
		{
			return _registryId;
		}

		/**
		 * Checks for a <code>scrollRect</code> and returns the width of the <code>scrollRect</code>.
		 * Otherwise the <code>super.width</code> is returned. This fixes a FlashPlayer bug; Flash doesn't immediatly
		 * update the objects width when a scrollRect is set on a DisplayObject.
		 */
		override public function get width():Number
		{
			return scrollRect ? scrollRect.width : super.width;
		}
		
		/**
		 * If the object does not have a width and is not scaled to 0 the object is empty, 
		 * setting the width is useless and can only cause weird errors, so we don't.
		 */
		override public function set width(value:Number):void
		{
			if (super.width || !scaleX) super.width = value;
		}
		
		/**
		 * Checks for a <code>scrollRect</code> and returns the height of the <code>scrollRect</code>.
		 * Otherwise the <code>super.height</code> is returned. This fixes a FlashPlayer bug; Flash doesn't immediatly
		 * update the objects height when a scrollRect is set on a DisplayObject.
		 */
		override public function get height():Number
		{
			return scrollRect ? scrollRect.height : super.height;
		}

		/**
		 * If the object does not have a height and is not scaled to 0 the object is empty, 
		 * setting the height is useless and can only cause weird errors, so we don't. 
		 */
		override public function set height(value:Number):void
		{
			if (super.height || !scaleY) super.height = value;
		}
		
		/**
		 * When object is not on the stage it gets the stage reference from the StageProvider. So therefore this object
		 * will always has a reference to the stage.
		 */
		override public function get stage():Stage
		{
			return super.stage || StageProvider.stage;
		}
		
		/**
		 * @inheritDoc
		 */
		public function get onStage():Boolean
		{
			return _onStage;
		}
		
		/**
		 * @inheritDoc
		 */
		public function get hasParent():Boolean
		{
			return _onParent;
		}
		
		/**
		 * @inheritDoc
		 */
		public function removeFromParent():void
		{
			if (parent && _onParent) parent.removeChild(this);
		}
		
		/**
		 * @inheritDoc
		 */
		public function get autoAlpha():Number
		{
			return visible ? alpha : 0;
		}

		/**
		 * @inheritDoc
		 */
		public function set autoAlpha(value:Number):void
		{
			alpha = value;
			visible = alpha > 0;
		}
		
		/**
		 * @inheritDoc
		 */
		public function get position():Point
		{
			return new Point(x, y);
		}
		
		/**
		 * @inheritDoc
		 */
		public function set position(value:Point):void
		{
			x = value.x;
			y = value.y;
		}
		
		/**
		 * @inheritDoc
		 */
		public function get scale():Number
		{
			return scaleX == scaleY ? scaleX : NaN;
		}
		
		/**
		 * @inheritDoc
		 */
		public function set scale(value:Number):void
		{
			scaleX = scaleY = value;
		}
		
		/**
		 * @inheritDoc
		 */
		public function get destructOnUnload():Boolean
		{
			return _destructOnUnload;
		}
		
		/**
		 * @inheritDoc
		 */
		public function set destructOnUnload(value:Boolean):void
		{
			_destructOnUnload = value;
		}

		/**
		 * @inheritDoc
		 */
		public function get children():Vector.<DisplayObject>
		{
			var i:int = numChildren;
			var children:Vector.<DisplayObject> = new Vector.<DisplayObject>(i, true);
			for (--i; i >= 0; --i)
			{
				children[i] = getChildAt(i);
			}
			return children;
		}
		
		/**
		 * @inheritDoc
		 */
		public function addChildAtPosition(child:DisplayObject, x:Number, y:Number, index:int = -1):DisplayObject
		{
			child.x = x;
			child.y = y;
			
			return index < 0 ? addChild(child) : addChildAt(child, index);
		}
		
		
		/**
		 * @inheritDoc
		 * 
		 * Checks if this object has event listeners of this event before dispatching the event. Should speed up the
		 * application.
		 */
		override public function dispatchEvent(event:Event):Boolean 
		{
			if (hasEventListener(event.type) || event.bubbles) 
			{
				return super.dispatchEvent(event);
			}
			return true;
		}

		/**
		 * @inheritDoc
		 */
		override public function addEventListener(type:String, listener:Function, useCapture:Boolean = false, priority:int = 0, useWeakReference:Boolean = false):void 
		{
			super.addEventListener(type, listener, useCapture, priority, useWeakReference);
			if (getEventListenerManager()) _eventListenerManager.templelibrary::addEventListener(type, listener, useCapture, priority, useWeakReference);
		}
		
		/**
		 * @inheritDoc
		 */
		public function addEventListenerOnce(type:String, listener:Function, useCapture:Boolean = false, priority:int = 0):void
		{
			if (getEventListenerManager()) _eventListenerManager.addEventListenerOnce(type, listener, useCapture, priority);
		}

		/**
		 * @inheritDoc
		 */
		override public function removeEventListener(type:String, listener:Function, useCapture:Boolean = false):void 
		{
			super.removeEventListener(type, listener, useCapture);
			if (_eventListenerManager) _eventListenerManager.templelibrary::removeEventListener(type, listener, useCapture);
		}

		/**
		 * @inheritDoc
		 */
		public function removeAllStrongEventListenersForType(type:String):void 
		{
			if (_eventListenerManager) _eventListenerManager.removeAllStrongEventListenersForType(type);
		}
		
		/**
		 * @inheritDoc
		 */
		public function removeAllOnceEventListenersForType(type:String):void
		{
			if (_eventListenerManager) _eventListenerManager.removeAllOnceEventListenersForType(type);
		}

		/**
		 * @inheritDoc
		 */
		public function removeAllStrongEventListenersForListener(listener:Function):void 
		{
			if (_eventListenerManager) _eventListenerManager.removeAllStrongEventListenersForListener(listener);
		}

		/**
		 * @inheritDoc
		 */
		public function removeAllEventListeners():void 
		{
			if (_eventListenerManager) _eventListenerManager.removeAllEventListeners();
		}
		
		/**
		 * @inheritDoc
		 */
		public function listenTo(dispatcher:IEventDispatcher, type:String, listener:Function, useCapture:Boolean = false, priority:int = 0):void
		{
			if (getEventListenerManager()) _eventListenerManager.listenTo(dispatcher, type, listener, useCapture, priority);
		}
		
		/**
		 * @inheritDoc
		 */
		public function listenOnceTo(dispatcher:IEventDispatcher, type:String, listener:Function, useCapture:Boolean = false, priority:int = 0):void
		{
			if (getEventListenerManager()) _eventListenerManager.listenOnceTo(dispatcher, type, listener, useCapture, priority);
		}
		
		[Temple]
		/**
		 * @inheritDoc
		 */
		public function get eventListenerManager():EventListenerManager
		{
			return _eventListenerManager;
		}
		
		private function getEventListenerManager():EventListenerManager
		{
			if (_isDestructed)
			{
				logError("Object is destructed, don't add event listeners");
				return null;
			}
			return _eventListenerManager ||= EventListenerManager.getInstance(this) || new EventListenerManager(this);
		}
		
		/**
		 * @inheritDoc
		 */
		public function get debug():Boolean
		{
			return _debug;
		}

		/**
		 * @inheritDoc
		 */
		[Inspectable(name="Debug", type="Boolean", defaultValue="false")]
		public function set debug(value:Boolean):void
		{
			_debug = value;
		}
		
		/**
		 * Does a Log.debug, but has already filled in some known data.
		 * @param data the data to be logged
		 * 
		 * @see temple.core.debug.log.Log#debug()
		 * @see temple.core.debug.log.LogLevel#DEBUG
		 */
		protected final function logDebug(data:*):void
		{
			Log.templelibrary::send(data, toString(), LogLevel.DEBUG, _registryId);
		}
		
		/**
		 * Does a Log.error, but has already filled in some known data.
		 * @param data the data to be logged
		 * 
		 * @see temple.core.debug.log.Log#error()
		 * @see temple.core.debug.log.LogLevel#ERROR
		 */
		protected final function logError(data:*):void
		{
			Log.templelibrary::send(data, toString(), LogLevel.ERROR, _registryId);
		}
		
		/**
		 * Does a Log.fatal, but has already filled in some known data.
		 * @param data the data to be logged
		 * 
		 * @see temple.core.debug.log.Log#fatal()
		 * @see temple.core.debug.log.LogLevel#FATAL
		 */
		protected final function logFatal(data:*):void
		{
			Log.templelibrary::send(data, toString(), LogLevel.FATAL, _registryId);
		}
		
		/**
		 * Does a Log.info, but has already filled in some known data.
		 * @param data the data to be logged
		 * 
		 * @see temple.core.debug.log.Log#info()
		 * @see temple.core.debug.log.LogLevel#INFO
		 */
		protected final function logInfo(data:*):void
		{
			Log.templelibrary::send(data, toString(), LogLevel.INFO, _registryId);
		}
		
		/**
		 * Does a Log.status, but has already filled in some known data.
		 * @param data the data to be logged
		 * 
		 * @see temple.core.debug.log.Log#status()
		 * @see temple.core.debug.log.LogLevel#STATUS
		 */
		protected final function logStatus(data:*):void
		{
			Log.templelibrary::send(data, toString(), LogLevel.STATUS, _registryId);
		}
		
		/**
		 * Does a Log.warn, but has already filled in some known data.
		 * @param data the data to be logged
		 * 
		 * @see temple.core.debug.log.Log#warn()
		 * @see temple.core.debug.log.LogLevel#WARN
		 */
		protected final function logWarn(data:*):void
		{
			Log.templelibrary::send(data, toString(), LogLevel.WARN, _registryId);
		}

		private function handleUnload(event:Event):void
		{
			if (_destructOnUnload) destruct();
		}
		
		private function handleAdded(event:Event):void
		{
			if (event.currentTarget == this) _onParent = true;
		}

		private function handleAddedToStage(event:Event):void
		{
			_onStage = true;
			StageProvider.stage ||= super.stage;
		}

		private function handleRemoved(event:Event):void
		{
			if (event.target == this)
			{
				_onParent = false;
				if (!_isDestructed) super.addEventListener(Event.ENTER_FRAME, handleDestructedFrameDelay);
			}
		}
		
		private function handleDestructedFrameDelay(event:Event):void
		{
			super.removeEventListener(Event.ENTER_FRAME, handleDestructedFrameDelay);
			checkParent();
		}

		/**
		 * Check objects parent, after being removed. If the object still has a parent, the object has been removed by a timeline animation.
		 * If an object is removed by a timeline animation, the object is not used anymore and can be destructed
		 */
		private function checkParent():void
		{
			if (parent && !_onParent) destruct();
		}

		private function handleRemovedFromStage(event:Event):void
		{
			_onStage = false;
		}		

		/**
		 * List of property names which are output in the toString() method.
		 */
		protected final function get toStringProps():Vector.<String>
		{
			return _toStringProps;
		}
		
		/**
		 * @private
		 *
		 * Possibility to modify the toStringProps array from outside, using the templelibrary namespace.
		 */
		templelibrary final function get toStringProps():Vector.<String>
		{
			return _toStringProps;
		}
		
		/**
		 * A Boolean which indicates if empty properties are output in the toString() method.
		 */
		protected final function get emptyPropsInToString():Boolean
		{
			return _emptyPropsInToString;
		}

		/**
		 * @private
		 */
		protected final function set emptyPropsInToString(value:Boolean):void
		{
			_emptyPropsInToString = value;
		}

		/**
		 * @private
		 * 
		 * Possibility to modify the emptyPropsInToString value from outside, using the templelibrary namespace.
		 */
		templelibrary final function get emptyPropsInToString():Boolean
		{
			return _emptyPropsInToString;
		}
		
		/**
		 * @private
		 */
		templelibrary final function set emptyPropsInToString(value:Boolean):void
		{
			_emptyPropsInToString = value;
		}

		/**
		 * @inheritDoc
		 */
		override public function toString():String
		{
			return objectToString(this, toStringProps, !emptyPropsInToString);
		}
		
		[Temple]
		/**
		 * @inheritDoc
		 */
		public final function get isDestructed():Boolean
		{
			return _isDestructed;
		}

		/**
		 * @inheritDoc
		 */
		public function destruct():void 
		{
			if (_isDestructed) return;
			
			dispatchEvent(new DestructEvent(DestructEvent.DESTRUCT));
			
			// clear mask, so it won't keep a reference to an other object
			mask = null;
			stop();
			clearFrameScripts();
			_frameScripts = null;
			
			if (stage && stage.focus == this) stage.focus = null;
			
			if (loaderInfo) loaderInfo.removeEventListener(Event.UNLOAD, handleUnload);
			
			if (_eventListenerManager)
			{
				_eventListenerManager.destruct();
				_eventListenerManager = null;
			}
			
			super.removeEventListener(Event.ENTER_FRAME, handleDestructedFrameDelay);
			super.removeEventListener(Event.ADDED, handleAdded);
			super.removeEventListener(Event.ADDED_TO_STAGE, handleAddedToStage);
			super.removeEventListener(Event.REMOVED, handleRemoved);
			super.removeEventListener(Event.REMOVED_FROM_STAGE, handleRemovedFromStage);
			
			Destructor.destructChildren(this);
			if (parent)
			{
				if (parent is Loader)
				{
					Loader(parent).unload();
				}
				else
				{
					if (_onParent)
					{
						if (name && parent.hasOwnProperty(name)) parent[name] = null;
						parent.removeChild(this);
					}
					else
					{
						// something weird happened, since we have a parent but didn't receive an ADDED event. So do the try-catch thing
						try
						{
							if (name && parent.hasOwnProperty(name)) parent[name] = null;
							parent.removeChild(this);
						}
						catch (e:Error){}
					}
				}
			}
			_isDestructed = true;
		}
	}
}