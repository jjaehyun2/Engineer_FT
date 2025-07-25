/*
Feathers
Copyright 2012-2015 Bowler Hat LLC. All Rights Reserved.

This program is free software. You can redistribute and/or modify it in
accordance with the terms of the accompanying license agreement.
*/
package feathers.controls.supportClasses
{
	import feathers.controls.GroupedList;
	import feathers.controls.Scroller;
	import feathers.controls.renderers.IGroupedListFooterRenderer;
	import feathers.controls.renderers.IGroupedListHeaderRenderer;
	import feathers.controls.renderers.IGroupedListItemRenderer;
	import feathers.core.FeathersControl;
	import feathers.core.IFeathersControl;
	import feathers.core.IValidating;
	import feathers.core.PropertyProxy;
	import feathers.data.HierarchicalCollection;
	import feathers.events.CollectionEventType;
	import feathers.events.FeathersEventType;
	import feathers.layout.IGroupedLayout;
	import feathers.layout.ILayout;
	import feathers.layout.IVariableVirtualLayout;
	import feathers.layout.IVirtualLayout;
	import feathers.layout.LayoutBoundsResult;
	import feathers.layout.ViewPortBounds;

	import flash.errors.IllegalOperationError;
	import flash.geom.Point;
	import flash.utils.Dictionary;

	import starling.display.DisplayObject;
	import starling.events.Event;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;

	/**
	 * @private
	 * Used internally by GroupedList. Not meant to be used on its own.
	 */
	public class GroupedListDataViewPort extends FeathersControl implements IViewPort
	{
		private static const INVALIDATION_FLAG_ITEM_RENDERER_FACTORY:String = "itemRendererFactory";

		private static const HELPER_POINT:Point = new Point();
		private static const HELPER_VECTOR:Vector.<int> = new <int>[];

		public function GroupedListDataViewPort()
		{
			super();
			this.addEventListener(TouchEvent.TOUCH, touchHandler);
			this.addEventListener(Event.REMOVED_FROM_STAGE, removedFromStageHandler);
		}

		private var touchPointID:int = -1;

		private var _viewPortBounds:ViewPortBounds = new ViewPortBounds();

		private var _layoutResult:LayoutBoundsResult = new LayoutBoundsResult();

		private var _minVisibleWidth:Number = 0;

		public function get minVisibleWidth():Number
		{
			return this._minVisibleWidth;
		}

		public function set minVisibleWidth(value:Number):void
		{
			if(this._minVisibleWidth == value)
			{
				return;
			}
			if(value !== value) //isNaN
			{
				throw new ArgumentError("minVisibleWidth cannot be NaN");
			}
			this._minVisibleWidth = value;
			this.invalidate(INVALIDATION_FLAG_SIZE);
		}

		private var _maxVisibleWidth:Number = Number.POSITIVE_INFINITY;

		public function get maxVisibleWidth():Number
		{
			return this._maxVisibleWidth;
		}

		public function set maxVisibleWidth(value:Number):void
		{
			if(this._maxVisibleWidth == value)
			{
				return;
			}
			if(value !== value) //isNaN
			{
				throw new ArgumentError("maxVisibleWidth cannot be NaN");
			}
			this._maxVisibleWidth = value;
			this.invalidate(INVALIDATION_FLAG_SIZE);
		}

		private var actualVisibleWidth:Number = NaN;

		private var explicitVisibleWidth:Number = NaN;

		public function get visibleWidth():Number
		{
			return this.actualVisibleWidth;
		}

		public function set visibleWidth(value:Number):void
		{
			if(this.explicitVisibleWidth == value ||
				(value !== value && this.explicitVisibleWidth !== this.explicitVisibleWidth)) //isNaN
			{
				return;
			}
			this.explicitVisibleWidth = value;
			this.invalidate(INVALIDATION_FLAG_SIZE);
		}

		private var _minVisibleHeight:Number = 0;

		public function get minVisibleHeight():Number
		{
			return this._minVisibleHeight;
		}

		public function set minVisibleHeight(value:Number):void
		{
			if(this._minVisibleHeight == value)
			{
				return;
			}
			if(value !== value) //isNaN
			{
				throw new ArgumentError("minVisibleHeight cannot be NaN");
			}
			this._minVisibleHeight = value;
			this.invalidate(INVALIDATION_FLAG_SIZE);
		}

		private var _maxVisibleHeight:Number = Number.POSITIVE_INFINITY;

		public function get maxVisibleHeight():Number
		{
			return this._maxVisibleHeight;
		}

		public function set maxVisibleHeight(value:Number):void
		{
			if(this._maxVisibleHeight == value)
			{
				return;
			}
			if(value !== value) //isNaN
			{
				throw new ArgumentError("maxVisibleHeight cannot be NaN");
			}
			this._maxVisibleHeight = value;
			this.invalidate(INVALIDATION_FLAG_SIZE);
		}

		private var actualVisibleHeight:Number;

		private var explicitVisibleHeight:Number = NaN;

		public function get visibleHeight():Number
		{
			return this.actualVisibleHeight;
		}

		public function set visibleHeight(value:Number):void
		{
			if(this.explicitVisibleHeight == value ||
				(value !== value && this.explicitVisibleHeight !== this.explicitVisibleHeight)) //isNaN
			{
				return;
			}
			this.explicitVisibleHeight = value;
			this.invalidate(INVALIDATION_FLAG_SIZE);
		}

		protected var _contentX:Number = 0;

		public function get contentX():Number
		{
			return this._contentX;
		}

		protected var _contentY:Number = 0;

		public function get contentY():Number
		{
			return this._contentY;
		}

		public function get horizontalScrollStep():Number
		{
			if(this._typicalItemRenderer === null)
			{
				return 0;
			}
			var itemRendererWidth:Number = this._typicalItemRenderer.width;
			var itemRendererHeight:Number = this._typicalItemRenderer.height;
			if(itemRendererWidth < itemRendererHeight)
			{
				return itemRendererWidth;
			}
			return itemRendererHeight;
		}

		public function get verticalScrollStep():Number
		{
			if(this._typicalItemRenderer === null)
			{
				return 0;
			}
			var itemRendererWidth:Number = this._typicalItemRenderer.width;
			var itemRendererHeight:Number = this._typicalItemRenderer.height;
			if(itemRendererWidth < itemRendererHeight)
			{
				return itemRendererWidth;
			}
			return itemRendererHeight;
		}

		private var _layoutItems:Vector.<DisplayObject> = new <DisplayObject>[];

		private var _typicalItemIsInDataProvider:Boolean = false;
		private var _typicalItemRenderer:IGroupedListItemRenderer;

		private var _unrenderedItems:Vector.<int> = new <int>[];
		private var _defaultItemRendererStorage:ItemRendererFactoryStorage = new ItemRendererFactoryStorage();
		private var _firstItemRendererStorage:ItemRendererFactoryStorage;
		private var _lastItemRendererStorage:ItemRendererFactoryStorage;
		private var _singleItemRendererStorage:ItemRendererFactoryStorage;
		private var _itemStorageMap:Object;
		private var _itemRendererMap:Dictionary = new Dictionary(true);

		private var _unrenderedHeaders:Vector.<int> = new <int>[];
		private var _defaultHeaderRendererStorage:HeaderRendererFactoryStorage = new HeaderRendererFactoryStorage();
		private var _headerStorageMap:Object;
		private var _headerRendererMap:Dictionary = new Dictionary(true);

		private var _unrenderedFooters:Vector.<int> = new <int>[];
		private var _defaultFooterRendererStorage:FooterRendererFactoryStorage = new FooterRendererFactoryStorage();
		private var _footerStorageMap:Object;
		private var _footerRendererMap:Dictionary = new Dictionary(true);

		private var _headerIndices:Vector.<int> = new <int>[];
		private var _footerIndices:Vector.<int> = new <int>[];

		private var _isScrolling:Boolean = false;

		private var _owner:GroupedList;

		public function get owner():GroupedList
		{
			return this._owner;
		}

		public function set owner(value:GroupedList):void
		{
			if(this._owner == value)
			{
				return;
			}
			if(this._owner)
			{
				this._owner.removeEventListener(FeathersEventType.SCROLL_START, owner_scrollStartHandler);
			}
			this._owner = value;
			if(this._owner)
			{
				this._owner.addEventListener(FeathersEventType.SCROLL_START, owner_scrollStartHandler);
			}
		}

		private var _updateForDataReset:Boolean = false;

		private var _dataProvider:HierarchicalCollection;

		public function get dataProvider():HierarchicalCollection
		{
			return this._dataProvider;
		}

		public function set dataProvider(value:HierarchicalCollection):void
		{
			if(this._dataProvider == value)
			{
				return;
			}
			if(this._dataProvider)
			{
				this._dataProvider.removeEventListener(Event.CHANGE, dataProvider_changeHandler);
				this._dataProvider.removeEventListener(CollectionEventType.RESET, dataProvider_resetHandler);
				this._dataProvider.removeEventListener(CollectionEventType.ADD_ITEM, dataProvider_addItemHandler);
				this._dataProvider.removeEventListener(CollectionEventType.REMOVE_ITEM, dataProvider_removeItemHandler);
				this._dataProvider.removeEventListener(CollectionEventType.REPLACE_ITEM, dataProvider_replaceItemHandler);
				this._dataProvider.removeEventListener(CollectionEventType.UPDATE_ITEM, dataProvider_updateItemHandler);
				this._dataProvider.removeEventListener(CollectionEventType.UPDATE_ALL, dataProvider_updateAllHandler);
			}
			this._dataProvider = value;
			if(this._dataProvider)
			{
				this._dataProvider.addEventListener(Event.CHANGE, dataProvider_changeHandler);
				this._dataProvider.addEventListener(CollectionEventType.RESET, dataProvider_resetHandler);
				this._dataProvider.addEventListener(CollectionEventType.ADD_ITEM, dataProvider_addItemHandler);
				this._dataProvider.addEventListener(CollectionEventType.REMOVE_ITEM, dataProvider_removeItemHandler);
				this._dataProvider.addEventListener(CollectionEventType.REPLACE_ITEM, dataProvider_replaceItemHandler);
				this._dataProvider.addEventListener(CollectionEventType.UPDATE_ITEM, dataProvider_updateItemHandler);
				this._dataProvider.addEventListener(CollectionEventType.UPDATE_ALL, dataProvider_updateAllHandler);
			}
			if(this._layout is IVariableVirtualLayout)
			{
				IVariableVirtualLayout(this._layout).resetVariableVirtualCache();
			}
			this._updateForDataReset = true;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		private var _isSelectable:Boolean = true;

		public function get isSelectable():Boolean
		{
			return this._isSelectable;
		}

		public function set isSelectable(value:Boolean):void
		{
			if(this._isSelectable == value)
			{
				return;
			}
			this._isSelectable = value;
			if(!this._isSelectable)
			{
				this.setSelectedLocation(-1, -1);
			}
			this.invalidate(INVALIDATION_FLAG_SELECTED);
		}

		private var _selectedGroupIndex:int = -1;

		public function get selectedGroupIndex():int
		{
			return this._selectedGroupIndex;
		}

		private var _selectedItemIndex:int = -1;

		public function get selectedItemIndex():int
		{
			return this._selectedItemIndex;
		}

		private var _itemRendererType:Class;

		public function get itemRendererType():Class
		{
			return this._itemRendererType;
		}

		public function set itemRendererType(value:Class):void
		{
			if(this._itemRendererType == value)
			{
				return;
			}

			this._itemRendererType = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _itemRendererFactory:Function;

		public function get itemRendererFactory():Function
		{
			return this._itemRendererFactory;
		}

		public function set itemRendererFactory(value:Function):void
		{
			if(this._itemRendererFactory === value)
			{
				return;
			}

			this._itemRendererFactory = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _itemRendererFactories:Object;

		public function get itemRendererFactories():Object
		{
			return this._itemRendererFactories;
		}

		/**
		 * @private
		 */
		public function set itemRendererFactories(value:Object):void
		{
			if(this._itemRendererFactories === value)
			{
				return;
			}

			this._itemRendererFactories = value;
			if(value !== null)
			{
				this._itemStorageMap = {};
			}
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _factoryIDFunction:Function;

		public function get factoryIDFunction():Function
		{
			return this._factoryIDFunction;
		}

		/**
		 * @private
		 */
		public function set factoryIDFunction(value:Function):void
		{
			if(this._factoryIDFunction === value)
			{
				return;
			}

			this._factoryIDFunction = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _customItemRendererStyleName:String;

		public function get customItemRendererStyleName():String
		{
			return this._customItemRendererStyleName;
		}

		public function set customItemRendererStyleName(value:String):void
		{
			if(this._customItemRendererStyleName == value)
			{
				return;
			}
			this._customItemRendererStyleName = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _typicalItem:Object = null;

		public function get typicalItem():Object
		{
			return this._typicalItem;
		}

		public function set typicalItem(value:Object):void
		{
			if(this._typicalItem == value)
			{
				return;
			}
			this._typicalItem = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		private var _itemRendererProperties:PropertyProxy;

		public function get itemRendererProperties():PropertyProxy
		{
			return this._itemRendererProperties;
		}

		public function set itemRendererProperties(value:PropertyProxy):void
		{
			if(this._itemRendererProperties == value)
			{
				return;
			}
			if(this._itemRendererProperties)
			{
				this._itemRendererProperties.removeOnChangeCallback(childProperties_onChange);
			}
			this._itemRendererProperties = PropertyProxy(value);
			if(this._itemRendererProperties)
			{
				this._itemRendererProperties.addOnChangeCallback(childProperties_onChange);
			}
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		private var _firstItemRendererType:Class;

		public function get firstItemRendererType():Class
		{
			return this._firstItemRendererType;
		}

		public function set firstItemRendererType(value:Class):void
		{
			if(this._firstItemRendererType == value)
			{
				return;
			}

			this._firstItemRendererType = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _firstItemRendererFactory:Function;

		public function get firstItemRendererFactory():Function
		{
			return this._firstItemRendererFactory;
		}

		public function set firstItemRendererFactory(value:Function):void
		{
			if(this._firstItemRendererFactory === value)
			{
				return;
			}

			this._firstItemRendererFactory = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _customFirstItemRendererStyleName:String;

		public function get customFirstItemRendererStyleName():String
		{
			return this._customFirstItemRendererStyleName;
		}

		public function set customFirstItemRendererStyleName(value:String):void
		{
			if(this._customFirstItemRendererStyleName == value)
			{
				return;
			}
			this._customFirstItemRendererStyleName = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _lastItemRendererType:Class;

		public function get lastItemRendererType():Class
		{
			return this._lastItemRendererType;
		}

		public function set lastItemRendererType(value:Class):void
		{
			if(this._lastItemRendererType == value)
			{
				return;
			}

			this._lastItemRendererType = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _lastItemRendererFactory:Function;

		public function get lastItemRendererFactory():Function
		{
			return this._lastItemRendererFactory;
		}

		public function set lastItemRendererFactory(value:Function):void
		{
			if(this._lastItemRendererFactory === value)
			{
				return;
			}

			this._lastItemRendererFactory = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _customLastItemRendererStyleName:String;

		public function get customLastItemRendererStyleName():String
		{
			return this._customLastItemRendererStyleName;
		}

		public function set customLastItemRendererStyleName(value:String):void
		{
			if(this._customLastItemRendererStyleName == value)
			{
				return;
			}
			this._customLastItemRendererStyleName = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _singleItemRendererType:Class;

		public function get singleItemRendererType():Class
		{
			return this._singleItemRendererType;
		}

		public function set singleItemRendererType(value:Class):void
		{
			if(this._singleItemRendererType == value)
			{
				return;
			}

			this._singleItemRendererType = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _singleItemRendererFactory:Function;

		public function get singleItemRendererFactory():Function
		{
			return this._singleItemRendererFactory;
		}

		public function set singleItemRendererFactory(value:Function):void
		{
			if(this._singleItemRendererFactory === value)
			{
				return;
			}

			this._singleItemRendererFactory = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _customSingleItemRendererStyleName:String;

		public function get customSingleItemRendererStyleName():String
		{
			return this._customSingleItemRendererStyleName;
		}

		public function set customSingleItemRendererStyleName(value:String):void
		{
			if(this._customSingleItemRendererStyleName == value)
			{
				return;
			}
			this._customSingleItemRendererStyleName = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _headerRendererType:Class;

		public function get headerRendererType():Class
		{
			return this._headerRendererType;
		}

		public function set headerRendererType(value:Class):void
		{
			if(this._headerRendererType == value)
			{
				return;
			}

			this._headerRendererType = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _headerRendererFactory:Function;

		public function get headerRendererFactory():Function
		{
			return this._headerRendererFactory;
		}

		public function set headerRendererFactory(value:Function):void
		{
			if(this._headerRendererFactory === value)
			{
				return;
			}

			this._headerRendererFactory = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _headerRendererFactories:Object;

		public function get headerRendererFactories():Object
		{
			return this._headerRendererFactories;
		}

		/**
		 * @private
		 */
		public function set headerRendererFactories(value:Object):void
		{
			if(this._headerRendererFactories === value)
			{
				return;
			}

			this._headerRendererFactories = value;
			if(value !== null)
			{
				this._headerStorageMap = {};
			}
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _headerFactoryIDFunction:Function;

		public function get headerFactoryIDFunction():Function
		{
			return this._headerFactoryIDFunction;
		}

		/**
		 * @private
		 */
		public function set headerFactoryIDFunction(value:Function):void
		{
			if(this._headerFactoryIDFunction === value)
			{
				return;
			}

			this._headerFactoryIDFunction = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _customHeaderRendererStyleName:String;

		public function get customHeaderRendererStyleName():String
		{
			return this._customHeaderRendererStyleName;
		}

		public function set customHeaderRendererStyleName(value:String):void
		{
			if(this._customHeaderRendererStyleName == value)
			{
				return;
			}
			this._customHeaderRendererStyleName = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _headerRendererProperties:PropertyProxy;

		public function get headerRendererProperties():PropertyProxy
		{
			return this._headerRendererProperties;
		}

		public function set headerRendererProperties(value:PropertyProxy):void
		{
			if(this._headerRendererProperties == value)
			{
				return;
			}
			if(this._headerRendererProperties)
			{
				this._headerRendererProperties.removeOnChangeCallback(childProperties_onChange);
			}
			this._headerRendererProperties = PropertyProxy(value);
			if(this._headerRendererProperties)
			{
				this._headerRendererProperties.addOnChangeCallback(childProperties_onChange);
			}
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		private var _footerRendererType:Class;

		public function get footerRendererType():Class
		{
			return this._footerRendererType;
		}

		public function set footerRendererType(value:Class):void
		{
			if(this._footerRendererType == value)
			{
				return;
			}

			this._footerRendererType = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _footerRendererFactory:Function;

		public function get footerRendererFactory():Function
		{
			return this._footerRendererFactory;
		}

		public function set footerRendererFactory(value:Function):void
		{
			if(this._footerRendererFactory === value)
			{
				return;
			}

			this._footerRendererFactory = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _footerRendererFactories:Object;

		public function get footerRendererFactories():Object
		{
			return this._footerRendererFactories;
		}

		/**
		 * @private
		 */
		public function set footerRendererFactories(value:Object):void
		{
			if(this._footerRendererFactories === value)
			{
				return;
			}

			this._footerRendererFactories = value;
			if(value !== null)
			{
				this._footerStorageMap = {};
			}
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _footerFactoryIDFunction:Function;

		public function get footerFactoryIDFunction():Function
		{
			return this._footerFactoryIDFunction;
		}

		/**
		 * @private
		 */
		public function set footerFactoryIDFunction(value:Function):void
		{
			if(this._footerFactoryIDFunction === value)
			{
				return;
			}

			this._footerFactoryIDFunction = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _customFooterRendererStyleName:String;

		public function get customFooterRendererStyleName():String
		{
			return this._customFooterRendererStyleName;
		}

		public function set customFooterRendererStyleName(value:String):void
		{
			if(this._customFooterRendererStyleName == value)
			{
				return;
			}
			this._customFooterRendererStyleName = value;
			this.invalidate(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
		}

		private var _footerRendererProperties:PropertyProxy;

		public function get footerRendererProperties():PropertyProxy
		{
			return this._footerRendererProperties;
		}

		public function set footerRendererProperties(value:PropertyProxy):void
		{
			if(this._footerRendererProperties == value)
			{
				return;
			}
			if(this._footerRendererProperties)
			{
				this._footerRendererProperties.removeOnChangeCallback(childProperties_onChange);
			}
			this._footerRendererProperties = PropertyProxy(value);
			if(this._footerRendererProperties)
			{
				this._footerRendererProperties.addOnChangeCallback(childProperties_onChange);
			}
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		private var _ignoreLayoutChanges:Boolean = false;
		private var _ignoreRendererResizing:Boolean = false;

		private var _layout:ILayout;

		public function get layout():ILayout
		{
			return this._layout;
		}

		public function set layout(value:ILayout):void
		{
			if(this._layout == value)
			{
				return;
			}
			if(this._layout)
			{
				this._layout.removeEventListener(Event.CHANGE, layout_changeHandler);
			}
			this._layout = value;
			if(this._layout)
			{
				if(this._layout is IVariableVirtualLayout)
				{
					var variableVirtualLayout:IVariableVirtualLayout = IVariableVirtualLayout(this._layout);

					//headers and footers are almost always going to have a
					//different height, so we might as well force it because if
					//we don't, there will be a lot of support requests
					variableVirtualLayout.hasVariableItemDimensions = true;
					
					variableVirtualLayout.resetVariableVirtualCache();
				}
				this._layout.addEventListener(Event.CHANGE, layout_changeHandler);
			}
			this.invalidate(INVALIDATION_FLAG_LAYOUT);
		}

		private var _horizontalScrollPosition:Number = 0;

		public function get horizontalScrollPosition():Number
		{
			return this._horizontalScrollPosition;
		}

		public function set horizontalScrollPosition(value:Number):void
		{
			if(this._horizontalScrollPosition == value)
			{
				return;
			}
			this._horizontalScrollPosition = value;
			this.invalidate(INVALIDATION_FLAG_SCROLL);
		}

		private var _verticalScrollPosition:Number = 0;

		public function get verticalScrollPosition():Number
		{
			return this._verticalScrollPosition;
		}

		public function set verticalScrollPosition(value:Number):void
		{
			if(this._verticalScrollPosition == value)
			{
				return;
			}
			this._verticalScrollPosition = value;
			this.invalidate(INVALIDATION_FLAG_SCROLL);
		}

		private var _minimumItemCount:int;
		private var _minimumHeaderCount:int;
		private var _minimumFooterCount:int;
		private var _minimumFirstAndLastItemCount:int;
		private var _minimumSingleItemCount:int;

		private var _ignoreSelectionChanges:Boolean = false;

		public function setSelectedLocation(groupIndex:int, itemIndex:int):void
		{
			if(this._selectedGroupIndex == groupIndex && this._selectedItemIndex == itemIndex)
			{
				return;
			}
			if((groupIndex < 0 && itemIndex >= 0) || (groupIndex >= 0 && itemIndex < 0))
			{
				throw new ArgumentError("To deselect items, group index and item index must both be < 0.");
			}
			this._selectedGroupIndex = groupIndex;
			this._selectedItemIndex = itemIndex;

			this.invalidate(INVALIDATION_FLAG_SELECTED);
			this.dispatchEventWith(Event.CHANGE);
		}

		public function getScrollPositionForIndex(groupIndex:int, itemIndex:int, result:Point = null):Point
		{
			if(!result)
			{
				result = new Point();
			}

			var displayIndex:int = this.locationToDisplayIndex(groupIndex, itemIndex);
			return this._layout.getScrollPositionForIndex(displayIndex, this._layoutItems,
				0, 0, this.actualVisibleWidth, this.actualVisibleHeight, result);
		}

		public function getNearestScrollPositionForIndex(groupIndex:int, itemIndex:int, result:Point = null):Point
		{
			if(!result)
			{
				result = new Point();
			}

			var displayIndex:int = this.locationToDisplayIndex(groupIndex, itemIndex);
			return this._layout.getNearestScrollPositionForIndex(displayIndex, this._horizontalScrollPosition,
				this._verticalScrollPosition, this._layoutItems, 0, 0, this.actualVisibleWidth, this.actualVisibleHeight, result);
		}

		override public function dispose():void
		{
			this.refreshInactiveRenderers(true);
			this.owner = null;
			this.dataProvider = null;
			this.layout = null;
			super.dispose();
		}

		override protected function draw():void
		{
			var dataInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_DATA);
			var scrollInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_SCROLL);
			var sizeInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_SIZE);
			var selectionInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_SELECTED);
			var itemRendererInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_ITEM_RENDERER_FACTORY);
			var stylesInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_STYLES);
			var stateInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_STATE);
			var layoutInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_LAYOUT);

			//scrolling only affects the layout is requiresLayoutOnScroll is true
			if(!layoutInvalid && scrollInvalid && this._layout && this._layout.requiresLayoutOnScroll)
			{
				layoutInvalid = true;
			}

			var basicsInvalid:Boolean = sizeInvalid || dataInvalid || layoutInvalid || itemRendererInvalid;

			var oldIgnoreRendererResizing:Boolean = this._ignoreRendererResizing;
			this._ignoreRendererResizing = true;
			var oldIgnoreLayoutChanges:Boolean = this._ignoreLayoutChanges;
			this._ignoreLayoutChanges = true;

			if(scrollInvalid || sizeInvalid)
			{
				this.refreshViewPortBounds();
			}
			if(basicsInvalid)
			{
				this.refreshInactiveRenderers(itemRendererInvalid);
			}
			if(dataInvalid || layoutInvalid || itemRendererInvalid)
			{
				this.refreshLayoutTypicalItem();
			}
			if(basicsInvalid)
			{
				this.refreshRenderers();
			}
			if(stylesInvalid || basicsInvalid)
			{
				this.refreshHeaderRendererStyles();
				this.refreshFooterRendererStyles();
				this.refreshItemRendererStyles();
			}
			if(selectionInvalid || basicsInvalid)
			{
				//unlike resizing renderers and layout changes, we only want to
				//stop listening for selection changes when we're forcibly
				//updating selection. other property changes on item renderers
				//can validly change selection, and we need to detect that.
				var oldIgnoreSelectionChanges:Boolean = this._ignoreSelectionChanges;
				this._ignoreSelectionChanges = true;
				this.refreshSelection();
				this._ignoreSelectionChanges = oldIgnoreSelectionChanges;
			}
			if(stateInvalid || basicsInvalid)
			{
				this.refreshEnabled();
			}
			this._ignoreLayoutChanges = oldIgnoreLayoutChanges;

			this._layout.layout(this._layoutItems, this._viewPortBounds, this._layoutResult);

			this._ignoreRendererResizing = oldIgnoreRendererResizing;

			this._contentX = this._layoutResult.contentX;
			this._contentY = this._layoutResult.contentY;
			this.setSizeInternal(this._layoutResult.contentWidth, this._layoutResult.contentHeight, false);
			this.actualVisibleWidth = this._layoutResult.viewPortWidth;
			this.actualVisibleHeight = this._layoutResult.viewPortHeight;

			//final validation to avoid juggler next frame issues
			this.validateRenderers();
		}

		private function validateRenderers():void
		{
			var itemCount:int = this._layoutItems.length;
			for(var i:int = 0; i < itemCount; i++)
			{
				var item:IValidating = this._layoutItems[i] as IValidating;
				if(item)
				{
					item.validate();
				}
			}
		}

		private function refreshEnabled():void
		{
			for each(var item:DisplayObject in this._layoutItems)
			{
				var control:IFeathersControl = item as IFeathersControl;
				if(control)
				{
					control.isEnabled = this._isEnabled;
				}
			}
		}

		private function invalidateParent(flag:String = INVALIDATION_FLAG_ALL):void
		{
			Scroller(this.parent).invalidate(flag);
		}

		private function refreshLayoutTypicalItem():void
		{
			var virtualLayout:IVirtualLayout = this._layout as IVirtualLayout;
			if(!virtualLayout || !virtualLayout.useVirtualLayout)
			{
				if(!this._typicalItemIsInDataProvider && this._typicalItemRenderer)
				{
					//the old layout was virtual, but this one isn't
					this.destroyItemRenderer(this._typicalItemRenderer);
					this._typicalItemRenderer = null;
				}
				return;
			}

			var newTypicalItemIsInDataProvider:Boolean = false;
			var typicalItem:Object = this._typicalItem;
			var groupCount:int = 0;
			var typicalGroupLength:int = 0;
			var typicalItemGroupIndex:int = 0;
			var typicalItemItemIndex:int = 0;
			if(this._dataProvider)
			{
				if(typicalItem !== null)
				{
					this._dataProvider.getItemLocation(typicalItem, HELPER_VECTOR);
					if(HELPER_VECTOR.length > 1)
					{
						newTypicalItemIsInDataProvider = true;
						typicalItemGroupIndex = HELPER_VECTOR[0];
						typicalItemItemIndex = HELPER_VECTOR[1];
					}
				}
				else
				{
					groupCount = this._dataProvider.getLength();
					if(groupCount > 0)
					{
						for(var i:int = 0; i < groupCount; i++)
						{
							typicalGroupLength = this._dataProvider.getLength(i);
							if(typicalGroupLength > 0)
							{
								newTypicalItemIsInDataProvider = true;
								typicalItemGroupIndex = i;
								typicalItem = this._dataProvider.getItemAt(i, 0);
								break;
							}
						}
					}
				}
			}

			if(typicalItem !== null)
			{
				var typicalItemRenderer:IGroupedListItemRenderer = IGroupedListItemRenderer(this._itemRendererMap[typicalItem]);
				if(typicalItemRenderer)
				{
					//at this point, the item already has an item renderer.
					//(this doesn't necessarily mean that the current typical
					//item was the typical item last time this function was
					//called)
					
					//the indices may have changed if items were added, removed,
					//or reordered in the data provider
					typicalItemRenderer.groupIndex = typicalItemGroupIndex;
					typicalItemRenderer.itemIndex = typicalItemItemIndex;
				}
				if(!typicalItemRenderer && this._typicalItemRenderer)
				{
					//the typical item has changed, and doesn't have an item
					//renderer yet. the previous typical item had an item
					//renderer, so we will try to reuse it.

					var canReuse:Boolean = !this._typicalItemIsInDataProvider;
					if(canReuse)
					{
						//we can't reuse if the factoryID has changed, though!
						var factoryID:String = null;
						if(this._factoryIDFunction !== null)
						{
							factoryID = this.getFactoryID(typicalItem, typicalItemGroupIndex, typicalItemItemIndex);
						}
						if(this._typicalItemRenderer.factoryID !== factoryID)
						{
							canReuse = false;
						}
					}
					if(canReuse)
					{
						//we can reuse the item renderer used for the old
						//typical item!
						typicalItemRenderer = this._typicalItemRenderer;
						typicalItemRenderer.data = typicalItem;
						typicalItemRenderer.groupIndex = typicalItemGroupIndex;
						typicalItemRenderer.itemIndex = typicalItemItemIndex;
					}
				}
				if(!typicalItemRenderer)
				{
					typicalItemRenderer = this.createItemRenderer(typicalItem, 0, 0, 0, false, !newTypicalItemIsInDataProvider);
					if(!this._typicalItemIsInDataProvider && this._typicalItemRenderer)
					{
						//get rid of the old one if it isn't needed anymore
						//since it is not in the data provider, we don't need to mess
						//with the renderer map dictionary.
						this.destroyItemRenderer(this._typicalItemRenderer);
						this._typicalItemRenderer = null;
					}
				}
			}

			virtualLayout.typicalItem = DisplayObject(typicalItemRenderer);
			this._typicalItemRenderer = typicalItemRenderer;
			this._typicalItemIsInDataProvider = newTypicalItemIsInDataProvider;
			if(this._typicalItemRenderer && !this._typicalItemIsInDataProvider)
			{
				//we need to know if this item renderer resizes to adjust the
				//layout because the layout may use this item renderer to resize
				//the other item renderers
				this._typicalItemRenderer.addEventListener(FeathersEventType.RESIZE, itemRenderer_resizeHandler);
			}
		}

		private function refreshItemRendererStyles():void
		{
			for each(var item:DisplayObject in this._layoutItems)
			{
				var itemRenderer:IGroupedListItemRenderer = item as IGroupedListItemRenderer;
				if(itemRenderer)
				{
					this.refreshOneItemRendererStyles(itemRenderer);
				}
			}
		}

		private function refreshHeaderRendererStyles():void
		{
			for each(var item:DisplayObject in this._layoutItems)
			{
				var headerRenderer:IGroupedListHeaderRenderer = item as IGroupedListHeaderRenderer;
				if(headerRenderer)
				{
					this.refreshOneHeaderRendererStyles(headerRenderer);
				}
			}
		}

		private function refreshFooterRendererStyles():void
		{
			for each(var item:DisplayObject in this._layoutItems)
			{
				var footerRenderer:IGroupedListFooterRenderer = item as IGroupedListFooterRenderer;
				if(footerRenderer)
				{
					this.refreshOneFooterRendererStyles(footerRenderer);
				}
			}
		}

		private function refreshOneItemRendererStyles(renderer:IGroupedListItemRenderer):void
		{
			var displayRenderer:DisplayObject = DisplayObject(renderer);
			for(var propertyName:String in this._itemRendererProperties)
			{
				var propertyValue:Object = this._itemRendererProperties[propertyName];
				displayRenderer[propertyName] = propertyValue;
			}
		}

		private function refreshOneHeaderRendererStyles(renderer:IGroupedListHeaderRenderer):void
		{
			var displayRenderer:DisplayObject = DisplayObject(renderer);
			for(var propertyName:String in this._headerRendererProperties)
			{
				var propertyValue:Object = this._headerRendererProperties[propertyName];
				displayRenderer[propertyName] = propertyValue;
			}
		}

		private function refreshOneFooterRendererStyles(renderer:IGroupedListFooterRenderer):void
		{
			var displayRenderer:DisplayObject = DisplayObject(renderer);
			for(var propertyName:String in this._footerRendererProperties)
			{
				var propertyValue:Object = this._footerRendererProperties[propertyName];
				displayRenderer[propertyName] = propertyValue;
			}
		}

		private function refreshSelection():void
		{
			for each(var item:DisplayObject in this._layoutItems)
			{
				var itemRenderer:IGroupedListItemRenderer = item as IGroupedListItemRenderer;
				if(itemRenderer)
				{
					itemRenderer.isSelected = itemRenderer.groupIndex == this._selectedGroupIndex &&
						itemRenderer.itemIndex == this._selectedItemIndex;
				}
			}
		}

		private function refreshViewPortBounds():void
		{
			this._viewPortBounds.x = this._viewPortBounds.y = 0;
			this._viewPortBounds.scrollX = this._horizontalScrollPosition;
			this._viewPortBounds.scrollY = this._verticalScrollPosition;
			this._viewPortBounds.explicitWidth = this.explicitVisibleWidth;
			this._viewPortBounds.explicitHeight = this.explicitVisibleHeight;
			this._viewPortBounds.minWidth = this._minVisibleWidth;
			this._viewPortBounds.minHeight = this._minVisibleHeight;
			this._viewPortBounds.maxWidth = this._maxVisibleWidth;
			this._viewPortBounds.maxHeight = this._maxVisibleHeight;
		}

		private function refreshInactiveRenderers(itemRendererTypeIsInvalid:Boolean):void
		{
			var hasCustomFirstItemRenderer:Boolean = this._firstItemRendererType || this._firstItemRendererFactory != null || this._customFirstItemRendererStyleName;
			if(hasCustomFirstItemRenderer)
			{
				if(!this._firstItemRendererStorage)
				{
					this._firstItemRendererStorage = new ItemRendererFactoryStorage();
				}
			}
			else
			{
				this._firstItemRendererStorage = null;
			}
			var hasCustomLastItemRenderer:Boolean = this._lastItemRendererType || this._lastItemRendererFactory != null || this._customLastItemRendererStyleName;
			if(hasCustomLastItemRenderer)
			{
				if(!this._lastItemRendererStorage)
				{
					this._lastItemRendererStorage = new ItemRendererFactoryStorage();
				}
			}
			else
			{
				this._lastItemRendererStorage = null;
			}
			var hasCustomSingleItemRenderer:Boolean = this._singleItemRendererType || this._singleItemRendererFactory != null || this._customSingleItemRendererStyleName;
			if(hasCustomSingleItemRenderer)
			{
				if(!this._singleItemRendererStorage)
				{
					this._singleItemRendererStorage = new ItemRendererFactoryStorage();
				}
			}
			else
			{
				this._singleItemRendererStorage = null;
			}
			
			this.refreshInactiveItemRenderers(this._defaultItemRendererStorage, itemRendererTypeIsInvalid);
			if(this._firstItemRendererStorage)
			{
				this.refreshInactiveItemRenderers(this._firstItemRendererStorage, itemRendererTypeIsInvalid);
			}
			if(this._lastItemRendererStorage)
			{
				this.refreshInactiveItemRenderers(this._lastItemRendererStorage, itemRendererTypeIsInvalid);
			}
			if(this._singleItemRendererStorage)
			{
				this.refreshInactiveItemRenderers(this._singleItemRendererStorage, itemRendererTypeIsInvalid);
			}
			for(var factoryID:String in this._itemStorageMap)
			{
				var itemStorage:ItemRendererFactoryStorage = ItemRendererFactoryStorage(this._itemStorageMap[factoryID]);
				this.refreshInactiveItemRenderers(itemStorage, itemRendererTypeIsInvalid);
			}

			this.refreshInactiveHeaderRenderers(this._defaultHeaderRendererStorage, itemRendererTypeIsInvalid);
			for(factoryID in this._headerStorageMap)
			{
				var headerStorage:HeaderRendererFactoryStorage = HeaderRendererFactoryStorage(this._headerStorageMap[factoryID]);
				this.refreshInactiveHeaderRenderers(headerStorage, itemRendererTypeIsInvalid);
			}

			this.refreshInactiveFooterRenderers(this._defaultFooterRendererStorage, itemRendererTypeIsInvalid);
			for(factoryID in this._footerStorageMap)
			{
				var footerStorage:FooterRendererFactoryStorage = FooterRendererFactoryStorage(this._footerStorageMap[factoryID]);
				this.refreshInactiveFooterRenderers(footerStorage, itemRendererTypeIsInvalid);
			}
			
			if(itemRendererTypeIsInvalid && this._typicalItemRenderer)
			{
				if(this._typicalItemIsInDataProvider)
				{
					delete this._itemRendererMap[this._typicalItemRenderer.data];
				}
				this.destroyItemRenderer(this._typicalItemRenderer);
				this._typicalItemRenderer = null;
				this._typicalItemIsInDataProvider = false;
			}
			
			this._headerIndices.length = 0;
			this._footerIndices.length = 0;
		}

		private function refreshInactiveItemRenderers(storage:ItemRendererFactoryStorage, itemRendererTypeIsInvalid:Boolean):void
		{
			var temp:Vector.<IGroupedListItemRenderer> = storage.inactiveItemRenderers;
			storage.inactiveItemRenderers = storage.activeItemRenderers;
			storage.activeItemRenderers = temp;
			if(storage.activeItemRenderers.length > 0)
			{
				throw new IllegalOperationError("GroupedListDataViewPort: active item renderers should be empty.");
			}

			if(itemRendererTypeIsInvalid)
			{
				this.recoverInactiveItemRenderers(storage);
				this.freeInactiveItemRenderers(storage, 0);
			}
		}

		private function refreshInactiveHeaderRenderers(storage:HeaderRendererFactoryStorage, itemRendererTypeIsInvalid:Boolean):void
		{
			var temp:Vector.<IGroupedListHeaderRenderer> = storage.inactiveHeaderRenderers;
			storage.inactiveHeaderRenderers = storage.activeHeaderRenderers;
			storage.activeHeaderRenderers = temp;
			if(storage.activeHeaderRenderers.length > 0)
			{
				throw new IllegalOperationError("GroupedListDataViewPort: active header renderers should be empty.");
			}

			if(itemRendererTypeIsInvalid)
			{
				this.recoverInactiveHeaderRenderers(storage);
				this.freeInactiveHeaderRenderers(storage, 0);
			}
		}

		private function refreshInactiveFooterRenderers(storage:FooterRendererFactoryStorage, itemRendererTypeIsInvalid:Boolean):void
		{
			var temp:Vector.<IGroupedListFooterRenderer> = storage.inactiveFooterRenderers;
			storage.inactiveFooterRenderers = storage.activeFooterRenderers;
			storage.activeFooterRenderers = temp;
			if(storage.activeFooterRenderers.length > 0)
			{
				throw new IllegalOperationError("GroupedListDataViewPort: active footer renderers should be empty.");
			}
			
			if(itemRendererTypeIsInvalid)
			{
				this.recoverInactiveFooterRenderers(storage);
				this.freeInactiveFooterRenderers(storage, 0);
			}
		}

		private function refreshRenderers():void
		{
			if(this._typicalItemRenderer)
			{
				if(this._typicalItemIsInDataProvider)
				{
					var itemStorage:ItemRendererFactoryStorage = this.factoryIDToStorage(this._typicalItemRenderer.factoryID,
						this._typicalItemRenderer.groupIndex, this._typicalItemRenderer.itemIndex);
					var inactiveItemRenderers:Vector.<IGroupedListItemRenderer> = itemStorage.inactiveItemRenderers;
					var activeItemRenderers:Vector.<IGroupedListItemRenderer> = itemStorage.activeItemRenderers;
					
					//this renderer is already is use by the typical item, so we
					//don't want to allow it to be used by other items.
					var inactiveIndex:int = inactiveItemRenderers.indexOf(this._typicalItemRenderer);
					if(inactiveIndex >= 0)
					{
						inactiveItemRenderers.splice(inactiveIndex, 1);
					}
					//if refreshLayoutTypicalItem() was called, it will have already
					//added the typical item renderer to the active renderers. if
					//not, we need to do it here.
					var activeRenderersCount:int = activeItemRenderers.length;
					if(activeRenderersCount == 0)
					{
						activeItemRenderers[activeRenderersCount] = this._typicalItemRenderer;
					}
				}
				//we need to set the typical item renderer's properties here
				//because they may be needed for proper measurement in a virtual
				//layout.
				this.refreshOneItemRendererStyles(this._typicalItemRenderer);
			}

			this.findUnrenderedData();
			this.recoverInactiveItemRenderers(this._defaultItemRendererStorage);
			if(this._firstItemRendererStorage)
			{
				this.recoverInactiveItemRenderers(this._firstItemRendererStorage);
			}
			if(this._lastItemRendererStorage)
			{
				this.recoverInactiveItemRenderers(this._lastItemRendererStorage);
			}
			if(this._singleItemRendererStorage)
			{
				this.recoverInactiveItemRenderers(this._singleItemRendererStorage);
			}
			if(this._itemStorageMap)
			{
				for(var factoryID:String in this._itemStorageMap)
				{
					itemStorage = ItemRendererFactoryStorage(this._itemStorageMap[factoryID]);
					this.recoverInactiveItemRenderers(itemStorage);
				}
			}
			this.recoverInactiveHeaderRenderers(this._defaultHeaderRendererStorage);
			if(this._headerStorageMap)
			{
				for(factoryID in this._headerStorageMap)
				{
					var headerStorage:HeaderRendererFactoryStorage = HeaderRendererFactoryStorage(this._headerStorageMap[factoryID]);
					this.recoverInactiveHeaderRenderers(headerStorage);
				}
			}
			this.recoverInactiveFooterRenderers(this._defaultFooterRendererStorage);
			if(this._footerStorageMap)
			{
				for(factoryID in this._footerStorageMap)
				{
					var footerStorage:FooterRendererFactoryStorage = FooterRendererFactoryStorage(this._footerStorageMap[factoryID]);
					this.recoverInactiveFooterRenderers(footerStorage);
				}
			}
			
			this.renderUnrenderedData();
			
			this.freeInactiveItemRenderers(this._defaultItemRendererStorage, this._minimumItemCount);
			if(this._firstItemRendererStorage)
			{
				this.freeInactiveItemRenderers(this._firstItemRendererStorage, this._minimumFirstAndLastItemCount);
			}
			if(this._lastItemRendererStorage)
			{
				this.freeInactiveItemRenderers(this._lastItemRendererStorage, this._minimumFirstAndLastItemCount);
			}
			if(this._singleItemRendererStorage)
			{
				this.freeInactiveItemRenderers(this._singleItemRendererStorage, this._minimumSingleItemCount);
			}
			if(this._itemStorageMap)
			{
				for(factoryID in this._itemStorageMap)
				{
					itemStorage = ItemRendererFactoryStorage(this._itemStorageMap[factoryID]);
					this.freeInactiveItemRenderers(itemStorage, 1);
				}
			}
			this.freeInactiveHeaderRenderers(this._defaultHeaderRendererStorage, this._minimumHeaderCount);
			if(this._headerStorageMap)
			{
				for(factoryID in this._headerStorageMap)
				{
					headerStorage = HeaderRendererFactoryStorage(this._headerStorageMap[factoryID]);
					this.freeInactiveHeaderRenderers(headerStorage, 1);
				}
			}
			this.freeInactiveFooterRenderers(this._defaultFooterRendererStorage, this._minimumFooterCount);
			if(this._footerStorageMap)
			{
				for(factoryID in this._footerStorageMap)
				{
					footerStorage = FooterRendererFactoryStorage(this._footerStorageMap[factoryID]);
					this.freeInactiveFooterRenderers(footerStorage, 1);
				}
			}
			
			this._updateForDataReset = false;
		}

		private function findUnrenderedData():void
		{
			var groupCount:int = this._dataProvider ? this._dataProvider.getLength() : 0;
			var totalLayoutCount:int = 0;
			var totalHeaderCount:int = 0;
			var totalFooterCount:int = 0;
			var totalSingleItemCount:int = 0;
			var averageItemsPerGroup:int = 0;
			for(var i:int = 0; i < groupCount; i++)
			{
				var group:Object = this._dataProvider.getItemAt(i);
				if(this._owner.groupToHeaderData(group) !== null)
				{
					this._headerIndices[totalHeaderCount] = totalLayoutCount;
					totalLayoutCount++;
					totalHeaderCount++;
				}
				var currentItemCount:int = this._dataProvider.getLength(i);
				totalLayoutCount += currentItemCount;
				averageItemsPerGroup += currentItemCount;
				if(currentItemCount == 0)
				{
					totalSingleItemCount++;
				}
				if(this._owner.groupToFooterData(group) !== null)
				{
					this._footerIndices[totalFooterCount] = totalLayoutCount;
					totalLayoutCount++;
					totalFooterCount++;
				}
			}
			this._layoutItems.length = totalLayoutCount;
			if(this._layout is IGroupedLayout)
			{
				IGroupedLayout(this._layout).headerIndices = this._headerIndices;
			}
			var virtualLayout:IVirtualLayout = this._layout as IVirtualLayout;
			var useVirtualLayout:Boolean = virtualLayout && virtualLayout.useVirtualLayout;
			if(useVirtualLayout)
			{
				virtualLayout.measureViewPort(totalLayoutCount, this._viewPortBounds, HELPER_POINT);
				var viewPortWidth:Number = HELPER_POINT.x;
				var viewPortHeight:Number = HELPER_POINT.y;
				virtualLayout.getVisibleIndicesAtScrollPosition(this._horizontalScrollPosition, this._verticalScrollPosition, viewPortWidth, viewPortHeight, totalLayoutCount, HELPER_VECTOR);

				averageItemsPerGroup /= groupCount;

				if(this._typicalItemRenderer)
				{
					var minimumTypicalItemEdge:Number = this._typicalItemRenderer.height;
					if(this._typicalItemRenderer.width < minimumTypicalItemEdge)
					{
						minimumTypicalItemEdge = this._typicalItemRenderer.width;
					}

					var maximumViewPortEdge:Number = viewPortWidth;
					if(viewPortHeight > viewPortWidth)
					{
						maximumViewPortEdge = viewPortHeight;
					}
					this._minimumFirstAndLastItemCount = this._minimumSingleItemCount = this._minimumHeaderCount = this._minimumFooterCount = Math.ceil(maximumViewPortEdge / (minimumTypicalItemEdge * averageItemsPerGroup));
					this._minimumHeaderCount = Math.min(this._minimumHeaderCount, totalHeaderCount);
					this._minimumFooterCount = Math.min(this._minimumFooterCount, totalFooterCount);
					this._minimumSingleItemCount = Math.min(this._minimumSingleItemCount, totalSingleItemCount);

					//assumes that zero headers/footers might be visible
					this._minimumItemCount = Math.ceil(maximumViewPortEdge / minimumTypicalItemEdge) + 1;
				}
				else
				{
					this._minimumFirstAndLastItemCount = 1;
					this._minimumHeaderCount = 1;
					this._minimumFooterCount = 1;
					this._minimumSingleItemCount = 1;
					this._minimumItemCount = 1;
				}
			}
			var currentIndex:int = 0;
			for(i = 0; i < groupCount; i++)
			{
				group = this._dataProvider.getItemAt(i);
				var header:Object = this._owner.groupToHeaderData(group);
				if(header !== null)
				{
					//the end index is included in the visible items
					if(useVirtualLayout && HELPER_VECTOR.indexOf(currentIndex) < 0)
					{
						this._layoutItems[currentIndex] = null;
					}
					else
					{
						this.findRendererForHeader(header, i, currentIndex);
					}
					currentIndex++;
				}
				currentItemCount = this._dataProvider.getLength(i);
				for(var j:int = 0; j < currentItemCount; j++)
				{
					if(useVirtualLayout && HELPER_VECTOR.indexOf(currentIndex) < 0)
					{
						if(this._typicalItemRenderer && this._typicalItemIsInDataProvider &&
							this._typicalItemRenderer.groupIndex === i &&
							this._typicalItemRenderer.itemIndex === j)
						{
							//the indices may have changed if items were added, removed,
							//or reordered in the data provider
							this._typicalItemRenderer.layoutIndex = currentIndex;
						}
						this._layoutItems[currentIndex] = null;
					}
					else
					{
						var item:Object = this._dataProvider.getItemAt(i, j);
						this.findRendererForItem(item, i, j, currentIndex);
					}
					currentIndex++;
				}
				var footer:Object = this._owner.groupToFooterData(group);
				if(footer !== null)
				{
					if(useVirtualLayout && HELPER_VECTOR.indexOf(currentIndex) < 0)
					{
						this._layoutItems[currentIndex] = null;
					}
					else
					{
						this.findRendererForFooter(footer, i, currentIndex);
					}
					currentIndex++;
				}
			}
			//update the typical item renderer's visibility
			if(this._typicalItemRenderer)
			{
				if(useVirtualLayout && this._typicalItemIsInDataProvider)
				{
					var index:int = HELPER_VECTOR.indexOf(this._typicalItemRenderer.layoutIndex);
					if(index >= 0)
					{
						this._typicalItemRenderer.visible = true;
					}
					else
					{
						this._typicalItemRenderer.visible = false;

						//uncomment these lines to see a hidden typical item for
						//debugging purposes...
						/*this._typicalItemRenderer.visible = true;
						this._typicalItemRenderer.x = this._horizontalScrollPosition;
						this._typicalItemRenderer.y = this._verticalScrollPosition;*/
					}
				}
				else
				{
					this._typicalItemRenderer.visible = this._typicalItemIsInDataProvider;
				}
			}
			HELPER_VECTOR.length = 0;
		}

		private function findRendererForItem(item:Object, groupIndex:int, itemIndex:int, layoutIndex:int):void
		{
			var itemRenderer:IGroupedListItemRenderer = IGroupedListItemRenderer(this._itemRendererMap[item]);
			if(itemRenderer)
			{
				//the indices may have changed if items were added, removed,
				//or reordered in the data provider
				itemRenderer.groupIndex = groupIndex;
				itemRenderer.itemIndex = itemIndex;
				itemRenderer.layoutIndex = layoutIndex;
				if(this._updateForDataReset)
				{
					//similar to calling updateItemAt(), replacing the data
					//provider or resetting its source means that we should
					//trick the item renderer into thinking it has new data.
					//many developers seem to expect this behavior, so while
					//it's not the most optimal for performance, it saves on
					//support time in the forums. thankfully, it's still
					//somewhat optimized since the same item renderer will
					//receive the same data, and the children generally
					//won't have changed much, if at all.
					itemRenderer.data = null;
					itemRenderer.data = item;
				}

				//the typical item renderer is a special case, and we will
				//have already put it into the active renderers, so we don't
				//want to do it again!
				if(this._typicalItemRenderer != itemRenderer)
				{
					var storage:ItemRendererFactoryStorage = this.factoryIDToStorage(itemRenderer.factoryID,
						itemRenderer.groupIndex, itemRenderer.itemIndex);
					var activeItemRenderers:Vector.<IGroupedListItemRenderer> = storage.activeItemRenderers;
					var inactiveItemRenderers:Vector.<IGroupedListItemRenderer> = storage.inactiveItemRenderers;
					activeItemRenderers[activeItemRenderers.length] = itemRenderer;
					var inactiveIndex:int = inactiveItemRenderers.indexOf(itemRenderer);
					if(inactiveIndex >= 0)
					{
						inactiveItemRenderers.splice(inactiveIndex, 1);
					}
					else
					{
						throw new IllegalOperationError("GroupedListDataViewPort: renderer map contains bad data.");
					}
				}
				itemRenderer.visible = true;
				this._layoutItems[layoutIndex] = DisplayObject(itemRenderer);
			}
			else
			{
				var pushIndex:int = this._unrenderedItems.length;
				this._unrenderedItems[pushIndex] = groupIndex;
				pushIndex++;
				this._unrenderedItems[pushIndex] = itemIndex;
				pushIndex++;
				this._unrenderedItems[pushIndex] = layoutIndex;
			}
		}

		private function findRendererForHeader(header:Object, groupIndex:int, layoutIndex:int):void
		{
			var headerRenderer:IGroupedListHeaderRenderer = IGroupedListHeaderRenderer(this._headerRendererMap[header]);
			if(headerRenderer)
			{
				headerRenderer.groupIndex = groupIndex;
				headerRenderer.layoutIndex = layoutIndex;
				if(this._updateForDataReset)
				{
					//see comments in item renderer section below
					headerRenderer.data = null;
					headerRenderer.data = header;
				}
				var storage:HeaderRendererFactoryStorage = this.headerFactoryIDToStorage(headerRenderer.factoryID);
				var activeHeaderRenderers:Vector.<IGroupedListHeaderRenderer> = storage.activeHeaderRenderers;
				var inactiveHeaderRenderers:Vector.<IGroupedListHeaderRenderer> = storage.inactiveHeaderRenderers;
				activeHeaderRenderers[activeHeaderRenderers.length] = headerRenderer;
				inactiveHeaderRenderers.splice(inactiveHeaderRenderers.indexOf(headerRenderer), 1);
				headerRenderer.visible = true;
				this._layoutItems[layoutIndex] = DisplayObject(headerRenderer);
			}
			else
			{
				var pushIndex:int = this._unrenderedHeaders.length;
				this._unrenderedHeaders[pushIndex] = groupIndex;
				pushIndex++;
				this._unrenderedHeaders[pushIndex] = layoutIndex;
			}
		}

		private function findRendererForFooter(footer:Object, groupIndex:int, layoutIndex:int):void
		{
			var footerRenderer:IGroupedListFooterRenderer = IGroupedListFooterRenderer(this._footerRendererMap[footer]);
			if(footerRenderer)
			{
				footerRenderer.groupIndex = groupIndex;
				footerRenderer.layoutIndex = layoutIndex;
				if(this._updateForDataReset)
				{
					//see comments in item renderer section above
					footerRenderer.data = null;
					footerRenderer.data = footer;
				}
				var storage:FooterRendererFactoryStorage = this.footerFactoryIDToStorage(footerRenderer.factoryID);
				var activeFooterRenderers:Vector.<IGroupedListFooterRenderer> = storage.activeFooterRenderers;
				var inactiveFooterRenderers:Vector.<IGroupedListFooterRenderer> = storage.inactiveFooterRenderers;
				activeFooterRenderers[activeFooterRenderers.length] = footerRenderer;
				inactiveFooterRenderers.splice(inactiveFooterRenderers.indexOf(footerRenderer), 1);
				footerRenderer.visible = true;
				this._layoutItems[layoutIndex] = DisplayObject(footerRenderer);
			}
			else
			{
				var pushIndex:int = this._unrenderedFooters.length;
				this._unrenderedFooters[pushIndex] = groupIndex;
				pushIndex++;
				this._unrenderedFooters[pushIndex] = layoutIndex;
			}
		}

		private function renderUnrenderedData():void
		{
			var rendererCount:int = this._unrenderedItems.length;
			for(var i:int = 0; i < rendererCount; i += 3)
			{
				var groupIndex:int = this._unrenderedItems.shift();
				var itemIndex:int = this._unrenderedItems.shift();
				var layoutIndex:int = this._unrenderedItems.shift();
				var item:Object = this._dataProvider.getItemAt(groupIndex, itemIndex);
				var itemRenderer:IGroupedListItemRenderer = this.createItemRenderer(
					item, groupIndex, itemIndex, layoutIndex, true, false);
				this._layoutItems[layoutIndex] = DisplayObject(itemRenderer);
			}

			rendererCount = this._unrenderedHeaders.length;
			for(i = 0; i < rendererCount; i += 2)
			{
				groupIndex = this._unrenderedHeaders.shift();
				layoutIndex = this._unrenderedHeaders.shift();
				item = this._dataProvider.getItemAt(groupIndex);
				item = this._owner.groupToHeaderData(item);
				var headerRenderer:IGroupedListHeaderRenderer = this.createHeaderRenderer(item, groupIndex, layoutIndex, false);
				this._layoutItems[layoutIndex] = DisplayObject(headerRenderer);
			}

			rendererCount = this._unrenderedFooters.length;
			for(i = 0; i < rendererCount; i += 2)
			{
				groupIndex = this._unrenderedFooters.shift();
				layoutIndex = this._unrenderedFooters.shift();
				item = this._dataProvider.getItemAt(groupIndex);
				item = this._owner.groupToFooterData(item);
				var footerRenderer:IGroupedListFooterRenderer = this.createFooterRenderer(item, groupIndex, layoutIndex, false);
				this._layoutItems[layoutIndex] = DisplayObject(footerRenderer);
			}
		}

		private function recoverInactiveItemRenderers(storage:ItemRendererFactoryStorage):void
		{
			var inactiveItemRenderers:Vector.<IGroupedListItemRenderer> = storage.inactiveItemRenderers;
			var rendererCount:int = inactiveItemRenderers.length;
			for(var i:int = 0; i < rendererCount; i++)
			{
				var itemRenderer:IGroupedListItemRenderer = inactiveItemRenderers[i];
				if(!itemRenderer || itemRenderer.groupIndex < 0)
				{
					continue;
				}
				this._owner.dispatchEventWith(FeathersEventType.RENDERER_REMOVE, false, itemRenderer);
				delete this._itemRendererMap[itemRenderer.data];
			}
		}

		private function recoverInactiveHeaderRenderers(storage:HeaderRendererFactoryStorage):void
		{
			var inactiveHeaderRenderers:Vector.<IGroupedListHeaderRenderer> = storage.inactiveHeaderRenderers;
			var headerRendererCount:int = inactiveHeaderRenderers.length;
			for(var i:int = 0; i < headerRendererCount; i++)
			{
				var headerRenderer:IGroupedListHeaderRenderer = inactiveHeaderRenderers[i];
				if(!headerRenderer)
				{
					continue;
				}
				this._owner.dispatchEventWith(FeathersEventType.RENDERER_REMOVE, false, headerRenderer);
				delete this._headerRendererMap[headerRenderer.data];
			}
		}

		private function recoverInactiveFooterRenderers(storage:FooterRendererFactoryStorage):void
		{
			var inactiveFooterRenderers:Vector.<IGroupedListFooterRenderer> = storage.inactiveFooterRenderers;
			var footerRendererCount:int = inactiveFooterRenderers.length;
			for(var i:int = 0; i < footerRendererCount; i++)
			{
				var footerRenderer:IGroupedListFooterRenderer = inactiveFooterRenderers[i];
				if(!footerRenderer)
				{
					continue;
				}
				this._owner.dispatchEventWith(FeathersEventType.RENDERER_REMOVE, false, footerRenderer);
				delete this._footerRendererMap[footerRenderer.data];
			}
		}

		private function freeInactiveItemRenderers(storage:ItemRendererFactoryStorage, minimumItemCount:int):void
		{
			var inactiveItemRenderers:Vector.<IGroupedListItemRenderer> = storage.inactiveItemRenderers;
			var activeItemRenderers:Vector.<IGroupedListItemRenderer> = storage.activeItemRenderers;
			var activeItemRenderersCount:int = activeItemRenderers.length;
			
			//we may keep around some extra renderers to avoid too much
			//allocation and garbage collection. they'll be hidden.
			var keepCount:int = minimumItemCount - activeItemRenderersCount;
			if(keepCount > inactiveItemRenderers.length)
			{
				keepCount = inactiveItemRenderers.length;
			}
			for(var i:int = 0; i < keepCount; i++)
			{
				var itemRenderer:IGroupedListItemRenderer = inactiveItemRenderers.shift();
				itemRenderer.data = null;
				itemRenderer.groupIndex = -1;
				itemRenderer.itemIndex = -1;
				itemRenderer.layoutIndex = -1;
				itemRenderer.visible = false;
				activeItemRenderers[activeItemRenderersCount] = itemRenderer;
				activeItemRenderersCount++;
			}
			var rendererCount:int = inactiveItemRenderers.length;
			for(i = 0; i < rendererCount; i++)
			{
				itemRenderer = inactiveItemRenderers.shift();
				if(!itemRenderer)
				{
					continue;
				}
				this.destroyItemRenderer(itemRenderer);
			}
		}


		private function freeInactiveHeaderRenderers(storage:HeaderRendererFactoryStorage, minimumHeaderCount:int):void
		{
			var inactiveHeaderRenderers:Vector.<IGroupedListHeaderRenderer> = storage.inactiveHeaderRenderers;
			var activeHeaderRenderers:Vector.<IGroupedListHeaderRenderer> = storage.activeHeaderRenderers;
			var activeHeaderRenderersCount:int = activeHeaderRenderers.length;
			
			var keepCount:int = minimumHeaderCount - activeHeaderRenderersCount;
			if(keepCount > inactiveHeaderRenderers.length)
			{
				keepCount = inactiveHeaderRenderers.length;
			}
			for(var i:int = 0; i < keepCount; i++)
			{
				var headerRenderer:IGroupedListHeaderRenderer = inactiveHeaderRenderers.shift();
				headerRenderer.visible = false;
				headerRenderer.data = null;
				headerRenderer.groupIndex = -1;
				headerRenderer.layoutIndex = -1;
				activeHeaderRenderers[activeHeaderRenderersCount] = headerRenderer;
				activeHeaderRenderersCount++;
			}
			var inactiveHeaderRendererCount:int = inactiveHeaderRenderers.length;
			for(i = 0; i < inactiveHeaderRendererCount; i++)
			{
				headerRenderer = inactiveHeaderRenderers.shift();
				if(!headerRenderer)
				{
					continue;
				}
				this.destroyHeaderRenderer(headerRenderer);
			}
		}

		private function freeInactiveFooterRenderers(storage:FooterRendererFactoryStorage, minimumFooterCount:int):void
		{
			var inactiveFooterRenderers:Vector.<IGroupedListFooterRenderer> = storage.inactiveFooterRenderers;
			var activeFooterRenderers:Vector.<IGroupedListFooterRenderer> = storage.activeFooterRenderers;
			var activeFooterRenderersCount:int = activeFooterRenderers.length;
			
			var keepCount:int = minimumFooterCount - activeFooterRenderersCount;
			if(keepCount > inactiveFooterRenderers.length)
			{
				keepCount = inactiveFooterRenderers.length;
			}
			for(var i:int = 0; i < keepCount; i++)
			{
				var footerRenderer:IGroupedListFooterRenderer = inactiveFooterRenderers.shift();
				footerRenderer.visible = false;
				footerRenderer.data = null;
				footerRenderer.groupIndex = -1;
				footerRenderer.layoutIndex = -1;
				activeFooterRenderers[activeFooterRenderersCount] = footerRenderer;
				activeFooterRenderersCount++
			}
			var inactiveFooterRendererCount:int = inactiveFooterRenderers.length;
			for(i = 0; i < inactiveFooterRendererCount; i++)
			{
				footerRenderer = inactiveFooterRenderers.shift();
				if(!footerRenderer)
				{
					continue;
				}
				this.destroyFooterRenderer(footerRenderer);
			}
		}

		private function createItemRenderer(item:Object, groupIndex:int, itemIndex:int,
			layoutIndex:int, useCache:Boolean, isTemporary:Boolean):IGroupedListItemRenderer
		{
			var factoryID:String = null;
			if(this._factoryIDFunction !== null)
			{
				factoryID = this.getFactoryID(item, groupIndex, itemIndex);
			}
			var itemRendererFactory:Function = this.factoryIDToFactory(factoryID, groupIndex, itemIndex);
			var storage:ItemRendererFactoryStorage = this.factoryIDToStorage(factoryID, groupIndex, itemIndex);
			var customStyleName:String = this.indexToCustomStyleName(groupIndex, itemIndex);
			var inactiveItemRenderers:Vector.<IGroupedListItemRenderer> = storage.inactiveItemRenderers;
			var activeItemRenderers:Vector.<IGroupedListItemRenderer> = storage.activeItemRenderers;
			if(!useCache || isTemporary || inactiveItemRenderers.length === 0)
			{
				var itemRenderer:IGroupedListItemRenderer;
				if(itemRendererFactory !== null)
				{
					itemRenderer = IGroupedListItemRenderer(itemRendererFactory());
				}
				else
				{
					var ItemRendererType:Class = this.indexToItemRendererType(groupIndex, itemIndex);
					itemRenderer = IGroupedListItemRenderer(new ItemRendererType());
				}
				var uiRenderer:IFeathersControl = IFeathersControl(itemRenderer);
				if(customStyleName && customStyleName.length > 0)
				{
					uiRenderer.styleNameList.add(customStyleName);
				}
				this.addChild(DisplayObject(itemRenderer));
			}
			else
			{
				itemRenderer = inactiveItemRenderers.shift();
			}
			itemRenderer.data = item;
			itemRenderer.groupIndex = groupIndex;
			itemRenderer.itemIndex = itemIndex;
			itemRenderer.layoutIndex = layoutIndex;
			itemRenderer.owner = this._owner;
			itemRenderer.factoryID = factoryID;
			itemRenderer.visible = true;

			if(!isTemporary)
			{
				this._itemRendererMap[item] = itemRenderer;
				activeItemRenderers.push(itemRenderer);
				itemRenderer.addEventListener(Event.TRIGGERED, renderer_triggeredHandler);
				itemRenderer.addEventListener(Event.CHANGE, renderer_changeHandler);
				itemRenderer.addEventListener(FeathersEventType.RESIZE, itemRenderer_resizeHandler);
				this._owner.dispatchEventWith(FeathersEventType.RENDERER_ADD, false, itemRenderer);
			}

			return itemRenderer;
		}

		private function createHeaderRenderer(header:Object, groupIndex:int, layoutIndex:int, isTemporary:Boolean = false):IGroupedListHeaderRenderer
		{
			var factoryID:String = null;
			if(this._headerFactoryIDFunction !== null)
			{
				if(this._headerFactoryIDFunction.length === 1)
				{
					factoryID = this._headerFactoryIDFunction(header);
				}
				else
				{
					factoryID = this._headerFactoryIDFunction(header, groupIndex);
				}
			}
			var headerRendererFactory:Function = this.headerFactoryIDToFactory(factoryID);
			var storage:HeaderRendererFactoryStorage = this.headerFactoryIDToStorage(factoryID);
			var inactiveHeaderRenderers:Vector.<IGroupedListHeaderRenderer> = storage.inactiveHeaderRenderers;
			var activeHeaderRenderers:Vector.<IGroupedListHeaderRenderer> = storage.activeHeaderRenderers;
			if(isTemporary || inactiveHeaderRenderers.length === 0)
			{
				var headerRenderer:IGroupedListHeaderRenderer;
				if(headerRendererFactory !== null)
				{
					headerRenderer = IGroupedListHeaderRenderer(headerRendererFactory());
				}
				else
				{
					headerRenderer = IGroupedListHeaderRenderer(new this._headerRendererType());
				}
				var uiRenderer:IFeathersControl = IFeathersControl(headerRenderer);
				if(this._customHeaderRendererStyleName && this._customHeaderRendererStyleName.length > 0)
				{
					uiRenderer.styleNameList.add(this._customHeaderRendererStyleName);
				}
				this.addChild(DisplayObject(headerRenderer));
			}
			else
			{
				headerRenderer = inactiveHeaderRenderers.shift();
			}
			headerRenderer.data = header;
			headerRenderer.groupIndex = groupIndex;
			headerRenderer.layoutIndex = layoutIndex;
			headerRenderer.owner = this._owner;
			headerRenderer.factoryID = factoryID;
			headerRenderer.visible = true;

			if(!isTemporary)
			{
				this._headerRendererMap[header] = headerRenderer;
				activeHeaderRenderers.push(headerRenderer);
				headerRenderer.addEventListener(FeathersEventType.RESIZE, headerRenderer_resizeHandler);
				this._owner.dispatchEventWith(FeathersEventType.RENDERER_ADD, false, headerRenderer);
			}

			return headerRenderer;
		}

		private function createFooterRenderer(footer:Object, groupIndex:int, layoutIndex:int, isTemporary:Boolean = false):IGroupedListFooterRenderer
		{
			var factoryID:String = null;
			if(this._footerFactoryIDFunction !== null)
			{
				if(this._footerFactoryIDFunction.length === 1)
				{
					factoryID = this._footerFactoryIDFunction(footer);
				}
				else
				{
					factoryID = this._footerFactoryIDFunction(footer, groupIndex);
				}
			}
			var footerRendererFactory:Function = this.footerFactoryIDToFactory(factoryID);
			var storage:FooterRendererFactoryStorage = this.footerFactoryIDToStorage(factoryID);
			var inactiveFooterRenderers:Vector.<IGroupedListFooterRenderer> = storage.inactiveFooterRenderers;
			var activeFooterRenderers:Vector.<IGroupedListFooterRenderer> = storage.activeFooterRenderers;
			if(isTemporary || inactiveFooterRenderers.length === 0)
			{
				var footerRenderer:IGroupedListFooterRenderer;
				if(footerRendererFactory !== null)
				{
					footerRenderer = IGroupedListFooterRenderer(footerRendererFactory());
				}
				else
				{
					footerRenderer = IGroupedListFooterRenderer(new this._footerRendererType());
				}
				var uiRenderer:IFeathersControl = IFeathersControl(footerRenderer);
				if(this._customFooterRendererStyleName && this._customFooterRendererStyleName.length > 0)
				{
					uiRenderer.styleNameList.add(this._customFooterRendererStyleName);
				}
				this.addChild(DisplayObject(footerRenderer));
			}
			else
			{
				footerRenderer = inactiveFooterRenderers.shift();
			}
			footerRenderer.data = footer;
			footerRenderer.groupIndex = groupIndex;
			footerRenderer.layoutIndex = layoutIndex;
			footerRenderer.owner = this._owner;
			footerRenderer.factoryID = factoryID;
			footerRenderer.visible = true;

			if(!isTemporary)
			{
				this._footerRendererMap[footer] = footerRenderer;
				activeFooterRenderers[activeFooterRenderers.length] = footerRenderer;
				footerRenderer.addEventListener(FeathersEventType.RESIZE, footerRenderer_resizeHandler);
				this._owner.dispatchEventWith(FeathersEventType.RENDERER_ADD, false, footerRenderer);
			}

			return footerRenderer;
		}

		private function destroyItemRenderer(renderer:IGroupedListItemRenderer):void
		{
			renderer.removeEventListener(Event.TRIGGERED, renderer_triggeredHandler);
			renderer.removeEventListener(Event.CHANGE, renderer_changeHandler);
			renderer.removeEventListener(FeathersEventType.RESIZE, itemRenderer_resizeHandler);
			renderer.owner = null;
			renderer.data = null;
			this.removeChild(DisplayObject(renderer), true);
		}

		private function destroyHeaderRenderer(renderer:IGroupedListHeaderRenderer):void
		{
			renderer.removeEventListener(FeathersEventType.RESIZE, headerRenderer_resizeHandler);
			renderer.owner = null;
			renderer.data = null;
			this.removeChild(DisplayObject(renderer), true);
		}

		private function destroyFooterRenderer(renderer:IGroupedListFooterRenderer):void
		{
			renderer.removeEventListener(FeathersEventType.RESIZE, footerRenderer_resizeHandler);
			renderer.owner = null;
			renderer.data = null;
			this.removeChild(DisplayObject(renderer), true);
		}

		private function groupToHeaderDisplayIndex(groupIndex:int):int
		{
			var group:Object = this._dataProvider.getItemAt(groupIndex);
			var header:Object = this._owner.groupToHeaderData(group);
			if(!header)
			{
				return -1;
			}
			var displayIndex:int = 0;
			var groupCount:int = this._dataProvider.getLength();
			for(var i:int = 0; i < groupCount; i++)
			{
				group = this._dataProvider.getItemAt(i);
				header = this._owner.groupToHeaderData(group);
				if(header)
				{
					if(groupIndex == i)
					{
						return displayIndex;
					}
					displayIndex++;
				}
				var groupLength:int = this._dataProvider.getLength(i);
				for(var j:int = 0; j < groupLength; j++)
				{
					displayIndex++;
				}
				var footer:Object = this._owner.groupToFooterData(group);
				if(footer)
				{
					displayIndex++;
				}
			}
			return -1;
		}

		private function groupToFooterDisplayIndex(groupIndex:int):int
		{
			var group:Object = this._dataProvider.getItemAt(groupIndex);
			var footer:Object = this._owner.groupToFooterData(group);
			if(!footer)
			{
				return -1;
			}
			var displayIndex:int = 0;
			var groupCount:int = this._dataProvider.getLength();
			for(var i:int = 0; i < groupCount; i++)
			{
				group = this._dataProvider.getItemAt(i);
				var header:Object = this._owner.groupToHeaderData(group);
				if(header)
				{
					displayIndex++;
				}
				var groupLength:int = this._dataProvider.getLength(i);
				for(var j:int = 0; j < groupLength; j++)
				{
					displayIndex++;
				}
				footer = this._owner.groupToFooterData(group);
				if(footer)
				{
					if(groupIndex == i)
					{
						return displayIndex;
					}
					displayIndex++;
				}
			}
			return -1;
		}

		private function locationToDisplayIndex(groupIndex:int, itemIndex:int):int
		{
			var displayIndex:int = 0;
			var groupCount:int = this._dataProvider.getLength();
			for(var i:int = 0; i < groupCount; i++)
			{
				if(itemIndex < 0 && groupIndex == i)
				{
					return displayIndex;
				}
				var group:Object = this._dataProvider.getItemAt(i);
				var header:Object = this._owner.groupToHeaderData(group);
				if(header)
				{
					displayIndex++;
				}
				var groupLength:int = this._dataProvider.getLength(i);
				for(var j:int = 0; j < groupLength; j++)
				{
					if(groupIndex == i && itemIndex == j)
					{
						return displayIndex;
					}
					displayIndex++;
				}
				var footer:Object = this._owner.groupToFooterData(group);
				if(footer)
				{
					displayIndex++;
				}
			}
			return -1;
		}
		
		private function indexToItemRendererType(groupIndex:int, itemIndex:int):Class
		{
			var groupLength:int = this._dataProvider.getLength(groupIndex);
			if(itemIndex === 0)
			{
				if(this._singleItemRendererType !== null && groupLength === 1)
				{
					return this._singleItemRendererType;
				}
				else if(this._firstItemRendererType !== null)
				{
					return this._firstItemRendererType;
				}
			}
			if(this._lastItemRendererType !== null && itemIndex === (groupLength - 1))
			{
				return this._lastItemRendererType;
			}
			return this._itemRendererType;
		}

		private function indexToCustomStyleName(groupIndex:int, itemIndex:int):String
		{
			var groupLength:int = this._dataProvider.getLength(groupIndex);
			if(itemIndex === 0)
			{
				if(this._customSingleItemRendererStyleName !== null && groupLength === 1)
				{
					return this._customSingleItemRendererStyleName;
				}
				else if(this._customFirstItemRendererStyleName !== null)
				{
					return this._customFirstItemRendererStyleName;
				}
			}
			if(this._customLastItemRendererStyleName !== null && itemIndex === (groupLength - 1))
			{
				return this._customLastItemRendererStyleName;
			}
			return this._customItemRendererStyleName;
		}

		private function getFactoryID(item:Object, groupIndex:int, itemIndex:int):String
		{
			if(this._factoryIDFunction === null)
			{
				return null;
			}
			if(this._factoryIDFunction.length === 1)
			{
				return this._factoryIDFunction(item);
			}
			return this._factoryIDFunction(item, groupIndex, itemIndex);
		}

		private function factoryIDToFactory(id:String, groupIndex:int, itemIndex:int):Function
		{
			if(id !== null)
			{
				if(id in this._itemRendererFactories)
				{
					return this._itemRendererFactories[id] as Function;
				}
				else
				{
					throw new ReferenceError("Cannot find item renderer factory for ID \"" + id + "\".")
				}
			}
			var groupLength:int = this._dataProvider.getLength(groupIndex);
			if(itemIndex === 0)
			{
				if(this._singleItemRendererFactory !== null && groupLength === 1)
				{
					return this._singleItemRendererFactory;
				}
				else if(this._firstItemRendererFactory !== null)
				{
					return this._firstItemRendererFactory;
				}
			}
			if(this._lastItemRendererFactory !== null && itemIndex === (groupLength - 1))
			{
				return this._lastItemRendererFactory;
			}
			return this._itemRendererFactory;
		}

		private function factoryIDToStorage(id:String, groupIndex:int, itemIndex:int):ItemRendererFactoryStorage
		{
			if(id !== null)
			{
				if(id in this._itemStorageMap)
				{
					return ItemRendererFactoryStorage(this._itemStorageMap[id]);
				}
				var storage:ItemRendererFactoryStorage = new ItemRendererFactoryStorage();
				this._itemStorageMap[id] = storage;
				return storage;
			}
			var groupLength:int = this._dataProvider.getLength(groupIndex);
			if(itemIndex === 0)
			{
				if(this._singleItemRendererStorage !== null && groupLength === 1)
				{
					return this._singleItemRendererStorage;
				}
				else if(this._firstItemRendererStorage !== null)
				{
					return this._firstItemRendererStorage;
				}
			}
			if(this._lastItemRendererStorage !== null && itemIndex === (groupLength - 1))
			{
				return this._lastItemRendererStorage;
			}
			return this._defaultItemRendererStorage;
		}

		private function headerFactoryIDToFactory(id:String):Function
		{
			if(id !== null)
			{
				if(id in this._headerRendererFactories)
				{
					return this._headerRendererFactories[id] as Function;
				}
				else
				{
					throw new ReferenceError("Cannot find header renderer factory for ID \"" + id + "\".")
				}
			}
			return this._headerRendererFactory;
		}

		private function headerFactoryIDToStorage(id:String):HeaderRendererFactoryStorage
		{
			if(id !== null)
			{
				if(id in this._headerStorageMap)
				{
					return HeaderRendererFactoryStorage(this._headerStorageMap[id]);
				}
				var storage:HeaderRendererFactoryStorage = new HeaderRendererFactoryStorage();
				this._headerStorageMap[id] = storage;
				return storage;
			}
			return this._defaultHeaderRendererStorage;
		}

		private function footerFactoryIDToFactory(id:String):Function
		{
			if(id !== null)
			{
				if(id in this._footerRendererFactories)
				{
					return this._footerRendererFactories[id] as Function;
				}
				else
				{
					throw new ReferenceError("Cannot find footer renderer factory for ID \"" + id + "\".")
				}
			}
			return this._footerRendererFactory;
		}

		private function footerFactoryIDToStorage(id:String):FooterRendererFactoryStorage
		{
			if(id !== null)
			{
				if(id in this._footerStorageMap)
				{
					return FooterRendererFactoryStorage(this._footerStorageMap[id]);
				}
				var storage:FooterRendererFactoryStorage = new FooterRendererFactoryStorage();
				this._footerStorageMap[id] = storage;
				return storage;
			}
			return this._defaultFooterRendererStorage;
		}

		private function childProperties_onChange(proxy:PropertyProxy, name:String):void
		{
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		private function owner_scrollStartHandler(event:Event):void
		{
			this._isScrolling = true;
		}

		private function dataProvider_changeHandler(event:Event):void
		{
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		private function dataProvider_addItemHandler(event:Event, indices:Array):void
		{
			var layout:IVariableVirtualLayout = this._layout as IVariableVirtualLayout;
			if(!layout || !layout.hasVariableItemDimensions)
			{
				return;
			}
			var groupIndex:int = indices[0] as int;
			if(indices.length > 1) //adding an item
			{
				var itemIndex:int = indices[1] as int;
				var itemDisplayIndex:int = this.locationToDisplayIndex(groupIndex, itemIndex);
				layout.addToVariableVirtualCacheAtIndex(itemDisplayIndex);
			}
			else //adding a whole group
			{
				var headerDisplayIndex:int = this.groupToHeaderDisplayIndex(groupIndex);
				if(headerDisplayIndex >= 0)
				{
					layout.addToVariableVirtualCacheAtIndex(headerDisplayIndex);
				}
				var groupLength:int = this._dataProvider.getLength(groupIndex);
				if(groupLength > 0)
				{
					var displayIndex:int = headerDisplayIndex;
					if(displayIndex < 0)
					{
						displayIndex = this.locationToDisplayIndex(groupIndex, 0);
					}
					groupLength += displayIndex;
					for(var i:int = displayIndex; i < groupLength; i++)
					{
						layout.addToVariableVirtualCacheAtIndex(displayIndex);
					}
				}
				var footerDisplayIndex:int = this.groupToFooterDisplayIndex(groupIndex);
				if(footerDisplayIndex >= 0)
				{
					layout.addToVariableVirtualCacheAtIndex(footerDisplayIndex);
				}
			}
		}

		private function dataProvider_removeItemHandler(event:Event, indices:Array):void
		{
			var layout:IVariableVirtualLayout = this._layout as IVariableVirtualLayout;
			if(!layout || !layout.hasVariableItemDimensions)
			{
				return;
			}
			var groupIndex:int = indices[0] as int;
			if(indices.length > 1) //removing an item
			{
				var itemIndex:int = indices[1] as int;
				var displayIndex:int = this.locationToDisplayIndex(groupIndex, itemIndex);
				layout.removeFromVariableVirtualCacheAtIndex(displayIndex);
			}
			else //removing a whole group
			{
				//TODO: figure out the length of the previous group so that we
				//don't need to reset the whole cache
				layout.resetVariableVirtualCache();
			}
		}

		private function dataProvider_replaceItemHandler(event:Event, indices:Array):void
		{
			var layout:IVariableVirtualLayout = this._layout as IVariableVirtualLayout;
			if(!layout || !layout.hasVariableItemDimensions)
			{
				return;
			}
			var groupIndex:int = indices[0] as int;
			if(indices.length > 1) //replacing an item
			{
				var itemIndex:int = indices[1] as int;
				var displayIndex:int = this.locationToDisplayIndex(groupIndex, itemIndex);
				layout.resetVariableVirtualCacheAtIndex(displayIndex);
			}
			else //replacing a whole group
			{
				//TODO: figure out the length of the previous group so that we
				//don't need to reset the whole cache
				layout.resetVariableVirtualCache();
			}
		}

		private function dataProvider_resetHandler(event:Event):void
		{
			this._updateForDataReset = true;

			var layout:IVariableVirtualLayout = this._layout as IVariableVirtualLayout;
			if(!layout || !layout.hasVariableItemDimensions)
			{
				return;
			}
			layout.resetVariableVirtualCache();
		}

		private function dataProvider_updateItemHandler(event:Event, indices:Array):void
		{
			var groupIndex:int = indices[0] as int;
			if(indices.length > 1) //updating a single item
			{
				var itemIndex:int = indices[1] as int;
				var item:Object = this._dataProvider.getItemAt(groupIndex, itemIndex);
				var itemRenderer:IGroupedListItemRenderer = IGroupedListItemRenderer(this._itemRendererMap[item]);
				if(itemRenderer)
				{
					itemRenderer.data = null;
					itemRenderer.data = item;
				}
			}
			else //updating a whole group
			{
				var groupLength:int = this._dataProvider.getLength(groupIndex);
				for(var i:int = 0; i < groupLength; i++)
				{
					item = this._dataProvider.getItemAt(groupIndex, i);
					if(item)
					{
						itemRenderer = IGroupedListItemRenderer(this._itemRendererMap[item]);
						if(itemRenderer)
						{
							itemRenderer.data = null;
							itemRenderer.data = item;
						}
					}
				}
				var group:Object = this._dataProvider.getItemAt(groupIndex);
				item = this._owner.groupToHeaderData(group);
				if(item)
				{
					var headerRenderer:IGroupedListHeaderRenderer = IGroupedListHeaderRenderer(this._headerRendererMap[item]);
					if(headerRenderer)
					{
						headerRenderer.data = null;
						headerRenderer.data = item;
					}
				}
				item = this._owner.groupToFooterData(group);
				if(item)
				{
					var footerRenderer:IGroupedListFooterRenderer = IGroupedListFooterRenderer(this._footerRendererMap[item]);
					if(footerRenderer)
					{
						footerRenderer.data = null;
						footerRenderer.data = item;
					}
				}

				//we need to invalidate because the group may have more or fewer items
				this.invalidate(INVALIDATION_FLAG_DATA);

				var layout:IVariableVirtualLayout = this._layout as IVariableVirtualLayout;
				if(!layout || !layout.hasVariableItemDimensions)
				{
					return;
				}
				//TODO: figure out the length of the previous group so that we
				//don't need to reset the whole cache
				layout.resetVariableVirtualCache();
			}
		}

		private function dataProvider_updateAllHandler(event:Event):void
		{
			for(var item:Object in this._itemRendererMap)
			{
				var itemRenderer:IGroupedListItemRenderer = IGroupedListItemRenderer(this._itemRendererMap[item]);
				if(!itemRenderer)
				{
					return;
				}
				itemRenderer.data = null;
				itemRenderer.data = item;
			}
			for(var header:Object in this._headerRendererMap)
			{
				var headerRenderer:IGroupedListHeaderRenderer = IGroupedListHeaderRenderer(this._headerRendererMap[header]);
				if(!headerRenderer)
				{
					return;
				}
				headerRenderer.data = null;
				headerRenderer.data = header;
			}
			for(var footer:Object in this._footerRendererMap)
			{
				var footerRenderer:IGroupedListFooterRenderer = IGroupedListFooterRenderer(this._footerRendererMap[footer]);
				if(!footerRenderer)
				{
					return;
				}
				footerRenderer.data = null;
				footerRenderer.data = footer;
			}
		}

		private function layout_changeHandler(event:Event):void
		{
			if(this._ignoreLayoutChanges)
			{
				return;
			}
			this.invalidate(INVALIDATION_FLAG_LAYOUT);
			this.invalidateParent(INVALIDATION_FLAG_LAYOUT);
		}

		private function itemRenderer_resizeHandler(event:Event):void
		{
			if(this._ignoreRendererResizing)
			{
				return;
			}
			if(event.currentTarget === this._typicalItemRenderer && !this._typicalItemIsInDataProvider)
			{
				return;
			}
			var renderer:IGroupedListItemRenderer = IGroupedListItemRenderer(event.currentTarget);
			if(renderer.layoutIndex < 0)
			{
				return;
			}
			this.invalidate(INVALIDATION_FLAG_LAYOUT);
			this.invalidateParent(INVALIDATION_FLAG_LAYOUT);
			var layout:IVariableVirtualLayout = this._layout as IVariableVirtualLayout;
			if(!layout || !layout.hasVariableItemDimensions)
			{
				return;
			}
			layout.resetVariableVirtualCacheAtIndex(renderer.layoutIndex, DisplayObject(renderer));
		}

		private function headerRenderer_resizeHandler(event:Event):void
		{
			if(this._ignoreRendererResizing)
			{
				return;
			}
			var renderer:IGroupedListHeaderRenderer = IGroupedListHeaderRenderer(event.currentTarget);
			if(renderer.layoutIndex < 0)
			{
				return;
			}
			this.invalidate(INVALIDATION_FLAG_LAYOUT);
			this.invalidateParent(INVALIDATION_FLAG_LAYOUT);
			var layout:IVariableVirtualLayout = this._layout as IVariableVirtualLayout;
			if(!layout || !layout.hasVariableItemDimensions)
			{
				return;
			}
			layout.resetVariableVirtualCacheAtIndex(renderer.layoutIndex, DisplayObject(renderer));
		}

		private function footerRenderer_resizeHandler(event:Event):void
		{
			if(this._ignoreRendererResizing)
			{
				return;
			}
			var renderer:IGroupedListFooterRenderer = IGroupedListFooterRenderer(event.currentTarget);
			if(renderer.layoutIndex < 0)
			{
				return;
			}
			this.invalidate(INVALIDATION_FLAG_LAYOUT);
			this.invalidateParent(INVALIDATION_FLAG_LAYOUT);
			var layout:IVariableVirtualLayout = this._layout as IVariableVirtualLayout;
			if(!layout || !layout.hasVariableItemDimensions)
			{
				return;
			}
			layout.resetVariableVirtualCacheAtIndex(renderer.layoutIndex, DisplayObject(renderer));
		}

		private function renderer_triggeredHandler(event:Event):void
		{
			var renderer:IGroupedListItemRenderer = IGroupedListItemRenderer(event.currentTarget);
			this.parent.dispatchEventWith(Event.TRIGGERED, false, renderer.data);
		}

		private function renderer_changeHandler(event:Event):void
		{
			if(this._ignoreSelectionChanges)
			{
				return;
			}
			var renderer:IGroupedListItemRenderer = IGroupedListItemRenderer(event.currentTarget);
			if(!this._isSelectable || this._isScrolling)
			{
				renderer.isSelected = false;
				return;
			}
			if(renderer.isSelected)
			{
				this.setSelectedLocation(renderer.groupIndex, renderer.itemIndex);
			}
			else
			{
				this.setSelectedLocation(-1, -1);
			}
		}

		private function removedFromStageHandler(event:Event):void
		{
			this.touchPointID = -1;
		}

		private function touchHandler(event:TouchEvent):void
		{
			if(!this._isEnabled)
			{
				this.touchPointID = -1;
				return;
			}

			if(this.touchPointID >= 0)
			{
				var touch:Touch = event.getTouch(this, TouchPhase.ENDED, this.touchPointID);
				if(!touch)
				{
					return;
				}
				this.touchPointID = -1;
			}
			else
			{
				touch = event.getTouch(this, TouchPhase.BEGAN);
				if(!touch)
				{
					return;
				}
				this.touchPointID = touch.id;
				this._isScrolling = false;
			}
		}
	}
}

import feathers.controls.renderers.IGroupedListFooterRenderer;
import feathers.controls.renderers.IGroupedListHeaderRenderer;
import feathers.controls.renderers.IGroupedListItemRenderer;

class ItemRendererFactoryStorage
{
	public var activeItemRenderers:Vector.<IGroupedListItemRenderer> = new <IGroupedListItemRenderer>[];
	public var inactiveItemRenderers:Vector.<IGroupedListItemRenderer> = new <IGroupedListItemRenderer>[];
}

class HeaderRendererFactoryStorage
{
	public var activeHeaderRenderers:Vector.<IGroupedListHeaderRenderer> = new <IGroupedListHeaderRenderer>[];
	public var inactiveHeaderRenderers:Vector.<IGroupedListHeaderRenderer> = new <IGroupedListHeaderRenderer>[];
}

class FooterRendererFactoryStorage
{
	public var activeFooterRenderers:Vector.<IGroupedListFooterRenderer> = new <IGroupedListFooterRenderer>[];
	public var inactiveFooterRenderers:Vector.<IGroupedListFooterRenderer> = new <IGroupedListFooterRenderer>[];
}