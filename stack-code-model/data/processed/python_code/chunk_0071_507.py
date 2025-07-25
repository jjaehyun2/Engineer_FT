/*
 *      _________  __      __
 *    _/        / / /____ / /________ ____ ____  ___
 *   _/        / / __/ -_) __/ __/ _ `/ _ `/ _ \/ _ \
 *  _/________/  \__/\__/\__/_/  \_,_/\_, /\___/_//_/
 *                                   /___/
 * 
 * Tetragon : Game Engine for multi-platform ActionScript projects.
 * http://www.tetragonengine.com/ - Copyright (C) 2012 Sascha Balkau
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
package tetragon.util.tween
{
	import tetragon.util.tween.plugins.TweenPlugin;

	import flash.display.Shape;
	import flash.events.Event;
	import flash.utils.Dictionary;
	import flash.utils.describeType;
	import flash.utils.getTimer;
	
	
	/**
	 * Tween is an extremely fast, lightweight, and flexible tweening engine that
	 * serves as the foundation of the GreenSock Tweening Platform. A Tween instance
	 * handles tweening one or more numeric properties of any object over time, updating
	 * them on every frame. Sounds simple, but there's a wealth of capabilities and
	 * conveniences at your fingertips with Tween. With plenty of other tweening
	 * engines to choose from, here's why you might want to consider Tween: <ul>
	 * <li><b> SPEED </b>- Tween has been highly optimized for maximum performance.
	 * See some speed comparisons yourself at <a
	 * href="http://www.greensock.com/tweening-speed-test/"
	 * >http://www.greensock.com/tweening-speed-test/</a></li>
	 * 
	 * <li><b> Feature set </b>- In addition to tweening ANY numeric property of ANY
	 * object, Tween can tween filters, hex colors, volume, tint, frames, and even do
	 * bezier tweening, plus LOTS more. TweenMax extends Tween and adds even more
	 * capabilities like repeat, yoyo, repeatDelay, timeScale, event dispatching,
	 * on-the-fly destination value updates, rounding and more. Overwrite management is an
	 * important consideration in a tweening engine as well which is another area where
	 * the GreenSock Tweening Platform shines. You have options for AUTO overwriting or
	 * you can manually define how each tween will handle overlapping tweens of the same
	 * object.</li>
	 * 
	 * <li><b> Expandability </b>- With its plugin architecture, you can activate as many
	 * (or as few) features as your project requires. Write your own plugin to handle
	 * particular special properties in custom ways. Minimize bloat, and maximize
	 * performance.</li>
	 * 
	 * <li><b> Sequencing, grouping, and management features </b>- TimelineLite and
	 * TimelineMax make it surprisingly simple to create complex sequences or groups of
	 * tweens that you can control as a whole. play(), pause(), restart(), or reverse().
	 * You can even tween a timeline's <code>currentTime</code> or
	 * <code>currentProgress</code> property to fastforward or rewind the entire timeline.
	 * Add labels, gotoAndPlay(), change the timeline's timeScale, nest timelines within
	 * timelines, and lots more.</li>
	 * 
	 * <li><b> Ease of use </b>- Designers and Developers alike rave about how intuitive
	 * the platform is.</li>
	 * 
	 * <li><b> Updates </b>- Frequent updates and feature additions make the GreenSock
	 * Tweening Platform reliable and robust.</li>
	 * 
	 * <li><b> AS2 and AS3 </b>- Most other engines are only developed for AS2 or AS3 but
	 * not both.</li> </ul>
	 * 
	 * <hr /> <b>SPECIAL PROPERTIES (no plugins required):</b> The following special
	 * properties can be defined in the <code>vars</code> parameter which can be either a
	 * generic Object or a <code><a
	 * href="data/TweenVars.html">TweenVars</a></code> instance: <br />
	 * 
	 * <ul> <li><b> delay : Number</b> Amount of delay in seconds (or frames for
	 * frames-based tweens) before the tween should begin.</li>
	 * 
	 * <li><b> useFrames : Boolean</b> If useFrames is set to true, the tweens's timing
	 * mode will be based on frames. Otherwise, it will be based on seconds/time. NOTE: a
	 * tween's timing mode is always determined by its parent timeline. </li>
	 * 
	 * <li><b> ease : Function</b> Use any standard easing equation to control the rate of
	 * change. For example, <code>Elastic.easeOut</code>. The Default is
	 * Quad.easeOut.</li>
	 * 
	 * <li><b> easeParams : Array</b> An Array of extra parameters to feed the easing
	 * equation. This can be useful when using an ease like <code>Elastic</code> and want
	 * to control extra parameters like the amplitude and period. Most easing equations,
	 * however, don't require extra parameters so you won't need to pass in any
	 * easeParams.</li>
	 * 
	 * <li><b> immediateRender : Boolean</b> Normally when you create a tween, it begins
	 * rendering on the very next frame (when the Flash Player dispatches an ENTER_FRAME
	 * event) unless you specify a <code>delay</code>. This allows you to insert tweens
	 * into timelines and perform other actions that may affect its timing. However, if
	 * you prefer to force the tween to render immediately when it is created, set
	 * <code>immediateRender</code> to true. Or to prevent a tween with a duration of zero
	 * from rendering immediately, set <code>immediateRender</code> to false.</li>
	 * 
	 * <li><b> onInit : Function</b> A function that should be called just before the
	 * tween inits (renders for the first time). Since onInit runs before the start/end
	 * values are recorded internally, it is a good place to run code that affects the
	 * target's initial position or other tween-related properties. onStart, by contrast,
	 * runs AFTER the tween inits and the start/end values are recorded internally.
	 * onStart is called every time the tween begins which can happen more than once if
	 * the tween is restarted multiple times.</li>
	 * 
	 * <li><b> onInitParams : Array</b> An Array of parameters to pass the onInit
	 * function.</li>
	 * 
	 * <li><b> onStart : Function</b> A function that should be called when the tween
	 * begins (when its currentTime is at 0 and changes to some other value which can
	 * happen more than once if the tween is restarted multiple times).</li>
	 * 
	 * <li><b> onStartParams : Array</b> An Array of parameters to pass the onStart
	 * function.</li>
	 * 
	 * <li><b> onUpdate : Function</b> A function that should be called every time the
	 * tween's time/position is updated (on every frame while the tween is active)</li>
	 * 
	 * <li><b> onUpdateParams : Array</b> An Array of parameters to pass the onUpdate
	 * function</li>
	 * 
	 * <li><b> onComplete : Function</b> A function that should be called when the tween
	 * has finished </li>
	 * 
	 * <li><b> onCompleteParams : Array</b> An Array of parameters to pass the onComplete
	 * function</li>
	 * 
	 * <li><b> onReverseComplete : Function</b> A function that should be called when the
	 * tween has reached its starting point again after having been reversed. </li>
	 * 
	 * <li><b> onReverseCompleteParams : Array</b> An Array of parameters to pass the
	 * onReverseComplete function</li>
	 * 
	 * <li><b> paused : Boolean</b> If true, the tween will be paused initially.</li>
	 * 
	 * <li><b> overwrite : int</b> Controls how (and if) other tweens of the same target
	 * are overwritten by this tween. There are several modes to choose from, but only the
	 * first two are available in Tween unless <code>OverwriteManager.init()</code>
	 * has been called (please see <a
	 * href="http://www.greensock.com/overwritemanager/">http
	 * ://www.greensock.com/overwritemanager/</a> for details and a full explanation of
	 * the various modes): <ul> <li>NONE (0) (or false) </li>
	 * 
	 * <li>ALL_IMMEDIATE (1) (or true) - this is the default mode in Tween</li>
	 * 
	 * <li>AUTO (2) - this is the default mode if TweenMax, TimelineLite, or TimelineMax
	 * is used in the swf. (these classes automatically init() OverwriteManager if you
	 * haven't done so already)</li>
	 * 
	 * <li>CONCURRENT (3) (requires OverwriteManager)</li>
	 * 
	 * <li>ALL_ONSTART (4) (requires OverwriteManager)</li>
	 * 
	 * <li>PREEXISTING (5) (requires OverwriteManager)</li>
	 * 
	 * </ul></li> </ul>
	 * 
	 * <b>Note:</b> Using a <code><a
	 * href="data/TweenVars.html">TweenVars</a></code> instance instead of a
	 * generic object to define your <code>vars</code> is a bit more verbose but provides
	 * code hinting and improved debugging because it enforces strict data typing. Use
	 * whichever one you prefer.<br /><br />
	 * 
	 * <b>PLUGINS:</b><br /><br />
	 * 
	 * There are many plugins that add capabilities through other special properties. Some
	 * examples are "tint", "volume", "frame", "frameLabel", "bezier", "blurFilter",
	 * "colorMatrixFilter", "hexColors", and many more. Adding the capabilities is as
	 * simple as activating the plugin with a single line of code, like
	 * TweenPlugin.activate([TintPlugin]); Get information about all the plugins at <a
	 * href="http://www.Tween.com">http://www.Tween.com</a><br /><br />
	 * 
	 * <b>EXAMPLES:</b> <br /><br />
	 * 
	 * Please see <a href="http://www.Tween.com">http://www.Tween.com</a> for
	 * examples, tutorials, and interactive demos. <br /><br />
	 * 
	 * <b>NOTES / TIPS:</b><br /><br /> <ul> <li> The base Tween class adds about
	 * 4.7kb to your compressed swf (if no plugins are activated)</li>
	 * 
	 * <li> Passing values as Strings will make the tween relative to the current value.
	 * For example, if you do <code>Tween.to(mc, 2, {x:"-20"});</code> it'll move the
	 * mc.x to the left 20 pixels which is the same as doing <code>Tween.to(mc, 2,
	 * {x:mc.x - 20});</code> You could also cast it like: <code>Tween.to(mc, 2,
	 * {x:String(myVariable)});</code></li>
	 * 
	 * <li> You can change the <code>Tween.defaultEase</code> function if you prefer
	 * something other than <code>Regular.easeOut</code>.</li>
	 * 
	 * <li> Kill all tweens for a particular object anytime with the
	 * <code>Tween.killTweensOf(mc); </code></li>
	 * 
	 * <li> You can kill all delayedCalls to a particular function using
	 * <code>Tween.killDelayedCallsTo(myFunction);</code> This can be helpful if you
	 * want to preempt a call.</li>
	 * 
	 * <li> Use the <code>Tween.from()</code> method to animate things into place. For
	 * example, if you have things set up on the stage in the spot where they should end
	 * up, and you just want to animate them into place, you can pass in the beginning x
	 * and/or y and/or alpha (or whatever properties you want).</li>
	 * 
	 * <li> If you find this class useful, please consider joining Club GreenSock which
	 * not only helps to sustain ongoing development, but also gets you bonus plugins,
	 * classes and other benefits that are ONLY available to members. Learn more at <a
	 * href="http://www.greensock.com/club/">http://www.greensock.com/club/</a></li> </ul>
	 */
	public class Tween extends TweenBase
	{
		//-----------------------------------------------------------------------------------------
		// Properties
		//-----------------------------------------------------------------------------------------
		
		/**
		 * @private
		 */
		public static const version:Number = 11.695;
		
		/**
		 * When plugins are activated, the class is added (named based on the special
		 * property) to this map so that we can quickly look it up in the
		 * init() method.
		 * 
		 * @private
		 */
		public static var plugins:Object = {};
		
		/**
		 * @private
		 */
		public static var fastEaseLookup:Dictionary = new Dictionary(false);
		
		/**
		 * For notifying plugins of significant events like when the tween finishes
		 * initializing, when it is disabled/enabled, and when it completes (some plugins
		 * need to take actions when those events occur)
		 * 
		 * @private
		 */
		public static var onPluginEvent:Function;
		
		/**
		 * @private
		 */
		public static var killDelayedCallsTo:Function = Tween.killTweensOf;
		
		/**
		 * Provides an easy way to change the default easing equation.
		 */
		public static var defaultEase:Function = Tween.easeOut;
		
		/**
		 * Makes it possible to integrate OverwriteManager for adding various overwriting
		 * capabilities.
		 * 
		 * @private
		 */
		public static var overwriteManager:Object;
		
		/**
		 * Gets updated on every frame. This syncs all the tweens and prevents drifting of
		 * the startTime that happens under heavy loads with most other engines.
		 * 
		 * @private
		 */
		public static var rootFrame:Number;
		
		/**
		 * All tweens get associated with a timeline. The rootTimeline is the default for
		 * all time-based tweens.
		 * 
		 * @private
		 */
		public static var rootTimeline:TimelineBase;
		
		/**
		 * All tweens get associated with a timeline. The rootFramesTimeline is the
		 * default for all frames-based tweens.
		 * 
		 * @private
		 */
		public static var rootFramesTimeline:TimelineBase;
		
		/**
		 * Holds references to all our tween instances organized by target for quick
		 * lookups (for overwriting).
		 * 
		 * @private
		 */
		public static var masterList:Dictionary = new Dictionary(false);
		
		/**
		 * Drives all our ENTER_FRAME events.
		 * 
		 * @private
		 */
		private static var _shape:Shape;
		
		/**
		 * Lookup for all of the reserved "special property" keywords.
		 * 
		 * @private
		 */
		 protected static var _reservedProperties:Object =
		 {
			data: 1,
			delay: 1,
			ease: 1,
			easeParams: 1,
			immediateRender: 1,
			orientToBezier: 1,
			overwrite: 1,
			paused: 1,
			proxiedEase: 1,
			repeat: 1,
			repeatDelay: 1,
			runBackwards: 1,
			startAt: 1,
			timeScale: 1,
			timeline: 1,
			useFrames: 1,
			yoyo: 1,
			onComplete: 1,
			onCompleteListener: 1,
			onCompleteParams: 1,
			onInit: 1,
			onInitParams: 1,
			onRepeat: 1,
			onRepeatListener: 1,
			onRepeatParams: 1,
			onReverseComplete: 1,
			onReverseCompleteListener: 1,
			onReverseCompleteParams: 1,
			onStart: 1,
			onStartListener: 1,
			onStartParams: 1,
			onUpdate: 1,
			onUpdateListener: 1,
			onUpdateParams: 1
		};
		
		/**
		 * Target object whose properties this tween affects. This can be ANY object, not
		 * just a DisplayObject.
		 * 
		 * @private
		 **/
		public var target:Object;
		
		/**
		 * Lookup object for TweenVO objects. For example, if this tween is handling the
		 * "x" and "y" properties of the target, the voLookup object will have an
		 * "x" and "y" property, each pointing to the associated TweenVO object. This
		 * can be very helpful for speeding up overwriting. This is a public variable, but
		 * should almost never be used directly.
		 * 
		 * @private
		 */
		public var voLookup:Object;
		
		/**
		 * result of _ease(this.currentTime, 0, 1, this.duration). Usually between 0 and
		 * 1, but not always (like with Elastic.easeOut, it could shoot past 1 or 0).
		 * 
		 * @private
		 */
		public var ratio:Number = 0;
		
		/**
		 * First TweenVO instance - all of which are stored in a linked list for speed.
		 * Traverse them using nextNode and prevNode. Typically you should NOT use this
		 * property (it is made public for speed and file size purposes).
		 * 
		 * @private
		 */
		public var cachedVO:TweenVO;
		
		/**
		 * Easing method to use which determines how the values animate over time.
		 * Examples are Elastic.easeOut and Strong.easeIn. Many are found in the
		 * fl.motion.easing package or com.greensock.easing.
		 * 
		 * @private
		 */
		protected var _ease:Function;
		
		/**
		 * 0 = NONE, 1 = ALL, 2 = AUTO 3 = CONCURRENT, 4 = ALL_AFTER
		 * 
		 * @private
		 */
		protected var _overwriteMode:int;
		
		/**
		 * When other tweens overwrite properties in this tween, the properties get added
		 * to this object. Remember, sometimes properties are overwritten BEFORE the tween
		 * inits, like when two tweens start at the same time, the later one overwrites
		 * the previous one.
		 * 
		 * @private
		 */
		protected var _overwrittenProps:Object;
		
		/**
		 * If this tween has any TweenPlugins, we set this to true - it helps speed things
		 * up in onComplete
		 * 
		 * @private
		 */
		protected var _hasPlugins:Boolean;
		
		/**
		 * If this tween has any TweenPlugins that need to be notified of a change in the
		 * "enabled" status, this will be true. (speeds things up in the enabled setter)
		 * 
		 * @private
		 */
		protected var _notifyPluginsOfEnabled:Boolean;
		
		
		//-----------------------------------------------------------------------------------------
		// Constructor
		//-----------------------------------------------------------------------------------------
		
		/**
		 * @param tweenTarget Target object whose properties this tween affects. This can be
		 *            ANY object, not just a DisplayObject.
		 * @param duration Duration in seconds (or in frames if the tween's timing mode is
		 *            frames-based)
		 * @param tweenVars An object containing the end values of the properties you're
		 *            tweening. For example, to tween to x=100, y=100, you could pass
		 *            {x:100, y:100}. It can also contain special properties like
		 *            "onComplete", "ease", "delay", etc.
		 */
		public function Tween(tweenTarget:Object, duration:Number, tweenVars:TweenVars = null)
		{
			super(duration, tweenVars);
			
			if (!tweenTarget) throw new Error("tweenTarget cannot be null.");
			
			target = tweenTarget;
			voLookup = {};
			
			/* If timeScale is in the vars object and the target is a TweenBase, this
			 * tween's timeScale must be adjusted (in TweenBase's constructor, it was
			 * set to whatever the vars.timeScale was). */
			if (target is TweenBase && !isNaN(vars.timeScale))
			{
				cachedTimeScale = 1.0;
			}
			
			/* Temporarily - we'll check the vars object for an ease property in the init()
			 * method. We set it to the default initially for speed purposes. */
			_ease = defaultEase;
			
			/* Handle overwriting (if necessary) on tweens of the same object and add
			 * the tween to the Dictionary for future reference. Also remember to
			 * accommodate Tween vars and TweenPro vars. */
			_overwriteMode = (vars.overwriteMode <= 0
				|| (!overwriteManager['enabled'] && vars.overwriteMode > 1))
					? overwriteManager['mode']
					: vars.overwriteMode;
			
			var tweens:Array = masterList[target];
			if (!tweens)
			{
				masterList[target] = [this];
			}
			else
			{
				/* Overwrite all other existing tweens of the same object (ALL mode). */
				if (_overwriteMode == 1)
				{
					for each (var t:Tween in tweens)
					{
						if (!t.gc) t.setEnabled(false, false);
					}
					masterList[target] = [this];
				}
				else
				{
					tweens[tweens.length] = this;
				}
			}
			
			if (active || vars.immediateRender)
			{
				renderTime(0, false, true);
			}
		}
		
		
		//-----------------------------------------------------------------------------------------
		// Public Methods
		//-----------------------------------------------------------------------------------------
		
		/**
		 * Allows particular properties of the tween to be killed. For example, if a tween
		 * is affecting the "x", "y", and "alpha" properties and you want to kill just the
		 * "x" and "y" parts of the tween, you'd do <code>myTween.killVars({x:true,
		 * y:true});</code>
		 * 
		 * @param vars An object containing a corresponding property for each one that
		 *            should be killed. The values don't really matter. For example, to
		 *            kill the x and y property tweens, do <code>myTween.killVars({x:true,
		 *            y:true});</code>
		 * @param permanent If true, the properties specified in the vars object will be
		 *            permanently disallowed in the tween. Typically the only time false
		 *            might be used is while the tween is in the process of initting and a
		 *            plugin needs to make sure tweens of a particular property (or set of
		 *            properties) is killed.
		 * @return Boolean value indicating whether or not properties may have changed on
		 *         the target when any of the vars were disabled. For example, when a
		 *         motionBlur (plugin) is disabled, it swaps out a BitmapData for the
		 *         target and may alter the alpha. We need to know this in order to
		 *         determine whether or not a new tween that is overwriting this one
		 *         should be re-initted() with the changed properties.
		 */
		public function killVars(vars:Object, permanent:Boolean = true):Boolean
		{
			if (!_overwrittenProps) _overwrittenProps = {};
			
			var p:String;
			var vo:TweenVO;
			var changed:Boolean;
			
			for (p in vars)
			{
				if (p in voLookup)
				{
					vo = voLookup[p];
					if (vo.plugin && vo.name == MULTIPLE)
					{
						vo.plugin.killProperties(vars);
						if (vo.plugin.overwriteProperties.length == 0)
						{
							vo.name = "";
						}
						if (p != vo.plugin.propertyName || vo.name == "")
						{
							delete voLookup[p];
						}
					}
					
					if (vo.name != MULTIPLE)
					{
						/* Remove TweenVO (do it inline to improve speed and keep file size low). */
						if (vo.next) vo.next.prev = vo.prev;
						if (vo.prev) vo.prev.next = vo.next;
						else if (cachedVO == vo) cachedVO = vo.next;
						
						if (vo.plugin)
						{
							if (vo.plugin.onDisable != null)
							{
								vo.plugin.onDisable();
								/* Some plugins need to be notified so they can perform
								 * cleanup tasks first. */
								if (vo.plugin.activeDisable) changed = true;
							}
						}
						delete voLookup[p];
					}
				}
				
				if (permanent && vars != _overwrittenProps)
				{
					_overwrittenProps[p] = 1;
				}
			}
			
			return changed;
		}
		
		
		/**
		 * @inheritDoc
		 */
		override public function invalidate():void
		{
			if (_notifyPluginsOfEnabled && cachedVO) onPluginEvent(TweenPlugin.ON_DISABLE, this);
			cachedVO = null;
			_overwrittenProps = null;
			_hasUpdate = initialized = active = _notifyPluginsOfEnabled = false;
			voLookup = {};
		}
		
		
		//-----------------------------------------------------------------------------------------
		// Static Methods
		//-----------------------------------------------------------------------------------------
		
		/**
		 * Static method for creating a Tween instance. This can be more intuitive for
		 * some developers and shields them from potential garbage collection issues that
		 * could arise when assigning a tween instance to a variable that persists. The
		 * following lines of code produce exactly the same result: <br /><br /><code>
		 * 
		 * var myTween:Tween = new Tween(mc, 1, {x:100}); <br /> Tween.to(mc,
		 * 1, {x:100}); <br /> var myTween:Tween = Tween.to(mc, 1,
		 * {x:100});</code>
		 * 
		 * @param target Target object whose properties this tween affects. This can be
		 *            ANY object, not just a DisplayObject.
		 * @param duration Duration in seconds (or in frames if the tween's timing mode is
		 *            frames-based)
		 * @param vars An object containing the end values of the properties you're
		 *            tweening. For example, to tween to x=100, y=100, you could pass
		 *            {x:100, y:100}. It can also contain special properties like
		 *            "onComplete", "ease", "delay", etc.
		 * @return Tween instance
		 */
		public static function to(target:Object, duration:Number, vars:TweenVars):Tween
		{
			return new Tween(target, duration, vars);
		}
		
		
		/**
		 * Static method for creating a Tween instance that tweens in the opposite
		 * direction compared to a Tween.to() tween. In other words, you define the
		 * START values in the vars object instead of the end values, and the tween will
		 * use the current values as the end values. This can be very useful for animating
		 * things into place on the stage because you can build them in their end
		 * positions and do some simple Tween.from() calls to animate them into place.
		 * <b>NOTE:</b> By default, <code>immediateRender</code> is <code>true</code> in
		 * from() tweens, meaning that they immediately render their starting state
		 * regardless of any delay that is specified. You can override this behavior by
		 * passing <code>immediateRender:false</code> in the <code>vars</code> object so
		 * that it will wait to render until the tween actually begins (often the desired
		 * behavior when inserting into timelines). To illustrate the default behavior,
		 * the following code will immediately set the <code>alpha</code> of
		 * <code>mc</code> to 0 and then wait 2 seconds before tweening the
		 * <code>alpha</code> back to 1 over the course of 1.5 seconds:<br /><br /><code>
		 * 
		 * Tween.from(mc, 1.5, {alpha:0, delay:2});</code>
		 * 
		 * @param target Target object whose properties this tween affects. This can be
		 *            ANY object, not just a DisplayObject.
		 * @param duration Duration in seconds (or in frames if the tween's timing mode is
		 *            frames-based)
		 * @param vars An object containing the start values of the properties you're
		 *            tweening. For example, to tween from x=100, y=100, you could pass
		 *            {x:100, y:100}. It can also contain special properties like
		 *            "onComplete", "ease", "delay", etc.
		 * @return Tween instance
		 */
		public static function from(target:Object, duration:Number, vars:TweenVars):Tween
		{
			if (vars.isGSVars)
			{
				// to accommodate TweenMaxVars instances for strong data typing and code hinting.
				vars = vars.vars;
			}
			vars.runBackwards = true;
			if (!("immediateRender" in vars)) vars.immediateRender = true;
			return new Tween(target, duration, vars);
		}
		
		
		/**
		 * Provides a simple way to call a function after a set amount of time (or
		 * frames). You can optionally pass any number of parameters to the function too.
		 * For example:<br /><br /><code>
		 * 
		 * Tween.delayedCall(1, myFunction, ["param1", 2]); <br /> function
		 * myFunction(param1:String, param2:Number):void { <br />
		 * trace("called myFunction and passed params: " + param1 + ", " + param2); <br />
		 * } </code>
		 * 
		 * @param delay Delay in seconds (or frames if useFrames is true) before the
		 *            function should be called
		 * @param onComplete Function to call
		 * @param onCompleteParams An Array of parameters to pass the function.
		 * @param useFrames If the delay should be measured in frames instead of seconds,
		 *            set useFrames to true (default is false)
		 * @return Tween instance
		 */
		public static function delayedCall(delay:Number, onComplete:Function,
			onCompleteParams:Array = null, useFrames:Boolean = false):Tween
		{
			var vars:TweenVars = new TweenVars();
			vars.delay = delay;
			vars.onComplete = onComplete;
			vars.completeParams = onCompleteParams;
			vars.immediateRender = false;
			vars.useFrames = useFrames;
			vars.overwriteMode = 0;
			return new Tween(onComplete, 0, vars);
		}
		
		
		/**
		 * Kills all the tweens of a particular object or delayedCalls to a particular
		 * function, optionally completing them first. If, for example, you want to kill
		 * all tweens of the "mc" object, you'd do:<br /><br /><code>
		 * 
		 * Tween.killTweensOf(mc);<br /><br /></code>
		 * 
		 * You can also just kill certain tweening properties of a particular object. For
		 * example, if you only want to kill all the "alpha" and "x" portions of mc's
		 * tweens, you'd do:<br /><br /><code>
		 * 
		 * Tween.killTweensOf(mc, false, {alpha:true, x:true});<br /><br /></code>
		 * 
		 * To kill all the delayedCalls that were created like
		 * <code>Tween.delayedCall(5, myFunction);</code>, you can simply call
		 * <code>Tween.killTweensOf(myFunction);</code> because delayedCalls are just
		 * tweens that have their <code>target</code> and <code>onComplete</code> set to
		 * the same function (and a <code>delay</code> of course). <br /><br />
		 * 
		 * <code>killTweensOf()</code> affects tweens that haven't begun yet too. If, for
		 * example, a tween of object "mc" has a delay of 5 seconds and
		 * <code>Tween.killTweensOf(mc)</code> is called 2 seconds after the tween was
		 * created, it will still be killed even though it hasn't started yet. <br /><br
		 * />
		 * 
		 * @param target Object whose tweens should be immediately killed
		 * @param complete Indicates whether or not the tweens should be forced to
		 *            completion before being killed.
		 * @param vars An object defining which tweening properties should be killed (null
		 *            causes all properties to be killed). For example, if you only want
		 *            to kill "alpha" and "x" tweens of object "mc", you'd do
		 *            <code>myTimeline.killTweensOf(mc, true, {alpha:true,
		 *            x:true})</code>. If there are no tweening properties remaining in a
		 *            tween after the indicated properties are killed, the entire tween is
		 *            killed, meaning any onComplete, onUpdate, onStart, etc. won't fire.
		 */
		public static function killTweensOf(target:Object, complete:Boolean = false,
			vars:Object = null):void
		{
			if (target in masterList)
			{
				var a:Array = masterList[target];
				var i:int = a.length;
				var tween:Tween;
				
				while (--i > -1)
				{
					tween = a[i];
					if (!tween.gc)
					{
						if (complete)
						{
							tween.complete(false, false);
						}
						if (vars != null)
						{
							tween.killVars(vars);
						}
						if (vars == null || (tween.cachedVO == null && tween.initialized))
						{
							tween.setEnabled(false, false);
						}
					}
				}
				if (vars == null)
				{
					delete masterList[target];
				}
			}
		}
		
		
		/**
		 * Default easing equation.
		 * @private
		 * 
		 * @param t time
		 * @param b start (must always be 0)
		 * @param c change (must always be 1)
		 * @param d duration
		 * @return Eased value
		 */
		protected static function easeOut(t:Number, b:Number, c:Number, d:Number):Number
		{
			return 1 - (t = 1 - (t / d)) * t;
		}
		
		
		/**
		 * Initializes the class, activates default plugins, and starts the root
		 * timelines. This should only be called internally. It is technically public only
		 * so that other classes in the GreenSock Tweening Platform can access it, but
		 * again, please avoid calling this method directly.
		 * 
		 * @private
		 */
		public static function initClass():void
		{
			// ACTIVATE PLUGINS HERE...
			/*
			TweenPlugin.activate([
							
			AutoAlphaPlugin,			// tweens alpha and then toggles "visible" to false if/when alpha is zero
			EndArrayPlugin,				// tweens numbers in an Array
			FramePlugin,				// tweens MovieClip frames
			RemoveTintPlugin,			// allows you to remove a tint
			TintPlugin,					// tweens tints
			VisiblePlugin,				// tweens a target's "visible" property
			VolumePlugin,				// tweens the volume of a MovieClip or SoundChannel or anything with a "soundTransform" property
				
			BevelFilterPlugin,			// tweens BevelFilters
			BezierPlugin,				// enables bezier tweening
			BezierThroughPlugin,		// enables bezierThrough tweening
			BlurFilterPlugin,			// tweens BlurFilters
			ColorMatrixFilterPlugin,	// tweens ColorMatrixFilters (including hue, saturation, colorize, contrast, brightness, and threshold)
			DropShadowFilterPlugin,		// tweens DropShadowFilters
			GlowFilterPlugin,			// tweens GlowFilters
			HexColorsPlugin,			// tweens hex colors
			ShortRotationPlugin,		// tweens rotation values in the shortest direction
				
			ColorTransformPlugin,		// tweens advanced color properties like exposure, brightness, tintAmount, redOffset, redMultiplier, etc.
			FrameLabelPlugin,			// tweens a MovieClip to particular label
			QuaternionsPlugin,			// tweens 3D Quaternions
			ScalePlugin,				// Tweens both the _xscale and _yscale properties
			ScrollRectPlugin,			// tweens the scrollRect property of a DisplayObject
			SetSizePlugin,				// tweens the width/height of components via setSize()
			SetActualSizePlugin			// tweens the width/height of components via setActualSize()
			TransformMatrixPlugin,		// Tweens the transform.matrix property of any DisplayObject
					
			// DynamicPropsPlugin,			// tweens to dynamic end values. You associate the property with a particular function that returns the target end value **Club GreenSock membership benefit**
			// MotionBlurPlugin,			// applies a directional blur to a DisplayObject based on the velocity and angle of movement. **Club GreenSock membership benefit**
			// Physics2DPlugin,			// allows you to apply basic physics in 2D space, like velocity, angle, gravity, friction, acceleration, and accelerationAngle. **Club GreenSock membership benefit**
			// PhysicsPropsPlugin,			// allows you to apply basic physics to any property using forces like velocity, acceleration, and/or friction. **Club GreenSock membership benefit**
			// TransformAroundCenterPlugin,//tweens the scale and/or rotation of DisplayObjects using the DisplayObject's center as the registration point **Club GreenSock membership benefit**
			// TransformAroundPointPlugin,	// tweens the scale and/or rotation of DisplayObjects around a particular point (like a custom registration point) **Club GreenSock membership benefit**
				
				
			{}]);
			 */
			
			rootFrame = 0;
			rootTimeline = new TimelineBase(null);
			rootFramesTimeline = new TimelineBase(null);
			rootTimeline.cachedStartTime = getTimer() * 0.001;
			rootFramesTimeline.cachedStartTime = rootFrame;
			rootTimeline.autoRemoveChildren = true;
			rootFramesTimeline.autoRemoveChildren = true;
			
			_shape = new Shape();
			_shape.addEventListener(Event.ENTER_FRAME, updateAll, false, 0, true);
			
			if (overwriteManager == null)
			{
				overwriteManager = {mode: 1, enabled: false};
			}
		}
		
		
		//-----------------------------------------------------------------------------------------
		// Callback Handlers
		//-----------------------------------------------------------------------------------------
		
		/**
		 * Updates the rootTimeline and rootFramesTimeline and collects garbage every 60 frames.
		 * 
		 * @private
		 * @param e ENTER_FRAME Event
		 */
		protected static function updateAll(e:Event = null):void
		{
			rootTimeline.renderTime(((getTimer() * 0.001) - rootTimeline.cachedStartTime) * rootTimeline.cachedTimeScale, false, false);
			rootFrame += 1;
			rootFramesTimeline.renderTime((rootFrame - rootFramesTimeline.cachedStartTime) * rootFramesTimeline.cachedTimeScale, false, false);
			
			if (!(rootFrame % 60))
			{
				// garbage collect every 60 frames...
				var ml:Dictionary = masterList, tgt:Object, a:Array, i:int;
				for (tgt in ml)
				{
					a = ml[tgt];
					i = a.length;
					while (--i > -1)
					{
						if (Tween(a[i]).gc)
						{
							a.splice(i, 1);
						}
					}
					if (a.length == 0)
					{
						delete ml[tgt];
					}
				}
			}
		}
		
		
		//-----------------------------------------------------------------------------------------
		// Private Methods
		//-----------------------------------------------------------------------------------------
		
		/**
		 * Initializes the property tweens, determining their start values and amount of
		 * change. Also triggers overwriting if necessary and sets the _hasUpdate
		 * variable.
		 * 
		 * @private
		 */
		protected function init():void
		{
			if (vars.onInit != null)
			{
				vars.onInit.apply(null, vars.initParams);
			}
			
			var plugin:TweenPlugin;
			var prioritize:Boolean = false;
			var siblings:Array;
			var p:String;
			
			if (typeof(vars.ease) == "function")
			{
				_ease = vars.ease;
			}
			if (vars.easeParams)
			{
				vars.proxiedEase = _ease;
				_ease = easeProxy;
			}
			
			cachedVO = null;
			voLookup = {};
			
			/* Create a temporary list of all tween vars, both pre-defined ones and
			 * dynamic properties. This is necessary because we can't simply loop over
			 * pre-defined properties with for in/for each in. */
			var a:Array = [];
			/* Add dynamic properties. */
			for (p in vars)
			{
				a.push(p);
			}
			/* Add pre-defined properties (getting from introspection). */
			var plist:XMLList = flash.utils.describeType(vars)..variable.@name;
			for each (p in plist)
			{
				a.push(p);
			}
			
			for each (p in a)
			{
				if (p in _reservedProperties && !(p == TIME_SCALE && target is TweenBase))
				{
					/* ignore. */
				}
				/* Tween is a plugin. */
				else if (plugins[p] && (plugin = new (plugins[p] as Class)()).onInitTween(target, vars[p], this))
				{
					cachedVO = new TweenVO(plugin, CHANGE_FACTOR, 0.0, 1.0,
						(plugin.overwriteProperties.length == 1) ? plugin.overwriteProperties[0] : MULTIPLE,
						plugin, cachedVO);
					
					if (cachedVO.name == MULTIPLE)
					{
						var i:int = plugin.overwriteProperties.length;
						while (--i > -1)
						{
							voLookup[plugin.overwriteProperties[i]] = cachedVO;
						}
					}
					else
					{
						voLookup[cachedVO.name] = cachedVO;
					}
					
					cachedVO.priority = plugin.priority;
					prioritize = true;
					
					if (plugin.onDisable != null || plugin.onEnable != null)
					{
						_notifyPluginsOfEnabled = true;
					}
					_hasPlugins = true;
				}
				/* Only create VOs for properties that are actually part of target object. */
				else if (target.hasOwnProperty(p))
				{
					cachedVO = new TweenVO(target, p, target[p],
						(typeof(vars[p]) == "number")
							? vars[p] - target[p]
							: vars[p],
						p, null, cachedVO);
					voLookup[p] = cachedVO;
				}
			}
			
			if (prioritize)
			{
				// reorders the linked list in order of priority. Uses a static
				// TweenPlugin method in order to minimize file size in Tween.
				onPluginEvent(TweenPlugin.ON_INIT_ALL_PROPERTIES, this);
			}
			
			if (vars.runBackwards)
			{
				var pt:TweenVO = cachedVO;
				while (pt)
				{
					pt.start += pt.change;
					pt.change = -pt.change;
					pt = pt.next;
				}
			}
			
			_hasUpdate = Boolean(vars.onUpdate != null);
			
			if (_overwrittenProps)
			{
				// another tween may have tried to overwrite properties of this tween
				// before init() was called (like if two tweens start at the same time,
				// the one created second will run first).
				killVars(_overwrittenProps);
				if (cachedVO == null)
				{
					// if all tweening properties have been overwritten, kill the tween.
					setEnabled(false, false);
				}
			}
			
			if (_overwriteMode > 1 && cachedVO && (siblings == masterList[target]) && siblings.length > 1)
			{
				if (overwriteManager['manageOverwrites'](this, voLookup, siblings, _overwriteMode))
				{
					// one of the plugins had activeDisable set to true, so properties
					// may have changed when it was disabled meaning we need to re-init().
					init();
				}
			}
			initialized = true;
		}
		
		
		/**
		 * @inheritDoc
		 */
		override public function renderTime(time:Number, suppressEvents:Boolean = false,
			force:Boolean = false):void
		{
			var isComplete:Boolean, prevTime:Number = cachedTime;
			if (time >= cachedDuration)
			{
				cachedTotalTime = cachedTime = cachedDuration;
				ratio = 1;
				isComplete = !cachedReversed;
				if (cachedDuration == 0)
				{
					// zero-duration tweens are tricky because we must discern the
					// momentum/direction of time in order to determine whether the
					// starting values should be rendered or the ending values. If
					// the "playhead" of its timeline goes past the zero-duration
					// tween in the forward direction or lands directly on it, the
					// end values should be rendered, but if the timeline's "playhead"
					// moves past it in the backward direction (from a postitive time
					// to a negative time), the starting values must be rendered.
					if ((time == 0 || _rawPrevTime < 0) && _rawPrevTime != time)
					{
						force = true;
					}
					_rawPrevTime = time;
				}
			}
			else if (time <= 0)
			{
				cachedTotalTime = cachedTime = ratio = 0;
				if (time < 0)
				{
					active = false;
					if (cachedDuration == 0)
					{
						// zero-duration tweens are tricky because we must discern the
						// momentum/direction of time in order to determine whether the
						// starting values should be rendered or the ending values. If
						// the "playhead" of its timeline goes past the zero-duration
						// tween in the forward direction or lands directly on it, the
						// end values should be rendered, but if the timeline's
						// "playhead" moves past it in the backward direction (from
						// a postitive time to a negative time), the starting values
						// must be rendered.
						if (_rawPrevTime > 0)
						{
							force = true;
							isComplete = true;
						}
						_rawPrevTime = time;
					}
				}
				if (cachedReversed && prevTime != 0)
				{
					isComplete = true;
				}
			}
			else
			{
				cachedTotalTime = cachedTime = time;
				ratio = _ease(time, 0, 1, cachedDuration);
			}
			
			if (cachedTime == prevTime && !force)
			{
				return;
			}
			else if (!initialized)
			{
				init();
				if (!isComplete && cachedTime)
				{
					// _ease is initially set to defaultEase, so now that init() has run,
					// _ease is set properly and we need to recalculate the ratio. Overall
					// this is faster than using conditional logic earlier in the method
					// to avoid having to set ratio twice because we only init() once but
					// renderTime() gets called VERY frequently.
					ratio = _ease(cachedTime, 0, 1, cachedDuration);
				}
			}
			if (!active && !cachedPaused)
			{
				// so that if the user renders a tween (as opposed to the timeline
				// rendering it), the timeline is forced to re-render and align it
				// with the proper time/frame on the next rendering cycle. Maybe the
				// tween already finished but the user manually re-renders it as halfway done.
				active = true;
			}
			if (prevTime == 0 && vars.onStart && (cachedTime != 0 || cachedDuration == 0) && !suppressEvents)
			{
				vars.onStart.apply(null, vars.startParams);
			}
			
			var pt:TweenVO = cachedVO;
			while (pt)
			{
				pt.target[pt.property] = pt.start + (ratio * pt.change);
				pt = pt.next;
			}
			
			if (_hasUpdate && !suppressEvents)
			{
				vars.onUpdate.apply(null, vars.updateParams);
			}
			
			if (isComplete && !gc)
			{
				// check gc because there's a chance that kill() could be called in an onUpdate
				if (_hasPlugins && cachedVO)
				{
					onPluginEvent(TweenPlugin.ON_COMPLETE, this);
				}
				complete(true, suppressEvents);
			}
		}
		
		
		/**
		 * @inheritDoc
		 */
		override public function setEnabled(enabled:Boolean,
			ignoreTimeline:Boolean = false):Boolean
		{
			if (enabled)
			{
				var a:Array = Tween.masterList[target];
				if (!a)
				{
					Tween.masterList[target] = [this];
				}
				else if (a.indexOf(this) == -1)
				{
					a[a.length] = this;
				}
			}
			
			super.setEnabled(enabled, ignoreTimeline);
			
			if (_notifyPluginsOfEnabled && cachedVO)
			{
				return onPluginEvent(((enabled) ? TweenPlugin.ON_ENABLE : TweenPlugin.ON_DISABLE), this);
			}
			return false;
		}
		
		
		/**
		 * Only used for easing equations that accept extra parameters (like
		 * Elastic.easeOut and Back.easeOut). Basically, it acts as a proxy. To utilize
		 * it, pass an Array of extra parameters via the vars object's "easeParams"
		 * special property.
		 * 
		 * @private
		 * 
		 * @param t time
		 * @param b start
		 * @param c change
		 * @param d duration
		 * @return Eased value
		 */
		protected function easeProxy(t:Number, b:Number, c:Number, d:Number):Number
		{
			return vars.proxiedEase.apply(null, arguments.concat(vars.easeParams));
		}
	}
}