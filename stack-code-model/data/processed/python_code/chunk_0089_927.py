/*
Feathers
Copyright 2012-2013 Joshua Tynjala. All Rights Reserved.

This program is free software. You can redistribute and/or modify it in
accordance with the terms of the accompanying license agreement.
*/
package feathers.controls
{
	import feathers.core.FeathersControl;
	import feathers.core.PropertyProxy;
	import feathers.core.ToggleGroup;
	import feathers.data.ListCollection;
	import feathers.events.CollectionEventType;
	import feathers.layout.HorizontalLayout;
	import feathers.layout.LayoutBoundsResult;
	import feathers.layout.VerticalLayout;
	import feathers.layout.ViewPortBounds;

	import starling.display.DisplayObject;
	import starling.events.Event;

	/**
	 * Dispatched when the selected tab changes.
	 *
	 * @eventType starling.events.Event.CHANGE
	 */
	[Event(name="change",type="starling.events.Event")]

	[DefaultProperty("dataProvider")]
	/**
	 * A line of tabs (vertical or horizontal), where one may be selected at a
	 * time.
	 *
	 * <p>The following example sets the data provider, selects the second tab,
	 * and listens for when the selection changes:</p>
	 *
	 * <listing version="3.0">
	 * var tabs:TabBar = new TabBar();
	 * tabs.dataProvider = new ListCollection(
	 * [
	 *     { label: "One" },
	 *     { label: "Two" },
	 *     { label: "Three" },
	 * ]);
	 * tabs.selectedIndex = 1;
	 * tabs.addEventListener( Event.CHANGE, tabs_changeHandler );
	 * this.addChild( tabs );</listing>
	 *
	 * @see http://wiki.starling-framework.org/feathers/tab-bar
	 */
	public class TabBar extends FeathersControl
	{
		/**
		 * @private
		 */
		protected static const INVALIDATION_FLAG_TAB_FACTORY:String = "tabFactory";

		/**
		 * @private
		 */
		protected static const NOT_PENDING_INDEX:int = -2;

		/**
		 * @private
		 */
		private static const DEFAULT_TAB_FIELDS:Vector.<String> = new <String>
		[
			"defaultIcon",
			"upIcon",
			"downIcon",
			"hoverIcon",
			"disabledIcon",
			"defaultSelectedIcon",
			"selectedUpIcon",
			"selectedDownIcon",
			"selectedHoverIcon",
			"selectedDisabledIcon"
		];

		/**
		 * The tabs are displayed in order from left to right.
		 *
		 * @see #direction
		 */
		public static const DIRECTION_HORIZONTAL:String = "horizontal";

		/**
		 * The tabs are displayed in order from top to bottom.
		 *
		 * @see #direction
		 */
		public static const DIRECTION_VERTICAL:String = "vertical";

		/**
		 * The tabs will be aligned horizontally to the left edge of the tab
		 * bar.
		 *
		 * @see #horizontalAlign
		 */
		public static const HORIZONTAL_ALIGN_LEFT:String = "left";

		/**
		 * The tabs will be aligned horizontally to the center of the tab bar.
		 *
		 * @see #horizontalAlign
		 */
		public static const HORIZONTAL_ALIGN_CENTER:String = "center";

		/**
		 * The tabs will be aligned horizontally to the right edge of the tab
		 * bar.
		 *
		 * @see #horizontalAlign
		 */
		public static const HORIZONTAL_ALIGN_RIGHT:String = "right";

		/**
		 * If the direction is vertical, each tab will fill the entire width of
		 * the tab bar, and if the direction is horizontal, the alignment will
		 * behave the same as <code>HORIZONTAL_ALIGN_LEFT</code>.
		 *
		 * @see #horizontalAlign
		 * @see #direction
		 */
		public static const HORIZONTAL_ALIGN_JUSTIFY:String = "justify";

		/**
		 * The tabs will be aligned vertically to the top edge of the tab bar.
		 */
		public static const VERTICAL_ALIGN_TOP:String = "top";

		/**
		 * The tabs will be aligned vertically to the middle of the tab bar.
		 *
		 * @see #verticalAlign
		 */
		public static const VERTICAL_ALIGN_MIDDLE:String = "middle";

		/**
		 * The tabs will be aligned vertically to the bottom edge of the tab
		 * bar.
		 *
		 * @see #verticalAlign
		 */
		public static const VERTICAL_ALIGN_BOTTOM:String = "bottom";

		/**
		 * If the direction is horizontal, each tab will fill the entire height
		 * of the tab bar. If the direction is vertical, the alignment will
		 * behave the same as <code>VERTICAL_ALIGN_TOP</code>.
		 *
		 * @see #verticalAlign
		 * @see #direction
		 */
		public static const VERTICAL_ALIGN_JUSTIFY:String = "justify";

		/**
		 * The default value added to the <code>nameList</code> of the tabs.
		 *
		 * @see feathers.core.IFeathersControl#nameList
		 */
		public static const DEFAULT_CHILD_NAME_TAB:String = "feathers-tab-bar-tab";

		/**
		 * @private
		 */
		protected static function defaultTabFactory():Button
		{
			return new Button();
		}

		/**
		 * Constructor.
		 */
		public function TabBar()
		{
		}

		/**
		 * The value added to the <code>nameList</code> of the tabs. This
		 * variable is <code>protected</code> so that sub-classes can customize
		 * the tab name in their constructors instead of using the default
		 * name defined by <code>DEFAULT_CHILD_NAME_TAB</code>.
		 *
		 * <p>To customize the tab name without subclassing, see
		 * <code>customTabName</code>.</p>
		 *
		 * @see #customTabName
		 * @see feathers.core.IFeathersControl#nameList
		 */
		protected var tabName:String = DEFAULT_CHILD_NAME_TAB;

		/**
		 * The value added to the <code>nameList</code> of the first tab. This
		 * variable is <code>protected</code> so that sub-classes can customize
		 * the first tab name in their constructors instead of using the default
		 * name defined by <code>DEFAULT_CHILD_NAME_TAB</code>.
		 *
		 * <p>To customize the first tab name without subclassing, see
		 * <code>customFirstTabName</code>.</p>
		 *
		 * @see #customFirstTabName
		 * @see feathers.core.IFeathersControl#nameList
		 */
		protected var firstTabName:String = DEFAULT_CHILD_NAME_TAB;

		/**
		 * The value added to the <code>nameList</code> of the last tab. This
		 * variable is <code>protected</code> so that sub-classes can customize
		 * the last tab name in their constructors instead of using the default
		 * name defined by <code>DEFAULT_CHILD_NAME_TAB</code>.
		 *
		 * <p>To customize the last tab name without subclassing, see
		 * <code>customLastTabName</code>.</p>
		 *
		 * @see #customLastTabName
		 * @see feathers.core.IFeathersControl#nameList
		 */
		protected var lastTabName:String = DEFAULT_CHILD_NAME_TAB;

		/**
		 * The toggle group.
		 */
		protected var toggleGroup:ToggleGroup;

		/**
		 * @private
		 */
		protected var activeFirstTab:Button;

		/**
		 * @private
		 */
		protected var inactiveFirstTab:Button;

		/**
		 * @private
		 */
		protected var activeLastTab:Button;

		/**
		 * @private
		 */
		protected var inactiveLastTab:Button;

		/**
		 * @private
		 */
		protected var _layoutItems:Vector.<DisplayObject> = new <DisplayObject>[];

		/**
		 * @private
		 */
		protected var activeTabs:Vector.<Button> = new <Button>[];

		/**
		 * @private
		 */
		protected var inactiveTabs:Vector.<Button> = new <Button>[];

		/**
		 * @private
		 */
		protected var _dataProvider:ListCollection;

		/**
		 * The collection of data to be displayed with tabs. The default
		 * <em>tab initializer</em> interprets this data to customize the tabs
		 * with various fields available to buttons, including the following:
		 *
		 * <ul>
		 *     <li>label</li>
		 *     <li>defaultIcon</li>
		 *     <li>upIcon</li>
		 *     <li>downIcon</li>
		 *     <li>hoverIcon</li>
		 *     <li>disabledIcon</li>
		 *     <li>defaultSelectedIcon</li>
		 *     <li>selectedUpIcon</li>
		 *     <li>selectedDownIcon</li>
		 *     <li>selectedHoverIcon</li>
		 *     <li>selectedDisabledIcon</li>
		 * </ul>
		 *
		 * <p>The following example passes in a data provider:</p>
		 *
		 * <listing version="3.0">
		 * list.dataProvider = new ListCollection(
		 * [
		 *     { label: "General", defaultIcon: new Image( generalTexture ) },
		 *     { label: "Security", defaultIcon: new Image( securityTexture ) },
		 *     { label: "Advanced", defaultIcon: new Image( advancedTexture ) },
		 * ]);</listing>
		 *
		 * @default null
		 *
		 * @see #tabInitializer
		 */
		public function get dataProvider():ListCollection
		{
			return this._dataProvider;
		}

		/**
		 * @private
		 */
		public function set dataProvider(value:ListCollection):void
		{
			if(this._dataProvider == value)
			{
				return;
			}
			var oldSelectedIndex:int = this.selectedIndex;
			var oldSelectedItem:Object = this.selectedItem;
			if(this._dataProvider)
			{
				this._dataProvider.removeEventListener(CollectionEventType.ADD_ITEM, dataProvider_addItemHandler);
				this._dataProvider.removeEventListener(CollectionEventType.REMOVE_ITEM, dataProvider_removeItemHandler);
				this._dataProvider.removeEventListener(CollectionEventType.REPLACE_ITEM, dataProvider_replaceItemHandler);
				this._dataProvider.removeEventListener(CollectionEventType.UPDATE_ITEM, dataProvider_updateItemHandler);
				this._dataProvider.removeEventListener(CollectionEventType.RESET, dataProvider_resetHandler);
			}
			this._dataProvider = value;
			if(this._dataProvider)
			{
				this._dataProvider.addEventListener(CollectionEventType.ADD_ITEM, dataProvider_addItemHandler);
				this._dataProvider.addEventListener(CollectionEventType.REMOVE_ITEM, dataProvider_removeItemHandler);
				this._dataProvider.addEventListener(CollectionEventType.REPLACE_ITEM, dataProvider_replaceItemHandler);
				this._dataProvider.addEventListener(CollectionEventType.UPDATE_ITEM, dataProvider_updateItemHandler);
				this._dataProvider.addEventListener(CollectionEventType.RESET, dataProvider_resetHandler);
			}
			if(!this._dataProvider || this._dataProvider.length == 0)
			{
				this.selectedIndex = -1;
			}
			else
			{
				this.selectedIndex = 0;
			}
			//this ensures that Event.CHANGE will dispatch for selectedItem
			//changing, even if selectedIndex has not changed.
			if(this.selectedIndex == oldSelectedIndex && this.selectedItem != oldSelectedItem)
			{
				this.dispatchEventWith(Event.CHANGE);
			}
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected var verticalLayout:VerticalLayout;

		/**
		 * @private
		 */
		protected var horizontalLayout:HorizontalLayout;

		/**
		 * @private
		 */
		protected var _viewPortBounds:ViewPortBounds = new ViewPortBounds();

		/**
		 * @private
		 */
		protected var _layoutResult:LayoutBoundsResult = new LayoutBoundsResult();

		/**
		 * @private
		 */
		protected var _direction:String = DIRECTION_HORIZONTAL;

		[Inspectable(type="String",enumeration="horizontal,vertical")]
		/**
		 * The tab bar layout is either vertical or horizontal.
		 *
		 * <p>In the following example, the tab bar's direction is set to
		 * vertical:</p>
		 *
		 * <listing version="3.0">
		 * tabs.direction = TabBar.DIRECTION_VERTICAL;</listing>
		 *
		 * @default TabBar.DIRECTION_HORIZONTAL
		 *
		 * @see #DIRECTION_HORIZONTAL
		 * @see #DIRECTION_VERTICAL
		 */
		public function get direction():String
		{
			return this._direction;
		}

		/**
		 * @private
		 */
		public function set direction(value:String):void
		{
			if(this._direction == value)
			{
				return;
			}
			this._direction = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _horizontalAlign:String = HORIZONTAL_ALIGN_JUSTIFY;

		[Inspectable(type="String",enumeration="left,center,right,justify")]
		/**
		 * Determines how the tabs are horizontally aligned within the bounds
		 * of the tab bar (on the x-axis).
		 *
		 * <p>The following example aligns the tabs to the left:</p>
		 *
		 * <listing version="3.0">
		 * tabs.horizontalAlign = TabBar.HORIZONTAL_ALIGN_LEFT;</listing>
		 *
		 * @default TabBar.HORIZONTAL_ALIGN_JUSTIFY
		 *
		 * @see #HORIZONTAL_ALIGN_LEFT
		 * @see #HORIZONTAL_ALIGN_CENTER
		 * @see #HORIZONTAL_ALIGN_RIGHT
		 * @see #HORIZONTAL_ALIGN_JUSTIFY
		 */
		public function get horizontalAlign():String
		{
			return this._horizontalAlign;
		}

		/**
		 * @private
		 */
		public function set horizontalAlign(value:String):void
		{
			if(this._horizontalAlign == value)
			{
				return;
			}
			this._horizontalAlign = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _verticalAlign:String = VERTICAL_ALIGN_JUSTIFY;

		[Inspectable(type="String",enumeration="top,middle,bottom,justify")]
		/**
		 * Determines how the tabs are vertically aligned within the bounds
		 * of the tab bar (on the y-axis).
		 *
		 * <p>The following example aligns the tabs to the top:</p>
		 *
		 * <listing version="3.0">
		 * tabs.verticalAlign = TabBar.VERTICAL_ALIGN_TOP;</listing>
		 *
		 * @default TabBar.VERTICAL_ALIGN_JUSTIFY
		 *
		 * @see #VERTICAL_ALIGN_TOP
		 * @see #VERTICAL_ALIGN_MIDDLE
		 * @see #VERTICAL_ALIGN_RIGHT
		 * @see #VERTICAL_ALIGN_JUSTIFY
		 */
		public function get verticalAlign():String
		{
			return this._verticalAlign;
		}

		/**
		 * @private
		 */
		public function set verticalAlign(value:String):void
		{
			if(this._verticalAlign == value)
			{
				return;
			}
			this._verticalAlign = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _distributeTabSizes:Boolean = true;

		/**
		 * If <code>true</code>, the tabs will be equally sized in the direction
		 * of the layout. In other words, if the tab bar is horizontal, each tab
		 * will have the same width, and if the tab bar is vertical, each tab
		 * will have the same height. If <code>false</code>, the tabs will be
		 * sized to their ideal dimensions.
		 *
		 * <p>The following example aligns the tabs to the middle without distributing them:</p>
		 *
		 * <listing version="3.0">
		 * tabs.direction = TabBar.DIRECTION_VERTICAL;
		 * tabs.verticalAlign = TabBar.VERTICAL_ALIGN_MIDDLE;
		 * tabs.distributeTabSizes = false;</listing>
		 *
		 * @default true
		 */
		public function get distributeTabSizes():Boolean
		{
			return this._distributeTabSizes;
		}

		/**
		 * @private
		 */
		public function set distributeTabSizes(value:Boolean):void
		{
			if(this._distributeTabSizes == value)
			{
				return;
			}
			this._distributeTabSizes = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _gap:Number = 0;

		/**
		 * Space, in pixels, between tabs.
		 *
		 * <p>In the following example, the tab bar's gap is set to 20 pixels:</p>
		 *
		 * <listing version="3.0">
		 * tabs.gap = 20;</listing>
		 *
		 * @default 0
		 */
		public function get gap():Number
		{
			return this._gap;
		}

		/**
		 * @private
		 */
		public function set gap(value:Number):void
		{
			if(this._gap == value)
			{
				return;
			}
			this._gap = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _firstGap:Number = NaN;

		/**
		 * Space, in pixels, between the first two tabs. If <code>NaN</code>,
		 * the default <code>gap</code> property will be used.
		 *
		 * <p>The following example sets the gap between the first and second
		 * tab to a different value than the standard gap:</p>
		 *
		 * <listing version="3.0">
		 * tabs.firstGap = 30;
		 * tabs.gap = 20;</listing>
		 *
		 * @default NaN
		 *
		 * @see #gap
		 * @see #lastGap
		 */
		public function get firstGap():Number
		{
			return this._firstGap;
		}

		/**
		 * @private
		 */
		public function set firstGap(value:Number):void
		{
			if(this._firstGap == value)
			{
				return;
			}
			this._firstGap = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _lastGap:Number = NaN;

		/**
		 * Space, in pixels, between the last two tabs. If <code>NaN</code>,
		 * the default <code>gap</code> property will be used.
		 *
		 * <p>The following example sets the gap between the last and next to last
		 * tab to a different value than the standard gap:</p>
		 *
		 * <listing version="3.0">
		 * tabs.lastGap = 30;
		 * tabs.gap = 20;</listing>
		 *
		 * @default NaN
		 *
		 * @see #gap
		 * @see #firstGap
		 */
		public function get lastGap():Number
		{
			return this._lastGap;
		}

		/**
		 * @private
		 */
		public function set lastGap(value:Number):void
		{
			if(this._lastGap == value)
			{
				return;
			}
			this._lastGap = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * Quickly sets all padding properties to the same value. The
		 * <code>padding</code> getter always returns the value of
		 * <code>paddingTop</code>, but the other padding values may be
		 * different.
		 *
		 * <p>In the following example, the padding of all sides of the tab bar
		 * is set to 20 pixels:</p>
		 *
		 * <listing version="3.0">
		 * tabs.padding = 20;</listing>
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
		 * The minimum space, in pixels, between the tab bar's top edge and the
		 * tabs.
		 *
		 * <p>In the following example, the padding on the top edge of the
		 * tab bar is set to 20 pixels:</p>
		 *
		 * <listing version="3.0">
		 * tabs.paddingTop = 20;</listing>
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
		 * The minimum space, in pixels, between the tab bar's right edge and
		 * the tabs.
		 *
		 * <p>In the following example, the padding on the right edge of the
		 * tab bar is set to 20 pixels:</p>
		 *
		 * <listing version="3.0">
		 * tabs.paddingRight = 20;</listing>
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
		 * The minimum space, in pixels, between the tab bar's bottom edge and
		 * the tabs.
		 *
		 * <p>In the following example, the padding on the bottom edge of the
		 * tab bar is set to 20 pixels:</p>
		 *
		 * <listing version="3.0">
		 * tabs.paddingBottom = 20;</listing>
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
		 * The minimum space, in pixels, between the tab bar's left edge and the
		 * tabs.
		 *
		 * <p>In the following example, the padding on the left edge of the
		 * tab bar is set to 20 pixels:</p>
		 *
		 * <listing version="3.0">
		 * tabs.paddingLeft = 20;</listing>
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
		protected var _tabFactory:Function = defaultTabFactory;

		/**
		 * Creates a new tab. A tab must be an instance of <code>Button</code>.
		 * This factory can be used to change properties on the tabs when they
		 * are first created. For instance, if you are skinning Feathers
		 * components without a theme, you might use this factory to set skins
		 * and other styles on a tab.
		 *
		 * <p>This function is expected to have the following signature:</p>
		 *
		 * <pre>function():Button</pre>
		 *
		 * <p>In the following example, a custom tab factory is passed to the
		 * tab bar:</p>
		 *
		 * <listing version="3.0">
		 * tabs.tabFactory = function():Button
		 * {
		 *     var tab:Button = new Button();
		 *     tab.defaultSkin = new Image( upTexture );
		 *     tab.defaultSelectedSkin = new Image( selectedTexture );
		 *     tab.downSkin = new Image( downTexture );
		 *     return tab;
		 * };</listing>
		 *
		 * @default null
		 *
		 * @see feathers.controls.Button
		 * @see #firstTabFactory
		 * @see #lastTabFactory
		 */
		public function get tabFactory():Function
		{
			return this._tabFactory;
		}

		/**
		 * @private
		 */
		public function set tabFactory(value:Function):void
		{
			if(this._tabFactory == value)
			{
				return;
			}
			this._tabFactory = value;
			this.invalidate(INVALIDATION_FLAG_TAB_FACTORY);
		}

		/**
		 * @private
		 */
		protected var _firstTabFactory:Function;

		/**
		 * Creates a new first tab. If the <code>firstTabFactory</code> is
		 * <code>null</code>, then the tab bar will use the <code>tabFactory</code>.
		 * The first tab must be an instance of <code>Button</code>. This
		 * factory can be used to change properties on the first tab when it
		 * is first created. For instance, if you are skinning Feathers
		 * components without a theme, you might use this factory to set skins
		 * and other styles on the first tab.
		 *
		 * <p>This function is expected to have the following signature:</p>
		 *
		 * <pre>function():Button</pre>
		 *
		 * <p>In the following example, a custom first tab factory is passed to the
		 * tab bar:</p>
		 *
		 * <listing version="3.0">
		 * tabs.firstTabFactory = function():Button
		 * {
		 *     var tab:Button = new Button();
		 *     tab.defaultSkin = new Image( upTexture );
		 *     tab.defaultSelectedSkin = new Image( selectedTexture );
		 *     tab.downSkin = new Image( downTexture );
		 *     return tab;
		 * };</listing>
		 *
		 * @default null
		 *
		 * @see feathers.controls.Button
		 * @see #tabFactory
		 * @see #lastTabFactory
		 */
		public function get firstTabFactory():Function
		{
			return this._firstTabFactory;
		}

		/**
		 * @private
		 */
		public function set firstTabFactory(value:Function):void
		{
			if(this._firstTabFactory == value)
			{
				return;
			}
			this._firstTabFactory = value;
			this.invalidate(INVALIDATION_FLAG_TAB_FACTORY);
		}

		/**
		 * @private
		 */
		protected var _lastTabFactory:Function;

		/**
		 * Creates a new last tab. If the <code>lastTabFactory</code> is
		 * <code>null</code>, then the tab bar will use the <code>tabFactory</code>.
		 * The last tab must be an instance of <code>Button</code>. This
		 * factory can be used to change properties on the last tab when it
		 * is first created. For instance, if you are skinning Feathers
		 * components without a theme, you might use this factory to set skins
		 * and other styles on the last tab.
		 *
		 * <p>This function is expected to have the following signature:</p>
		 *
		 * <pre>function():Button</pre>
		 *
		 * <p>In the following example, a custom last tab factory is passed to the
		 * tab bar:</p>
		 *
		 * <listing version="3.0">
		 * tabs.lastTabFactory = function():Button
		 * {
		 *     var tab:Button = new Button();
		 *     tab.defaultSkin = new Image( upTexture );
		 *     tab.defaultSelectedSkin = new Image( selectedTexture );
		 *     tab.downSkin = new Image( downTexture );
		 *     return tab;
		 * };</listing>
		 *
		 * @default null
		 *
		 * @see feathers.controls.Button
		 * @see #tabFactory
		 * @see #firstTabFactory
		 */
		public function get lastTabFactory():Function
		{
			return this._lastTabFactory;
		}

		/**
		 * @private
		 */
		public function set lastTabFactory(value:Function):void
		{
			if(this._lastTabFactory == value)
			{
				return;
			}
			this._lastTabFactory = value;
			this.invalidate(INVALIDATION_FLAG_TAB_FACTORY);
		}

		/**
		 * @private
		 */
		protected var _tabInitializer:Function = defaultTabInitializer;

		/**
		 * Modifies the properties of an individual tab, using an item from the
		 * data provider. The default initializer will set the tab's label and
		 * icons. A custom tab initializer can be provided to update additional
		 * properties or to use different field names in the data provider.
		 *
		 * <p>This function is expected to have the following signature:</p>
		 * <pre>function( tab:Button, item:Object ):void</pre>
		 *
		 * <p>In the following example, a custom tab initializer is passed to the
		 * tab bar:</p>
		 *
		 * <listing version="3.0">
		 * tabs.tabInitializer = function( tab:Button, item:Object ):void
		 * {
		 *     tab.label = item.text;
		 *     tab.defaultIcon = item.icon;
		 * };</listing>
		 *
		 * @see #dataProvider
		 */
		public function get tabInitializer():Function
		{
			return this._tabInitializer;
		}

		/**
		 * @private
		 */
		public function set tabInitializer(value:Function):void
		{
			if(this._tabInitializer == value)
			{
				return;
			}
			this._tabInitializer = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected var _ignoreSelectionChanges:Boolean = false;

		/**
		 * @private
		 */
		protected var _pendingSelectedIndex:int = NOT_PENDING_INDEX;

		/**
		 * The index of the currently selected tab. Returns -1 if no tab is
		 * selected.
		 *
		 * <p>In the following example, the tab bar's selected index is changed:</p>
		 *
		 * <listing version="3.0">
		 * tabs.selectedIndex = 2;</listing>
		 *
		 * <p>The following example listens for when selection changes and
		 * requests the selected index:</p>
		 *
		 * <listing version="3.0">
		 * function tabs_changeHandler( event:Event ):void
		 * {
		 *     var tabs:TabBar = TabBar( event.currentTarget );
		 *     var index:int = tabs.selectedIndex;
		 *
		 * }
		 * tabs.addEventListener( Event.CHANGE, tabs_changeHandler );</listing>
		 * 
		 * @default -1
		 * 
		 * @see #selectedItem
		 */
		public function get selectedIndex():int
		{
			if(this._pendingSelectedIndex != NOT_PENDING_INDEX)
			{
				return this._pendingSelectedIndex;
			}
			if(!this.toggleGroup)
			{
				return -1;
			}
			return this.toggleGroup.selectedIndex;
		}

		/**
		 * @private
		 */
		public function set selectedIndex(value:int):void
		{
			if(this._pendingSelectedIndex == value ||
				(this._pendingSelectedIndex == NOT_PENDING_INDEX && this.toggleGroup && this.toggleGroup.selectedIndex == value))
			{
				return;
			}
			this._pendingSelectedIndex = value;
			this.invalidate(INVALIDATION_FLAG_SELECTED);
		}

		/**
		 * The currently selected item from the data provider. Returns
		 * <code>null</code> if no item is selected.
		 *
		 * <p>In the following example, the tab bar's selected item is changed:</p>
		 *
		 * <listing version="3.0">
		 * tabs.selectedItem = tabs.dataProvider.getItemAt(2);</listing>
		 *
		 * <p>The following example listens for when selection changes and
		 * requests the selected item:</p>
		 *
		 * <listing version="3.0">
		 * function tabs_changeHandler( event:Event ):void
		 * {
		 *     var tabs:TabBar = TabBar( event.currentTarget );
		 *     var item:Object = tabs.selectedItem;
		 *
		 * }
		 * tabs.addEventListener( Event.CHANGE, tabs_changeHandler );</listing>
		 * 
		 * @default null
		 * 
		 * @see #selectedIndex
		 */
		public function get selectedItem():Object
		{
			const index:int = this.selectedIndex;
			if(!this._dataProvider || index < 0 || index >= this._dataProvider.length)
			{
				return null;
			}
			return this._dataProvider.getItemAt(index);
		}

		/**
		 * @private
		 */
		public function set selectedItem(value:Object):void
		{
			if(!this._dataProvider)
			{
				this.selectedIndex = -1;
				return;
			}
			this.selectedIndex = this._dataProvider.getItemIndex(value);
		}

		/**
		 * @private
		 */
		protected var _customTabName:String;

		/**
		 * A name to add to all tabs in this tab bar. Typically used by a theme
		 * to provide different skins to different tab bars.
		 *
		 * <p>In the following example, a custom tab name is provided to the tab
		 * bar:</p>
		 *
		 * <listing version="3.0">
		 * tabs.customTabName = "my-custom-tab";</listing>
		 *
		 * <p>In your theme, you can target this sub-component name to provide
		 * different skins than the default style:</p>
		 *
		 * <listing version="3.0">
		 * setInitializerForClass( Button, customTabInitializer, "my-custom-tab");</listing>
		 *
		 * @default null
		 *
		 * @see #DEFAULT_CHILD_NAME_TAB
		 * @see feathers.core.FeathersControl#nameList
		 * @see feathers.core.DisplayListWatcher
		 */
		public function get customTabName():String
		{
			return this._customTabName;
		}

		/**
		 * @private
		 */
		public function set customTabName(value:String):void
		{
			if(this._customTabName == value)
			{
				return;
			}
			this._customTabName = value;
			this.invalidate(INVALIDATION_FLAG_TAB_FACTORY);
		}

		/**
		 * @private
		 */
		protected var _customFirstTabName:String;

		/**
		 * A name to add to the first tab in this tab bar. Typically used by a
		 * theme to provide different skins to the first tab.
		 *
		 * <p>In the following example, a custom first tab name is provided to the tab
		 * bar:</p>
		 *
		 * <listing version="3.0">
		 * tabs.customFirstTabName = "my-custom-first-tab";</listing>
		 *
		 * <p>In your theme, you can target this sub-component name to provide
		 * different skins than the default style:</p>
		 *
		 * <listing version="3.0">
		 * setInitializerForClass( Button, customFirstTabInitializer, "my-custom-first-tab");</listing>
		 *
		 * @default null
		 *
		 * @see feathers.core.FeathersControl#nameList
		 * @see feathers.core.DisplayListWatcher
		 */
		public function get customFirstTabName():String
		{
			return this._customFirstTabName;
		}

		/**
		 * @private
		 */
		public function set customFirstTabName(value:String):void
		{
			if(this._customFirstTabName == value)
			{
				return;
			}
			this._customFirstTabName = value;
			this.invalidate(INVALIDATION_FLAG_TAB_FACTORY);
		}

		/**
		 * @private
		 */
		protected var _customLastTabName:String;

		/**
		 * A name to add to the last tab in this tab bar. Typically used by a
		 * theme to provide different skins to the last tab.
		 *
		 * <p>In the following example, a custom tab name is provided to the tab
		 * bar:</p>
		 *
		 * <listing version="3.0">
		 * tabs.customLastTabName = "my-custom-last-tab";</listing>
		 *
		 * <p>In your theme, you can target this sub-component name to provide
		 * different skins than the default style:</p>
		 *
		 * <listing version="3.0">
		 * setInitializerForClass( Button, customLastTabInitializer, "my-custom-last-tab");</listing>
		 *
		 * @default null
		 *
		 * @see feathers.core.FeathersControl#nameList
		 * @see feathers.core.DisplayListWatcher
		 */
		public function get customLastTabName():String
		{
			return this._customLastTabName;
		}

		/**
		 * @private
		 */
		public function set customLastTabName(value:String):void
		{
			if(this._customLastTabName == value)
			{
				return;
			}
			this._customLastTabName = value;
			this.invalidate(INVALIDATION_FLAG_TAB_FACTORY);
		}

		/**
		 * @private
		 */
		protected var _tabProperties:PropertyProxy;

		/**
		 * A set of key/value pairs to be passed down to all of the tab bar's
		 * tabs. These values are shared by each tabs, so values that cannot be
		 * shared (such as display objects that need to be added to the display
		 * list) should be passed to tabs using the <code>tabFactory</code> or
		 * in a theme. The buttons in a tab bar are instances of
		 * <code>feathers.controls.Button</code> that are created by
		 * <code>tabFactory</code>.
		 *
		 * <p>If the subcomponent has its own subcomponents, their properties
		 * can be set too, using attribute <code>&#64;</code> notation. For example,
		 * to set the skin on the thumb which is in a <code>SimpleScrollBar</code>,
		 * which is in a <code>List</code>, you can use the following syntax:</p>
		 * <pre>list.verticalScrollBarProperties.&#64;thumbProperties.defaultSkin = new Image(texture);</pre>
		 *
		 * <p>Setting properties in a <code>tabFactory</code> function instead
		 * of using <code>tabProperties</code> will result in better
		 * performance.</p>
		 *
		 * <p>In the following example, the tab bar's tab properties are updated:</p>
		 *
		 * <listing version="3.0">
		 * tabs.tabProperties.iconPosition = Button.ICON_POSITION_RIGHT;</listing>
		 *
		 * @default null
		 *
		 * @see #tabFactory
		 * @see feathers.controls.Button
		 */
		public function get tabProperties():Object
		{
			if(!this._tabProperties)
			{
				this._tabProperties = new PropertyProxy(childProperties_onChange);
			}
			return this._tabProperties;
		}

		/**
		 * @private
		 */
		public function set tabProperties(value:Object):void
		{
			if(this._tabProperties == value)
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
			if(this._tabProperties)
			{
				this._tabProperties.removeOnChangeCallback(childProperties_onChange);
			}
			this._tabProperties = PropertyProxy(value);
			if(this._tabProperties)
			{
				this._tabProperties.addOnChangeCallback(childProperties_onChange);
			}
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		override public function dispose():void
		{
			this.dataProvider = null;
			super.dispose();
		}

		/**
		 * @private
		 */
		override protected function initialize():void
		{
			this.toggleGroup = new ToggleGroup();
			this.toggleGroup.isSelectionRequired = true;
			this.toggleGroup.addEventListener(Event.CHANGE, toggleGroup_changeHandler);
		}

		/**
		 * @private
		 */
		override protected function draw():void
		{
			const dataInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_DATA);
			const stylesInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_STYLES);
			const stateInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_STATE);
			const selectionInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_SELECTED);
			const tabFactoryInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_TAB_FACTORY);
			var sizeInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_SIZE);

			if(dataInvalid || tabFactoryInvalid)
			{
				this.refreshTabs(tabFactoryInvalid);
			}

			if(dataInvalid || tabFactoryInvalid || stylesInvalid)
			{
				this.refreshTabStyles();
			}

			if(dataInvalid || tabFactoryInvalid || selectionInvalid)
			{
				this.commitSelection();
			}

			if(dataInvalid || tabFactoryInvalid || stateInvalid)
			{
				this.commitEnabled();
			}

			if(stylesInvalid)
			{
				this.refreshLayoutStyles();
			}

			this.layoutTabs();
		}

		/**
		 * @private
		 */
		protected function commitSelection():void
		{
			if(this._pendingSelectedIndex == NOT_PENDING_INDEX || !this.toggleGroup)
			{
				return;
			}
			if(this.toggleGroup.selectedIndex == this._pendingSelectedIndex)
			{
				this._pendingSelectedIndex = NOT_PENDING_INDEX;
				return;
			}

			this.toggleGroup.selectedIndex = this._pendingSelectedIndex;
			this._pendingSelectedIndex = NOT_PENDING_INDEX;
			this.dispatchEventWith(Event.CHANGE);
		}

		/**
		 * @private
		 */
		protected function commitEnabled():void
		{
			for each(var tab:Button in this.activeTabs)
			{
				tab.isEnabled = this._isEnabled;
			}
		}

		/**
		 * @private
		 */
		protected function refreshTabStyles():void
		{
			for each(var tab:Button in this.activeTabs)
			{
				for(var propertyName:String in this._tabProperties)
				{
					var propertyValue:Object = this._tabProperties[propertyName];
					if(tab.hasOwnProperty(propertyName))
					{
						tab[propertyName] = propertyValue;
					}
				}
			}
		}

		/**
		 * @private
		 */
		protected function refreshLayoutStyles():void
		{
			if(this._direction == DIRECTION_VERTICAL)
			{
				if(this.horizontalLayout)
				{
					this.horizontalLayout = null;
				}
				if(!this.verticalLayout)
				{
					this.verticalLayout = new VerticalLayout();
					this.verticalLayout.useVirtualLayout = false;
				}
				this.verticalLayout.distributeHeights = this._distributeTabSizes;
				this.verticalLayout.horizontalAlign = this._horizontalAlign;
				this.verticalLayout.verticalAlign = (this._verticalAlign == VERTICAL_ALIGN_JUSTIFY) ? VERTICAL_ALIGN_TOP : this._verticalAlign;
				this.verticalLayout.gap = this._gap;
				this.verticalLayout.firstGap = this._firstGap;
				this.verticalLayout.lastGap = this._lastGap;
				this.verticalLayout.paddingTop = this._paddingTop;
				this.verticalLayout.paddingRight = this._paddingRight;
				this.verticalLayout.paddingBottom = this._paddingBottom;
				this.verticalLayout.paddingLeft = this._paddingLeft;
			}
			else //horizontal
			{
				if(this.verticalLayout)
				{
					this.verticalLayout = null;
				}
				if(!this.horizontalLayout)
				{
					this.horizontalLayout = new HorizontalLayout();
					this.horizontalLayout.useVirtualLayout = false;
				}
				this.horizontalLayout.distributeWidths = this._distributeTabSizes;
				this.horizontalLayout.horizontalAlign = (this._horizontalAlign == HORIZONTAL_ALIGN_JUSTIFY) ? HORIZONTAL_ALIGN_LEFT : this._horizontalAlign;
				this.horizontalLayout.verticalAlign = this._verticalAlign;
				this.horizontalLayout.gap = this._gap;
				this.horizontalLayout.firstGap = this._firstGap;
				this.horizontalLayout.lastGap = this._lastGap;
				this.horizontalLayout.paddingTop = this._paddingTop;
				this.horizontalLayout.paddingRight = this._paddingRight;
				this.horizontalLayout.paddingBottom = this._paddingBottom;
				this.horizontalLayout.paddingLeft = this._paddingLeft;
			}
		}

		/**
		 * @private
		 */
		protected function defaultTabInitializer(tab:Button, item:Object):void
		{
			if(item is Object)
			{
				if(item.hasOwnProperty("label"))
				{
					tab.label = item.label;
				}
				else
				{
					tab.label = item.toString();
				}
				for each(var field:String in DEFAULT_TAB_FIELDS)
				{
					if(item.hasOwnProperty(field))
					{
						tab[field] = item[field];
					}
				}
			}
			else
			{
				tab.label = "";
			}

		}

		/**
		 * @private
		 */
		protected function refreshTabs(isFactoryInvalid:Boolean):void
		{
			var oldIgnoreSelectionChanges:Boolean = this._ignoreSelectionChanges;
			this._ignoreSelectionChanges = true;
			var oldSelectedIndex:int = this.toggleGroup.selectedIndex;
			this.toggleGroup.removeAllItems();
			var temp:Vector.<Button> = this.inactiveTabs;
			this.inactiveTabs = this.activeTabs;
			this.activeTabs = temp;
			this.activeTabs.length = 0;
			this._layoutItems.length = 0;
			temp = null;
			if(isFactoryInvalid)
			{
				this.clearInactiveTabs();
			}
			else
			{
				if(this.activeFirstTab)
				{
					this.inactiveTabs.shift();
				}
				this.inactiveFirstTab = this.activeFirstTab;

				if(this.activeLastTab)
				{
					this.inactiveTabs.pop();
				}
				this.inactiveLastTab = this.activeLastTab;
			}
			this.activeFirstTab = null;
			this.activeLastTab = null;

			var pushIndex:int = 0;
			const itemCount:int = this._dataProvider ? this._dataProvider.length : 0;
			const lastItemIndex:int = itemCount - 1;
			for(var i:int = 0; i < itemCount; i++)
			{
				var item:Object = this._dataProvider.getItemAt(i);
				if(i == 0)
				{
					var tab:Button = this.activeFirstTab = this.createFirstTab(item);
				}
				else if(i == lastItemIndex)
				{
					tab = this.activeLastTab = this.createLastTab(item);
				}
				else
				{
					tab = this.createTab(item);
				}
				this.toggleGroup.addItem(tab);
				this.activeTabs[pushIndex] = tab;
				this._layoutItems[pushIndex] = tab;
				pushIndex++;
			}

			this.clearInactiveTabs();
			this._ignoreSelectionChanges = oldIgnoreSelectionChanges;
			if(oldSelectedIndex >= 0)
			{
				var newSelectedIndex:int = this.activeTabs.length - 1;
				if(oldSelectedIndex < newSelectedIndex)
				{
					newSelectedIndex = oldSelectedIndex;
				}
				//removing all items from the ToggleGroup clears the selection,
				//so we need to set it back to the old value (or a new clamped
				//value). we want the change event to dispatch only if the old
				//value and the new value don't match.
				this._ignoreSelectionChanges = oldSelectedIndex == newSelectedIndex;
				this.toggleGroup.selectedIndex = newSelectedIndex;
				this._ignoreSelectionChanges = oldIgnoreSelectionChanges;
			}
		}

		/**
		 * @private
		 */
		protected function clearInactiveTabs():void
		{
			const itemCount:int = this.inactiveTabs.length;
			for(var i:int = 0; i < itemCount; i++)
			{
				var tab:Button = this.inactiveTabs.shift();
				this.destroyTab(tab);
			}

			if(this.inactiveFirstTab)
			{
				this.destroyTab(this.inactiveFirstTab);
				this.inactiveFirstTab = null;
			}

			if(this.inactiveLastTab)
			{
				this.destroyTab(this.inactiveLastTab);
				this.inactiveLastTab = null;
			}
		}

		/**
		 * @private
		 */
		protected function createFirstTab(item:Object):Button
		{
			if(this.inactiveFirstTab)
			{
				var tab:Button = this.inactiveFirstTab;
				this.inactiveFirstTab = null;
			}
			else
			{
				const factory:Function = this._firstTabFactory != null ? this._firstTabFactory : this._tabFactory;
				tab = Button(factory());
				if(this._customFirstTabName)
				{
					tab.nameList.add(this._customFirstTabName);
				}
				else if(this._customTabName)
				{
					tab.nameList.add(this._customTabName);
				}
				else
				{
					tab.nameList.add(this.firstTabName);
				}
				tab.isToggle = true;
				this.addChild(tab);
			}
			this._tabInitializer(tab, item);
			return tab;
		}

		/**
		 * @private
		 */
		protected function createLastTab(item:Object):Button
		{
			if(this.inactiveLastTab)
			{
				var tab:Button = this.inactiveLastTab;
				this.inactiveLastTab = null;
			}
			else
			{
				const factory:Function = this._lastTabFactory != null ? this._lastTabFactory : this._tabFactory;
				tab = Button(factory());
				if(this._customLastTabName)
				{
					tab.nameList.add(this._customLastTabName);
				}
				else if(this._customTabName)
				{
					tab.nameList.add(this._customTabName);
				}
				else
				{
					tab.nameList.add(this.lastTabName);
				}
				tab.isToggle = true;
				this.addChild(tab);
			}
			this._tabInitializer(tab, item);
			return tab;
		}

		/**
		 * @private
		 */
		protected function createTab(item:Object):Button
		{
			if(this.inactiveTabs.length == 0)
			{
				var tab:Button = this._tabFactory();
				if(this._customTabName)
				{
					tab.nameList.add(this._customTabName);
				}
				else
				{
					tab.nameList.add(this.tabName);
				}
				tab.isToggle = true;
				this.addChild(tab);
			}
			else
			{
				tab = this.inactiveTabs.shift();
			}
			this._tabInitializer(tab, item);
			return tab;
		}

		/**
		 * @private
		 */
		protected function destroyTab(tab:Button):void
		{
			this.toggleGroup.removeItem(tab);
			this.removeChild(tab, true);
		}

		/**
		 * @private
		 */
		protected function layoutTabs():void
		{
			this._viewPortBounds.x = 0;
			this._viewPortBounds.y = 0;
			this._viewPortBounds.scrollX = 0;
			this._viewPortBounds.scrollY = 0;
			this._viewPortBounds.explicitWidth = this.explicitWidth;
			this._viewPortBounds.explicitHeight = this.explicitHeight;
			this._viewPortBounds.minWidth = this._minWidth;
			this._viewPortBounds.minHeight = this._minHeight;
			this._viewPortBounds.maxWidth = this._maxWidth;
			this._viewPortBounds.maxHeight = this._maxHeight;
			if(this.verticalLayout)
			{
				this.verticalLayout.layout(this._layoutItems, this._viewPortBounds, this._layoutResult);
			}
			else if(this.horizontalLayout)
			{
				this.horizontalLayout.layout(this._layoutItems, this._viewPortBounds, this._layoutResult);
			}
			this.setSizeInternal(this._layoutResult.contentWidth, this._layoutResult.contentHeight, false);
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
		protected function toggleGroup_changeHandler(event:Event):void
		{
			if(this._ignoreSelectionChanges || this._pendingSelectedIndex != NOT_PENDING_INDEX)
			{
				return;
			}
			this.dispatchEventWith(Event.CHANGE);
		}

		/**
		 * @private
		 */
		protected function dataProvider_addItemHandler(event:Event, index:int):void
		{
			if(this.toggleGroup && this.toggleGroup.selectedIndex >= index)
			{
				//let's keep the same item selected
				this._pendingSelectedIndex = this.toggleGroup.selectedIndex + 1;
				this.invalidate(INVALIDATION_FLAG_SELECTED);
			}
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected function dataProvider_removeItemHandler(event:Event, index:int):void
		{
			if(this.toggleGroup && this.toggleGroup.selectedIndex > index)
			{
				//let's keep the same item selected
				this._pendingSelectedIndex = this.toggleGroup.selectedIndex - 1;
				this.invalidate(INVALIDATION_FLAG_SELECTED);
			}
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected function dataProvider_resetHandler(event:Event):void
		{
			if(this.toggleGroup && this._dataProvider.length > 0)
			{
				//the data provider has changed drastically. we should reset the
				//selection to the first item.
				this._pendingSelectedIndex = 0;
				this.invalidate(INVALIDATION_FLAG_SELECTED);
			}
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected function dataProvider_replaceItemHandler(event:Event, index:int):void
		{
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected function dataProvider_updateItemHandler(event:Event, index:int):void
		{
			this.invalidate(INVALIDATION_FLAG_DATA);
		}
	}
}