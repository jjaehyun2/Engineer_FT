/*
Feathers
Copyright 2012-2013 Joshua Tynjala. All Rights Reserved.

This program is free software. You can redistribute and/or modify it in
accordance with the terms of the accompanying license agreement.
*/
package feathers.controls
{
	import flash.events.MouseEvent;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import flash.utils.getTimer;
	
	import feathers.controls.supportClasses.IViewPort;
	import feathers.core.FeathersControl;
	import feathers.core.PropertyProxy;
	import feathers.events.ExclusiveTouch;
	import feathers.events.FeathersEventType;
	import feathers.system.DeviceCapabilities;
	import feathers.utils.math.roundDownToNearest;
	import feathers.utils.math.roundToNearest;
	import feathers.utils.math.roundUpToNearest;
	
	import starling.animation.IAnimatable;
	import starling.animation.Transitions;
	import starling.animation.Tween;
	import starling.core.Starling;
	import starling.display.DisplayObject;
	import starling.display.Quad;
	import starling.events.Event;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;

	/**
	 * Dispatched when the scroller scrolls in either direction or when the view
	 * port's scrolling bounds have changed. Listen for <code>FeathersEventType.SCROLL_START</code>
	 * to know when scrolling starts as a result of user interaction or when
	 * scrolling is triggered by an animation. Similarly, listen for
	 * <code>FeathersEventType.SCROLL_COMPLETE</code> to know when the scrolling
	 * ends.
	 *
	 * @eventType starling.events.Event.SCROLL
	 * @see feathers.events.FeathersEventType.SCROLL_START
	 * @see feathers.events.FeathersEventType.SCROLL_COMPLETE
	 */
	[Event(name="scroll",type="starling.events.Event")]

	/**
	 * Dispatched when the scroller starts scrolling in either direction
	 * as a result of either user interaction or animation.
	 *
	 * <p>Note: If <code>horizontalScrollPosition</code> or <code>verticalScrollPosition</code>
	 * is set manually (in other words, the scrolling is not triggered by user
	 * interaction or an animated scroll), no <code>FeathersEventType.SCROLL_START</code>
	 * or <code>FeathersEventType.SCROLL_COMPLETE</code> events will be
	 * dispatched.</p>
	 *
	 * @eventType feathers.events.FeathersEventType.SCROLL_START
	 * @see feathers.events.FeathersEventType.SCROLL_COMPLETE
	 * @see feathers.events.FeathersEventType.SCROLL
	 */
	[Event(name="scrollStart",type="starling.events.Event")]

	/**
	 * Dispatched when the scroller finishes scrolling in either direction
	 * as a result of either user interaction or animation. Animations may not
	 * end at the same time that user interaction ends, so the event may be
	 * delayed if user interaction triggers scrolling again.
	 *
	 * <p>Note: If <code>horizontalScrollPosition</code> or <code>verticalScrollPosition</code>
	 * is set manually (in other words, the scrolling is not triggered by user
	 * interaction or an animated scroll), no <code>FeathersEventType.SCROLL_START</code>
	 * or <code>FeathersEventType.SCROLL_COMPLETE</code> events will be
	 * dispatched.</p>
	 *
	 * @eventType feathers.events.FeathersEventType.SCROLL_COMPLETE
	 * @see feathers.events.FeathersEventType.SCROLL_START
	 * @see feathers.events.FeathersEventType.SCROLL
	 */
	[Event(name="scrollComplete",type="starling.events.Event")]

	/**
	 * Dispatched when the user starts dragging the scroller when
	 * <code>INTERACTION_MODE_TOUCH</code> is enabled or when the user starts
	 * interacting with the scroll bar.
	 *
	 * <p>Note: If <code>horizontalScrollPosition</code> or <code>verticalScrollPosition</code>
	 * is set manually (in other words, the scrolling is not triggered by user
	 * interaction), no <code>FeathersEventType.BEGIN_INTERACTION</code>
	 * or <code>FeathersEventType.END_INTERACTION</code> events will be
	 * dispatched.</p>
	 *
	 * @eventType feathers.events.FeathersEventType.BEGIN_INTERACTION
	 * @see feathers.events.FeathersEventType.END_INTERACTION
	 * @see feathers.events.FeathersEventType.SCROLL
	 */
	[Event(name="beginInteraction",type="starling.events.Event")]

	/**
	 * Dispatched when the user stops dragging the scroller when
	 * <code>INTERACTION_MODE_TOUCH</code> is enabled or when the user stops
	 * interacting with the scroll bar. The scroller may continue scrolling
	 * after this event is dispatched if the user interaction has also triggered
	 * an animation.
	 *
	 * <p>Note: If <code>horizontalScrollPosition</code> or <code>verticalScrollPosition</code>
	 * is set manually (in other words, the scrolling is not triggered by user
	 * interaction), no <code>FeathersEventType.BEGIN_INTERACTION</code>
	 * or <code>FeathersEventType.END_INTERACTION</code> events will be
	 * dispatched.</p>
	 *
	 * @eventType feathers.events.FeathersEventType.END_INTERACTION
	 * @see feathers.events.FeathersEventType.BEGIN_INTERACTION
	 * @see feathers.events.FeathersEventType.SCROLL
	 */
	[Event(name="endInteraction",type="starling.events.Event")]

	/**
	 * Allows horizontal and vertical scrolling of a <em>view port</em>. Not
	 * meant to be used as a standalone container or component. Generally meant
	 * to be the super class of another component that needs to support
	 * scrolling. To put components in a generic scrollable container (with
	 * optional layout), see <code>ScrollContainer</code>. To scroll long
	 * passages of text, see <code>ScrollText</code>.
	 *
	 * <p>This component is generally not instantiated directly. Instead it is
	 * typically used as a super class for other scrolling components like lists
	 * and containers. With that in mind, no code example is included here.</p>
	 *
	 * @see http://wiki.starling-framework.org/feathers/scroller
	 * @see ScrollContainer
	 * @see ScrollText
	 */
	public class Scroller extends FeathersControl implements IAnimatable
	{
		/**
		 * @private
		 */
		private static const HELPER_POINT:Point = new Point();

		/**
		 * @private
		 */
		protected static const INVALIDATION_FLAG_SCROLL_BAR_RENDERER:String = "scrollBarRenderer";

		/**
		 * @private
		 */
		protected static const INVALIDATION_FLAG_PENDING_SCROLL:String = "pendingScroll";

		/**
		 * @private
		 */
		protected static const INVALIDATION_FLAG_PENDING_REVEAL_SCROLL_BARS:String = "pendingRevealScrollBars";

		/**
		 * The scroller may scroll if the view port is larger than the
		 * scroller's bounds. If the interaction mode is touch, the elastic
		 * edges will only be active if the maximum scroll position is greater
		 * than zero. If the scroll bar display mode is fixed, the scroll bar
		 * will only be visible when the maximum scroll position is greater than
		 * zero.
		 *
		 * @see feathers.controls.Scroller#horizontalScrollPolicy
		 * @see feathers.controls.Scroller#verticalScrollPolicy
		 */
		public static const SCROLL_POLICY_AUTO:String = "auto";

		/**
		 * The scroller will always scroll. If the interaction mode is touch,
		 * elastic edges will always be active, even when the maximum scroll
		 * position is zero. If the scroll bar display mode is fixed, the scroll
		 * bar will always be visible.
		 *
		 * @see feathers.controls.Scroller#horizontalScrollPolicy
		 * @see feathers.controls.Scroller#verticalScrollPolicy
		 */
		public static const SCROLL_POLICY_ON:String = "on";

		/**
		 * The scroller does not scroll at all. If the scroll bar display mode
		 * is fixed or float, the scroll bar will never be visible.
		 *
		 * @see feathers.controls.Scroller#horizontalScrollPolicy
		 * @see feathers.controls.Scroller#verticalScrollPolicy
		 */
		public static const SCROLL_POLICY_OFF:String = "off";

		/**
		 * The scroll bars appear above the scroller's view port, and fade out
		 * when not in use.
		 *
		 * @see feathers.controls.Scroller#scrollBarDisplayMode
		 */
		public static const SCROLL_BAR_DISPLAY_MODE_FLOAT:String = "float";

		/**
		 * The scroll bars are always visible and appear next to the scroller's
		 * view port, making the view port smaller than the scroller.
		 *
		 * @see feathers.controls.Scroller#scrollBarDisplayMode
		 */
		public static const SCROLL_BAR_DISPLAY_MODE_FIXED:String = "fixed";

		/**
		 * The scroll bars are never visible.
		 *
		 * @see feathers.controls.Scroller#scrollBarDisplayMode
		 */
		public static const SCROLL_BAR_DISPLAY_MODE_NONE:String = "none";

		/**
		 * The vertical scroll bar will be positioned on the right.
		 *
		 * @see feathers.controls.Scroller#verticalScrollBarPosition
		 */
		public static const VERTICAL_SCROLL_BAR_POSITION_RIGHT:String = "right";

		/**
		 * The vertical scroll bar will be positioned on the left.
		 *
		 * @see feathers.controls.Scroller#verticalScrollBarPosition
		 */
		public static const VERTICAL_SCROLL_BAR_POSITION_LEFT:String = "left";

		/**
		 * The user may touch anywhere on the scroller and drag to scroll. The
		 * scroll bars will be visual indicator of position, but they will not
		 * be interactive.
		 *
		 * @see feathers.controls.Scroller#interactionMode
		 */
		public static const INTERACTION_MODE_TOUCH:String = "touch";

		/**
		 * The user may only interact with the scroll bars to scroll. The user
		 * cannot touch anywhere in the scroller's content and drag like a touch
		 * interface.
		 *
		 * @see feathers.controls.Scroller#interactionMode
		 */
		public static const INTERACTION_MODE_MOUSE:String = "mouse";

		/**
		 * The user may touch anywhere on the scroller and drag to scroll, and
		 * the scroll bars may be dragged separately. For most touch interfaces,
		 * this is not a common behavior. The scroll bar on touch interfaces is
		 * often simply a visual indicator and non-interactive.
		 *
		 * <p>One case where this mode might be used is a "scroll bar" that
		 * displays a tappable alphabetical index to navigate a
		 * <code>GroupedList</code> with alphabetical categories.</p>
		 *
		 * @see feathers.controls.Scroller#interactionMode
		 */
		public static const INTERACTION_MODE_TOUCH_AND_SCROLL_BARS:String = "touchAndScrollBars";

		/**
		 * Flag to indicate that the clipping has changed.
		 */
		protected static const INVALIDATION_FLAG_CLIPPING:String = "clipping";

		/**
		 * @private
		 * The point where we stop calculating velocity changes because floating
		 * point issues can start to appear.
		 */
		private static const MINIMUM_VELOCITY:Number = 0.02;

		/**
		 * @private
		 * The friction applied every frame when the scroller is "thrown".
		 */
		private static const FRICTION:Number = 0.998;

		/**
		 * @private
		 * Extra friction applied when the scroller is beyond its bounds and
		 * needs to bounce back.
		 */
		private static const EXTRA_FRICTION:Number = 0.95;

		/**
		 * @private
		 * The current velocity is given high importance.
		 */
		private static const CURRENT_VELOCITY_WEIGHT:Number = 2.33;

		/**
		 * @private
		 * Older saved velocities are given less importance.
		 */
		private static const VELOCITY_WEIGHTS:Vector.<Number> = new <Number>[1, 1.33, 1.66, 2];

		/**
		 * @private
		 */
		private static const MAXIMUM_SAVED_VELOCITY_COUNT:int = 4;

		/**
		 * The default value added to the <code>nameList</code> of the
		 * horizontal scroll bar.
		 *
		 * @see feathers.core.IFeathersControl#nameList
		 */
		public static const DEFAULT_CHILD_NAME_HORIZONTAL_SCROLL_BAR:String = "feathers-scroller-horizontal-scroll-bar";

		/**
		 * The default value added to the <code>nameList</code> of the vertical
		 * scroll bar.
		 *
		 * @see feathers.core.IFeathersControl#nameList
		 */
		public static const DEFAULT_CHILD_NAME_VERTICAL_SCROLL_BAR:String = "feathers-scroller-vertical-scroll-bar";

		/**
		 * @private
		 */
		protected static function defaultHorizontalScrollBarFactory():IScrollBar
		{
			const scrollBar:SimpleScrollBar = new SimpleScrollBar();
			scrollBar.direction = SimpleScrollBar.DIRECTION_HORIZONTAL;
			return scrollBar;
		}

		/**
		 * @private
		 */
		protected static function defaultVerticalScrollBarFactory():IScrollBar
		{
			const scrollBar:SimpleScrollBar = new SimpleScrollBar();
			scrollBar.direction = SimpleScrollBar.DIRECTION_VERTICAL;
			return scrollBar;
		}

		/**
		 * Constructor.
		 */
		public function Scroller()
		{
			super();

			this.addEventListener(Event.ADDED_TO_STAGE, scroller_addedToStageHandler);
			this.addEventListener(Event.REMOVED_FROM_STAGE, scroller_removedFromStageHandler);
		}

		/**
		 * The value added to the <code>nameList</code> of the horizontal scroll
		 * bar. This variable is <code>protected</code> so that sub-classes can
		 * customize the horizontal scroll bar name in their constructors
		 * instead of using the default name defined by <code>DEFAULT_CHILD_NAME_HORIZONTAL_SCROLL_BAR</code>.
		 *
		 * <p>To customize the horizontal scroll bar name without subclassing, see
		 * <code>customHorizontalScrollBarName</code>.</p>
		 *
		 * @see #customHorizontalScrollBarName
		 * @see feathers.core.IFeathersControl#nameList
		 */
		protected var horizontalScrollBarName:String = DEFAULT_CHILD_NAME_HORIZONTAL_SCROLL_BAR;

		/**
		 * The value added to the <code>nameList</code> of the vertical scroll
		 * bar. This variable is <code>protected</code> so that sub-classes can
		 * customize the horizontal scroll bar name in their constructors
		 * instead of using the default name defined by <code>DEFAULT_CHILD_NAME_HORIZONTAL_SCROLL_BAR</code>.
		 *
		 * <p>To customize the vertical scroll bar name without subclassing, see
		 * <code>customVerticalScrollBarName</code>.</p>
		 *
		 * @see #customVerticalScrollBarName
		 * @see feathers.core.IFeathersControl#nameList
		 */
		protected var verticalScrollBarName:String = DEFAULT_CHILD_NAME_VERTICAL_SCROLL_BAR;

		/**
		 * The horizontal scrollbar instance. May be null.
		 *
		 * <p>For internal use in subclasses.</p>
		 *
		 * @see #horizontalScrollBarFactory
		 * @see #createScrollBars()
		 */
		protected var horizontalScrollBar:IScrollBar;

		/**
		 * The vertical scrollbar instance. May be null.
		 *
		 * <p>For internal use in subclasses.</p>
		 *
		 * @see #verticalScrollBarFactory
		 * @see #createScrollBars()
		 */
		protected var verticalScrollBar:IScrollBar;

		/**
		 * @private
		 */
		protected var _topViewPortOffset:Number;

		/**
		 * @private
		 */
		protected var _rightViewPortOffset:Number;

		/**
		 * @private
		 */
		protected var _bottomViewPortOffset:Number;

		/**
		 * @private
		 */
		protected var _leftViewPortOffset:Number;

		/**
		 * @private
		 */
		protected var _hasHorizontalScrollBar:Boolean = false;

		/**
		 * @private
		 */
		protected var _hasVerticalScrollBar:Boolean = false;

		/**
		 * @private
		 */
		protected var _horizontalScrollBarTouchPointID:int = -1;

		/**
		 * @private
		 */
		protected var _verticalScrollBarTouchPointID:int = -1;

		/**
		 * @private
		 */
		protected var _touchPointID:int = -1;

		/**
		 * @private
		 */
		protected var _startTouchX:Number;

		/**
		 * @private
		 */
		protected var _startTouchY:Number;

		/**
		 * @private
		 */
		protected var _startHorizontalScrollPosition:Number;

		/**
		 * @private
		 */
		protected var _startVerticalScrollPosition:Number;

		/**
		 * @private
		 */
		protected var _currentTouchX:Number;

		/**
		 * @private
		 */
		protected var _currentTouchY:Number;

		/**
		 * @private
		 */
		protected var _previousTouchTime:int;

		/**
		 * @private
		 */
		protected var _previousTouchX:Number;

		/**
		 * @private
		 */
		protected var _previousTouchY:Number;

		/**
		 * @private
		 */
		protected var _velocityX:Number = 0;

		/**
		 * @private
		 */
		protected var _velocityY:Number = 0;

		/**
		 * @private
		 */
		protected var _previousVelocityX:Vector.<Number> = new <Number>[];

		/**
		 * @private
		 */
		protected var _previousVelocityY:Vector.<Number> = new <Number>[];

		/**
		 * @private
		 */
		protected var _lastViewPortWidth:Number = 0;

		/**
		 * @private
		 */
		protected var _lastViewPortHeight:Number = 0;

		/**
		 * @private
		 */
		protected var _hasViewPortBoundsChanged:Boolean = false;

		/**
		 * @private
		 */
		protected var _horizontalAutoScrollTween:Tween;

		/**
		 * @private
		 */
		protected var _verticalAutoScrollTween:Tween;

		/**
		 * @private
		 */
		protected var _isDraggingHorizontally:Boolean = false;

		/**
		 * @private
		 */
		protected var _isDraggingVertically:Boolean = false;

		/**
		 * @private
		 */
		protected var ignoreViewPortResizing:Boolean = false;

		/**
		 * @private
		 */
		protected var _touchBlocker:Quad;

		/**
		 * @private
		 */
		protected var _viewPort:IViewPort;

		/**
		 * The display object displayed and scrolled within the Scroller.
		 *
		 * @default null
		 */
		public function get viewPort():IViewPort
		{
			return this._viewPort;
		}

		/**
		 * @private
		 */
		public function set viewPort(value:IViewPort):void
		{
			if(this._viewPort == value)
			{
				return;
			}
			if(this._viewPort)
			{
				this._viewPort.removeEventListener(FeathersEventType.RESIZE, viewPort_resizeHandler);
				this.removeRawChildInternal(DisplayObject(this._viewPort));
			}
			this._viewPort = value;
			if(this._viewPort)
			{
				this._viewPort.addEventListener(FeathersEventType.RESIZE, viewPort_resizeHandler);
				this.addRawChildAtInternal(DisplayObject(this._viewPort), 0);
			}
			this.invalidate(INVALIDATION_FLAG_SIZE);
		}

		/**
		 * @private
		 */
		protected var _snapToPages:Boolean = false;

		/**
		 * Determines if scrolling will snap to the nearest page.
		 *
		 * <p>In the following example, the scroller snaps to the nearest page:</p>
		 *
		 * <listing version="3.0">
		 * scroller.snapToPages = true;</listing>
		 *
		 * @default false
		 */
		public function get snapToPages():Boolean
		{
			return this._snapToPages;
		}

		/**
		 * @private
		 */
		public function set snapToPages(value:Boolean):void
		{
			if(this._snapToPages == value)
			{
				return;
			}
			this._snapToPages = value;
			this.invalidate(INVALIDATION_FLAG_SCROLL);
		}

		/**
		 * @private
		 */
		protected var _horizontalScrollBarFactory:Function = defaultHorizontalScrollBarFactory;

		/**
		 * Creates the horizontal scroll bar. The horizontal scroll bar must be
		 * an instance of <code>IScrollBar</code>. This factory can be used to
		 * change properties on the horizontal scroll bar when it is first
		 * created. For instance, if you are skinning Feathers components
		 * without a theme, you might use this factory to set skins and other
		 * styles on the horizontal scroll bar.
		 *
		 * <p>This function is expected to have the following signature:</p>
		 *
		 * <pre>function():IScrollBar</pre>
		 *
		 * <p>In the following example, a custom horizontal scroll bar factory
		 * is passed to the scroller:</p>
		 *
		 * <listing version="3.0">
		 * scroller.horizontalScrollBarFactory = function():IScrollBar
		 * {
		 *    return new ScrollBar();
		 * };</listing>
		 *
		 * @default null
		 *
		 * @see feathers.controls.IScrollBar
		 * @see #horizontalScrollBarProperties
		 */
		public function get horizontalScrollBarFactory():Function
		{
			return this._horizontalScrollBarFactory;
		}
		
		public  function advanceTime(time:Number):void
		{
			enterFrameHandler();
			
		}

		/**
		 * @private
		 */
		public function set horizontalScrollBarFactory(value:Function):void
		{
			if(this._horizontalScrollBarFactory == value)
			{
				return;
			}
			this._horizontalScrollBarFactory = value;
			this.invalidate(INVALIDATION_FLAG_SCROLL_BAR_RENDERER);
		}

		/**
		 * @private
		 */
		protected var _customHorizontalScrollBarName:String;

		/**
		 * A name to add to the container's horizontal scroll bar sub-component.
		 * Typically used by a theme to provide different skins to different
		 * containers.
		 *
		 * <p>In the following example, a custom horizontal scroll bar name
		 * is passed to the scroller:</p>
		 *
		 * <listing version="3.0">
		 * scroller.customHorizontalScrollBarName = "my-custom-horizontal-scroll-bar";</listing>
		 *
		 * <p>In your theme, you can target this sub-component name to provide
		 * different skins than the default style:</p>
		 *
		 * <listing version="3.0">
		 * setInitializerForClass( SimpleScrollBar, customHorizontalScrollBarInitializer, "my-custom-horizontal-scroll-bar");</listing>
		 *
		 * @default null
		 *
		 * @see #DEFAULT_CHILD_NAME_HORIZONTAL_SCROLL_BAR
		 * @see feathers.core.FeathersControl#nameList
		 * @see feathers.core.DisplayListWatcher
		 * @see #horizontalScrollBarFactory
		 * @see #horizontalScrollBarProperties
		 */
		public function get customHorizontalScrollBarName():String
		{
			return this._customHorizontalScrollBarName;
		}

		/**
		 * @private
		 */
		public function set customHorizontalScrollBarName(value:String):void
		{
			if(this._customHorizontalScrollBarName == value)
			{
				return;
			}
			this._customHorizontalScrollBarName = value;
			this.invalidate(INVALIDATION_FLAG_SCROLL_BAR_RENDERER);
		}

		/**
		 * @private
		 */
		protected var _horizontalScrollBarProperties:PropertyProxy;

		/**
		 * A set of key/value pairs to be passed down to the scroller's
		 * horizontal scroll bar instance (if it exists). The scroll bar is an
		 * <code>IScrollBar</code> instance. The available properties depend on
		 * which implementation of <code>IScrollBar</code> is returned by
		 * <code>horizontalScrollBarFactory</code>. The most common
		 * implementations are <code>SimpleScrollBar</code> and <code>ScrollBar</code>.
		 *
		 * <p>If the subcomponent has its own subcomponents, their properties
		 * can be set too, using attribute <code>&#64;</code> notation. For example,
		 * to set the skin on the thumb which is in a <code>SimpleScrollBar</code>,
		 * which is in a <code>List</code>, you can use the following syntax:</p>
		 * <pre>list.verticalScrollBarProperties.&#64;thumbProperties.defaultSkin = new Image(texture);</pre>
		 *
		 * <p>Setting properties in a <code>horizontalScrollBarFactory</code>
		 * function instead of using <code>horizontalScrollBarProperties</code>
		 * will result in better performance.</p>
		 *
		 * <p>In the following example, properties for the horizontal scroll bar
		 * are passed to the scroller:</p>
		 *
		 * <listing version="3.0">
		 * scroller.horizontalScrollBarProperties.liveDragging = false;</listing>
		 *
		 * @default null
		 *
		 * @see #horizontalScrollBarFactory
		 * @see feathers.controls.IScrollBar
		 * @see feathers.controls.SimpleScrollBar
		 * @see feathers.controls.ScrollBar
		 */
		public function get horizontalScrollBarProperties():Object
		{
			if(!this._horizontalScrollBarProperties)
			{
				this._horizontalScrollBarProperties = new PropertyProxy(childProperties_onChange);
			}
			return this._horizontalScrollBarProperties;
		}

		/**
		 * @private
		 */
		public function set horizontalScrollBarProperties(value:Object):void
		{
			if(this._horizontalScrollBarProperties == value)
			{
				return;
			}
			if(!value)
			{
				value = new PropertyProxy();
			}
			if(!(value is PropertyProxy))
			{
				const newValue:PropertyProxy = new PropertyProxy();
				for(var propertyName:String in value)
				{
					newValue[propertyName] = value[propertyName];
				}
				value = newValue;
			}
			if(this._horizontalScrollBarProperties)
			{
				this._horizontalScrollBarProperties.removeOnChangeCallback(childProperties_onChange);
			}
			this._horizontalScrollBarProperties = PropertyProxy(value);
			if(this._horizontalScrollBarProperties)
			{
				this._horizontalScrollBarProperties.addOnChangeCallback(childProperties_onChange);
			}
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _verticalScrollBarPosition:String = VERTICAL_SCROLL_BAR_POSITION_RIGHT;

		[Inspectable(type="String",enumeration="right,left")]
		/**
		 * Determines where the vertical scroll bar will be positioned.
		 *
		 * <p>In the following example, the scroll bars is positioned on the left:</p>
		 *
		 * <listing version="3.0">
		 * scroller.verticalScrollBarPosition = Scroller.VERTICAL_SCROLL_BAR_POSITION_LEFT;</listing>
		 *
		 * @default Scroller.VERTICAL_SCROLL_BAR_POSITION_RIGHT
		 *
		 * @see #VERTICAL_SCROLL_BAR_POSITION_RIGHT
		 * @see #VERTICAL_SCROLL_BAR_POSITION_LEFT
		 */
		public function get verticalScrollBarPosition():String
		{
			return this._verticalScrollBarPosition;
		}

		/**
		 * @private
		 */
		public function set verticalScrollBarPosition(value:String):void
		{
			if(this._verticalScrollBarPosition == value)
			{
				return;
			}
			this._verticalScrollBarPosition = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _verticalScrollBarFactory:Function = defaultVerticalScrollBarFactory;

		/**
		 * Creates the vertical scroll bar. The vertical scroll bar must be an
		 * instance of <code>Button</code>. This factory can be used to change
		 * properties on the vertical scroll bar when it is first created. For
		 * instance, if you are skinning Feathers components without a theme,
		 * you might use this factory to set skins and other styles on the
		 * vertical scroll bar.
		 *
		 * <p>This function is expected to have the following signature:</p>
		 *
		 * <pre>function():IScrollBar</pre>
		 *
		 * <p>In the following example, a custom vertical scroll bar factory
		 * is passed to the scroller:</p>
		 *
		 * <listing version="3.0">
		 * scroller.verticalScrollBarFactory = function():IScrollBar
		 * {
		 *    return new ScrollBar();
		 * };</listing>
		 *
		 * @default null
		 *
		 * @see feathers.controls.IScrollBar
		 * @see #verticalScrollBarProperties
		 */
		public function get verticalScrollBarFactory():Function
		{
			return this._verticalScrollBarFactory;
		}

		/**
		 * @private
		 */
		public function set verticalScrollBarFactory(value:Function):void
		{
			if(this._verticalScrollBarFactory == value)
			{
				return;
			}
			this._verticalScrollBarFactory = value;
			this.invalidate(INVALIDATION_FLAG_SCROLL_BAR_RENDERER);
		}

		/**
		 * @private
		 */
		protected var _customVerticalScrollBarName:String;

		/**
		 * A name to add to the container's vertical scroll bar sub-component.
		 * Typically used by a theme to provide different skins to different
		 * containers.
		 *
		 * <p>In the following example, a custom vertical scroll bar name
		 * is passed to the scroller:</p>
		 *
		 * <listing version="3.0">
		 * scroller.customVerticalScrollBarName = "my-custom-vertical-scroll-bar";</listing>
		 *
		 * <p>In your theme, you can target this sub-component name to provide
		 * different skins than the default style:</p>
		 *
		 * <listing version="3.0">
		 * setInitializerForClass( SimpleScrollBar, customVerticalScrollBarInitializer, "my-custom-vertical-scroll-bar");</listing>
		 *
		 * @default null
		 *
		 * @see #DEFAULT_CHILD_NAME_VERTICAL_SCROLL_BAR
		 * @see feathers.core.FeathersControl#nameList
		 * @see feathers.core.DisplayListWatcher
		 * @see #verticalScrollBarFactory
		 * @see #verticalScrollBarProperties
		 */
		public function get customVerticalScrollBarName():String
		{
			return this._customVerticalScrollBarName;
		}

		/**
		 * @private
		 */
		public function set customVerticalScrollBarName(value:String):void
		{
			if(this._customVerticalScrollBarName == value)
			{
				return;
			}
			this._customVerticalScrollBarName = value;
			this.invalidate(INVALIDATION_FLAG_SCROLL_BAR_RENDERER);
		}

		/**
		 * @private
		 */
		protected var _verticalScrollBarProperties:PropertyProxy;

		/**
		 * A set of key/value pairs to be passed down to the scroller's
		 * vertical scroll bar instance (if it exists). The scroll bar is an
		 * <code>IScrollBar</code> instance. The available properties depend on
		 * which implementation of <code>IScrollBar</code> is returned by
		 * <code>verticalScrollBarFactory</code>. The most common
		 * implementations are <code>SimpleScrollBar</code> and <code>ScrollBar</code>.
		 *
		 * <p>If the subcomponent has its own subcomponents, their properties
		 * can be set too, using attribute <code>&#64;</code> notation. For example,
		 * to set the skin on the thumb which is in a <code>SimpleScrollBar</code>,
		 * which is in a <code>List</code>, you can use the following syntax:</p>
		 * <pre>list.verticalScrollBarProperties.&#64;thumbProperties.defaultSkin = new Image(texture);</pre>
		 *
		 * <p>Setting properties in a <code>verticalScrollBarFactory</code>
		 * function instead of using <code>verticalScrollBarProperties</code>
		 * will result in better performance.</p>
		 *
		 * <p>In the following example, properties for the vertical scroll bar
		 * are passed to the scroller:</p>
		 *
		 * <listing version="3.0">
		 * scroller.verticalScrollBarProperties.liveDragging = false;</listing>
		 *
		 * @default null
		 *
		 * @see #verticalScrollBarFactory
		 * @see feathers.controls.IScrollBar
		 * @see feathers.controls.SimpleScrollBar
		 * @see feathers.controls.ScrollBar
		 */
		public function get verticalScrollBarProperties():Object
		{
			if(!this._verticalScrollBarProperties)
			{
				this._verticalScrollBarProperties = new PropertyProxy(childProperties_onChange);
			}
			return this._verticalScrollBarProperties;
		}

		/**
		 * @private
		 */
		public function set verticalScrollBarProperties(value:Object):void
		{
			if(this._horizontalScrollBarProperties == value)
			{
				return;
			}
			if(!value)
			{
				value = new PropertyProxy();
			}
			if(!(value is PropertyProxy))
			{
				const newValue:PropertyProxy = new PropertyProxy();
				for(var propertyName:String in value)
				{
					newValue[propertyName] = value[propertyName];
				}
				value = newValue;
			}
			if(this._verticalScrollBarProperties)
			{
				this._verticalScrollBarProperties.removeOnChangeCallback(childProperties_onChange);
			}
			this._verticalScrollBarProperties = PropertyProxy(value);
			if(this._verticalScrollBarProperties)
			{
				this._verticalScrollBarProperties.addOnChangeCallback(childProperties_onChange);
			}
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var actualHorizontalScrollStep:Number = 1;

		/**
		 * @private
		 */
		protected var explicitHorizontalScrollStep:Number = NaN;

		/**
		 * The number of pixels the scroller can be stepped horizontally. Passed
		 * to the horizontal scroll bar, if one exists. Touch scrolling is not
		 * affected by the step value.
		 *
		 * <p>In the following example, the horizontal scroll step is customized:</p>
		 *
		 * <listing version="3.0">
		 * scroller.horizontalScrollStep = 0;</listing>
		 *
		 * @default NaN
		 */
		public function get horizontalScrollStep():Number
		{
			return this.actualHorizontalScrollStep;
		}

		/**
		 * @private
		 */
		public function set horizontalScrollStep(value:Number):void
		{
			if(this.explicitHorizontalScrollStep == value)
			{
				return;
			}
			this.explicitHorizontalScrollStep = value;
			this.invalidate(INVALIDATION_FLAG_SCROLL);
		}

		/**
		 * @private
		 */
		protected var _targetHorizontalScrollPosition:Number;

		/**
		 * @private
		 */
		protected var _horizontalScrollPosition:Number = 0;

		/**
		 * The number of pixels the scroller has been scrolled horizontally (on
		 * the x-axis).
		 *
		 * <p>In the following example, the horizontal scroll position is customized:</p>
		 *
		 * <listing version="3.0">
		 * scroller.horizontalScrollPosition = scroller.maxHorizontalScrollPosition;</listing>
		 *
		 * @see #minHorizontalScrollPosition
		 * @see #maxHorizontalScrollPosition
		 */
		public function get horizontalScrollPosition():Number
		{
			return this._horizontalScrollPosition;
		}

		/**
		 * @private
		 */
		public function set horizontalScrollPosition(value:Number):void
		{
			if(this._snapScrollPositionsToPixels)
			{
				value = Math.round(value);
			}
			if(this._horizontalScrollPosition == value)
			{
				return;
			}
			if(isNaN(value))
			{
				//there isn't any recovery from this, so stop it early
				throw new ArgumentError("horizontalScrollPosition cannot be NaN.");
			}
			this._horizontalScrollPosition = value;
			this.invalidate(INVALIDATION_FLAG_SCROLL);
		}

		/**
		 * @private
		 */
		protected var _minHorizontalScrollPosition:Number = 0;

		/**
		 * The number of pixels the scroller may be scrolled horizontally to the
		 * left. This value is automatically calculated based on the bounds of
		 * the viewport. The <code>horizontalScrollPosition</code> property may
		 * have a lower value than the minimum due to elastic edges. However,
		 * once the user stops interacting with the scroller, it will
		 * automatically animate back to the maximum or minimum position.
		 *
		 * @see #horizontalScrollPosition
		 * @see #maxHorizontalScrollPosition
		 */
		public function get minHorizontalScrollPosition():Number
		{
			return this._minHorizontalScrollPosition;
		}

		/**
		 * @private
		 */
		protected var _maxHorizontalScrollPosition:Number = 0;

		/**
		 * The number of pixels the scroller may be scrolled horizontally to the
		 * right. This value is automatically calculated based on the bounds of
		 * the viewport. The <code>horizontalScrollPosition</code> property may
		 * have a higher value than the maximum due to elastic edges. However,
		 * once the user stops interacting with the scroller, it will
		 * automatically animate back to the maximum or minimum position.
		 *
		 * @see #horizontalScrollPosition
		 * @see #minHorizontalScrollPosition
		 */
		public function get maxHorizontalScrollPosition():Number
		{
			return this._maxHorizontalScrollPosition;
		}

		/**
		 * @private
		 */
		protected var _horizontalPageIndex:int = 0;

		/**
		 * The index of the horizontal page, if snapping is enabled. If snapping
		 * is disabled, the index will always be <code>0</code>.
		 */
		public function get horizontalPageIndex():int
		{
			if(this.pendingHorizontalPageIndex >= 0)
			{
				return this.pendingHorizontalPageIndex;
			}
			return this._horizontalPageIndex;
		}

		/**
		 * @private
		 */
		protected var _horizontalPageCount:int = 1;

		/**
		 * The number of horizontal pages, if snapping is enabled. If snapping
		 * is disabled, the page count will always be <code>1</code>.
		 */
		public function get horizontalPageCount():int
		{
			return this._horizontalPageCount;
		}

		/**
		 * @private
		 */
		protected var _horizontalScrollPolicy:String = SCROLL_POLICY_AUTO;

		[Inspectable(type="String",enumeration="auto,on,off")]
		/**
		 * Determines whether the scroller may scroll horizontally (on the
		 * x-axis) or not.
		 *
		 * <p>In the following example, horizontal scrolling is disabled:</p>
		 *
		 * <listing version="3.0">
		 * scroller.horizontalScrollPolicy = Scroller.SCROLL_POLICY_OFF;</listing>
		 *
		 * @default Scroller.SCROLL_POLICY_AUTO
		 *
		 * @see #SCROLL_POLICY_AUTO
		 * @see #SCROLL_POLICY_ON
		 * @see #SCROLL_POLICY_OFF
		 */
		public function get horizontalScrollPolicy():String
		{
			return this._horizontalScrollPolicy;
		}

		/**
		 * @private
		 */
		public function set horizontalScrollPolicy(value:String):void
		{
			if(this._horizontalScrollPolicy == value)
			{
				return;
			}
			this._horizontalScrollPolicy = value;
			this.invalidate(INVALIDATION_FLAG_SCROLL);
			this.invalidate(INVALIDATION_FLAG_SCROLL_BAR_RENDERER);
		}

		/**
		 * @private
		 */
		protected var actualVerticalScrollStep:Number = 1;

		/**
		 * @private
		 */
		protected var explicitVerticalScrollStep:Number = NaN;

		/**
		 * The number of pixels the scroller can be stepped vertically. Passed
		 * to the vertical scroll bar, if it exists, and used for scrolling with
		 * the mouse wheel. Touch scrolling is not affected by the step value.
		 *
		 * <p>In the following example, the vertical scroll step is customized:</p>
		 *
		 * <listing version="3.0">
		 * scroller.verticalScrollStep = 0;</listing>
		 *
		 * @default NaN
		 */
		public function get verticalScrollStep():Number
		{
			return this.actualVerticalScrollStep;
		}

		/**
		 * @private
		 */
		public function set verticalScrollStep(value:Number):void
		{
			if(this.explicitVerticalScrollStep == value)
			{
				return;
			}
			this.explicitVerticalScrollStep = value;
			this.invalidate(INVALIDATION_FLAG_SCROLL);
		}

		/**
		 * @private
		 */
		protected var _verticalMouseWheelScrollStep:Number = NaN;

		/**
		 * The number of pixels the scroller can be stepped vertically when
		 * using the mouse wheel. If this value is <code>NaN</code>, the mouse
		 * wheel will use the same scroll step as the scroll bars.
		 *
		 * <p>In the following example, the vertical mouse wheel scroll step is
		 * customized:</p>
		 *
		 * <listing version="3.0">
		 * scroller.verticalMouseWheelScrollStep = 10;</listing>
		 *
		 * @default NaN
		 */
		public function get verticalMouseWheelScrollStep():Number
		{
			return this._verticalMouseWheelScrollStep;
		}

		/**
		 * @private
		 */
		public function set verticalMouseWheelScrollStep(value:Number):void
		{
			if(this._verticalMouseWheelScrollStep == value)
			{
				return;
			}
			this._verticalMouseWheelScrollStep = value;
			this.invalidate(INVALIDATION_FLAG_SCROLL);
		}

		/**
		 * @private
		 */
		protected var _targetVerticalScrollPosition:Number;

		/**
		 * @private
		 */
		protected var _verticalScrollPosition:Number = 0;

		/**
		 * The number of pixels the scroller has been scrolled vertically (on
		 * the y-axis).
		 *
		 * <p>In the following example, the vertical scroll position is customized:</p>
		 *
		 * <listing version="3.0">
		 * scroller.verticalScrollPosition = scroller.maxVerticalScrollPosition;</listing>
		 */
		public function get verticalScrollPosition():Number
		{
			return this._verticalScrollPosition;
		}

		/**
		 * @private
		 */
		public function set verticalScrollPosition(value:Number):void
		{
			if(this._snapScrollPositionsToPixels)
			{
				value = Math.round(value);
			}
			if(this._verticalScrollPosition == value)
			{
				return;
			}
			if(isNaN(value))
			{
				//there isn't any recovery from this, so stop it early
				throw new ArgumentError("verticalScrollPosition cannot be NaN.");
			}
			this._verticalScrollPosition = value;
			this.invalidate(INVALIDATION_FLAG_SCROLL);
		}

		/**
		 * @private
		 */
		protected var _minVerticalScrollPosition:Number = 0;

		/**
		 * The number of pixels the scroller may be scrolled vertically beyond
		 * the top edge. This value is automatically calculated based on the
		 * bounds of the viewport. The <code>verticalScrollPosition</code>
		 * property may have a lower value than the minimum due to elastic
		 * edges. However, once the user stops interacting with the scroller, it
		 * will automatically animate back to the maximum or minimum position.
		 *
		 * @see #verticalScrollPosition
		 * @see #maxVerticalScrollPosition
		 */
		public function get minVerticalScrollPosition():Number
		{
			return this._minVerticalScrollPosition;
		}

		/**
		 * @private
		 */
		protected var _maxVerticalScrollPosition:Number = 0;

		/**
		 * The number of pixels the scroller may be scrolled vertically beyond
		 * the bottom edge. This value is automatically calculated based on the
		 * bounds of the viewport. The <code>verticalScrollPosition</code>
		 * property may have a lower value than the minimum due to elastic
		 * edges. However, once the user stops interacting with the scroller, it
		 * will automatically animate back to the maximum or minimum position.
		 *
		 * @see #verticalScrollPosition
		 * @see #minVerticalScrollPosition
		 */
		public function get maxVerticalScrollPosition():Number
		{
			return this._maxVerticalScrollPosition;
		}

		/**
		 * @private
		 */
		protected var _verticalPageIndex:int = 0;

		/**
		 * The index of the vertical page, if snapping is enabled. If snapping
		 * is disabled, the index will always be <code>0</code>.
		 */
		public function get verticalPageIndex():int
		{
			if(this.pendingVerticalPageIndex >= 0)
			{
				return this.pendingVerticalPageIndex;
			}
			return this._verticalPageIndex;
		}

		/**
		 * @private
		 */
		protected var _verticalPageCount:int = 1;

		/**
		 * The number of vertical pages, if snapping is enabled. If snapping
		 * is disabled, the page count will always be <code>1</code>.
		 */
		public function get verticalPageCount():int
		{
			return this._verticalPageCount;
		}

		/**
		 * @private
		 */
		protected var _verticalScrollPolicy:String = SCROLL_POLICY_AUTO;

		[Inspectable(type="String",enumeration="auto,on,off")]
		/**
		 * Determines whether the scroller may scroll vertically (on the
		 * y-axis) or not.
		 *
		 * <p>In the following example, vertical scrolling is disabled:</p>
		 *
		 * <listing version="3.0">
		 * scroller.horizontalScrollPolicy = Scroller.SCROLL_POLICY_OFF;</listing>
		 *
		 * @default Scroller.SCROLL_POLICY_AUTO
		 *
		 * @see #SCROLL_POLICY_AUTO
		 * @see #SCROLL_POLICY_ON
		 * @see #SCROLL_POLICY_OFF
		 */
		public function get verticalScrollPolicy():String
		{
			return this._verticalScrollPolicy;
		}

		/**
		 * @private
		 */
		public function set verticalScrollPolicy(value:String):void
		{
			if(this._verticalScrollPolicy == value)
			{
				return;
			}
			this._verticalScrollPolicy = value;
			this.invalidate(INVALIDATION_FLAG_SCROLL);
			this.invalidate(INVALIDATION_FLAG_SCROLL_BAR_RENDERER);
		}

		/**
		 * @private
		 */
		protected var _clipContent:Boolean = true;

		/**
		 * If true, the viewport will be clipped to the scroller's bounds. In
		 * other words, anything appearing outside the scroller's bounds will
		 * not be visible.
		 *
		 * <p>To improve performance, turn off clipping and place other display
		 * objects over the edges of the scroller to hide the content that
		 * bleeds outside of the scroller's bounds.</p>
		 *
		 * <p>In the following example, clipping is disabled:</p>
		 *
		 * <listing version="3.0">
		 * scroller.clipContent = false;</listing>
		 *
		 * @default true
		 */
		public function get clipContent():Boolean
		{
			return this._clipContent;
		}

		/**
		 * @private
		 */
		public function set clipContent(value:Boolean):void
		{
			if(this._clipContent == value)
			{
				return;
			}
			this._clipContent = value;
			this.invalidate(INVALIDATION_FLAG_CLIPPING);
		}

		/**
		 * @private
		 */
		protected var actualPageWidth:Number = 0;

		/**
		 * @private
		 */
		protected var explicitPageWidth:Number = NaN;

		/**
		 * When set, the horizontal pages snap to this width value instead of
		 * the width of the scroller.
		 *
		 * <p>In the following example, the page width is set to 200 pixels:</p>
		 *
		 * <listing version="3.0">
		 * scroller.pageWidth = 200;</listing>
		 *
		 * @see #snapToPages
		 */
		public function get pageWidth():Number
		{
			return this.actualPageWidth;
		}

		/**
		 * @private
		 */
		public function set pageWidth(value:Number):void
		{
			if(this.explicitPageWidth == value)
			{
				return;
			}
			var valueIsNaN:Boolean = isNaN(value);
			if(valueIsNaN && isNaN(this.explicitPageWidth))
			{
				return;
			}
			this.explicitPageWidth = value;
			if(valueIsNaN)
			{
				//we need to calculate this value during validation
				this.actualPageWidth = 0;
			}
			else
			{
				this.actualPageWidth = this.explicitPageWidth;
			}
		}

		/**
		 * @private
		 */
		protected var actualPageHeight:Number = 0;

		/**
		 * @private
		 */
		protected var explicitPageHeight:Number = NaN;

		/**
		 * When set, the vertical pages snap to this height value instead of
		 * the height of the scroller.
		 *
		 * <p>In the following example, the page height is set to 200 pixels:</p>
		 *
		 * <listing version="3.0">
		 * scroller.pageHeight = 200;</listing>
		 *
		 * @see #snapToPages
		 */
		public function get pageHeight():Number
		{
			return this.actualPageHeight;
		}

		/**
		 * @private
		 */
		public function set pageHeight(value:Number):void
		{
			if(this.explicitPageHeight == value)
			{
				return;
			}
			var valueIsNaN:Boolean = isNaN(value);
			if(valueIsNaN && isNaN(this.explicitPageHeight))
			{
				return;
			}
			this.explicitPageHeight = value;
			if(valueIsNaN)
			{
				//we need to calculate this value during validation
				this.actualPageHeight = 0;
			}
			else
			{
				this.actualPageHeight = this.explicitPageHeight;
			}
		}

		/**
		 * @private
		 */
		protected var _hasElasticEdges:Boolean = true;

		/**
		 * Determines if the scrolling can go beyond the edges of the viewport.
		 *
		 * <p>In the following example, elastic edges are disabled:</p>
		 *
		 * <listing version="3.0">
		 * scroller.hasElasticEdges = false;</listing>
		 *
		 * @default true
		 */
		public function get hasElasticEdges():Boolean
		{
			return this._hasElasticEdges;
		}

		/**
		 * @private
		 */
		public function set hasElasticEdges(value:Boolean):void
		{
			this._hasElasticEdges = value;
		}

		/**
		 * @private
		 */
		protected var _elasticity:Number = 0.33;

		/**
		 * If the scroll position goes outside the minimum or maximum bounds,
		 * the scrolling will be constrained using this multiplier.
		 *
		 * <p>In the following example, the elasticity is customized:</p>
		 *
		 * <listing version="3.0">
		 * scroller.elasticity = 0.5;</listing>
		 *
		 * @default 0.33
		 */
		public function get elasticity():Number
		{
			return this._elasticity;
		}

		/**
		 * @private
		 */
		public function set elasticity(value:Number):void
		{
			this._elasticity = value;
		}

		/**
		 * @private
		 */
		protected var _scrollBarDisplayMode:String = SCROLL_BAR_DISPLAY_MODE_FLOAT;

		[Inspectable(type="String",enumeration="float,fixed,none")]
		/**
		 * Determines how the scroll bars are displayed.
		 *
		 * <p>In the following example, the scroll bars are fixed:</p>
		 *
		 * <listing version="3.0">
		 * scroller.scrollBarDisplayMode = Scroller.SCROLL_BAR_DISPLAY_MODE_FIXED;</listing>
		 *
		 * @default Scroller.SCROLL_BAR_DISPLAY_MODE_FLOAT
		 *
		 * @see #SCROLL_BAR_DISPLAY_MODE_FLOAT
		 * @see #SCROLL_BAR_DISPLAY_MODE_FIXED
		 * @see #SCROLL_BAR_DISPLAY_MODE_NONE
		 */
		public function get scrollBarDisplayMode():String
		{
			return this._scrollBarDisplayMode;
		}

		/**
		 * @private
		 */
		public function set scrollBarDisplayMode(value:String):void
		{
			if(this._scrollBarDisplayMode == value)
			{
				return;
			}
			this._scrollBarDisplayMode = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _interactionMode:String = INTERACTION_MODE_TOUCH;

		[Inspectable(type="String",enumeration="touch,mouse,touchAndScrollBars")]
		/**
		 * Determines how the user may interact with the scroller.
		 *
		 * <p>In the following example, the interaction mode is optimized for mouse:</p>
		 *
		 * <listing version="3.0">
		 * scroller.scrollBarDisplayMode = Scroller.INTERACTION_MODE_MOUSE;</listing>
		 *
		 * @default Scroller.INTERACTION_MODE_TOUCH
		 *
		 * @see #INTERACTION_MODE_TOUCH
		 * @see #INTERACTION_MODE_MOUSE
		 * @see #INTERACTION_MODE_TOUCH_AND_SCROLL_BARS
		 */
		public function get interactionMode():String
		{
			return this._interactionMode;
		}

		/**
		 * @private
		 */
		public function set interactionMode(value:String):void
		{
			if(this._interactionMode == value)
			{
				return;
			}
			this._interactionMode = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var originalBackgroundWidth:Number = NaN;

		/**
		 * @private
		 */
		protected var originalBackgroundHeight:Number = NaN;

		/**
		 * @private
		 */
		protected var currentBackgroundSkin:DisplayObject;

		/**
		 * @private
		 */
		protected var _backgroundSkin:DisplayObject;

		/**
		 * The default background to display.
		 *
		 * <p>In the following example, the scroller is given a background skin:</p>
		 *
		 * <listing version="3.0">
		 * scroller.backgroundSkin = new Image( texture );</listing>
		 *
		 * @default null
		 */
		public function get backgroundSkin():DisplayObject
		{
			return this._backgroundSkin;
		}

		/**
		 * @private
		 */
		public function set backgroundSkin(value:DisplayObject):void
		{
			if(this._backgroundSkin == value)
			{
				return;
			}

			if(this._backgroundSkin && this._backgroundSkin != this._backgroundDisabledSkin)
			{
				this.removeRawChildInternal(this._backgroundSkin);
			}
			this._backgroundSkin = value;
			if(this._backgroundSkin && this._backgroundSkin.parent != this)
			{
				this._backgroundSkin.visible = false;
				this.addRawChildInternal(this._backgroundSkin);
			}
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _backgroundDisabledSkin:DisplayObject;

		/**
		 * A background to display when the container is disabled.
		 *
		 * <p>In the following example, the scroller is given a disabled background skin:</p>
		 *
		 * <listing version="3.0">
		 * scroller.backgroundDisabledSkin = new Image( texture );</listing>
		 *
		 * @default null
		 */
		public function get backgroundDisabledSkin():DisplayObject
		{
			return this._backgroundDisabledSkin;
		}

		/**
		 * @private
		 */
		public function set backgroundDisabledSkin(value:DisplayObject):void
		{
			if(this._backgroundDisabledSkin == value)
			{
				return;
			}

			if(this._backgroundDisabledSkin && this._backgroundDisabledSkin != this._backgroundSkin)
			{
				this.removeRawChildInternal(this._backgroundDisabledSkin);
			}
			this._backgroundDisabledSkin = value;
			if(this._backgroundDisabledSkin && this._backgroundDisabledSkin.parent != this)
			{
				this._backgroundDisabledSkin.visible = false;
				this.addRawChildInternal(this._backgroundDisabledSkin);
			}
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _autoHideBackground:Boolean = false;

		/**
		 * If <code>true</code>, the background's <code>visible</code> property
		 * will be set to <code>false</code> when the scroll position is greater
		 * than or equal to the minimum scroll position and less than or equal
		 * to the maximum scroll position. The background will be visible when
		 * the content is extended beyond the scrolling bounds, such as when
		 * <code>hasElasticEdges</code> is <code>true</code>.
		 *
		 * <p>If the content is not fully opaque, this setting should not be
		 * enabled.</p>
		 *
		 * <p>This setting may be enabled to potentially improve performance.</p>
		 *
		 * <p>In the following example, the background is automatically hidden:</p>
		 *
		 * <listing version="3.0">
		 * scroller.autoHideBackground = true;</listing>
		 *
		 * @default false
		 */
		public function get autoHideBackground():Boolean
		{
			return this._autoHideBackground;
		}

		/**
		 * @private
		 */
		public function set autoHideBackground(value:Boolean):void
		{
			if(this._autoHideBackground == value)
			{
				return;
			}
			this._autoHideBackground = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _minimumDragDistance:Number = 0.04;

		/**
		 * The minimum physical distance (in inches) that a touch must move
		 * before the scroller starts scrolling.
		 *
		 * <p>In the following example, the minimum drag distance is customized:</p>
		 *
		 * <listing version="3.0">
		 * scroller.minimumDragDistance = 0.1;</listing>
		 *
		 * @default 0.04
		 */
		public function get minimumDragDistance():Number
		{
			return this._minimumDragDistance;
		}

		/**
		 * @private
		 */
		public function set minimumDragDistance(value:Number):void
		{
			this._minimumDragDistance = value;
		}

		/**
		 * @private
		 */
		protected var _minimumPageThrowVelocity:Number = 5;

		/**
		 * The minimum physical velocity (in inches per second) that a touch
		 * must move before the scroller will "throw" to the next page.
		 * Otherwise, it will settle to the nearest page.
		 *
		 * <p>In the following example, the minimum page throw velocity is customized:</p>
		 *
		 * <listing version="3.0">
		 * scroller.minimumPageThrowVelocity = 2;</listing>
		 *
		 * @default 5
		 */
		public function get minimumPageThrowVelocity():Number
		{
			return this._minimumPageThrowVelocity;
		}

		/**
		 * @private
		 */
		public function set minimumPageThrowVelocity(value:Number):void
		{
			this._minimumPageThrowVelocity = value;
		}

		/**
		 * Quickly sets all padding properties to the same value. The
		 * <code>padding</code> getter always returns the value of
		 * <code>paddingTop</code>, but the other padding values may be
		 * different.
		 *
		 * <p>In the following example, the padding is set to 20 pixels:</p>
		 *
		 * <listing version="3.0">
		 * scroller.padding = 20;</listing>
		 *
		 * @default 0
		 *
		 * @see #paddingTop
		 * @see #paddingRight
		 * @see #paddingBottom
		 * @see #paddingLeft
		 */
		public function get padding():Number
		{
			return this._paddingTop;
		}

		/**
		 * @private
		 */
		public function set padding(value:Number):void
		{
			this.paddingTop = value;
			this.paddingRight = value;
			this.paddingBottom = value;
			this.paddingLeft = value;
		}

		/**
		 * @private
		 */
		protected var _paddingTop:Number = 0;

		/**
		 * The minimum space, in pixels, between the container's top edge and the
		 * container's content.
		 *
		 * <p>In the following example, the top padding is set to 20 pixels:</p>
		 *
		 * <listing version="3.0">
		 * scroller.paddingTop = 20;</listing>
		 *
		 * @default 0
		 */
		public function get paddingTop():Number
		{
			return this._paddingTop;
		}

		/**
		 * @private
		 */
		public function set paddingTop(value:Number):void
		{
			if(this._paddingTop == value)
			{
				return;
			}
			this._paddingTop = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _paddingRight:Number = 0;

		/**
		 * The minimum space, in pixels, between the container's right edge and
		 * the container's content.
		 *
		 * <p>In the following example, the right padding is set to 20 pixels:</p>
		 *
		 * <listing version="3.0">
		 * scroller.paddingRight = 20;</listing>
		 *
		 * @default 0
		 */
		public function get paddingRight():Number
		{
			return this._paddingRight;
		}

		/**
		 * @private
		 */
		public function set paddingRight(value:Number):void
		{
			if(this._paddingRight == value)
			{
				return;
			}
			this._paddingRight = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _paddingBottom:Number = 0;

		/**
		 * The minimum space, in pixels, between the container's bottom edge and
		 * the container's content.
		 *
		 * <p>In the following example, the bottom padding is set to 20 pixels:</p>
		 *
		 * <listing version="3.0">
		 * scroller.paddingBottom = 20;</listing>
		 *
		 * @default 0
		 */
		public function get paddingBottom():Number
		{
			return this._paddingBottom;
		}

		/**
		 * @private
		 */
		public function set paddingBottom(value:Number):void
		{
			if(this._paddingBottom == value)
			{
				return;
			}
			this._paddingBottom = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _paddingLeft:Number = 0;

		/**
		 * The minimum space, in pixels, between the container's left edge and the
		 * container's content.
		 *
		 * <p>In the following example, the left padding is set to 20 pixels:</p>
		 *
		 * <listing version="3.0">
		 * scroller.paddingLeft = 20;</listing>
		 *
		 * @default 0
		 */
		public function get paddingLeft():Number
		{
			return this._paddingLeft;
		}

		/**
		 * @private
		 */
		public function set paddingLeft(value:Number):void
		{
			if(this._paddingLeft == value)
			{
				return;
			}
			this._paddingLeft = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _horizontalScrollBarHideTween:Tween;

		/**
		 * @private
		 */
		protected var _verticalScrollBarHideTween:Tween;

		/**
		 * @private
		 */
		protected var _hideScrollBarAnimationDuration:Number = 0.2;

		/**
		 * The duration, in seconds, of the animation when a scroll bar fades
		 * out.
		 *
		 * <p>In the following example, the duration of the animation that hides
		 * the scroll bars is set to 500 milliseconds:</p>
		 *
		 * <listing version="3.0">
		 * scroller.hideScrollBarAnimationDuration = 0.5;</listing>
		 *
		 * @default 0.2
		 */
		public function get hideScrollBarAnimationDuration():Number
		{
			return this._hideScrollBarAnimationDuration;
		}

		/**
		 * @private
		 */
		public function set hideScrollBarAnimationDuration(value:Number):void
		{
			this._hideScrollBarAnimationDuration = value;
		}

		/**
		 * @private
		 */
		protected var _hideScrollBarAnimationEase:Object = Transitions.EASE_OUT;

		/**
		 * The easing function used for hiding the scroll bars, if applicable.
		 *
		 * <p>In the following example, the ease of the animation that hides
		 * the scroll bars is customized:</p>
		 *
		 * <listing version="3.0">
		 * scroller.hideScrollBarAnimationEase = Transitions.EASE_IN_OUT;</listing>
		 *
		 * @default starling.animation.Transitions.EASE_OUT
		 *
		 * @see starling.animation.Transitions
		 */
		public function get hideScrollBarAnimationEase():Object
		{
			return this._hideScrollBarAnimationEase;
		}

		/**
		 * @private
		 */
		public function set hideScrollBarAnimationEase(value:Object):void
		{
			this._hideScrollBarAnimationEase = value;
		}

		/**
		 * @private
		 */
		protected var _elasticSnapDuration:Number = 0.24;

		/**
		 * The duration, in seconds, of the animation when a the scroller snaps
		 * back to the minimum or maximum position after going out of bounds.
		 *
		 * <p>In the following example, the duration of the animation that snaps
		 * the content back after pulling it beyond the edge is set to 500
		 * milliseconds:</p>
		 *
		 * <listing version="3.0">
		 * scroller.elasticSnapDuration = 0.5;</listing>
		 *
		 * @default 0.24
		 */
		public function get elasticSnapDuration():Number
		{
			return this._elasticSnapDuration;
		}

		/**
		 * @private
		 */
		public function set elasticSnapDuration(value:Number):void
		{
			this._elasticSnapDuration = value;
		}

		/**
		 * @private
		 */
		protected var _pageThrowDuration:Number = 0.5;

		/**
		 * The duration, in seconds, of the animation when the scroller is
		 * thrown to a page.
		 *
		 * <p>In the following example, the duration of the animation that
		 * changes the page when thrown is set to 250 milliseconds:</p>
		 *
		 * <listing version="3.0">
		 * scroller.pageThrowDuration = 0.25;</listing>
		 *
		 * @default 0.5
		 */
		public function get pageThrowDuration():Number
		{
			return this._pageThrowDuration;
		}

		/**
		 * @private
		 */
		public function set pageThrowDuration(value:Number):void
		{
			this._pageThrowDuration = value;
		}

		/**
		 * @private
		 */
		protected var _mouseWheelScrollDuration:Number = 0.35;

		/**
		 * The duration, in seconds, of the animation when the mouse wheel
		 * initiates a scroll action.
		 *
		 * <p>In the following example, the duration of the animation that runs
		 * when the mouse wheel is scrolled is set to 500 milliseconds:</p>
		 *
		 * <listing version="3.0">
		 * scroller.mouseWheelScrollDuration = 0.5;</listing>
		 *
		 * @default 0.35
		 */
		public function get mouseWheelScrollDuration():Number
		{
			return this._mouseWheelScrollDuration;
		}

		/**
		 * @private
		 */
		public function set mouseWheelScrollDuration(value:Number):void
		{
			this._mouseWheelScrollDuration = value;
		}

		/**
		 * @private
		 */
		protected var _throwEase:Object = Transitions.EASE_OUT;

		/**
		 * The easing function used for "throw" animations.
		 *
		 * <p>In the following example, the ease of throwing animations is
		 * customized:</p>
		 *
		 * <listing version="3.0">
		 * scroller.throwEase = Transitions.EASE_IN_OUT;</listing>
		 *
		 * @default starling.animation.Transitions.EASE_OUT
		 *
		 * @see starling.animation.Transitions
		 */
		public function get throwEase():Object
		{
			return this._throwEase;
		}

		/**
		 * @private
		 */
		public function set throwEase(value:Object):void
		{
			this._throwEase = value;
		}

		/**
		 * @private
		 */
		protected var _snapScrollPositionsToPixels:Boolean = false;

		/**
		 * If enabled, the scroll position will always be adjusted to whole
		 * pixels.
		 *
		 * <p>In the following example, the scroll position is snapped to pixels:</p>
		 *
		 * <listing version="3.0">
		 * scroller.snapScrollPositionsToPixels = true;</listing>
		 *
		 * @default false
		 */
		public function get snapScrollPositionsToPixels():Boolean
		{
			return this._snapScrollPositionsToPixels;
		}

		/**
		 * @private
		 */
		public function set snapScrollPositionsToPixels(value:Boolean):void
		{
			if(this._snapScrollPositionsToPixels == value)
			{
				return;
			}
			this._snapScrollPositionsToPixels = value;
			if(this._snapScrollPositionsToPixels)
			{
				this.horizontalScrollPosition = Math.round(this._horizontalScrollPosition);
				this.verticalScrollPosition = Math.round(this._verticalScrollPosition);
			}
		}

		/**
		 * @private
		 */
		protected var _horizontalScrollBarIsScrolling:Boolean = false;

		/**
		 * @private
		 */
		protected var _verticalScrollBarIsScrolling:Boolean = false;

		/**
		 * @private
		 */
		protected var _isScrolling:Boolean = false;

		/**
		 * Determines if the scroller is currently scrolling with user
		 * interaction or with animation.
		 */
		public function get isScrolling():Boolean
		{
			return this._isScrolling;
		}

		/**
		 * @private
		 */
		protected var _isScrollingStopped:Boolean = false;

		/**
		 * The pending horizontal scroll position to scroll to after validating.
		 * A value of <code>NaN</code> means that the scroller won't scroll to a
		 * horizontal position after validating.
		 */
		protected var pendingHorizontalScrollPosition:Number = NaN;

		/**
		 * The pending vertical scroll position to scroll to after validating.
		 * A value of <code>NaN</code> means that the scroller won't scroll to a
		 * vertical position after validating.
		 */
		protected var pendingVerticalScrollPosition:Number = NaN;

		/**
		 * The pending horizontal page index to scroll to after validating. A
		 * value of <code>-1</code> means that the scroller won't scroll to a
		 * horizontal page after validating.
		 */
		protected var pendingHorizontalPageIndex:int = -1;

		/**
		 * The pending vertical page index to scroll to after validating. A
		 * value of <code>-1</code> means that the scroller won't scroll to a
		 * vertical page after validating.
		 */
		protected var pendingVerticalPageIndex:int = -1;

		/**
		 * The duration of the pending scroll action.
		 */
		protected var pendingScrollDuration:Number;

		/**
		 * @private
		 */
		protected var isScrollBarRevealPending:Boolean = false;

		/**
		 * @private
		 */
		protected var _revealScrollBarsDuration:Number = 1.0;

		/**
		 * The duration, in seconds, that the scroll bars will be shown when
		 * calling <code>revealScrollBars()</code>
		 *
		 * @default 1.0
		 *
		 * @see #revealScrollBars()
		 */
		public function get revealScrollBarsDuration():Number
		{
			return this._revealScrollBarsDuration;
		}

		/**
		 * @private
		 */
		public function set revealScrollBarsDuration(value:Number):void
		{
			this._revealScrollBarsDuration = value;
		}

		/**
		 * @private
		 */
		override public function dispose():void
		{
			Starling.current.nativeStage.removeEventListener(MouseEvent.MOUSE_WHEEL, nativeStage_mouseWheelHandler);
			Starling.current.nativeStage.removeEventListener("orientationChange", nativeStage_orientationChangeHandler);
			super.dispose();
		}

		/**
		 * If the user is scrolling with touch or if the scrolling is animated,
		 * calling stopScrolling() will cause the scroller to ignore the drag
		 * and stop animations. This function may only be called during scrolling,
		 * so if you need to stop scrolling on a <code>TouchEvent</code> with
		 * <code>TouchPhase.BEGAN</code>, you may need to wait for the scroller
		 * to start scrolling before you can call this function.
		 *
		 * <p>In the following example, we listen for <code>FeathersEventType.SCROLL_START</code>
		 * to stop scrolling:</p>
		 *
		 * <listing version="3.0">
		 * scroller.addEventListener( FeathersEventType.SCROLL_START, function( event:Event ):void
		 * {
		 *     scroller.stopScrolling();
		 * });</listing>
		 */
		public function stopScrolling():void
		{
			if(this._horizontalAutoScrollTween)
			{
				Starling.juggler.remove(this._horizontalAutoScrollTween);
				this._horizontalAutoScrollTween = null;
			}
			if(this._verticalAutoScrollTween)
			{
				Starling.juggler.remove(this._verticalAutoScrollTween);
				this._verticalAutoScrollTween = null;
			}
			this._isScrollingStopped = true;
			this._velocityX = 0;
			this._velocityY = 0;
			this._previousVelocityX.length = 0;
			this._previousVelocityY.length = 0;
			this.hideHorizontalScrollBar();
			this.hideVerticalScrollBar();
		}

		/**
		 * After the next validation, scrolls to a specific position. May scroll
		 * in only one direction by passing in a value of <code>NaN</code> for
		 * either scroll position. If the <code>animationDuration</code> argument
		 * is greater than zero, the scroll will animate. The duration is in
		 * seconds.
		 *
		 * <p>Because this function is primarily designed for animation, using a
		 * duration of <code>0</code> may require a frame or two before the
		 * scroll position updates.</p>
		 *
		 * <p>In the following example, we scroll to the maximum vertical scroll
		 * position:</p>
		 *
		 * <listing version="3.0">
		 * scroller.scrollToPosition( scroller.horizontalScrollPosition, scroller.maxVerticalScrollPosition );</listing>
		 *
		 * @see #horizontalScrollPosition
		 * @see #verticalScrollPosition
		 */
		public function scrollToPosition(horizontalScrollPosition:Number, verticalScrollPosition:Number, animationDuration:Number = 0):void
		{
			this.pendingHorizontalPageIndex = -1;
			this.pendingVerticalPageIndex = -1;
			if(this.pendingHorizontalScrollPosition == horizontalScrollPosition &&
				this.pendingVerticalScrollPosition == verticalScrollPosition &&
				this.pendingScrollDuration == animationDuration)
			{
				return;
			}
			this.pendingHorizontalScrollPosition = horizontalScrollPosition;
			this.pendingVerticalScrollPosition = verticalScrollPosition;
			this.pendingScrollDuration = animationDuration;
			this.invalidate(INVALIDATION_FLAG_PENDING_SCROLL);
		}

		/**
		 * After the next validation, scrolls to a specific page index. May scroll
		 * in only one direction by passing in a value of <code>-1</code> for
		 * either page index. If the <code>animationDuration</code> argument
		 * is greater than zero, the scroll will animate. The duration is in
		 * seconds.
		 *
		 * <p>You can only scroll to a page if the <code>snapToPages</code>
		 * property is <code>true</code>.</p>
		 *
		 * <p>In the following example, we scroll to the last horizontal page:</p>
		 *
		 * <listing version="3.0">
		 * scroller.scrollToPageIndex( scroller.horizontalPageCount - 1, scroller.verticalPageIndex );</listing>
		 *
		 * @see #snapToPages
		 */
		public function scrollToPageIndex(horizontalPageIndex:int, verticalPageIndex:int, animationDuration:Number = 0):void
		{
			this.pendingHorizontalScrollPosition = NaN;
			this.pendingVerticalScrollPosition = NaN;
			const horizontalPageHasChanged:Boolean = (this.pendingHorizontalPageIndex >= 0 && this.pendingHorizontalPageIndex != horizontalPageIndex) ||
				(this.pendingHorizontalPageIndex < 0 && this._horizontalPageIndex != horizontalPageIndex);
			const verticalPageHasChanged:Boolean = (this.pendingVerticalPageIndex >= 0 && this.pendingVerticalPageIndex != verticalPageIndex) ||
				(this.pendingVerticalPageIndex < 0 && this._verticalPageIndex != verticalPageIndex);
			const durationHasChanged:Boolean = (this.pendingHorizontalPageIndex >= 0 || this.pendingVerticalPageIndex >= 0) && this.pendingScrollDuration == animationDuration
			if(!horizontalPageHasChanged && !verticalPageHasChanged &&
				!durationHasChanged)
			{
				return;
			}
			this.pendingHorizontalPageIndex = horizontalPageIndex;
			this.pendingVerticalPageIndex = verticalPageIndex;
			this.pendingScrollDuration = animationDuration;
			this.invalidate(INVALIDATION_FLAG_PENDING_SCROLL);
		}

		/**
		 * If the scroll bars are floating, briefly show them as a hint to the
		 * user. Useful when first navigating to a screen to give the user
		 * context about both the ability to scroll and the current scroll
		 * position.
		 *
		 * @see #revealScrollBarsDuration
		 */
		public function revealScrollBars():void
		{
			this.isScrollBarRevealPending = true;
			this.invalidate(INVALIDATION_FLAG_PENDING_REVEAL_SCROLL_BARS);
		}

		/**
		 * @private
		 */
		override public function hitTest(localPoint:Point, forTouch:Boolean = false):DisplayObject
		{
			//save localX and localY because localPoint could change after the
			//call to super.hitTest().
			const localX:Number = localPoint.x;
			const localY:Number = localPoint.y;
			//first check the children for touches
			var result:DisplayObject = super.hitTest(localPoint, forTouch);
			if(!result)
			{
				//we want to register touches in our hitArea as a last resort
				if(forTouch && (!this.visible || !this.touchable))
				{
					return null;
				}
				return this._hitArea.contains(localX, localY) ? this : null;
			}
			return result;
		}

		/**
		 * @private
		 */
		override protected function draw():void
		{
			var sizeInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_SIZE);
			//we don't use this flag in this class, but subclasses will use it,
			//and it's better to handle it here instead of having them
			//invalidate unrelated flags
			const dataInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_DATA);
			var scrollInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_SCROLL);
			const clippingInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_CLIPPING);
			const stylesInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_STYLES);
			const stateInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_STATE);
			const scrollBarInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_SCROLL_BAR_RENDERER);
			const pendingScrollInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_PENDING_SCROLL);
			const pendingRevealScrollBarsInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_PENDING_REVEAL_SCROLL_BARS);

			if(scrollBarInvalid)
			{
				this.createScrollBars();
			}

			if(sizeInvalid || stylesInvalid || stateInvalid)
			{
				this.refreshBackgroundSkin();
			}

			if(scrollBarInvalid || stylesInvalid)
			{
				this.refreshScrollBarStyles();
				this.refreshInteractionModeEvents();
			}

			if(scrollBarInvalid || stateInvalid)
			{
				this.refreshEnabled();
			}

			if(this.horizontalScrollBar)
			{
				this.horizontalScrollBar.validate();
			}
			if(this.verticalScrollBar)
			{
				this.verticalScrollBar.validate();
			}

			const oldMaxHorizontalScrollPosition:Number = this._maxHorizontalScrollPosition;
			const oldMaxVerticalScrollPosition:Number = this._maxVerticalScrollPosition;
			var loopCount:int = 0;
			do
			{
				this._hasViewPortBoundsChanged = false;
				//even if fixed, we need to measure without them first because
				//if the scroll policy is auto, we only show them when needed.
				if(scrollInvalid || dataInvalid || sizeInvalid || stylesInvalid || scrollBarInvalid)
				{
					this.calculateViewPortOffsets(true, false);
					this.refreshViewPortBoundsWithoutFixedScrollBars();
					this.calculateViewPortOffsets(false, false);
				}

				sizeInvalid = this.autoSizeIfNeeded() || sizeInvalid;

				//just in case autoSizeIfNeeded() is overridden, we need to call
				//this again and use actualWidth/Height instead of
				//explicitWidth/Height.
				this.calculateViewPortOffsets(false, true);

				if(scrollInvalid || dataInvalid || sizeInvalid || stylesInvalid || scrollBarInvalid)
				{
					this.refreshViewPortBoundsWithFixedScrollBars();
					this.refreshScrollValues(scrollInvalid);
				}
				loopCount++;
				if(loopCount >= 10)
				{
					//if it still fails after ten tries, we've probably entered
					//an infinite loop due to rounding errors or something
					break;
				}
			}
			while(this._hasViewPortBoundsChanged)
			this._lastViewPortWidth = viewPort.width;
			this._lastViewPortHeight = viewPort.height;
			if(scrollInvalid || this._maxHorizontalScrollPosition != oldMaxHorizontalScrollPosition ||
				this._maxVerticalScrollPosition != oldMaxVerticalScrollPosition)
			{
				scrollInvalid = true;
				this.dispatchEventWith(Event.SCROLL);
			}

			this.showOrHideChildren();

			if(scrollInvalid || sizeInvalid || stylesInvalid || scrollBarInvalid)
			{
				this.layoutChildren();
			}

			if(scrollInvalid || sizeInvalid || stylesInvalid || scrollBarInvalid)
			{
				this.refreshScrollBarValues();
			}

			if(scrollInvalid || sizeInvalid || stylesInvalid || scrollBarInvalid || clippingInvalid)
			{
				this.refreshClipRect();
			}

			if(pendingScrollInvalid)
			{
				this.handlePendingScroll();
			}

			if(pendingRevealScrollBarsInvalid)
			{
				this.handlePendingRevealScrollBars();
			}
		}

		/**
		 * If the component's dimensions have not been set explicitly, it will
		 * measure its content and determine an ideal size for itself. If the
		 * <code>explicitWidth</code> or <code>explicitHeight</code> member
		 * variables are set, those value will be used without additional
		 * measurement. If one is set, but not the other, the dimension with the
		 * explicit value will not be measured, but the other non-explicit
		 * dimension will still need measurement.
		 *
		 * <p>Calls <code>setSizeInternal()</code> to set up the
		 * <code>actualWidth</code> and <code>actualHeight</code> member
		 * variables used for layout.</p>
		 *
		 * <p>Meant for internal use, and subclasses may override this function
		 * with a custom implementation.</p>
		 */
		protected function autoSizeIfNeeded():Boolean
		{
			const needsWidth:Boolean = isNaN(this.explicitWidth);
			const needsHeight:Boolean = isNaN(this.explicitHeight);
			if(!needsWidth && !needsHeight)
			{
				return false;
			}

			var newWidth:Number = this.explicitWidth;
			var newHeight:Number = this.explicitHeight;
			if(needsWidth)
			{
				newWidth = this._viewPort.width + this._rightViewPortOffset + this._leftViewPortOffset;
				if(!isNaN(this.originalBackgroundWidth))
				{
					newWidth = Math.max(newWidth, this.originalBackgroundWidth);
				}
			}
			if(needsHeight)
			{
				newHeight = this._viewPort.height + this._bottomViewPortOffset + this._topViewPortOffset;
				if(!isNaN(this.originalBackgroundHeight))
				{
					newHeight = Math.max(newHeight, this.originalBackgroundHeight);
				}
			}
			return this.setSizeInternal(newWidth, newHeight, false);
		}

		/**
		 * Creates and adds the <code>horizontalScrollBar</code> and
		 * <code>verticalScrollBar</code> sub-components and removes the old
		 * instances, if they exist.
		 *
		 * <p>Meant for internal use, and subclasses may override this function
		 * with a custom implementation.</p>
		 *
		 * @see #horizontalScrollBar
		 * @see #verticalScrollBar
		 * @see #horizontalScrollBarFactory
		 * @see #verticalScrollBarFactory
		 */
		protected function createScrollBars():void
		{
			if(this.horizontalScrollBar)
			{
				this.horizontalScrollBar.removeEventListener(FeathersEventType.BEGIN_INTERACTION, horizontalScrollBar_beginInteractionHandler);
				this.horizontalScrollBar.removeEventListener(FeathersEventType.END_INTERACTION, horizontalScrollBar_endInteractionHandler);
				this.horizontalScrollBar.removeEventListener(Event.CHANGE, horizontalScrollBar_changeHandler);
				this.removeRawChildInternal(DisplayObject(this.horizontalScrollBar), true);
				this.horizontalScrollBar = null;
			}
			if(this.verticalScrollBar)
			{
				this.verticalScrollBar.removeEventListener(FeathersEventType.BEGIN_INTERACTION, verticalScrollBar_beginInteractionHandler);
				this.verticalScrollBar.removeEventListener(FeathersEventType.END_INTERACTION, verticalScrollBar_endInteractionHandler);
				this.verticalScrollBar.removeEventListener(Event.CHANGE, verticalScrollBar_changeHandler);
				this.removeRawChildInternal(DisplayObject(this.verticalScrollBar), true);
				this.verticalScrollBar = null;
			}

			if(this._scrollBarDisplayMode != SCROLL_BAR_DISPLAY_MODE_NONE &&
				this._horizontalScrollPolicy != SCROLL_POLICY_OFF && this._horizontalScrollBarFactory != null)
			{
				this.horizontalScrollBar = IScrollBar(this._horizontalScrollBarFactory());
				const horizontalScrollBarName:String = this._customHorizontalScrollBarName != null ? this._customHorizontalScrollBarName : this.horizontalScrollBarName;
				this.horizontalScrollBar.nameList.add(horizontalScrollBarName);
				this.horizontalScrollBar.addEventListener(Event.CHANGE, horizontalScrollBar_changeHandler);
				this.horizontalScrollBar.addEventListener(FeathersEventType.BEGIN_INTERACTION, horizontalScrollBar_beginInteractionHandler);
				this.horizontalScrollBar.addEventListener(FeathersEventType.END_INTERACTION, horizontalScrollBar_endInteractionHandler);
				this.addRawChildInternal(DisplayObject(this.horizontalScrollBar));
			}
			if(this._scrollBarDisplayMode != SCROLL_BAR_DISPLAY_MODE_NONE &&
				this._verticalScrollPolicy != SCROLL_POLICY_OFF && this._verticalScrollBarFactory != null)
			{
				this.verticalScrollBar = IScrollBar(this._verticalScrollBarFactory());
				const verticalScrollBarName:String = this._customVerticalScrollBarName != null ? this._customVerticalScrollBarName : this.verticalScrollBarName;
				this.verticalScrollBar.nameList.add(verticalScrollBarName);
				this.verticalScrollBar.addEventListener(Event.CHANGE, verticalScrollBar_changeHandler);
				this.verticalScrollBar.addEventListener(FeathersEventType.BEGIN_INTERACTION, verticalScrollBar_beginInteractionHandler);
				this.verticalScrollBar.addEventListener(FeathersEventType.END_INTERACTION, verticalScrollBar_endInteractionHandler);
				this.addRawChildInternal(DisplayObject(this.verticalScrollBar));
			}
		}

		/**
		 * Choose the appropriate background skin based on the control's current
		 * state.
		 */
		protected function refreshBackgroundSkin():void
		{
			this.currentBackgroundSkin = this._backgroundSkin;
			if(!this._isEnabled && this._backgroundDisabledSkin)
			{
				if(this._backgroundSkin)
				{
					this._backgroundSkin.visible = false;
				}
				this.currentBackgroundSkin = this._backgroundDisabledSkin;
			}
			else if(this._backgroundDisabledSkin)
			{
				this._backgroundDisabledSkin.visible = false;
			}
			if(this.currentBackgroundSkin)
			{
				//force it to the bottom
				this.setRawChildIndexInternal(this.currentBackgroundSkin, 0);

				if(isNaN(this.originalBackgroundWidth))
				{
					this.originalBackgroundWidth = this.currentBackgroundSkin.width;
				}
				if(isNaN(this.originalBackgroundHeight))
				{
					this.originalBackgroundHeight = this.currentBackgroundSkin.height;
				}
			}
		}

		/**
		 * @private
		 */
		protected function refreshScrollBarStyles():void
		{
			if(this.horizontalScrollBar)
			{
				var objectScrollBar:Object = this.horizontalScrollBar;
				for(var propertyName:String in this._horizontalScrollBarProperties)
				{
					if(objectScrollBar.hasOwnProperty(propertyName))
					{
						var propertyValue:Object = this._horizontalScrollBarProperties[propertyName];
						this.horizontalScrollBar[propertyName] = propertyValue;
					}
				}
				if(this._horizontalScrollBarHideTween)
				{
					Starling.juggler.remove(this._horizontalScrollBarHideTween);
					this._horizontalScrollBarHideTween = null;
				}
				this.horizontalScrollBar.alpha = this._scrollBarDisplayMode == SCROLL_BAR_DISPLAY_MODE_FLOAT ? 0 : 1;
				this.horizontalScrollBar.touchable = this._interactionMode == INTERACTION_MODE_MOUSE || this._interactionMode == INTERACTION_MODE_TOUCH_AND_SCROLL_BARS;
			}
			if(this.verticalScrollBar)
			{
				objectScrollBar = this.verticalScrollBar;
				for(propertyName in this._verticalScrollBarProperties)
				{
					if(objectScrollBar.hasOwnProperty(propertyName))
					{
						propertyValue = this._verticalScrollBarProperties[propertyName];
						this.verticalScrollBar[propertyName] = propertyValue;
					}
				}
				if(this._verticalScrollBarHideTween)
				{
					Starling.juggler.remove(this._verticalScrollBarHideTween);
					this._verticalScrollBarHideTween = null;
				}
				this.verticalScrollBar.alpha = this._scrollBarDisplayMode == SCROLL_BAR_DISPLAY_MODE_FLOAT ? 0 : 1;
				this.verticalScrollBar.touchable = this._interactionMode == INTERACTION_MODE_MOUSE || this._interactionMode == INTERACTION_MODE_TOUCH_AND_SCROLL_BARS;
			}
		}

		/**
		 * @private
		 */
		protected function refreshEnabled():void
		{
			if(this._viewPort)
			{
				this._viewPort.isEnabled = this._isEnabled;
			}
			if(this.horizontalScrollBar)
			{
				this.horizontalScrollBar.isEnabled = this._isEnabled;
			}
			if(this.verticalScrollBar)
			{
				this.verticalScrollBar.isEnabled = this._isEnabled;
			}
		}

		/**
		 * @private
		 */
		protected function refreshViewPortBoundsWithoutFixedScrollBars():void
		{
			var horizontalWidthOffset:Number = this._leftViewPortOffset + this._rightViewPortOffset;
			var verticalHeightOffset:Number = this._topViewPortOffset + this._bottomViewPortOffset;

			//if scroll bars are fixed, we're going to include the offsets even
			//if they may not be needed in the final pass. if not fixed, the
			//view port fills the entire bounds.
			this._viewPort.visibleWidth = this.explicitWidth - horizontalWidthOffset;
			this._viewPort.visibleHeight = this.explicitHeight - verticalHeightOffset;
			this._viewPort.minVisibleWidth = Math.max(0, this._minWidth - horizontalWidthOffset);
			this._viewPort.maxVisibleWidth = this._maxWidth - horizontalWidthOffset;
			this._viewPort.minVisibleHeight = Math.max(0, this._minHeight - verticalHeightOffset);
			this._viewPort.maxVisibleHeight = this._maxHeight - verticalHeightOffset;
			this._viewPort.horizontalScrollPosition = this._horizontalScrollPosition;
			this._viewPort.verticalScrollPosition = this._verticalScrollPosition;

			const oldIgnoreViewPortResizing:Boolean = this.ignoreViewPortResizing;
			if(this._scrollBarDisplayMode == SCROLL_BAR_DISPLAY_MODE_FIXED)
			{
				this.ignoreViewPortResizing = true;
			}
			this._viewPort.validate();
			this.ignoreViewPortResizing = oldIgnoreViewPortResizing;
		}

		/**
		 * @private
		 */
		protected function refreshViewPortBoundsWithFixedScrollBars():void
		{
			this._viewPort.visibleWidth = this.actualWidth - (this._leftViewPortOffset + this._rightViewPortOffset);
			this._viewPort.visibleHeight = this.actualHeight - (this._topViewPortOffset + this._bottomViewPortOffset);
			this._viewPort.validate();
		}

		/**
		 * @private
		 */
		protected function refreshScrollValues(isScrollInvalid:Boolean):void
		{
			if(isNaN(this.explicitHorizontalScrollStep))
			{
				if(this._viewPort)
				{
					this.actualHorizontalScrollStep = this._viewPort.horizontalScrollStep;
				}
				else
				{
					this.actualHorizontalScrollStep = 1;
				}
			}
			else
			{
				this.actualHorizontalScrollStep = this.explicitHorizontalScrollStep;
			}
			if(isNaN(this.explicitVerticalScrollStep))
			{
				if(this._viewPort)
				{
					this.actualVerticalScrollStep = this._viewPort.verticalScrollStep;
				}
				else
				{
					this.actualVerticalScrollStep = 1;
				}
			}
			else
			{
				this.actualVerticalScrollStep = this.explicitVerticalScrollStep;
			}

			if(isNaN(this.explicitPageWidth))
			{
				this.actualPageWidth = this.actualWidth - (this._leftViewPortOffset + this._rightViewPortOffset);
			}
			if(isNaN(this.explicitPageHeight))
			{
				this.actualPageHeight = this.actualHeight - (this._topViewPortOffset + this._bottomViewPortOffset);
			}
			const oldMaxHSP:Number = this._maxHorizontalScrollPosition;
			const oldMaxVSP:Number = this._maxVerticalScrollPosition;
			if(this._viewPort)
			{
				this._minHorizontalScrollPosition = this._viewPort.contentX;
				this._maxHorizontalScrollPosition = this._viewPort.width - this.actualPageWidth;
				if(this._maxHorizontalScrollPosition < this._minHorizontalScrollPosition)
				{
					this._maxHorizontalScrollPosition = this._minHorizontalScrollPosition;
				}
				this._minVerticalScrollPosition = this._viewPort.contentY;
				this._maxVerticalScrollPosition = this._viewPort.height - this.actualPageHeight;
				if(this._maxVerticalScrollPosition < this._minVerticalScrollPosition)
				{
					this._maxVerticalScrollPosition =  this._minVerticalScrollPosition;
				}
				if(this._snapScrollPositionsToPixels)
				{
					this._minHorizontalScrollPosition = Math.round(this._minHorizontalScrollPosition);
					this._minVerticalScrollPosition = Math.round(this._minVerticalScrollPosition);
					this._maxHorizontalScrollPosition = Math.round(this._maxHorizontalScrollPosition);
					this._maxVerticalScrollPosition = Math.round(this._maxVerticalScrollPosition);
				}
			}
			else
			{
				this._minHorizontalScrollPosition = 0;
				this._minVerticalScrollPosition = 0;
				this._maxHorizontalScrollPosition = 0;
				this._maxVerticalScrollPosition = 0;
			}
			if(this._snapToPages)
			{
				var horizontalRange:Number = this._maxHorizontalScrollPosition - this._minHorizontalScrollPosition;
				var verticalPageRange:Number = this._maxVerticalScrollPosition - this._minVerticalScrollPosition;
				this._horizontalPageCount = Math.ceil(horizontalRange / this.actualPageWidth) + 1;
				this._verticalPageCount = Math.ceil(verticalPageRange / this.actualPageHeight) + 1;
			}
			else
			{
				this._horizontalPageCount = 1;
				this._verticalPageCount = 1;
			}

			const maximumPositionsChanged:Boolean = this._maxHorizontalScrollPosition != oldMaxHSP || this._maxVerticalScrollPosition != oldMaxVSP;
			if(maximumPositionsChanged)
			{
				if(this._touchPointID < 0 && !this._horizontalAutoScrollTween)
				{
					if(this._snapToPages)
					{
						this._horizontalScrollPosition = roundToNearest(this._horizontalScrollPosition, this.actualPageWidth);
					}
					var targetHorizontalScrollPosition:Number = this._horizontalScrollPosition;
					if(targetHorizontalScrollPosition < this._minHorizontalScrollPosition)
					{
						targetHorizontalScrollPosition = this._minHorizontalScrollPosition;
					}
					else if(targetHorizontalScrollPosition > this._maxHorizontalScrollPosition)
					{
						targetHorizontalScrollPosition = this._maxHorizontalScrollPosition;
					}
					this.horizontalScrollPosition = targetHorizontalScrollPosition;
				}
				if(this._touchPointID < 0 && !this._verticalAutoScrollTween)
				{
					if(this._snapToPages)
					{
						this._verticalScrollPosition = roundToNearest(this._verticalScrollPosition, this.actualPageHeight);
					}
					var targetVerticalScrollPosition:Number = this._verticalScrollPosition;
					if(targetVerticalScrollPosition < this._minVerticalScrollPosition)
					{
						targetVerticalScrollPosition = this._minVerticalScrollPosition;
					}
					else if(targetVerticalScrollPosition > this._maxVerticalScrollPosition)
					{
						targetVerticalScrollPosition = this._maxVerticalScrollPosition;
					}
					this.verticalScrollPosition = targetVerticalScrollPosition;
				}
			}

			if(this._snapToPages)
			{
				if(isScrollInvalid && !this._isDraggingHorizontally && !this._horizontalAutoScrollTween && this.pendingHorizontalPageIndex < 0)
				{
					if(this._horizontalScrollPosition == this._maxHorizontalScrollPosition)
					{
						this._horizontalPageIndex = this._horizontalPageCount - 1;
					}
					else
					{
						var adjustedHorizontalScrollPosition:Number = this._horizontalScrollPosition - this._minHorizontalScrollPosition;
						this._horizontalPageIndex = Math.floor(adjustedHorizontalScrollPosition / this.actualPageWidth);
					}
				}
				if(isScrollInvalid && !this._isDraggingVertically && !this._verticalAutoScrollTween && this.pendingVerticalPageIndex < 0)
				{
					if(this._verticalScrollPosition == this._maxVerticalScrollPosition)
					{
						this._verticalPageIndex = this._verticalPageCount - 1;
					}
					else
					{
						var adjustedVerticalScrollPosition:Number = this._verticalScrollPosition - this._minVerticalScrollPosition;
						this._verticalPageIndex = Math.floor(adjustedVerticalScrollPosition / this.actualPageHeight);
					}
				}
			}
			else
			{
				this._horizontalPageIndex = this._verticalPageIndex = 0;
			}

			if(maximumPositionsChanged)
			{
				if(this._horizontalAutoScrollTween && this._targetHorizontalScrollPosition > this._maxHorizontalScrollPosition &&
					oldMaxHSP > this._maxHorizontalScrollPosition)
				{
					this._targetHorizontalScrollPosition -= (oldMaxHSP - this._maxHorizontalScrollPosition);
					this.throwTo(this._targetHorizontalScrollPosition, NaN, this._horizontalAutoScrollTween.totalTime - this._horizontalAutoScrollTween.currentTime);
				}
				if(this._verticalAutoScrollTween && this._targetVerticalScrollPosition > this._maxVerticalScrollPosition &&
					oldMaxVSP > this._maxVerticalScrollPosition)
				{
					this._targetVerticalScrollPosition -= (oldMaxVSP - this._maxVerticalScrollPosition);
					this.throwTo(NaN, this._targetVerticalScrollPosition, this._verticalAutoScrollTween.totalTime - this._verticalAutoScrollTween.currentTime);
				}
			}
		}

		/**
		 * @private
		 */
		protected function refreshScrollBarValues():void
		{
			if(this.horizontalScrollBar)
			{
				this.horizontalScrollBar.minimum = this._minHorizontalScrollPosition;
				this.horizontalScrollBar.maximum = this._maxHorizontalScrollPosition;
				this.horizontalScrollBar.value = this._horizontalScrollPosition;
				this.horizontalScrollBar.page = this._maxHorizontalScrollPosition * this.actualPageWidth / this._viewPort.width;
				this.horizontalScrollBar.step = this.actualHorizontalScrollStep;
			}

			if(this.verticalScrollBar)
			{
				this.verticalScrollBar.minimum = this._minVerticalScrollPosition;
				this.verticalScrollBar.maximum = this._maxVerticalScrollPosition;
				this.verticalScrollBar.value = this._verticalScrollPosition;
				this.verticalScrollBar.page = this._maxVerticalScrollPosition * this.actualPageHeight / this._viewPort.height;
				this.verticalScrollBar.step = this.actualVerticalScrollStep;
			}
		}

		/**
		 * @private
		 */
		protected function showOrHideChildren():void
		{
			var isFixed:Boolean = this._scrollBarDisplayMode == SCROLL_BAR_DISPLAY_MODE_FIXED;
			var childCount:int = this.numRawChildrenInternal;
			if(this.verticalScrollBar)
			{
				this.verticalScrollBar.visible = !isFixed || this._hasVerticalScrollBar;
				this.setRawChildIndexInternal(DisplayObject(this.verticalScrollBar), childCount - 1);
			}
			if(this.horizontalScrollBar)
			{
				this.horizontalScrollBar.visible = !isFixed || this._hasHorizontalScrollBar;
				if(this.verticalScrollBar)
				{
					this.setRawChildIndexInternal(DisplayObject(this.horizontalScrollBar), childCount - 2);
				}
				else
				{
					this.setRawChildIndexInternal(DisplayObject(this.horizontalScrollBar), childCount - 1);
				}
			}
			if(this.currentBackgroundSkin)
			{
				if(this._autoHideBackground)
				{
					this.currentBackgroundSkin.visible = this._viewPort.width < this.actualWidth ||
						this._viewPort.height < this.actualHeight ||
						this._horizontalScrollPosition < 0 ||
						this._horizontalScrollPosition > this._maxHorizontalScrollPosition ||
						this._verticalScrollPosition < 0 ||
						this._verticalScrollPosition > this._maxVerticalScrollPosition;
				}
				else
				{
					this.currentBackgroundSkin.visible = true;
				}
			}

		}

		/**
		 * @private
		 */
		protected function calculateViewPortOffsetsForFixedHorizontalScrollBar(forceScrollBars:Boolean = false, useActualBounds:Boolean = false):void
		{
			if(this.horizontalScrollBar)
			{
				var scrollerWidth:Number = useActualBounds ? this.actualWidth : (this.explicitWidth);
				var totalWidth:Number = this._viewPort.width + this._leftViewPortOffset + this._rightViewPortOffset;
				if(forceScrollBars || this._horizontalScrollPolicy == SCROLL_POLICY_ON ||
					((totalWidth > scrollerWidth || totalWidth > this._maxWidth) &&
						this._horizontalScrollPolicy != SCROLL_POLICY_OFF))
				{
					this._hasHorizontalScrollBar = true;
					this._bottomViewPortOffset += this.horizontalScrollBar.height;
				}
				else
				{
					this._hasHorizontalScrollBar = false;
				}
			}
			else
			{
				this._hasHorizontalScrollBar = false;
			}
		}

		/**
		 * @private
		 */
		protected function calculateViewPortOffsetsForFixedVerticalScrollBar(forceScrollBars:Boolean = false, useActualBounds:Boolean = false):void
		{
			if(this.verticalScrollBar)
			{
				var scrollerHeight:Number = useActualBounds ? this.actualHeight : this.explicitHeight;
				var totalHeight:Number = this._viewPort.height + this._topViewPortOffset + this._bottomViewPortOffset;
				if(forceScrollBars || this._verticalScrollPolicy == SCROLL_POLICY_ON ||
					((totalHeight > scrollerHeight || totalHeight > this._maxHeight) &&
						this._verticalScrollPolicy != SCROLL_POLICY_OFF))
				{
					this._hasVerticalScrollBar = true;
					if(this._verticalScrollBarPosition == VERTICAL_SCROLL_BAR_POSITION_LEFT)
					{
						this._leftViewPortOffset += this.verticalScrollBar.width;
					}
					else
					{
						this._rightViewPortOffset += this.verticalScrollBar.width;
					}
				}
				else
				{
					this._hasVerticalScrollBar = false;
				}
			}
			else
			{
				this._hasVerticalScrollBar = false;
			}
		}

		/**
		 * @private
		 */
		protected function calculateViewPortOffsets(forceScrollBars:Boolean = false, useActualBounds:Boolean = false):void
		{
			//in fixed mode, if we determine that scrolling is required, we
			//remember the offsets for later. if scrolling is not needed, then
			//we will ignore the offsets from here forward
			this._topViewPortOffset = this._paddingTop;
			this._rightViewPortOffset = this._paddingRight;
			this._bottomViewPortOffset = this._paddingBottom;
			this._leftViewPortOffset = this._paddingLeft;
			if(this._scrollBarDisplayMode == SCROLL_BAR_DISPLAY_MODE_FIXED)
			{
				this.calculateViewPortOffsetsForFixedHorizontalScrollBar(forceScrollBars, useActualBounds);
				this.calculateViewPortOffsetsForFixedVerticalScrollBar(forceScrollBars, useActualBounds);
				//we need to double check the horizontal scroll bar because
				//adding a vertical scroll bar may require a horizontal one too.
				if(this._hasVerticalScrollBar && !this._hasHorizontalScrollBar)
				{
					this.calculateViewPortOffsetsForFixedHorizontalScrollBar(forceScrollBars, useActualBounds);
				}
			}
			else
			{
				this._hasHorizontalScrollBar = this._isDraggingHorizontally || this._horizontalAutoScrollTween;
				this._hasVerticalScrollBar = this._isDraggingVertically || this._verticalAutoScrollTween;
			}
		}

		/**
		 * @private
		 */
		protected function refreshInteractionModeEvents():void
		{
			if(this._interactionMode == INTERACTION_MODE_TOUCH || this._interactionMode == INTERACTION_MODE_TOUCH_AND_SCROLL_BARS)
			{
				this.addEventListener(TouchEvent.TOUCH, scroller_touchHandler);
				if(!this._touchBlocker)
				{
					this._touchBlocker = new Quad(100, 100, 0xff00ff);
					this._touchBlocker.alpha = 0;
					this._touchBlocker.visible = false;
					this.addRawChildInternal(this._touchBlocker);
				}
			}
			else
			{
				this.removeEventListener(TouchEvent.TOUCH, scroller_touchHandler);
				if(this._touchBlocker)
				{
					this.removeRawChildInternal(this._touchBlocker, true);
					this._touchBlocker = null;
				}
			}

			if((this._interactionMode == INTERACTION_MODE_MOUSE || this._interactionMode == INTERACTION_MODE_TOUCH_AND_SCROLL_BARS) &&
				this._scrollBarDisplayMode == SCROLL_BAR_DISPLAY_MODE_FLOAT)
			{
				if(this.horizontalScrollBar)
				{
					this.horizontalScrollBar.addEventListener(TouchEvent.TOUCH, horizontalScrollBar_touchHandler);
				}
				if(this.verticalScrollBar)
				{
					this.verticalScrollBar.addEventListener(TouchEvent.TOUCH, verticalScrollBar_touchHandler);
				}
			}
			else
			{
				if(this.horizontalScrollBar)
				{
					this.horizontalScrollBar.removeEventListener(TouchEvent.TOUCH, horizontalScrollBar_touchHandler);
				}
				if(this.verticalScrollBar)
				{
					this.verticalScrollBar.removeEventListener(TouchEvent.TOUCH, verticalScrollBar_touchHandler);
				}
			}
		}

		/**
		 * Positions and sizes children based on the actual width and height
		 * values.
		 */
		protected function layoutChildren():void
		{
			if(this.currentBackgroundSkin)
			{
				this.currentBackgroundSkin.width = this.actualWidth;
				this.currentBackgroundSkin.height = this.actualHeight;
			}

			if(this.horizontalScrollBar)
			{
				this.horizontalScrollBar.validate();
			}
			if(this.verticalScrollBar)
			{
				this.verticalScrollBar.validate();
			}
			if(this._touchBlocker)
			{
				this._touchBlocker.x = this._leftViewPortOffset;
				this._touchBlocker.y = this._topViewPortOffset;
				this._touchBlocker.width = this._viewPort.visibleWidth;
				this._touchBlocker.height = this._viewPort.visibleHeight;
			}

			this._viewPort.x = this._leftViewPortOffset - this._horizontalScrollPosition;
			this._viewPort.y = this._topViewPortOffset - this._verticalScrollPosition;

			if(this.horizontalScrollBar)
			{
				this.horizontalScrollBar.x = this._leftViewPortOffset;
				this.horizontalScrollBar.y = this._topViewPortOffset + this._viewPort.visibleHeight;
				if(this._scrollBarDisplayMode != SCROLL_BAR_DISPLAY_MODE_FIXED)
				{
					this.horizontalScrollBar.y -= this.horizontalScrollBar.height;
					if((this._hasVerticalScrollBar || this._verticalScrollBarHideTween) && this.verticalScrollBar)
					{
						this.horizontalScrollBar.width = this._viewPort.visibleWidth - this.verticalScrollBar.width;
					}
					else
					{
						this.horizontalScrollBar.width = this._viewPort.visibleWidth;
					}
				}
				else
				{
					this.horizontalScrollBar.width = this._viewPort.visibleWidth;
				}
			}

			if(this.verticalScrollBar)
			{
				if(this._verticalScrollBarPosition == VERTICAL_SCROLL_BAR_POSITION_LEFT)
				{
					this.verticalScrollBar.x = this._paddingLeft;
				}
				else
				{
					this.verticalScrollBar.x = this._leftViewPortOffset + this._viewPort.visibleWidth;
				}
				this.verticalScrollBar.y = this._topViewPortOffset;
				if(this._scrollBarDisplayMode != SCROLL_BAR_DISPLAY_MODE_FIXED)
				{
					this.verticalScrollBar.x -= this.verticalScrollBar.width;
					if((this._hasHorizontalScrollBar || this._horizontalScrollBarHideTween) && this.horizontalScrollBar)
					{
						this.verticalScrollBar.height = this._viewPort.visibleHeight - this.horizontalScrollBar.height;
					}
					else
					{
						this.verticalScrollBar.height = this._viewPort.visibleHeight;
					}
				}
				else
				{
					this.verticalScrollBar.height = this._viewPort.visibleHeight;
				}
			}
		}

		/**
		 * @private
		 */
		protected function refreshClipRect():void
		{
			const hasElasticEdgesAndTouch:Boolean = this._hasElasticEdges && (this._interactionMode == INTERACTION_MODE_TOUCH || this._interactionMode == INTERACTION_MODE_TOUCH_AND_SCROLL_BARS);
			const contentIsLargeEnoughToScroll:Boolean = this._maxHorizontalScrollPosition != this._minHorizontalScrollPosition || this._maxVerticalScrollPosition != this._minVerticalScrollPosition;
			if(this._clipContent && (hasElasticEdgesAndTouch || contentIsLargeEnoughToScroll))
			{
				if(!this._viewPort.clipRect)
				{
					this._viewPort.clipRect = new Rectangle();
				}

				const clipRect:Rectangle = this._viewPort.clipRect;
				clipRect.x = this._horizontalScrollPosition;
				clipRect.y = this._verticalScrollPosition;
				var clipWidth:Number = this.actualWidth - this._leftViewPortOffset - this._rightViewPortOffset;
				if(clipWidth < 0)
				{
					clipWidth = 0;
				}
				clipRect.width = clipWidth;
				var clipHeight:Number = this.actualHeight - this._topViewPortOffset - this._bottomViewPortOffset;
				if(clipHeight < 0)
				{
					clipHeight = 0;
				}
				clipRect.height = clipHeight;
				this._viewPort.clipRect = clipRect;
			}
			else
			{
				this._viewPort.clipRect = null;
			}
		}

		/**
		 * @private
		 */
		protected function get numRawChildrenInternal():int
		{
			if(this is IScrollContainer)
			{
				return IScrollContainer(this).numRawChildren;
			}
			return this.numChildren;
		}

		/**
		 * @private
		 */
		protected function addRawChildInternal(child:DisplayObject):DisplayObject
		{
			if(this is IScrollContainer)
			{
				return IScrollContainer(this).addRawChild(child);
			}
			return this.addChild(child);
		}

		/**
		 * @private
		 */
		protected function addRawChildAtInternal(child:DisplayObject, index:int):DisplayObject
		{
			if(this is IScrollContainer)
			{
				return IScrollContainer(this).addRawChildAt(child, index);
			}
			return this.addChildAt(child, index);
		}

		/**
		 * @private
		 */
		protected function removeRawChildInternal(child:DisplayObject, dispose:Boolean = false):DisplayObject
		{
			if(this is IScrollContainer)
			{
				return IScrollContainer(this).removeRawChild(child, dispose);
			}
			return this.removeChild(child, dispose);
		}

		/**
		 * @private
		 */
		protected function removeRawChildAtInternal(index:int, dispose:Boolean = false):DisplayObject
		{
			if(this is IScrollContainer)
			{
				return IScrollContainer(this).removeRawChildAt(index, dispose);
			}
			return this.removeChildAt(index, dispose);
		}

		/**
		 * @private
		 */
		protected function setRawChildIndexInternal(child:DisplayObject, index:int):void
		{
			if(this is IScrollContainer)
			{
				return IScrollContainer(this).setRawChildIndex(child, index);
			}
			return this.setChildIndex(child, index);
		}

		/**
		 * @private
		 */
		protected function updateHorizontalScrollFromTouchPosition(touchX:Number):void
		{
			const offset:Number = this._startTouchX - touchX;
			var position:Number = this._startHorizontalScrollPosition + offset;
			if(position < this._minHorizontalScrollPosition)
			{
				if(this._hasElasticEdges)
				{
					position -= (position - this._minHorizontalScrollPosition) * (1 - this._elasticity);
				}
				else
				{
					position = this._minHorizontalScrollPosition;
				}
			}
			else if(position > this._maxHorizontalScrollPosition)
			{
				if(this._hasElasticEdges)
				{
					position -= (position - this._maxHorizontalScrollPosition) * (1 - this._elasticity);
				}
				else
				{
					position = this._maxHorizontalScrollPosition;
				}
			}
			this.horizontalScrollPosition = position;
		}

		/**
		 * @private
		 */
		protected function updateVerticalScrollFromTouchPosition(touchY:Number):void
		{
			const offset:Number = this._startTouchY - touchY;
			var position:Number = this._startVerticalScrollPosition + offset;
			if(position < this._minVerticalScrollPosition)
			{
				if(this._hasElasticEdges)
				{
					position -= (position - this._minVerticalScrollPosition) * (1 - this._elasticity);
				}
				else
				{
					position = this._minVerticalScrollPosition;
				}
			}
			else if(position > this._maxVerticalScrollPosition)
			{
				if(this._hasElasticEdges)
				{
					position -= (position - this._maxVerticalScrollPosition) * (1 - this._elasticity);
				}
				else
				{
					position = this._maxVerticalScrollPosition;
				}
			}
			this.verticalScrollPosition = position;
		}

		/**
		 * Immediately throws the scroller to the specified position, with
		 * optional animation. If you want to throw in only one direction, pass
		 * in <code>NaN</code> for the value that you do not want to change. The
		 * scroller should be validated before throwing.
		 *
		 * @see #scrollToPosition()
		 */
		protected function throwTo(targetHorizontalScrollPosition:Number = NaN, targetVerticalScrollPosition:Number = NaN, duration:Number = 0.5):void
		{
			if(!isNaN(targetHorizontalScrollPosition))
			{
				if(this._horizontalAutoScrollTween)
				{
					Starling.juggler.remove(this._horizontalAutoScrollTween);
					this._horizontalAutoScrollTween = null;
				}
				if(this._horizontalScrollPosition != targetHorizontalScrollPosition)
				{
					this.revealHorizontalScrollBar();
					this.startScroll();
					if(duration == 0)
					{
						this.horizontalScrollPosition = targetHorizontalScrollPosition;
					}
					else
					{
						this._targetHorizontalScrollPosition = targetHorizontalScrollPosition;
						this._horizontalAutoScrollTween = new Tween(this, duration, this._throwEase);
						this._horizontalAutoScrollTween.animate("horizontalScrollPosition", targetHorizontalScrollPosition);
						this._horizontalAutoScrollTween.onComplete = horizontalAutoScrollTween_onComplete;
						Starling.juggler.add(this._horizontalAutoScrollTween);
					}
				}
				else
				{
					this.finishScrollingHorizontally();
				}
			}

			if(!isNaN(targetVerticalScrollPosition))
			{
				if(this._verticalAutoScrollTween)
				{
					Starling.juggler.remove(this._verticalAutoScrollTween);
					this._verticalAutoScrollTween = null;
				}
				if(this._verticalScrollPosition != targetVerticalScrollPosition)
				{
					this.revealVerticalScrollBar();
					this.startScroll();
					if(duration == 0)
					{
						this.verticalScrollPosition = targetVerticalScrollPosition;
					}
					else
					{
						this._targetVerticalScrollPosition = targetVerticalScrollPosition;
						this._verticalAutoScrollTween = new Tween(this, duration, this._throwEase);
						this._verticalAutoScrollTween.animate("verticalScrollPosition", targetVerticalScrollPosition);
						this._verticalAutoScrollTween.onComplete = verticalAutoScrollTween_onComplete;
						Starling.juggler.add(this._verticalAutoScrollTween);
					}
				}
				else
				{
					this.finishScrollingVertically();
				}
			}

			if(duration == 0)
			{
				this.completeScroll();
			}
		}

		/**
		 * Immediately throws the scroller to the specified page index, with
		 * optional animation. If you want to throw in only one direction, pass
		 * in a parameter value of <code>-1</code> for the direction that should
		 * not change. The scroller should be validated before throwing.
		 *
		 * @see #scrollToPageIndex()
		 */
		public function throwToPage(targetHorizontalPageIndex:int = -1, targetVerticalPageIndex:int = -1, duration:Number = 0.5):void
		{
			var targetHorizontalScrollPosition:Number = this._horizontalScrollPosition;
			if(targetHorizontalPageIndex >= 0)
			{
				targetHorizontalScrollPosition = this.actualPageWidth * targetHorizontalPageIndex;
			}
			if(targetHorizontalScrollPosition < this._minHorizontalScrollPosition)
			{
				targetHorizontalScrollPosition = this._minHorizontalScrollPosition;
			}
			if(targetHorizontalScrollPosition > this._maxHorizontalScrollPosition)
			{
				targetHorizontalScrollPosition = this._maxHorizontalScrollPosition;
			}
			var targetVerticalScrollPosition:Number = this._verticalScrollPosition;
			if(targetVerticalPageIndex >= 0)
			{
				targetVerticalScrollPosition = this.actualPageHeight * targetVerticalPageIndex;
			}
			if(targetVerticalScrollPosition < this._minVerticalScrollPosition)
			{
				targetVerticalScrollPosition = this._minVerticalScrollPosition;
			}
			if(targetVerticalScrollPosition > this._maxVerticalScrollPosition)
			{
				targetVerticalScrollPosition = this._maxVerticalScrollPosition;
			}
			if(duration > 0)
			{
				this.throwTo(targetHorizontalScrollPosition, targetVerticalScrollPosition, duration);
			}
			else
			{
				this.horizontalScrollPosition = targetHorizontalScrollPosition;
				this.verticalScrollPosition = targetVerticalScrollPosition;
			}
			if(targetHorizontalPageIndex >= 0)
			{
				this._horizontalPageIndex = targetHorizontalPageIndex;
			}
			if(targetVerticalPageIndex >= 0)
			{
				this._verticalPageIndex = targetVerticalPageIndex;
			}
		}

		/**
		 * @private
		 */
		protected function finishScrollingHorizontally():void
		{
			var targetHorizontalScrollPosition:Number = NaN;
			if(this._horizontalScrollPosition < this._minHorizontalScrollPosition)
			{
				targetHorizontalScrollPosition = this._minHorizontalScrollPosition;
			}
			else if(this._horizontalScrollPosition > this._maxHorizontalScrollPosition)
			{
				targetHorizontalScrollPosition = this._maxHorizontalScrollPosition;
			}

			this._isDraggingHorizontally = false;
			if(isNaN(targetHorizontalScrollPosition))
			{
				this.completeScroll();
			}
			else
			{
				this.throwTo(targetHorizontalScrollPosition, NaN, this._elasticSnapDuration);
			}
		}

		/**
		 * @private
		 */
		protected function finishScrollingVertically():void
		{
			var targetVerticalScrollPosition:Number = NaN;
			if(this._verticalScrollPosition < this._minVerticalScrollPosition)
			{
				targetVerticalScrollPosition = this._minVerticalScrollPosition;
			}
			else if(this._verticalScrollPosition > this._maxVerticalScrollPosition)
			{
				targetVerticalScrollPosition = this._maxVerticalScrollPosition;
			}

			this._isDraggingVertically = false;
			if(isNaN(targetVerticalScrollPosition))
			{
				this.completeScroll();
			}
			else
			{
				this.throwTo(NaN, targetVerticalScrollPosition, this._elasticSnapDuration);
			}
		}

		/**
		 * @private
		 */
		protected function throwHorizontally(pixelsPerMS:Number):void
		{
			if(this._snapToPages)
			{
				const inchesPerSecond:Number = 1000 * pixelsPerMS / (DeviceCapabilities.dpi / Starling.contentScaleFactor);
				if(inchesPerSecond > this._minimumPageThrowVelocity)
				{
					var snappedPageHorizontalScrollPosition:Number = roundDownToNearest(this._horizontalScrollPosition, this.actualPageWidth);
				}
				else if(inchesPerSecond < -this._minimumPageThrowVelocity)
				{
					snappedPageHorizontalScrollPosition = roundUpToNearest(this._horizontalScrollPosition, this.actualPageWidth);
				}
				else
				{
					const lastPageWidth:Number = this._maxHorizontalScrollPosition % this.actualPageWidth;
					var startOfLastPage:Number = this._maxHorizontalScrollPosition - lastPageWidth;
					if(lastPageWidth < this.actualPageWidth && this._horizontalScrollPosition >= startOfLastPage)
					{
						const lastPagePosition:Number = this._horizontalScrollPosition - startOfLastPage;
						if(inchesPerSecond > this._minimumPageThrowVelocity)
						{
							snappedPageHorizontalScrollPosition = startOfLastPage + roundDownToNearest(lastPagePosition, lastPageWidth);
						}
						else if(inchesPerSecond < -this._minimumPageThrowVelocity)
						{
							snappedPageHorizontalScrollPosition = startOfLastPage + roundUpToNearest(lastPagePosition, lastPageWidth);
						}
						else
						{
							snappedPageHorizontalScrollPosition = startOfLastPage + roundToNearest(lastPagePosition, lastPageWidth);
						}
					}
					else
					{
						snappedPageHorizontalScrollPosition = roundToNearest(this._horizontalScrollPosition, this.actualPageWidth);
					}
				}
				if(snappedPageHorizontalScrollPosition < this._minHorizontalScrollPosition)
				{
					snappedPageHorizontalScrollPosition = this._minHorizontalScrollPosition;
				}
				else if(snappedPageHorizontalScrollPosition > this._maxHorizontalScrollPosition)
				{
					snappedPageHorizontalScrollPosition = this._maxHorizontalScrollPosition;
				}
				if(snappedPageHorizontalScrollPosition == this._maxHorizontalScrollPosition)
				{
					var targetHorizontalPageIndex:int = this._horizontalPageCount - 1;
				}
				else
				{
					targetHorizontalPageIndex = (snappedPageHorizontalScrollPosition - this._minHorizontalScrollPosition) / this.actualPageWidth;
				}
				this.throwToPage(targetHorizontalPageIndex, -1, this._pageThrowDuration);
				return;
			}

			const absPixelsPerMS:Number = Math.abs(pixelsPerMS);
			if(absPixelsPerMS <= MINIMUM_VELOCITY)
			{
				this.finishScrollingHorizontally();
				return;
			}
			var targetHorizontalScrollPosition:Number = this._horizontalScrollPosition + (pixelsPerMS - MINIMUM_VELOCITY) / Math.log(FRICTION);
			if(targetHorizontalScrollPosition < this._minHorizontalScrollPosition || targetHorizontalScrollPosition > this._maxHorizontalScrollPosition)
			{
				var duration:Number = 0;
				targetHorizontalScrollPosition = this._horizontalScrollPosition;
				while(Math.abs(pixelsPerMS) > MINIMUM_VELOCITY)
				{
					targetHorizontalScrollPosition -= pixelsPerMS;
					if(targetHorizontalScrollPosition < this._minHorizontalScrollPosition || targetHorizontalScrollPosition > this._maxHorizontalScrollPosition)
					{
						if(this._hasElasticEdges)
						{
							pixelsPerMS *= FRICTION * EXTRA_FRICTION;
						}
						else
						{
							if(targetHorizontalScrollPosition < this._minHorizontalScrollPosition)
							{
								targetHorizontalScrollPosition = this._minHorizontalScrollPosition;
							}
							else if(targetHorizontalScrollPosition > this._maxHorizontalScrollPosition)
							{
								targetHorizontalScrollPosition = this._maxHorizontalScrollPosition;
							}
							duration++;
							break;
						}
					}
					else
					{
						pixelsPerMS *= FRICTION;
					}
					duration++;
				}
			}
			else
			{
				duration = Math.log(MINIMUM_VELOCITY / absPixelsPerMS) / Math.log(FRICTION);
			}
			this.throwTo(targetHorizontalScrollPosition, NaN, duration / 1000);
		}

		/**
		 * @private
		 */
		protected function throwVertically(pixelsPerMS:Number):void
		{
			if(this._snapToPages)
			{
				const inchesPerSecond:Number = 1000 * pixelsPerMS / (DeviceCapabilities.dpi / Starling.contentScaleFactor);
				if(inchesPerSecond > this._minimumPageThrowVelocity)
				{
					var snappedPageVerticalScrollPosition:Number = roundDownToNearest(this._verticalScrollPosition, this.actualPageHeight);
				}
				else if(inchesPerSecond < -this._minimumPageThrowVelocity)
				{
					snappedPageVerticalScrollPosition = roundUpToNearest(this._verticalScrollPosition, this.actualPageHeight);
				}
				else
				{
					const lastPageHeight:Number = this._maxVerticalScrollPosition % this.actualPageHeight;
					var startOfLastPage:Number = this._maxVerticalScrollPosition - lastPageHeight;
					if(lastPageHeight < this.actualPageHeight && this._verticalScrollPosition >= startOfLastPage)
					{
						const lastPagePosition:Number = this._verticalScrollPosition - startOfLastPage;
						if(inchesPerSecond > this._minimumPageThrowVelocity)
						{
							snappedPageVerticalScrollPosition = startOfLastPage + roundDownToNearest(lastPagePosition, lastPageHeight);
						}
						else if(inchesPerSecond < -this._minimumPageThrowVelocity)
						{
							snappedPageVerticalScrollPosition = startOfLastPage + roundUpToNearest(lastPagePosition, lastPageHeight);
						}
						else
						{
							snappedPageVerticalScrollPosition = startOfLastPage + roundToNearest(lastPagePosition, lastPageHeight);
						}
					}
					else
					{
						snappedPageVerticalScrollPosition = roundToNearest(this._verticalScrollPosition, this.actualPageHeight);
					}
				}
				if(snappedPageVerticalScrollPosition < this._minVerticalScrollPosition)
				{
					snappedPageVerticalScrollPosition = this._minVerticalScrollPosition;
				}
				else if(snappedPageVerticalScrollPosition > this._maxVerticalScrollPosition)
				{
					snappedPageVerticalScrollPosition = this._maxVerticalScrollPosition;
				}
				if(snappedPageVerticalScrollPosition == this._maxVerticalScrollPosition)
				{
					var targetVerticalPageIndex:int = this._verticalPageCount - 1;
				}
				else
				{
					targetVerticalPageIndex = (snappedPageVerticalScrollPosition - this._minVerticalScrollPosition) / this.actualPageHeight;
				}
				this.throwToPage(-1, targetVerticalPageIndex, this._pageThrowDuration);
				return;
			}

			const absPixelsPerMS:Number = Math.abs(pixelsPerMS);
			if(absPixelsPerMS <= MINIMUM_VELOCITY)
			{
				this.finishScrollingVertically();
				return;
			}
			var targetVerticalScrollPosition:Number = this._verticalScrollPosition + (pixelsPerMS - MINIMUM_VELOCITY) / Math.log(FRICTION);
			if(targetVerticalScrollPosition < this._minVerticalScrollPosition || targetVerticalScrollPosition > this._maxVerticalScrollPosition)
			{
				var duration:Number = 0;
				targetVerticalScrollPosition = this._verticalScrollPosition;
				while(Math.abs(pixelsPerMS) > MINIMUM_VELOCITY)
				{
					targetVerticalScrollPosition -= pixelsPerMS;
					if(targetVerticalScrollPosition < this._minVerticalScrollPosition || targetVerticalScrollPosition > this._maxVerticalScrollPosition)
					{
						if(this._hasElasticEdges)
						{
							pixelsPerMS *= FRICTION * EXTRA_FRICTION;
						}
						else
						{
							if(targetVerticalScrollPosition < this._minVerticalScrollPosition)
							{
								targetVerticalScrollPosition = this._minVerticalScrollPosition;
							}
							else if(targetVerticalScrollPosition > this._maxVerticalScrollPosition)
							{
								targetVerticalScrollPosition = this._maxVerticalScrollPosition;
							}
							duration++;
							break;
						}
					}
					else
					{
						pixelsPerMS *= FRICTION;
					}
					duration++;
				}
			}
			else
			{
				duration = Math.log(MINIMUM_VELOCITY / absPixelsPerMS) / Math.log(FRICTION);
			}
			this.throwTo(NaN, targetVerticalScrollPosition, duration / 1000);
		}

		/**
		 * @private
		 */
		protected function hideHorizontalScrollBar(delay:Number = 0):void
		{
			if(!this.horizontalScrollBar || this._scrollBarDisplayMode != SCROLL_BAR_DISPLAY_MODE_FLOAT || this._horizontalScrollBarHideTween)
			{
				return;
			}
			if(this.horizontalScrollBar.alpha == 0)
			{
				return;
			}
			if(this._hideScrollBarAnimationDuration == 0 && delay == 0)
			{
				this.horizontalScrollBar.alpha = 0;
			}
			else
			{
				this._horizontalScrollBarHideTween = new Tween(this.horizontalScrollBar, this._hideScrollBarAnimationDuration, this._hideScrollBarAnimationEase);
				this._horizontalScrollBarHideTween.fadeTo(0);
				this._horizontalScrollBarHideTween.delay = delay;
				this._horizontalScrollBarHideTween.onComplete = horizontalScrollBarHideTween_onComplete;
				Starling.juggler.add(this._horizontalScrollBarHideTween);
			}
		}

		/**
		 * @private
		 */
		protected function hideVerticalScrollBar(delay:Number = 0):void
		{
			if(!this.verticalScrollBar || this._scrollBarDisplayMode != SCROLL_BAR_DISPLAY_MODE_FLOAT || this._verticalScrollBarHideTween)
			{
				return;
			}
			if(this.verticalScrollBar.alpha == 0)
			{
				return;
			}
			if(this._hideScrollBarAnimationDuration == 0 && delay == 0)
			{
				this.verticalScrollBar.alpha = 0;
			}
			else
			{
				this._verticalScrollBarHideTween = new Tween(this.verticalScrollBar, this._hideScrollBarAnimationDuration, this._hideScrollBarAnimationEase);
				this._verticalScrollBarHideTween.fadeTo(0);
				this._verticalScrollBarHideTween.delay = delay;
				this._verticalScrollBarHideTween.onComplete = verticalScrollBarHideTween_onComplete;
				Starling.juggler.add(this._verticalScrollBarHideTween);
			}
		}

		/**
		 * @private
		 */
		protected function revealHorizontalScrollBar():void
		{
			if(!this.horizontalScrollBar || this._scrollBarDisplayMode != SCROLL_BAR_DISPLAY_MODE_FLOAT)
			{
				return;
			}
			if(this._horizontalScrollBarHideTween)
			{
				Starling.juggler.remove(this._horizontalScrollBarHideTween);
				this._horizontalScrollBarHideTween = null;
			}
			this.horizontalScrollBar.alpha = 1;
		}

		/**
		 * @private
		 */
		protected function revealVerticalScrollBar():void
		{
			if(!this.verticalScrollBar || this._scrollBarDisplayMode != SCROLL_BAR_DISPLAY_MODE_FLOAT)
			{
				return;
			}
			if(this._verticalScrollBarHideTween)
			{
				Starling.juggler.remove(this._verticalScrollBarHideTween);
				this._verticalScrollBarHideTween = null;
			}
			this.verticalScrollBar.alpha = 1;
		}

		/**
		 * If scrolling hasn't already started, prepares the scroller to scroll
		 * and dispatches <code>FeathersEventType.SCROLL_START</code>.
		 */
		protected function startScroll():void
		{
			if(this._isScrolling)
			{
				return;
			}
			this._isScrolling = true;
			if(this._touchBlocker)
			{
				this._touchBlocker.visible = true;
			}
			this.dispatchEventWith(FeathersEventType.SCROLL_START);
		}

		/**
		 * Prepares the scroller for normal interaction and dispatches
		 * <code>FeathersEventType.SCROLL_COMPLETE</code>.
		 */
		protected function completeScroll():void
		{
			if(!this._isScrolling || this._verticalAutoScrollTween || this._horizontalAutoScrollTween ||
				this._isDraggingHorizontally || this._isDraggingVertically ||
				this._horizontalScrollBarIsScrolling || this._verticalScrollBarIsScrolling)
			{
				return;
			}
			this._isScrolling = false;
			if(this._touchBlocker)
			{
				this._touchBlocker.visible = false;
			}
			this.hideHorizontalScrollBar();
			this.hideVerticalScrollBar();
			//we validate to ensure that the final Event.SCROLL
			//dispatched before FeathersEventType.SCROLL_COMPLETE
			this.validate();
			this.dispatchEventWith(FeathersEventType.SCROLL_COMPLETE);
		}

		/**
		 * Scrolls to a pending scroll position, if required.
		 */
		protected function handlePendingScroll():void
		{
			if(!isNaN(this.pendingHorizontalScrollPosition) || !isNaN(this.pendingVerticalScrollPosition))
			{
				this.throwTo(this.pendingHorizontalScrollPosition, this.pendingVerticalScrollPosition, this.pendingScrollDuration);
				this.pendingHorizontalScrollPosition = NaN;
				this.pendingVerticalScrollPosition = NaN;
			}
			if(this.pendingHorizontalPageIndex >= 0 || this.pendingVerticalPageIndex >= 0)
			{
				this.throwToPage(this.pendingHorizontalPageIndex, this.pendingVerticalPageIndex, this.pendingScrollDuration);
				this.pendingHorizontalPageIndex = -1;
				this.pendingVerticalPageIndex = -1;
			}
		}

		/**
		 * @private
		 */
		protected function handlePendingRevealScrollBars():void
		{
			if(!this.isScrollBarRevealPending || this._scrollBarDisplayMode != SCROLL_BAR_DISPLAY_MODE_FLOAT)
			{
				return;
			}
			this.revealHorizontalScrollBar();
			this.revealVerticalScrollBar();
			this.hideHorizontalScrollBar(this._revealScrollBarsDuration);
			this.hideVerticalScrollBar(this._revealScrollBarsDuration);
		}

		/**
		 * @private
		 */
		protected function viewPort_resizeHandler(event:Event):void
		{
			if(this.ignoreViewPortResizing ||
				(this._viewPort.width == this._lastViewPortWidth && this._viewPort.height == this._lastViewPortHeight))
			{
				return;
			}
			this._lastViewPortWidth = this._viewPort.width;
			this._lastViewPortHeight = this._viewPort.height;
			if(this._isValidating)
			{
				this._hasViewPortBoundsChanged = true;
			}
			else
			{
				this.invalidate(INVALIDATION_FLAG_SIZE);
			}
		}

		/**
		 * @private
		 */
		protected function childProperties_onChange(proxy:PropertyProxy, name:String):void
		{
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected function verticalScrollBar_changeHandler(event:Event):void
		{
			this.verticalScrollPosition = this.verticalScrollBar.value;
		}

		/**
		 * @private
		 */
		protected function horizontalScrollBar_changeHandler(event:Event):void
		{
			this.horizontalScrollPosition = this.horizontalScrollBar.value;
		}

		/**
		 * @private
		 */
		protected function horizontalScrollBar_beginInteractionHandler(event:Event):void
		{
			this._horizontalScrollBarIsScrolling = true;
			this.dispatchEventWith(FeathersEventType.BEGIN_INTERACTION);
			this.startScroll();
		}

		/**
		 * @private
		 */
		protected function horizontalScrollBar_endInteractionHandler(event:Event):void
		{
			this._horizontalScrollBarIsScrolling = false;
			this.dispatchEventWith(FeathersEventType.END_INTERACTION);
			this.completeScroll();
		}

		/**
		 * @private
		 */
		protected function verticalScrollBar_beginInteractionHandler(event:Event):void
		{
			this._verticalScrollBarIsScrolling = true;
			this.dispatchEventWith(FeathersEventType.BEGIN_INTERACTION);
			this.startScroll();
		}

		/**
		 * @private
		 */
		protected function verticalScrollBar_endInteractionHandler(event:Event):void
		{
			this._verticalScrollBarIsScrolling = false;
			this.dispatchEventWith(FeathersEventType.END_INTERACTION);
			this.completeScroll();
		}

		/**
		 * @private
		 */
		protected function horizontalAutoScrollTween_onComplete():void
		{
			this._horizontalAutoScrollTween = null;
			this.finishScrollingHorizontally();
		}

		/**
		 * @private
		 */
		protected function verticalAutoScrollTween_onComplete():void
		{
			this._verticalAutoScrollTween = null;
			this.finishScrollingVertically();
		}

		/**
		 * @private
		 */
		protected function horizontalScrollBarHideTween_onComplete():void
		{
			this._horizontalScrollBarHideTween = null;
		}

		/**
		 * @private
		 */
		protected function verticalScrollBarHideTween_onComplete():void
		{
			this._verticalScrollBarHideTween = null;
		}

		/**
		 * @private
		 */
		protected function scroller_touchHandler(event:TouchEvent):void
		{
			if(!this._isEnabled)
			{
				this._touchPointID = -1;
				return;
			}
			if(this._touchPointID >= 0)
			{
				return;
			}

			//any began touch is okay here. we don't need to check all touches.
			const touch:Touch = event.getTouch(this, TouchPhase.BEGAN);
			if(!touch)
			{
				return;
			}

			if(this._interactionMode == INTERACTION_MODE_TOUCH_AND_SCROLL_BARS &&
				(event.interactsWith(DisplayObject(this.horizontalScrollBar)) || event.interactsWith(DisplayObject(this.verticalScrollBar))))
			{
				return;
			}

			touch.getLocation(this, HELPER_POINT);
			var touchX:Number = HELPER_POINT.x;
			var touchY:Number = HELPER_POINT.y;
			if(touchX < this._leftViewPortOffset || touchY < this._topViewPortOffset ||
				touchX >= this.actualWidth - this._rightViewPortOffset ||
				touchY >= this.actualHeight - this._bottomViewPortOffset)
			{
				return;
			}

			var exclusiveTouch:ExclusiveTouch = ExclusiveTouch.forStage(this.stage);
			if(exclusiveTouch.getClaim(touch.id))
			{
				//already claimed
				return;
			}

			//if the scroll policy is off, we shouldn't stop this animation
			if(this._horizontalAutoScrollTween && this._horizontalScrollPolicy != Scroller.SCROLL_POLICY_OFF)
			{
				Starling.juggler.remove(this._horizontalAutoScrollTween);
				this._horizontalAutoScrollTween = null;
			}
			if(this._verticalAutoScrollTween && this._verticalScrollPolicy != Scroller.SCROLL_POLICY_OFF)
			{
				Starling.juggler.remove(this._verticalAutoScrollTween);
				this._verticalAutoScrollTween = null;
			}

			this._touchPointID = touch.id;
			this._velocityX = 0;
			this._velocityY = 0;
			this._previousVelocityX.length = 0;
			this._previousVelocityY.length = 0;
			this._previousTouchTime = getTimer();
			this._previousTouchX = this._startTouchX = this._currentTouchX = touchX;
			this._previousTouchY = this._startTouchY = this._currentTouchY = touchY;
			this._startHorizontalScrollPosition = this._horizontalScrollPosition;
			this._startVerticalScrollPosition = this._verticalScrollPosition;
			this._isScrollingStopped = false;

//			this.addEventListener(Event.ENTER_FRAME, enterFrameHandler);
			
			Starling.juggler.add(this);

			//we need to listen on the stage because if we scroll the bottom or
			//right edge past the top of the scroller, it gets stuck and we stop
			//receiving touch events for "this".
			this.stage.addEventListener(TouchEvent.TOUCH, stage_touchHandler);

			exclusiveTouch.addEventListener(Event.CHANGE, exclusiveTouch_changeHandler);
		}

		/**
		 * @private
		 */
		protected function enterFrameHandler(event:Event=null):void
		{
			if(this._isScrollingStopped)
			{
				return;
			}
			const now:int = getTimer();
			const timeOffset:int = now - this._previousTouchTime;
			if(timeOffset > 0)
			{
				//we're keeping previous velocity updates to improve accuracy
				this._previousVelocityX[this._previousVelocityX.length] = this._velocityX;
				if(this._previousVelocityX.length > MAXIMUM_SAVED_VELOCITY_COUNT)
				{
					this._previousVelocityX.shift();
				}
				this._previousVelocityY[this._previousVelocityY.length] = this._velocityY;
				if(this._previousVelocityY.length > MAXIMUM_SAVED_VELOCITY_COUNT)
				{
					this._previousVelocityY.shift();
				}
				this._velocityX = (this._currentTouchX - this._previousTouchX) / timeOffset;
				this._velocityY = (this._currentTouchY - this._previousTouchY) / timeOffset;
				this._previousTouchTime = now;
				this._previousTouchX = this._currentTouchX;
				this._previousTouchY = this._currentTouchY;
			}
			const horizontalInchesMoved:Number = Math.abs(this._currentTouchX - this._startTouchX) / (DeviceCapabilities.dpi / Starling.contentScaleFactor);
			const verticalInchesMoved:Number = Math.abs(this._currentTouchY - this._startTouchY) / (DeviceCapabilities.dpi / Starling.contentScaleFactor);
			if((this._horizontalScrollPolicy == SCROLL_POLICY_ON ||
				(this._horizontalScrollPolicy == SCROLL_POLICY_AUTO && this._minHorizontalScrollPosition != this._maxHorizontalScrollPosition)) &&
				!this._isDraggingHorizontally && horizontalInchesMoved >= this._minimumDragDistance)
			{
				if(this.horizontalScrollBar)
				{
					this.revealHorizontalScrollBar();
				}
				this._startTouchX = this._currentTouchX;
				this._startHorizontalScrollPosition = this._horizontalScrollPosition;
				this._isDraggingHorizontally = true;
				//if we haven't already started dragging in the other direction,
				//we need to dispatch the event that says we're starting.
				if(!this._isDraggingVertically)
				{
					this.dispatchEventWith(FeathersEventType.BEGIN_INTERACTION);
					var exclusiveTouch:ExclusiveTouch = ExclusiveTouch.forStage(this.stage);
					exclusiveTouch.removeEventListener(Event.CHANGE, exclusiveTouch_changeHandler);
					exclusiveTouch.claimTouch(this._touchPointID, this);
					this.startScroll();
				}
			}
			if((this._verticalScrollPolicy == SCROLL_POLICY_ON ||
				(this._verticalScrollPolicy == SCROLL_POLICY_AUTO && this._minVerticalScrollPosition != this._maxVerticalScrollPosition)) &&
				!this._isDraggingVertically && verticalInchesMoved >= this._minimumDragDistance)
			{
				if(this.verticalScrollBar)
				{
					this.revealVerticalScrollBar();
				}
				this._startTouchY = this._currentTouchY;
				this._startVerticalScrollPosition = this._verticalScrollPosition;
				this._isDraggingVertically = true;
				if(!this._isDraggingHorizontally)
				{
					exclusiveTouch = ExclusiveTouch.forStage(this.stage);
					exclusiveTouch.removeEventListener(Event.CHANGE, exclusiveTouch_changeHandler);
					exclusiveTouch.claimTouch(this._touchPointID, this);
					this.dispatchEventWith(FeathersEventType.BEGIN_INTERACTION);
					this.startScroll();
				}
			}
			if(this._isDraggingHorizontally && !this._horizontalAutoScrollTween)
			{
				this.updateHorizontalScrollFromTouchPosition(this._currentTouchX);
			}
			if(this._isDraggingVertically && !this._verticalAutoScrollTween)
			{
				this.updateVerticalScrollFromTouchPosition(this._currentTouchY);
			}
		}

		/**
		 * @private
		 */
		protected function stage_touchHandler(event:TouchEvent):void
		{
			var touch:Touch = event.getTouch(this.stage, null, this._touchPointID);
			if(!touch)
			{
				return;
			}

			if(touch.phase == TouchPhase.MOVED)
			{
				//we're saving these to use in the enter frame handler because
				//that provides a longer time offset
				touch.getLocation(this, HELPER_POINT);
				this._currentTouchX = HELPER_POINT.x;
				this._currentTouchY = HELPER_POINT.y;
			}
			else if(touch.phase == TouchPhase.ENDED)
			{
				if(!this._isDraggingHorizontally && !this._isDraggingVertically)
				{
					ExclusiveTouch.forStage(this.stage).removeEventListener(Event.CHANGE, exclusiveTouch_changeHandler);
				}
//				this.removeEventListener(Event.ENTER_FRAME, enterFrameHandler);
				Starling.juggler.remove(this);
				
				this.stage.removeEventListener(TouchEvent.TOUCH, stage_touchHandler);
				this._touchPointID = -1;
				this.dispatchEventWith(FeathersEventType.END_INTERACTION);
				var isFinishingHorizontally:Boolean = false;
				var isFinishingVertically:Boolean = false;
				if(this._horizontalScrollPosition < this._minHorizontalScrollPosition || this._horizontalScrollPosition > this._maxHorizontalScrollPosition)
				{
					isFinishingHorizontally = true;
					this.finishScrollingHorizontally();
				}
				if(this._verticalScrollPosition < this._minVerticalScrollPosition || this._verticalScrollPosition > this._maxVerticalScrollPosition)
				{
					isFinishingVertically = true;
					this.finishScrollingVertically();
				}
				if(isFinishingHorizontally && isFinishingVertically)
				{
					return;
				}

				if(!isFinishingHorizontally && this._isDraggingHorizontally)
				{
					//take the average for more accuracy
					var sum:Number = this._velocityX * CURRENT_VELOCITY_WEIGHT;
					var velocityCount:int = this._previousVelocityX.length;
					var totalWeight:Number = CURRENT_VELOCITY_WEIGHT;
					for(var i:int = 0; i < velocityCount; i++)
					{
						var weight:Number = VELOCITY_WEIGHTS[i];
						sum += this._previousVelocityX.shift() * weight;
						totalWeight += weight;
					}
					this.throwHorizontally(sum / totalWeight);
				}
				else
				{
					this.hideHorizontalScrollBar();
				}

				if(!isFinishingVertically && this._isDraggingVertically)
				{
					sum = this._velocityY * CURRENT_VELOCITY_WEIGHT;
					velocityCount = this._previousVelocityY.length;
					totalWeight = CURRENT_VELOCITY_WEIGHT;
					for(i = 0; i < velocityCount; i++)
					{
						weight = VELOCITY_WEIGHTS[i];
						sum += this._previousVelocityY.shift() * weight;
						totalWeight += weight;
					}
					this.throwVertically(sum / totalWeight);
				}
				else
				{
					this.hideVerticalScrollBar();
				}
			}
		}

		/**
		 * @private
		 */
		protected function exclusiveTouch_changeHandler(event:Event, touchID:int):void
		{
			if(this._touchPointID < 0 || this._touchPointID != touchID || this._isDraggingHorizontally || this._isDraggingVertically)
			{
				return;
			}
			var exclusiveTouch:ExclusiveTouch = ExclusiveTouch.forStage(this.stage);
			if(exclusiveTouch.getClaim(touchID) == this)
			{
				return;
			}

			this._touchPointID = -1;
//			this.removeEventListener(Event.ENTER_FRAME, enterFrameHandler);
			Starling.juggler.remove(this);
			this.stage.removeEventListener(TouchEvent.TOUCH, stage_touchHandler);
			exclusiveTouch.removeEventListener(Event.CHANGE, exclusiveTouch_changeHandler);
			this.dispatchEventWith(FeathersEventType.END_INTERACTION);
		}

		/**
		 * @private
		 */
		protected function nativeStage_mouseWheelHandler(event:MouseEvent):void
		{
			if(!this._isEnabled)
			{
				this._touchPointID = -1;
				return;
			}
			if(this._maxVerticalScrollPosition == 0 || this._verticalScrollPolicy == SCROLL_POLICY_OFF)
			{
				return;
			}

			var nativeScaleFactor:Number = 1;
			if(Starling.current.supportHighResolutions)
			{
				nativeScaleFactor = Starling.current.nativeStage.contentsScaleFactor;
			}
			var starlingViewPort:Rectangle = Starling.current.viewPort;
			var scaleFactor:Number = nativeScaleFactor / Starling.contentScaleFactor;
			HELPER_POINT.x = (event.stageX - starlingViewPort.x) / scaleFactor;
			HELPER_POINT.y = (event.stageY - starlingViewPort.y) / scaleFactor;
			if(this.contains(this.stage.hitTest(HELPER_POINT, true)))
			{
				this.globalToLocal(HELPER_POINT, HELPER_POINT);
				var localMouseX:Number = HELPER_POINT.x;
				var localMouseY:Number = HELPER_POINT.y;
				if(localMouseX < this._leftViewPortOffset || localMouseY < this._topViewPortOffset ||
					localMouseX >= this.actualWidth - this._rightViewPortOffset ||
					localMouseY >= this.actualHeight - this._bottomViewPortOffset)
				{
					return;
				}
				this.revealVerticalScrollBar();
				var scrollStep:Number = this._verticalMouseWheelScrollStep;
				if(isNaN(scrollStep))
				{
					scrollStep = this.actualVerticalScrollStep;
				}
				var targetVerticalScrollPosition:Number = this._verticalScrollPosition - event.delta * scrollStep;
				if(targetVerticalScrollPosition < this._minVerticalScrollPosition)
				{
					targetVerticalScrollPosition = this._minVerticalScrollPosition;
				}
				else if(targetVerticalScrollPosition > this._maxVerticalScrollPosition)
				{
					targetVerticalScrollPosition = this._maxVerticalScrollPosition;
				}
				this.throwTo(NaN, targetVerticalScrollPosition, this._mouseWheelScrollDuration);
			}
		}
		
		public function updateScrollBar(index:int = 1):void
		{
			this._verticalScrollPosition -= -28.85714285714858
			var targetVerticalScrollPosition:Number = _verticalScrollPosition;
			if(targetVerticalScrollPosition < this._minVerticalScrollPosition)
			{
				targetVerticalScrollPosition = this._minVerticalScrollPosition;
			}
			else if(targetVerticalScrollPosition > this._maxVerticalScrollPosition)
			{
				this._maxVerticalScrollPosition = targetVerticalScrollPosition;
			}
			this.throwTo(NaN, targetVerticalScrollPosition, this._mouseWheelScrollDuration);
		}
		
 


		/**
		 * @private
		 */
		protected function nativeStage_orientationChangeHandler(event:flash.events.Event):void
		{
			if(this._touchPointID < 0)
			{
				return;
			}
			this._startTouchX = this._previousTouchX = this._currentTouchX;
			this._startTouchY = this._previousTouchY = this._currentTouchY;
			this._startHorizontalScrollPosition = this._horizontalScrollPosition;
			this._startVerticalScrollPosition = this._verticalScrollPosition;
		}

		/**
		 * @private
		 */
		protected function horizontalScrollBar_touchHandler(event:TouchEvent):void
		{
			if(!this._isEnabled)
			{
				this._horizontalScrollBarTouchPointID = -1;
				return;
			}

			const displayHorizontalScrollBar:DisplayObject = DisplayObject(event.currentTarget);
			if(this._horizontalScrollBarTouchPointID >= 0)
			{
				var touch:Touch = event.getTouch(displayHorizontalScrollBar, TouchPhase.ENDED, this._horizontalScrollBarTouchPointID);
				if(!touch)
				{
					return;
				}

				this._horizontalScrollBarTouchPointID = -1;
				touch.getLocation(displayHorizontalScrollBar, HELPER_POINT);
				const isInBounds:Boolean = this.horizontalScrollBar.hitTest(HELPER_POINT, true) != null;
				if(!isInBounds)
				{
					this.hideHorizontalScrollBar();
				}
			}
			else
			{
				touch = event.getTouch(displayHorizontalScrollBar, TouchPhase.BEGAN);
				if(touch)
				{
					this._horizontalScrollBarTouchPointID = touch.id;
					return;
				}
				touch = event.getTouch(displayHorizontalScrollBar, TouchPhase.HOVER);
				if(touch)
				{
					this.revealHorizontalScrollBar();
					return;
				}

				//end hover
				this.hideHorizontalScrollBar();
			}
		}

		/**
		 * @private
		 */
		protected function verticalScrollBar_touchHandler(event:TouchEvent):void
		{
			if(!this._isEnabled)
			{
				this._verticalScrollBarTouchPointID = -1;
				return;
			}

			const displayVerticalScrollBar:DisplayObject = DisplayObject(event.currentTarget);
			if(this._verticalScrollBarTouchPointID >= 0)
			{
				var touch:Touch = event.getTouch(displayVerticalScrollBar, TouchPhase.ENDED, this._verticalScrollBarTouchPointID);
				if(!touch)
				{
					return;
				}

				this._verticalScrollBarTouchPointID = -1;
				touch.getLocation(displayVerticalScrollBar, HELPER_POINT);
				const isInBounds:Boolean = this.verticalScrollBar.hitTest(HELPER_POINT, true) != null;
				if(!isInBounds)
				{
					this.hideVerticalScrollBar();
				}
			}
			else
			{
				touch = event.getTouch(displayVerticalScrollBar, TouchPhase.BEGAN);
				if(touch)
				{
					this._verticalScrollBarTouchPointID = touch.id;
					return;
				}
				touch = event.getTouch(displayVerticalScrollBar, TouchPhase.HOVER);
				if(touch)
				{
					this.revealVerticalScrollBar();
					return;
				}

				//end hover
				this.hideVerticalScrollBar();
			}
		}

		/**
		 * @private
		 */
		protected function scroller_addedToStageHandler(event:Event):void
		{
			Starling.current.nativeStage.addEventListener(MouseEvent.MOUSE_WHEEL, nativeStage_mouseWheelHandler, false, 0, true);
			Starling.current.nativeStage.addEventListener("orientationChange", nativeStage_orientationChangeHandler, false, 0, true);
		}

		/**
		 * @private
		 */
		protected function scroller_removedFromStageHandler(event:Event):void
		{
			Starling.current.nativeStage.removeEventListener(MouseEvent.MOUSE_WHEEL, nativeStage_mouseWheelHandler);
			Starling.current.nativeStage.removeEventListener("orientationChange", nativeStage_orientationChangeHandler);
			if(this._touchPointID >= 0)
			{
				var exclusiveTouch:ExclusiveTouch = ExclusiveTouch.forStage(this.stage);
				exclusiveTouch.removeEventListener(Event.CHANGE, exclusiveTouch_changeHandler);
			}
			this._touchPointID = -1;
			this._horizontalScrollBarTouchPointID = -1;
			this._verticalScrollBarTouchPointID = -1;
			this._velocityX = 0;
			this._velocityY = 0;
			this._previousVelocityX.length = 0;
			this._previousVelocityY.length = 0;
			this._horizontalScrollBarIsScrolling = false;
			this._verticalScrollBarIsScrolling = false;
//			this.removeEventListener(Event.ENTER_FRAME, enterFrameHandler);
			Starling.juggler.remove(this);
			this.stage.removeEventListener(TouchEvent.TOUCH, stage_touchHandler);
			if(this._verticalAutoScrollTween)
			{
				Starling.juggler.remove(this._verticalAutoScrollTween);
				this._verticalAutoScrollTween = null;
			}
			if(this._horizontalAutoScrollTween)
			{
				Starling.juggler.remove(this._horizontalAutoScrollTween);
				this._horizontalAutoScrollTween = null;
			}

			//if we stopped the animation while the list was outside the scroll
			//bounds, then let's account for that
			const oldHorizontalScrollPosition:Number = this._horizontalScrollPosition;
			const oldVerticalScrollPosition:Number = this._verticalScrollPosition;
			if(this._horizontalScrollPosition < this._minHorizontalScrollPosition)
			{
				this._horizontalScrollPosition = this._minHorizontalScrollPosition;
			}
			else if(this._horizontalScrollPosition > this._maxHorizontalScrollPosition)
			{
				this._horizontalScrollPosition = this._maxHorizontalScrollPosition;
			}
			if(this._verticalScrollPosition < this._minVerticalScrollPosition)
			{
				this._verticalScrollPosition = this._minVerticalScrollPosition;
			}
			else if(this._verticalScrollPosition > this._maxVerticalScrollPosition)
			{
				this._verticalScrollPosition = this._maxVerticalScrollPosition;
			}
			if(oldHorizontalScrollPosition != this._horizontalScrollPosition ||
				oldVerticalScrollPosition != this._verticalScrollPosition)
			{
				this.dispatchEventWith(Event.SCROLL);
			}
		}
	}
}