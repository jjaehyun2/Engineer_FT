/*
Feathers
Copyright 2012-2021 Bowler Hat LLC. All Rights Reserved.

This program is free software. You can redistribute and/or modify it in
accordance with the terms of the accompanying license agreement.
*/
package feathers.layout
{
	import feathers.core.IValidating;

	import flash.errors.IllegalOperationError;
	import flash.geom.Point;
	import flash.ui.Keyboard;

	import starling.display.DisplayObject;

	/**
	 * Positions items as tiles (equal width and height) from left to right
	 * in multiple rows. Constrained to the suggested width, the tiled rows
	 * layout will change in height as the number of items increases or
	 * decreases.
	 *
	 * @see ../../../help/tiled-rows-layout.html How to use TiledRowsLayout with Feathers containers
	 *
	 * @productversion Feathers 1.0.0
	 */
	public class TiledRowsLayout extends BaseTiledLayout implements IVirtualLayout, IDragDropLayout
	{
		/**
		 * Constructor.
		 */
		public function TiledRowsLayout()
		{
			super();
		}

		/**
		 * Requests that the layout uses a specific number of columns in a row,
		 * if possible. Set to <code>0</code> to calculate the maximum of
		 * columns that will fit in the available space.
		 *
		 * <p>If the view port's explicit or maximum width is not large enough
		 * to fit the requested number of columns, it will use fewer. If the
		 * view port doesn't have an explicit width and the maximum width is
		 * equal to <code>Number.POSITIVE_INFINITY</code>, the width will be
		 * calculated automatically to fit the exact number of requested
		 * columns.</p>
		 *
		 * <p>If paging is enabled, this value will be used to calculate the
		 * number of columns in a page. If paging isn't enabled, this value will
		 * be used to calculate a minimum number of columns, even if there
		 * aren't enough items to fill each column.</p>
		 *
		 * @default 0
		 */
		override public function get requestedColumnCount():int
		{
			//this is an override so that this class can have its own documentation.
			return this._requestedColumnCount;
		}

		/**
		 * Requests that the layout uses a specific number of rows, if possible.
		 * If the view port's explicit or maximum height is not large enough to
		 * fit the requested number of rows, it will use fewer. Set to <code>0</code>
		 * to calculate the number of rows automatically based on width and
		 * height.
		 *
		 * <p>If paging is enabled, this value will be used to calculate the
		 * number of rows in a page. If paging isn't enabled, this value will
		 * be used to calculate a minimum number of rows, even if there aren't
		 * enough items to fill each row.</p>
		 *
		 * @default 0
		 */
		override public function get requestedRowCount():int
		{
			//this is an override so that this class can have its own documentation.
			return this._requestedRowCount;
		}

		/**
		 * If the total combined height of the rows is larger than the height
		 * of the view port, the layout will be split into pages where each
		 * page is filled with the maximum number of rows that may be displayed
		 * without cutting off any items.
		 *
		 * @default feathers.layout.Direction.NONE
		 *
		 * @see feathers.layout.Direction#NONE
		 * @see feathers.layout.Direction#HORIZONTAL
		 * @see feathers.layout.Direction#VERTICAL
		 */
		override public function get paging():String
		{
			//this is an override so that this class can have its own documentation.
			return this._paging;
		}

		/**
		 * If the total width of the tiles in a row (minus padding and gap)
		 * does not fill the entire row, the remaining space will be distributed
		 * to each tile equally.
		 *
		 * <p>If the container using the layout might resize, setting
		 * <code>requestedColumnCount</code> is recommended because the tiles
		 * will resize too, and their dimensions may not be reset.</p>
		 *
		 * @default false
		 *
		 * @see #requestedColumnCount
		 */
		override public function get distributeWidths():Boolean
		{
			return this._distributeWidths;
		}

		/**
		 * If the total height of the tiles in a column (minus padding and gap)
		 * does not fill the entire column, the remaining space will be
		 * distributed to each tile equally.
		 *
		 * <p>If the container using the layout might resize, setting
		 * <code>requestedRowCount</code> is recommended because the tiles
		 * will resize too, and their dimensions may not be reset.</p>
		 *
		 * <p>Note: If the <code>distributeHeights</code> property is set to
		 * <code>true</code>, the <code>useSquareTiles</code> property will be
		 * automatically changed to <code>false</code>.</p>
		 *
		 * @default false
		 *
		 * @see #requestedRowCount
		 * @see #useSquareTiles
		 */
		override public function get distributeHeights():Boolean
		{
			return this._distributeHeights;
		}

		/**
		 * @private
		 */
		override public function set distributeHeights(value:Boolean):void
		{
			super.distributeHeights = value;
			if(value)
			{
				this.useSquareTiles = false;
			}
		}

		/**
		 * @inheritDoc
		 */
		public function layout(items:Vector.<DisplayObject>, viewPortBounds:ViewPortBounds = null, result:LayoutBoundsResult = null):LayoutBoundsResult
		{
			if(!result)
			{
				result = new LayoutBoundsResult();
			}
			if(items.length == 0)
			{
				result.contentX = 0;
				result.contentY = 0;
				result.contentWidth = this._paddingLeft + this._paddingRight;
				result.contentHeight = this._paddingTop + this._paddingBottom;
				result.viewPortWidth = result.contentWidth;
				result.viewPortHeight = result.contentHeight;
				return result;
			}

			var scrollX:Number = viewPortBounds ? viewPortBounds.scrollX : 0;
			var scrollY:Number = viewPortBounds ? viewPortBounds.scrollY : 0;
			var boundsX:Number = viewPortBounds ? viewPortBounds.x : 0;
			var boundsY:Number = viewPortBounds ? viewPortBounds.y : 0;
			var minWidth:Number = viewPortBounds ? viewPortBounds.minWidth : 0;
			var minHeight:Number = viewPortBounds ? viewPortBounds.minHeight : 0;
			var maxWidth:Number = viewPortBounds ? viewPortBounds.maxWidth : Number.POSITIVE_INFINITY;
			var maxHeight:Number = viewPortBounds ? viewPortBounds.maxHeight : Number.POSITIVE_INFINITY;
			var explicitWidth:Number = viewPortBounds ? viewPortBounds.explicitWidth : NaN;
			var explicitHeight:Number = viewPortBounds ? viewPortBounds.explicitHeight : NaN;

			if(this._useVirtualLayout)
			{
				this.prepareTypicalItem();
				var calculatedTypicalItemWidth:Number = this._typicalItem ? this._typicalItem.width : 0;
				var calculatedTypicalItemHeight:Number = this._typicalItem ? this._typicalItem.height : 0;
			}

			this.validateItems(items);

			this._discoveredItemsCache.length = 0;
			var itemCount:int = items.length;
			var tileWidth:Number = 0;
			var tileHeight:Number = 0;
			if(this._useVirtualLayout)
			{
				//a virtual layout assumes that all items are the same size as
				//the typical item, so we don't need to measure every item in
				//that case
				tileWidth = calculatedTypicalItemWidth;
				tileHeight = calculatedTypicalItemHeight;
			}
			else
			{
				for(var i:int = 0; i < itemCount; i++)
				{
					var item:DisplayObject = items[i];
					if(!item)
					{
						continue;
					}
					if(item is ILayoutDisplayObject && !ILayoutDisplayObject(item).includeInLayout)
					{
						continue;
					}
					var itemWidth:Number = item.width;
					var itemHeight:Number = item.height;
					if(itemWidth > tileWidth)
					{
						tileWidth = itemWidth;
					}
					if(itemHeight > tileHeight)
					{
						tileHeight = itemHeight;
					}
				}
			}
			if(tileWidth < 0)
			{
				tileWidth = 0;
			}
			if(tileHeight < 0)
			{
				tileHeight = 0;
			}
			if(this._useSquareTiles)
			{
				if(tileWidth > tileHeight)
				{
					tileHeight = tileWidth;
				}
				else if(tileHeight > tileWidth)
				{
					tileWidth = tileHeight;
				}
			}

			var horizontalTileCount:int = this.calculateHorizontalTileCount(tileWidth,
				explicitWidth, maxWidth, this._paddingLeft + this._paddingRight,
				this._horizontalGap, this._requestedColumnCount, itemCount);
			if(explicitWidth === explicitWidth) //!isNaN
			{
				var availableWidth:Number = explicitWidth;
			}
			else
			{
				availableWidth = this._paddingLeft + this._paddingRight + ((tileWidth + this._horizontalGap) * horizontalTileCount) - this._horizontalGap;
				if(availableWidth < minWidth)
				{
					availableWidth = minWidth;
				}
				else if(availableWidth > maxWidth)
				{
					availableWidth = maxWidth;
				}
			}
			if(this._distributeWidths)
			{
				//distribute remaining space
				tileWidth = (availableWidth - this._paddingLeft - this._paddingRight - (horizontalTileCount * this._horizontalGap) + this._horizontalGap) / horizontalTileCount;
				if(this._useSquareTiles)
				{
					tileHeight = tileWidth;
				}
			}
			var verticalTileCount:int = this.calculateVerticalTileCount(tileHeight,
				explicitHeight, maxHeight, this._paddingTop + this._paddingBottom,
				this._verticalGap, this._requestedRowCount, itemCount,
				horizontalTileCount, this._distributeHeights && !this._useSquareTiles);
			if(explicitHeight === explicitHeight) //!isNaN
			{
				var availableHeight:Number = explicitHeight;
			}
			else
			{
				availableHeight = this._paddingTop + this._paddingBottom + ((tileHeight + this._verticalGap) * verticalTileCount) - this._verticalGap;
				if(availableHeight < minHeight)
				{
					availableHeight = minHeight;
				}
				else if(availableHeight > maxHeight)
				{
					availableHeight = maxHeight;
				}
			}
			if(this._distributeHeights && !this._useSquareTiles)
			{
				//distribute remaining space
				tileHeight = (availableHeight - this._paddingTop - this._paddingBottom - (verticalTileCount * this._verticalGap) + this._verticalGap) / verticalTileCount;
			}

			var totalPageContentWidth:Number = horizontalTileCount * (tileWidth + this._horizontalGap) - this._horizontalGap + this._paddingLeft + this._paddingRight;
			var totalPageContentHeight:Number = verticalTileCount * (tileHeight + this._verticalGap) - this._verticalGap + this._paddingTop + this._paddingBottom;

			var startX:Number = boundsX + this._paddingLeft;
			var startY:Number = boundsY + this._paddingTop;

			var perPage:int = horizontalTileCount * verticalTileCount;
			var pageIndex:int = 0;
			var nextPageStartIndex:int = perPage;
			var pageStartX:Number = startX;
			var positionX:Number = startX;
			var positionY:Number = startY;
			var itemIndex:int = 0;
			var discoveredItemsCachePushIndex:int = 0;
			for(i = 0; i < itemCount; i++)
			{
				item = items[i];
				if(item is ILayoutDisplayObject && !ILayoutDisplayObject(item).includeInLayout)
				{
					continue;
				}
				if(itemIndex != 0 && itemIndex % horizontalTileCount == 0)
				{
					positionX = pageStartX;
					positionY += tileHeight + this._verticalGap;
				}
				if(itemIndex == nextPageStartIndex)
				{
					//we're starting a new page, so handle alignment of the
					//items on the current page and update the positions
					if(this._paging !== Direction.NONE)
					{
						var discoveredItems:Vector.<DisplayObject> = this._useVirtualLayout ? this._discoveredItemsCache : items;
						var discoveredItemsFirstIndex:int = this._useVirtualLayout ? 0 : (itemIndex - perPage);
						var discoveredItemsLastIndex:int = this._useVirtualLayout ? (this._discoveredItemsCache.length - 1) : (itemIndex - 1);
						this.applyHorizontalAlign(discoveredItems, discoveredItemsFirstIndex, discoveredItemsLastIndex, totalPageContentWidth, availableWidth);
						this.applyVerticalAlign(discoveredItems, discoveredItemsFirstIndex, discoveredItemsLastIndex, totalPageContentHeight, availableHeight);
						this._discoveredItemsCache.length = 0;
						discoveredItemsCachePushIndex = 0;
					}
					pageIndex++;
					nextPageStartIndex += perPage;

					//we can use availableWidth and availableHeight here without
					//checking if they're NaN because we will never reach a
					//new page without them already being calculated.
					if(this._paging === Direction.HORIZONTAL)
					{
						positionX = pageStartX = startX + availableWidth * pageIndex;
						positionY = startY;
					}
					else if(this._paging === Direction.VERTICAL)
					{
						positionY = startY + availableHeight * pageIndex;
					}
				}
				if(item)
				{
					switch(this._tileHorizontalAlign)
					{
						case HorizontalAlign.JUSTIFY:
						{
							item.x = item.pivotX + positionX;
							item.width = tileWidth;
							break;
						}
						case HorizontalAlign.LEFT:
						{
							item.x = item.pivotX + positionX;
							break;
						}
						case HorizontalAlign.RIGHT:
						{
							item.x = item.pivotX + positionX + tileWidth - item.width;
							break;
						}
						default: //center or unknown
						{
							item.x = item.pivotX + positionX + Math.round((tileWidth - item.width) / 2);
						}
					}
					switch(this._tileVerticalAlign)
					{
						case VerticalAlign.JUSTIFY:
						{
							item.y = item.pivotY + positionY;
							item.height = tileHeight;
							break;
						}
						case VerticalAlign.TOP:
						{
							item.y = item.pivotY + positionY;
							break;
						}
						case VerticalAlign.BOTTOM:
						{
							item.y = item.pivotY + positionY + tileHeight - item.height;
							break;
						}
						default: //middle or unknown
						{
							item.y = item.pivotY + positionY + Math.round((tileHeight - item.height) / 2);
						}
					}
					if(this._useVirtualLayout)
					{
						this._discoveredItemsCache[discoveredItemsCachePushIndex] = item;
						discoveredItemsCachePushIndex++;
					}
				}
				positionX += tileWidth + this._horizontalGap;
				itemIndex++;
			}
			//align the last page
			if(this._paging !== Direction.NONE)
			{
				discoveredItems = this._useVirtualLayout ? this._discoveredItemsCache : items;
				discoveredItemsFirstIndex = this._useVirtualLayout ? 0 : (nextPageStartIndex - perPage);
				discoveredItemsLastIndex = this._useVirtualLayout ? (discoveredItems.length - 1) : (i - 1);
				this.applyHorizontalAlign(discoveredItems, discoveredItemsFirstIndex, discoveredItemsLastIndex, totalPageContentWidth, availableWidth);
				this.applyVerticalAlign(discoveredItems, discoveredItemsFirstIndex, discoveredItemsLastIndex, totalPageContentHeight, availableHeight);
			}

			if(this._paging === Direction.HORIZONTAL)
			{
				var totalWidth:Number = Math.ceil(itemCount / perPage) * availableWidth;
			}
			else //vertical or none
			{
				totalWidth = totalPageContentWidth;
			}
			if(this._paging === Direction.HORIZONTAL)
			{
				var totalHeight:Number = availableHeight;
			}
			else if(this._paging === Direction.VERTICAL)
			{
				totalHeight = Math.ceil(itemCount / perPage) * availableHeight;
			}
			else //none
			{
				totalHeight = positionY + tileHeight + this._paddingBottom;
				if(totalHeight < totalPageContentHeight)
				{
					totalHeight = totalPageContentHeight;
				}
			}

			if(this._paging === Direction.NONE)
			{
				discoveredItems = this._useVirtualLayout ? this._discoveredItemsCache : items;
				discoveredItemsLastIndex = discoveredItems.length - 1;
				this.applyHorizontalAlign(discoveredItems, 0, discoveredItemsLastIndex, totalWidth, availableWidth);
				this.applyVerticalAlign(discoveredItems, 0, discoveredItemsLastIndex, totalHeight, availableHeight);
			}
			this._discoveredItemsCache.length = 0;

			result.contentX = 0;
			result.contentY = 0;
			result.contentWidth = totalWidth;
			result.contentHeight = totalHeight;
			result.viewPortWidth = availableWidth;
			result.viewPortHeight = availableHeight;

			return result;
		}

		/**
		 * @inheritDoc
		 */
		public function measureViewPort(itemCount:int, viewPortBounds:ViewPortBounds = null, result:Point = null):Point
		{
			if(!result)
			{
				result = new Point();
			}
			if(!this._useVirtualLayout)
			{
				throw new IllegalOperationError("measureViewPort() may be called only if useVirtualLayout is true.");
			}

			var explicitWidth:Number = viewPortBounds ? viewPortBounds.explicitWidth : NaN;
			var explicitHeight:Number = viewPortBounds ? viewPortBounds.explicitHeight : NaN;
			var needsWidth:Boolean = explicitWidth !== explicitWidth; //isNaN;
			var needsHeight:Boolean = explicitHeight !== explicitHeight; //isNaN
			if(!needsWidth && !needsHeight)
			{
				result.x = explicitWidth;
				result.y = explicitHeight;
				return result;
			}
			var boundsX:Number = viewPortBounds ? viewPortBounds.x : 0;
			var boundsY:Number = viewPortBounds ? viewPortBounds.y : 0;
			var minWidth:Number = viewPortBounds ? viewPortBounds.minWidth : 0;
			var minHeight:Number = viewPortBounds ? viewPortBounds.minHeight : 0;
			var maxWidth:Number = viewPortBounds ? viewPortBounds.maxWidth : Number.POSITIVE_INFINITY;
			var maxHeight:Number = viewPortBounds ? viewPortBounds.maxHeight : Number.POSITIVE_INFINITY;

			this.prepareTypicalItem();
			var calculatedTypicalItemWidth:Number = this._typicalItem ? this._typicalItem.width : 0;
			var calculatedTypicalItemHeight:Number = this._typicalItem ? this._typicalItem.height : 0;

			var tileWidth:Number = calculatedTypicalItemWidth;
			var tileHeight:Number = calculatedTypicalItemHeight;
			if(tileWidth < 0)
			{
				tileWidth = 0;
			}
			if(tileHeight < 0)
			{
				tileHeight = 0;
			}
			if(this._useSquareTiles)
			{
				if(tileWidth > tileHeight)
				{
					tileHeight = tileWidth;
				}
				else if(tileHeight > tileWidth)
				{
					tileWidth = tileHeight;
				}
			}

			var horizontalTileCount:int = this.calculateHorizontalTileCount(tileWidth,
				explicitWidth, maxWidth, this._paddingLeft + this._paddingRight,
				this._horizontalGap, this._requestedColumnCount, itemCount);
			var verticalTileCount:int = this.calculateVerticalTileCount(tileHeight,
				explicitHeight, maxHeight, this._paddingTop + this._paddingBottom,
				this._verticalGap, this._requestedRowCount, itemCount,
				horizontalTileCount, this._distributeHeights && !this._useSquareTiles);
			if(explicitWidth === explicitWidth) //!isNaN
			{
				var availableWidth:Number = explicitWidth;
			}
			else
			{
				availableWidth = this._paddingLeft + this._paddingRight + ((tileWidth + this._horizontalGap) * horizontalTileCount) - this._horizontalGap;
				if(availableWidth < minWidth)
				{
					availableWidth = minWidth;
				}
				else if(availableWidth > maxWidth)
				{
					availableWidth = maxWidth;
				}
			}
			if(explicitHeight === explicitHeight) //!isNaN
			{
				var availableHeight:Number = explicitHeight;
			}
			else
			{
				availableHeight = this._paddingTop + this._paddingBottom + ((tileHeight + this._verticalGap) * verticalTileCount) - this._verticalGap;
				if(availableHeight < minHeight)
				{
					availableHeight = minHeight;
				}
				else if(availableHeight > maxHeight)
				{
					availableHeight = maxHeight;
				}
			}

			var totalPageContentWidth:Number = horizontalTileCount * (tileWidth + this._horizontalGap) - this._horizontalGap + this._paddingLeft + this._paddingRight;
			var totalPageContentHeight:Number = verticalTileCount * (tileHeight + this._verticalGap) - this._verticalGap + this._paddingTop + this._paddingBottom;

			var startX:Number = boundsX + this._paddingLeft;
			var startY:Number = boundsY + this._paddingTop;

			var perPage:int = horizontalTileCount * verticalTileCount;
			var pageIndex:int = 0;
			var nextPageStartIndex:int = perPage;
			var pageStartX:Number = startX;
			var positionX:Number = startX;
			var positionY:Number = startY;
			for(var i:int = 0; i < itemCount; i++)
			{
				if(i != 0 && i % horizontalTileCount == 0)
				{
					positionX = pageStartX;
					positionY += tileHeight + this._verticalGap;
				}
				if(i == nextPageStartIndex)
				{
					pageIndex++;
					nextPageStartIndex += perPage;

					//we can use availableWidth and availableHeight here without
					//checking if they're NaN because we will never reach a
					//new page without them already being calculated.
					if(this._paging === Direction.HORIZONTAL)
					{
						positionX = pageStartX = startX + availableWidth * pageIndex;
						positionY = startY;
					}
					else if(this._paging === Direction.VERTICAL)
					{
						positionY = startY + availableHeight * pageIndex;
					}
				}
			}

			if(this._paging === Direction.HORIZONTAL)
			{
				var totalWidth:Number = Math.ceil(itemCount / perPage) * availableWidth;
			}
			else
			{
				totalWidth = totalPageContentWidth;
			}
			if(this._paging === Direction.HORIZONTAL)
			{
				var totalHeight:Number = availableHeight;
			}
			else if(this._paging === Direction.VERTICAL)
			{
				totalHeight = Math.ceil(itemCount / perPage) * availableHeight;
			}
			else
			{
				totalHeight = positionY + tileHeight + this._paddingBottom;
				if(totalHeight < totalPageContentHeight)
				{
					totalHeight = totalPageContentHeight;
				}
			}

			if(needsWidth)
			{
				var resultX:Number = totalWidth;
				if(resultX < minWidth)
				{
					resultX = minWidth;
				}
				else if(resultX > maxWidth)
				{
					resultX = maxWidth;
				}
				result.x = resultX;
			}
			else
			{
				result.x = explicitWidth;
			}
			if(needsHeight)
			{
				var resultY:Number = totalHeight;
				if(resultY < minHeight)
				{
					resultY = minHeight;
				}
				else if(resultY > maxHeight)
				{
					resultY = maxHeight;
				}
				result.y = resultY;
			}
			else
			{
				result.y = explicitHeight;
			}
			return result;
		}

		/**
		 * @inheritDoc
		 */
		public function getVisibleIndicesAtScrollPosition(scrollX:Number, scrollY:Number, width:Number, height:Number, itemCount:int, result:Vector.<int> = null):Vector.<int>
		{
			if(result)
			{
				result.length = 0;
			}
			else
			{
				result = new <int>[];
			}
			if(!this._useVirtualLayout)
			{
				throw new IllegalOperationError("getVisibleIndicesAtScrollPosition() may be called only if useVirtualLayout is true.");
			}

			if(this._paging === Direction.HORIZONTAL)
			{
				this.getVisibleIndicesAtScrollPositionWithHorizontalPaging(scrollX, scrollY, width, height, itemCount, result);
			}
			else if(this._paging === Direction.VERTICAL)
			{
				this.getVisibleIndicesAtScrollPositionWithVerticalPaging(scrollX, scrollY, width, height, itemCount, result);
			}
			else //none
			{
				this.getVisibleIndicesAtScrollPositionWithoutPaging(scrollX, scrollY, width, height, itemCount, result);
			}

			return result;
		}

		/**
		 * @inheritDoc
		 */
		public function calculateNavigationDestination(items:Vector.<DisplayObject>, index:int, keyCode:uint, bounds:LayoutBoundsResult):int
		{
			var itemCount:int = items.length;
			if(keyCode == Keyboard.HOME)
			{
				return 0;
			}
			else if(keyCode == Keyboard.END)
			{
				return itemCount - 1;
			}

			if(this._useVirtualLayout)
			{
				this.prepareTypicalItem();
				var calculatedTypicalItemWidth:Number = this._typicalItem ? this._typicalItem.width : 0;
				var calculatedTypicalItemHeight:Number = this._typicalItem ? this._typicalItem.height : 0;
			}

			this.validateItems(items);

			this._discoveredItemsCache.length = 0;
			var tileWidth:Number = 0;
			var tileHeight:Number = 0;
			if(this._useVirtualLayout)
			{
				//a virtual layout assumes that all items are the same size as
				//the typical item, so we don't need to measure every item in
				//that case
				tileWidth = calculatedTypicalItemWidth;
				tileHeight = calculatedTypicalItemHeight;
			}
			else
			{
				for(var i:int = 0; i < itemCount; i++)
				{
					var item:DisplayObject = items[i];
					if(!item)
					{
						continue;
					}
					if(item is ILayoutDisplayObject && !ILayoutDisplayObject(item).includeInLayout)
					{
						continue;
					}
					var itemWidth:Number = item.width;
					var itemHeight:Number = item.height;
					if(itemWidth > tileWidth)
					{
						tileWidth = itemWidth;
					}
					if(itemHeight > tileHeight)
					{
						tileHeight = itemHeight;
					}
				}
			}
			if(tileWidth < 0)
			{
				tileWidth = 0;
			}
			if(tileHeight < 0)
			{
				tileHeight = 0;
			}
			if(this._useSquareTiles)
			{
				if(tileWidth > tileHeight)
				{
					tileHeight = tileWidth;
				}
				else if(tileHeight > tileWidth)
				{
					tileWidth = tileHeight;
				}
			}

			var availableWidth:Number = bounds.viewPortWidth;
			var horizontalTileCount:int = this.calculateHorizontalTileCount(tileWidth,
				availableWidth, Number.POSITIVE_INFINITY, this._paddingLeft + this._paddingRight,
				this._horizontalGap, this._requestedColumnCount, itemCount);
			var pageHorizontalTileCount:int = horizontalTileCount;
			var pageVerticalTileCount:int = this.calculateVerticalTileCount(tileHeight,
				bounds.viewPortHeight, Number.POSITIVE_INFINITY, this._paddingTop + this._paddingBottom,
				this._verticalGap, this._requestedRowCount, itemCount,
				pageHorizontalTileCount, this._distributeHeights && !this._useSquareTiles);
			var verticalTileCount:int = Math.ceil(itemCount / horizontalTileCount);
			var rowIndex:int = index / pageHorizontalTileCount;
			var columnIndex:int = index % pageHorizontalTileCount;
			if(this._paging === Direction.HORIZONTAL)
			{
				verticalTileCount = pageVerticalTileCount;
				var perPage:Number = pageHorizontalTileCount * pageVerticalTileCount;
				var pageCount:int = Math.ceil(itemCount / perPage);
				horizontalTileCount *= pageCount;
				while(rowIndex >= verticalTileCount)
				{
					rowIndex -= verticalTileCount;
					columnIndex += pageHorizontalTileCount;
				}
			}

			if(keyCode == Keyboard.PAGE_UP)
			{
				if(this._paging === Direction.HORIZONTAL)
				{
					columnIndex -= pageHorizontalTileCount;
				}
				else
				{
					rowIndex -= pageVerticalTileCount;
				}
			}
			else if(keyCode == Keyboard.PAGE_DOWN)
			{
				if(this._paging === Direction.HORIZONTAL)
				{
					columnIndex += pageHorizontalTileCount;
				}
				else
				{
					rowIndex += pageVerticalTileCount;
				}
			}
			else if(keyCode == Keyboard.UP)
			{
				rowIndex--;
			}
			else if(keyCode == Keyboard.DOWN)
			{
				rowIndex++;
			}
			else if(keyCode == Keyboard.LEFT)
			{
				columnIndex--;
			}
			else if(keyCode == Keyboard.RIGHT)
			{
				columnIndex++;
			}
			if(rowIndex < 0)
			{
				rowIndex = 0;
			}
			else if(rowIndex >= verticalTileCount)
			{
				rowIndex = verticalTileCount - 1;
			}
			if(columnIndex < 0)
			{
				columnIndex = 0;
			}
			else if(columnIndex >= horizontalTileCount)
			{
				columnIndex = horizontalTileCount - 1;
			}
			if(this._paging === Direction.HORIZONTAL)
			{
				while(columnIndex >= pageHorizontalTileCount)
				{
					columnIndex -= pageHorizontalTileCount;
					rowIndex += verticalTileCount;
				}
			}
			var result:int = rowIndex * pageHorizontalTileCount + columnIndex;
			if(result >= itemCount)
			{
				//nothing at this column on the next row
				result = itemCount - 1;
			}
			return result;
		}

		/**
		 * @inheritDoc
		 */
		public function getNearestScrollPositionForIndex(index:int, scrollX:Number, scrollY:Number, items:Vector.<DisplayObject>,
			x:Number, y:Number, width:Number, height:Number, result:Point = null):Point
		{
			return this.calculateScrollPositionForIndex(index, items, x, y, width, height, result, true, scrollX, scrollY);
		}

		/**
		 * @inheritDoc
		 */
		public function getScrollPositionForIndex(index:int, items:Vector.<DisplayObject>, x:Number, y:Number, width:Number, height:Number, result:Point = null):Point
		{
			return this.calculateScrollPositionForIndex(index, items, x, y, width, height, result, false);
		}

		/**
		 * @inheritDoc
		 */
		public function getDropIndex(x:Number, y:Number, items:Vector.<DisplayObject>,
			boundsX:Number, boundsY:Number, width:Number, height:Number):int
		{
			if(this._useVirtualLayout)
			{
				this.prepareTypicalItem();
				var calculatedTypicalItemWidth:Number = this._typicalItem ? this._typicalItem.width : 0;
				var calculatedTypicalItemHeight:Number = this._typicalItem ? this._typicalItem.height : 0;
			}

			var itemCount:int = items.length;
			var tileWidth:Number = this._useVirtualLayout ? calculatedTypicalItemWidth : 0;
			var tileHeight:Number = this._useVirtualLayout ? calculatedTypicalItemHeight : 0;
			//a virtual layout assumes that all items are the same size as
			//the typical item, so we don't need to measure every item in
			//that case
			if(!this._useVirtualLayout)
			{
				for(var i:int = 0; i < itemCount; i++)
				{
					var item:DisplayObject = items[i];
					if(!item)
					{
						continue;
					}
					if(item is ILayoutDisplayObject && !ILayoutDisplayObject(item).includeInLayout)
					{
						continue;
					}
					var itemWidth:Number = item.width;
					var itemHeight:Number = item.height;
					if(itemWidth > tileWidth)
					{
						tileWidth = itemWidth;
					}
					if(itemHeight > tileHeight)
					{
						tileHeight = itemHeight;
					}
				}
			}
			if(tileWidth < 0)
			{
				tileWidth = 0;
			}
			if(tileHeight < 0)
			{
				tileHeight = 0;
			}
			if(this._useSquareTiles)
			{
				if(tileWidth > tileHeight)
				{
					tileHeight = tileWidth;
				}
				else if(tileHeight > tileWidth)
				{
					tileWidth = tileHeight;
				}
			}
			var horizontalTileCount:int = (width - this._paddingLeft - this._paddingRight + this._horizontalGap) / (tileWidth + this._horizontalGap);
			if(horizontalTileCount < 1)
			{
				horizontalTileCount = 1;
			}
			else if(this._requestedColumnCount > 0 && horizontalTileCount > this._requestedColumnCount)
			{
				horizontalTileCount = this._requestedColumnCount;
			}
			var verticalTileCount:int = (height - this._paddingTop - this._paddingBottom + this._verticalGap) / (tileHeight + this._verticalGap);
			if(verticalTileCount < 1)
			{
				verticalTileCount = 1;
			}
			else if(this._requestedRowCount > 0 && verticalTileCount > this._requestedRowCount)
			{
				verticalTileCount = this._requestedRowCount;
			}
			var perPage:Number = horizontalTileCount * verticalTileCount;
			var startX:Number = boundsX + this._paddingLeft;
			var actualHorizontalTileCount:int = horizontalTileCount;
			if(actualHorizontalTileCount > itemCount)
			{
				actualHorizontalTileCount = itemCount;
			}
			if(this._horizontalAlign == HorizontalAlign.RIGHT)
			{
				startX = boundsX + this._paddingLeft + (width - this._paddingLeft - this._paddingRight) -
					((actualHorizontalTileCount * (tileWidth + this._horizontalGap)) - this._horizontalGap);
			}
			else if(this._horizontalAlign == HorizontalAlign.CENTER)
			{
				startX = boundsX + this._paddingLeft + ((width - this._paddingLeft - this._paddingRight) -
					((actualHorizontalTileCount * (tileWidth + this._horizontalGap)) - this._horizontalGap)) / 2;
			}
			var startY:Number = boundsY + this._paddingTop;
			if(this._paging != Direction.NONE || itemCount <= perPage)
			{
				var actualVerticalTileCount:int = verticalTileCount;
				if(itemCount <= perPage)
				{
					actualVerticalTileCount = Math.ceil(itemCount / actualHorizontalTileCount);
				}
				if(this._verticalAlign == VerticalAlign.BOTTOM)
				{
					startY = boundsY + this._paddingTop + (height - this._paddingTop - this._paddingBottom) -
						((actualVerticalTileCount * (tileHeight + this._verticalGap)) - this._verticalGap);
				}
				else if(this._verticalAlign == VerticalAlign.MIDDLE)
				{
					startY = boundsY + this._paddingTop + ((height - this._paddingTop - this._paddingBottom) -
						((actualVerticalTileCount * (tileHeight + this._verticalGap)) - this._verticalGap)) / 2;
				}
			}
			var pageIndex:int = 0;
			var rowIndex:int = 0;
			var lastRowIndex:int = int((itemCount - 1) / horizontalTileCount);
			var nextPageStartIndex:int = perPage;
			var pageStartX:Number = startX;
			var positionX:Number = startX;
			var positionY:Number = startY;
			for(i = 0; i < itemCount; i++)
			{
				item = items[i];
				if(item is ILayoutDisplayObject && !ILayoutDisplayObject(item).includeInLayout)
				{
					continue;
				}
				if(i != 0 && i % horizontalTileCount == 0)
				{
					if((x < (pageStartX + width)) &&
						(y < (positionY + tileHeight + (this._verticalGap / 2))))
					{
						//we're at the end of the previous row (but we also make
						//sure that we're not on the next page)
						return i;
					}
					positionX = pageStartX;
					positionY += tileHeight + this._verticalGap;
					rowIndex++;
				}
				if(i == nextPageStartIndex)
				{
					pageIndex++;
					nextPageStartIndex += perPage;

					//we can use availableWidth and availableHeight here without
					//checking if they're NaN because we will never reach a
					//new page without them already being calculated.
					if(this._paging === Direction.HORIZONTAL)
					{
						positionX = pageStartX = startX + width * pageIndex;
						positionY = startY;
					}
					else if(this._paging === Direction.VERTICAL)
					{
						positionY = startY + height * pageIndex;
					}
				}
				if((x < (positionX + (tileWidth / 2))) &&
					((y < (positionY + tileHeight + (this._verticalGap / 2))) || (rowIndex == lastRowIndex)))
				{
					return i;
				}
				positionX += tileWidth + this._horizontalGap;
			}
			return i;
		}

		/**
		 * @inheritDoc
		 */
		public function positionDropIndicator(dropIndicator:DisplayObject, index:int,
			x:Number, y:Number, items:Vector.<DisplayObject>, width:Number, height:Number):void
		{
			if(this._useVirtualLayout)
			{
				this.prepareTypicalItem();
				var calculatedTypicalItemWidth:Number = this._typicalItem ? this._typicalItem.width : 0;
				var calculatedTypicalItemHeight:Number = this._typicalItem ? this._typicalItem.height : 0;
			}

			var itemCount:int = items.length;
			var tileWidth:Number = this._useVirtualLayout ? calculatedTypicalItemWidth : 0;
			var tileHeight:Number = this._useVirtualLayout ? calculatedTypicalItemHeight : 0;
			//a virtual layout assumes that all items are the same size as
			//the typical item, so we don't need to measure every item in
			//that case
			if(!this._useVirtualLayout)
			{
				for(var i:int = 0; i < itemCount; i++)
				{
					var item:DisplayObject = items[i];
					if(!item)
					{
						continue;
					}
					if(item is ILayoutDisplayObject && !ILayoutDisplayObject(item).includeInLayout)
					{
						continue;
					}
					var itemWidth:Number = item.width;
					var itemHeight:Number = item.height;
					if(itemWidth > tileWidth)
					{
						tileWidth = itemWidth;
					}
					if(itemHeight > tileHeight)
					{
						tileHeight = itemHeight;
					}
				}
			}
			if(tileWidth < 0)
			{
				tileWidth = 0;
			}
			if(tileHeight < 0)
			{
				tileHeight = 0;
			}
			if(this._useSquareTiles)
			{
				if(tileWidth > tileHeight)
				{
					tileHeight = tileWidth;
				}
				else if(tileHeight > tileWidth)
				{
					tileWidth = tileHeight;
				}
			}
			var horizontalTileCount:int = (width - this._paddingLeft - this._paddingRight + this._horizontalGap) / (tileWidth + this._horizontalGap);
			if(horizontalTileCount < 1)
			{
				horizontalTileCount = 1;
			}
			else if(this._requestedColumnCount > 0 && horizontalTileCount > this._requestedColumnCount)
			{
				horizontalTileCount = this._requestedColumnCount;
			}
			var verticalTileCount:int = (height - this._paddingTop - this._paddingBottom + this._verticalGap) / (tileHeight + this._verticalGap);
			if(verticalTileCount < 1)
			{
				verticalTileCount = 1;
			}
			else if(this._requestedRowCount > 0 && verticalTileCount > this._requestedRowCount)
			{
				verticalTileCount = this._requestedRowCount;
			}
			var perPage:Number = horizontalTileCount * verticalTileCount;
			var startX:Number = this._paddingLeft;
			var actualHorizontalTileCount:int = horizontalTileCount;
			if(actualHorizontalTileCount > itemCount)
			{
				actualHorizontalTileCount = itemCount;
			}
			if(this._horizontalAlign == HorizontalAlign.RIGHT)
			{
				startX = this._paddingLeft + (width - this._paddingLeft - this._paddingRight) -
					((actualHorizontalTileCount * (tileWidth + this._horizontalGap)) - this._horizontalGap);
			}
			else if(this._horizontalAlign == HorizontalAlign.CENTER)
			{
				startX = this._paddingLeft + ((width - this._paddingLeft - this._paddingRight) -
					((actualHorizontalTileCount * (tileWidth + this._horizontalGap)) - this._horizontalGap)) / 2;
			}
			var startY:Number = this._paddingTop;
			if(this._paging != Direction.NONE || itemCount <= perPage)
			{
				var actualVerticalTileCount:int = verticalTileCount;
				if(itemCount <= perPage)
				{
					actualVerticalTileCount = Math.ceil(itemCount / actualHorizontalTileCount);
				}
				if(this._verticalAlign == VerticalAlign.BOTTOM)
				{
					startY = this._paddingTop + (height - this._paddingTop - this._paddingBottom) -
						((actualVerticalTileCount * (tileHeight + this._verticalGap)) - this._verticalGap);
				}
				else if(this._verticalAlign == VerticalAlign.MIDDLE)
				{
					startY = this._paddingTop + ((height - this._paddingTop - this._paddingBottom) -
						((actualVerticalTileCount * (tileHeight + this._verticalGap)) - this._verticalGap)) / 2;
				}
			}
			var pageIndex:int = 0;
			var rowIndex:int = 0;
			var lastRowIndex:int = int((itemCount - 1) / horizontalTileCount);
			var nextPageStartIndex:int = perPage;
			var pageStartX:Number = startX;
			var positionX:Number = startX;
			var positionY:Number = startY;
			var rowItemCount:int = 0;
			for(i = 0; i < itemCount; i++)
			{
				item = items[i];
				if(item is ILayoutDisplayObject && !ILayoutDisplayObject(item).includeInLayout)
				{
					continue;
				}
				if(i != 0 && i % horizontalTileCount == 0)
				{
					//start of a new row
					positionX = pageStartX;
					positionY += tileHeight + this._verticalGap;
					rowItemCount = 0;
					rowIndex++;
				}
				if(i == nextPageStartIndex)
				{
					//start of a new page
					pageIndex++;
					nextPageStartIndex += perPage;
					if(this._paging === Direction.HORIZONTAL)
					{
						positionX = pageStartX = startX + width * pageIndex;
						positionY = startY;
					}
					else if(this._paging === Direction.VERTICAL)
					{
						positionY = startY + height * pageIndex;
					}
				}
				if((x < (positionX + (tileWidth / 2))) &&
					((y < (positionY + tileHeight + (this._verticalGap / 2))) || (rowIndex == lastRowIndex)))
				{
					dropIndicator.x = positionX - dropIndicator.width / 2;
					dropIndicator.y = positionY;
					dropIndicator.height = tileHeight;
					return;
				}
				positionX += tileWidth + this._horizontalGap;

				if(rowItemCount > 0 &&
					(x < (positionX + (tileWidth / 2))) &&
					(x < (pageStartX + width)) && //not on next page
					(positionX + tileWidth) > (width - this._paddingRight) &&
					(y < (positionY + tileHeight + (this._verticalGap / 2))))
				{
					//index on next row, but position drop indicator at the end
					//of the current row
					dropIndicator.x = positionX - this._horizontalGap - dropIndicator.width / 2;
					dropIndicator.y = positionY;
					dropIndicator.height = tileHeight;
					return;
				}
				rowItemCount++;
			}
			dropIndicator.x = positionX - dropIndicator.width / 2;
			dropIndicator.y = positionY;
			dropIndicator.height = tileHeight;
		}

		/**
		 * @private
		 */
		protected function applyHorizontalAlign(items:Vector.<DisplayObject>, startIndex:int, endIndex:int, totalItemWidth:Number, availableWidth:Number):void
		{
			if(totalItemWidth >= availableWidth)
			{
				return;
			}
			var horizontalAlignOffsetX:Number = 0;
			if(this._horizontalAlign === HorizontalAlign.RIGHT)
			{
				horizontalAlignOffsetX = availableWidth - totalItemWidth;
			}
			else if(this._horizontalAlign !== HorizontalAlign.LEFT)
			{
				//we're going to default to center if we encounter an
				//unknown value
				horizontalAlignOffsetX = Math.round((availableWidth - totalItemWidth) / 2);
			}
			if(horizontalAlignOffsetX != 0)
			{
				for(var i:int = startIndex; i <= endIndex; i++)
				{
					var item:DisplayObject = items[i];
					if(item is ILayoutDisplayObject && !ILayoutDisplayObject(item).includeInLayout)
					{
						continue;
					}
					item.x += horizontalAlignOffsetX;
				}
			}
		}

		/**
		 * @private
		 */
		protected function applyVerticalAlign(items:Vector.<DisplayObject>, startIndex:int, endIndex:int, totalItemHeight:Number, availableHeight:Number):void
		{
			if(totalItemHeight >= availableHeight)
			{
				return;
			}
			var verticalAlignOffsetY:Number = 0;
			if(this._verticalAlign === VerticalAlign.BOTTOM)
			{
				verticalAlignOffsetY = availableHeight - totalItemHeight;
			}
			else if(this._verticalAlign === VerticalAlign.MIDDLE)
			{
				verticalAlignOffsetY = Math.round((availableHeight - totalItemHeight) / 2);
			}
			if(verticalAlignOffsetY != 0)
			{
				for(var i:int = startIndex; i <= endIndex; i++)
				{
					var item:DisplayObject = items[i];
					if(item is ILayoutDisplayObject && !ILayoutDisplayObject(item).includeInLayout)
					{
						continue;
					}
					item.y += verticalAlignOffsetY;
				}
			}
		}

		/**
		 * @private
		 */
		protected function getVisibleIndicesAtScrollPositionWithHorizontalPaging(scrollX:Number, scrollY:Number, width:Number, height:Number, itemCount:int, result:Vector.<int>):void
		{
			this.prepareTypicalItem();
			var calculatedTypicalItemWidth:Number = this._typicalItem ? this._typicalItem.width : 0;
			var calculatedTypicalItemHeight:Number = this._typicalItem ? this._typicalItem.height : 0;

			var tileWidth:Number = calculatedTypicalItemWidth;
			var tileHeight:Number = calculatedTypicalItemHeight;
			if(tileWidth < 0)
			{
				tileWidth = 0;
			}
			if(tileHeight < 0)
			{
				tileHeight = 0;
			}
			if(this._useSquareTiles)
			{
				if(tileWidth > tileHeight)
				{
					tileHeight = tileWidth;
				}
				else if(tileHeight > tileWidth)
				{
					tileWidth = tileHeight;
				}
			}
			var horizontalTileCount:int = this.calculateHorizontalTileCount(tileWidth,
				width, width, this._paddingLeft + this._paddingRight,
				this._horizontalGap, this._requestedColumnCount, itemCount);
			if(this._distributeWidths)
			{
				tileWidth = (width - this._paddingLeft - this._paddingRight - (horizontalTileCount * this._horizontalGap) + this._horizontalGap) / horizontalTileCount;
				if(this._useSquareTiles)
				{
					tileHeight = tileWidth;
				}
			}
			var verticalTileCount:int = this.calculateVerticalTileCount(tileHeight,
				height, height, this._paddingTop + this._paddingBottom,
				this._verticalGap, this._requestedRowCount, itemCount,
				horizontalTileCount, this._distributeHeights && !this._useSquareTiles);
			if(this._distributeHeights && !this._useSquareTiles)
			{
				tileHeight = (height - this._paddingTop - this._paddingBottom - (verticalTileCount * this._verticalGap) + this._verticalGap) / verticalTileCount;
			}
			var perPage:int = horizontalTileCount * verticalTileCount;
			var minimumItemCount:int = perPage + 2 * verticalTileCount;
			if(minimumItemCount > itemCount)
			{
				minimumItemCount = itemCount;
			}

			var startPageIndex:int = Math.round(scrollX / width);
			var minimum:int = startPageIndex * perPage;
			var totalRowWidth:Number = horizontalTileCount * (tileWidth + this._horizontalGap) - this._horizontalGap;
			var leftSideOffset:Number = 0;
			var rightSideOffset:Number = 0;
			if(totalRowWidth < width)
			{
				if(this._horizontalAlign === HorizontalAlign.RIGHT)
				{
					leftSideOffset = width - this._paddingLeft - this._paddingRight - totalRowWidth;
					rightSideOffset = 0;
				}
				else if(this._horizontalAlign === HorizontalAlign.CENTER)
				{
					leftSideOffset = rightSideOffset = Math.round((width - this._paddingLeft - this._paddingRight - totalRowWidth) / 2);
				}
				else //left
				{
					leftSideOffset = 0;
					rightSideOffset = width - this._paddingLeft - this._paddingRight - totalRowWidth;
				}
			}
			var columnOffset:int = 0;
			var pageStartPosition:Number = startPageIndex * width;
			var partialPageSize:Number = scrollX - pageStartPosition;
			if(partialPageSize < 0)
			{
				partialPageSize = -partialPageSize - this._paddingRight - rightSideOffset;
				if(partialPageSize < 0)
				{
					partialPageSize = 0;
				}
				columnOffset = -Math.floor(partialPageSize / (tileWidth + this._horizontalGap)) - 1;
				minimum += -perPage + horizontalTileCount + columnOffset;
			}
			else if(partialPageSize > 0)
			{
				partialPageSize = partialPageSize - this._paddingLeft - leftSideOffset;
				if(partialPageSize < 0)
				{
					partialPageSize = 0;
				}
				columnOffset = Math.floor(partialPageSize / (tileWidth + this._horizontalGap));
				minimum += columnOffset;
			}
			if(minimum < 0)
			{
				minimum = 0;
				columnOffset = 0;
			}
			if(minimum + minimumItemCount >= itemCount)
			{
				var resultPushIndex:int = result.length;
				//an optimized path when we're on or near the last page
				minimum = itemCount - minimumItemCount;
				for(var i:int = minimum; i < itemCount; i++)
				{
					result[resultPushIndex] = i;
					resultPushIndex++;
				}
			}
			else
			{
				var rowIndex:int = 0;
				var columnIndex:int = (horizontalTileCount + columnOffset) % horizontalTileCount;
				var pageStart:int = int(minimum / perPage) * perPage;
				i = minimum;
				var resultLength:int = 0;
				do
				{
					if(i < itemCount)
					{
						result[resultLength] = i;
						resultLength++;
					}
					rowIndex++;
					if(rowIndex == verticalTileCount)
					{
						rowIndex = 0;
						columnIndex++;
						if(columnIndex == horizontalTileCount)
						{
							columnIndex = 0;
							pageStart += perPage;
						}
						i = pageStart + columnIndex - horizontalTileCount;
					}
					i += horizontalTileCount;
				}
				while(resultLength < minimumItemCount && pageStart < itemCount);
			}
		}

		/**
		 * @private
		 */
		protected function getVisibleIndicesAtScrollPositionWithVerticalPaging(scrollX:Number, scrollY:Number, width:Number, height:Number, itemCount:int, result:Vector.<int>):void
		{
			this.prepareTypicalItem();
			var calculatedTypicalItemWidth:Number = this._typicalItem ? this._typicalItem.width : 0;
			var calculatedTypicalItemHeight:Number = this._typicalItem ? this._typicalItem.height : 0;

			var tileWidth:Number = calculatedTypicalItemWidth;
			var tileHeight:Number = calculatedTypicalItemHeight;
			if(tileWidth < 0)
			{
				tileWidth = 0;
			}
			if(tileHeight < 0)
			{
				tileHeight = 0;
			}
			if(this._useSquareTiles)
			{
				if(tileWidth > tileHeight)
				{
					tileHeight = tileWidth;
				}
				else if(tileHeight > tileWidth)
				{
					tileWidth = tileHeight;
				}
			}
			var horizontalTileCount:int = this.calculateHorizontalTileCount(tileWidth,
				width, width, this._paddingLeft + this._paddingRight,
				this._horizontalGap, this._requestedColumnCount, itemCount);
			if(this._distributeWidths)
			{
				tileWidth = (width - this._paddingLeft - this._paddingRight - (horizontalTileCount * this._horizontalGap) + this._horizontalGap) / horizontalTileCount;
				if(this._useSquareTiles)
				{
					tileHeight = tileWidth;
				}
			}
			var verticalTileCount:int = this.calculateVerticalTileCount(tileHeight,
				height, height, this._paddingTop + this._paddingBottom,
				this._verticalGap, this._requestedRowCount, itemCount,
				horizontalTileCount, this._distributeHeights && !this._useSquareTiles);
			if(this._distributeHeights && !this._useSquareTiles)
			{
				tileHeight = (height - this._paddingTop - this._paddingBottom - (verticalTileCount * this._verticalGap) + this._verticalGap) / verticalTileCount;
			}
			var perPage:int = horizontalTileCount * verticalTileCount;
			var minimumItemCount:int = perPage + 2 * horizontalTileCount;
			if(minimumItemCount > itemCount)
			{
				minimumItemCount = itemCount;
			}

			var startPageIndex:int = Math.round(scrollY / height);
			var minimum:int = startPageIndex * perPage;
			var totalColumnHeight:Number = verticalTileCount * (tileHeight + this._verticalGap) - this._verticalGap;
			var topSideOffset:Number = 0;
			var bottomSideOffset:Number = 0;
			if(totalColumnHeight < height)
			{
				if(this._verticalAlign === VerticalAlign.BOTTOM)
				{
					topSideOffset = height - this._paddingTop - this._paddingBottom - totalColumnHeight;
					bottomSideOffset = 0;
				}
				else if(this._verticalAlign === VerticalAlign.MIDDLE)
				{
					topSideOffset = bottomSideOffset = Math.round((height - this._paddingTop - this._paddingBottom - totalColumnHeight) / 2);
				}
				else //top
				{
					topSideOffset = 0;
					bottomSideOffset = height - this._paddingTop - this._paddingBottom - totalColumnHeight;
				}
			}
			var rowOffset:int = 0;
			var pageStartPosition:Number = startPageIndex * height;
			var partialPageSize:Number = scrollY - pageStartPosition;
			if(partialPageSize < 0)
			{
				partialPageSize = -partialPageSize - this._paddingBottom - bottomSideOffset;
				if(partialPageSize < 0)
				{
					partialPageSize = 0;
				}
				rowOffset = -Math.floor(partialPageSize / (tileHeight + this._verticalGap)) - 1;
				minimum += horizontalTileCount * rowOffset;
			}
			else if(partialPageSize > 0)
			{
				partialPageSize = partialPageSize - this._paddingTop - topSideOffset;
				if(partialPageSize < 0)
				{
					partialPageSize = 0;
				}
				rowOffset = Math.floor(partialPageSize / (tileHeight + this._verticalGap));
				minimum += horizontalTileCount * rowOffset;
			}
			if(minimum < 0)
			{
				minimum = 0;
				rowOffset = 0;
			}

			var maximum:int = minimum + minimumItemCount;
			if(maximum > itemCount)
			{
				maximum = itemCount;
			}
			minimum = maximum - minimumItemCount;
			var resultPushIndex:int = result.length;
			for(var i:int = minimum; i < maximum; i++)
			{
				result[resultPushIndex] = i;
				resultPushIndex++;
			}
		}

		/**
		 * @private
		 */
		protected function getVisibleIndicesAtScrollPositionWithoutPaging(scrollX:Number, scrollY:Number, width:Number, height:Number, itemCount:int, result:Vector.<int>):void
		{
			this.prepareTypicalItem();
			var calculatedTypicalItemWidth:Number = this._typicalItem ? this._typicalItem.width : 0;
			var calculatedTypicalItemHeight:Number = this._typicalItem ? this._typicalItem.height : 0;

			var tileWidth:Number = calculatedTypicalItemWidth;
			var tileHeight:Number = calculatedTypicalItemHeight;
			if(tileWidth < 0)
			{
				tileWidth = 0;
			}
			if(tileHeight < 0)
			{
				tileHeight = 0;
			}
			if(this._useSquareTiles)
			{
				if(tileWidth > tileHeight)
				{
					tileHeight = tileWidth;
				}
				else if(tileHeight > tileWidth)
				{
					tileWidth = tileHeight;
				}
			}
			var horizontalTileCount:int = this.calculateHorizontalTileCount(tileWidth,
				width, width, this._paddingLeft + this._paddingRight,
				this._horizontalGap, this._requestedColumnCount, itemCount);
			if(this._distributeWidths)
			{
				tileWidth = (width - this._paddingLeft - this._paddingRight - (horizontalTileCount * this._horizontalGap) + this._horizontalGap) / horizontalTileCount;
				if(this._useSquareTiles)
				{
					tileHeight = tileWidth;
				}
			}
			if(this._distributeHeights && !this._useSquareTiles)
			{
				var verticalTileCount:int = this.calculateVerticalTileCount(tileHeight,
					height, height, this._paddingTop + this._paddingBottom,
					this._verticalGap, this._requestedRowCount, itemCount,
					horizontalTileCount, this._distributeHeights && !this._useSquareTiles);
				tileHeight = (height - this._paddingTop - this._paddingBottom - (verticalTileCount * this._verticalGap) + this._verticalGap) / verticalTileCount;
			}
			verticalTileCount = Math.ceil((height + this._verticalGap) / (tileHeight + this._verticalGap)) + 1;
			var minimumItemCount:int = verticalTileCount * horizontalTileCount;
			if(minimumItemCount > itemCount)
			{
				minimumItemCount = itemCount;
			}
			var rowIndexOffset:int = 0;
			var totalRowHeight:Number = Math.ceil(itemCount / horizontalTileCount) * (tileHeight + this._verticalGap) - this._verticalGap;
			if(totalRowHeight < height)
			{
				if(this._verticalAlign === VerticalAlign.BOTTOM)
				{
					rowIndexOffset = Math.ceil((height - totalRowHeight) / (tileHeight + this._verticalGap));
				}
				else if(this._verticalAlign === VerticalAlign.MIDDLE)
				{
					rowIndexOffset = Math.ceil((height - totalRowHeight) / (tileHeight + this._verticalGap) / 2);
				}
			}
			var rowIndex:int = -rowIndexOffset + Math.floor((scrollY - this._paddingTop + this._verticalGap) / (tileHeight + this._verticalGap));
			var minimum:int = rowIndex * horizontalTileCount;
			if(minimum < 0)
			{
				minimum = 0;
			}
			var maximum:int = minimum + minimumItemCount;
			if(maximum > itemCount)
			{
				maximum = itemCount;
			}
			minimum = maximum - minimumItemCount;
			var resultPushIndex:int = result.length;
			for(var i:int = minimum; i < maximum; i++)
			{
				result[resultPushIndex] = i;
				resultPushIndex++;
			}
		}

		/**
		 * @private
		 */
		protected function validateItems(items:Vector.<DisplayObject>):void
		{
			var itemCount:int = items.length;
			for(var i:int = 0; i < itemCount; i++)
			{
				var item:DisplayObject = items[i];
				if(item is ILayoutDisplayObject && !ILayoutDisplayObject(item).includeInLayout)
				{
					continue;
				}
				if(item is IValidating)
				{
					IValidating(item).validate();
				}
			}
		}

		/**
		 * @private
		 */
		protected function prepareTypicalItem():void
		{
			if(!this._typicalItem)
			{
				return;
			}
			if(this._resetTypicalItemDimensionsOnMeasure)
			{
				this._typicalItem.width = this._typicalItemWidth;
				this._typicalItem.height = this._typicalItemHeight;
			}
			if(this._typicalItem is IValidating)
			{
				IValidating(this._typicalItem).validate();
			}
		}

		/**
		 * @inheritDoc
		 */
		public function calculateScrollPositionForIndex(index:int, items:Vector.<DisplayObject>,
			x:Number, y:Number, width:Number, height:Number, result:Point = null,
			nearest:Boolean = false, scrollX:Number = 0, scrollY:Number = 0):Point
		{
			if(!result)
			{
				result = new Point();
			}

			if(this._useVirtualLayout)
			{
				this.prepareTypicalItem();
				var calculatedTypicalItemWidth:Number = this._typicalItem ? this._typicalItem.width : 0;
				var calculatedTypicalItemHeight:Number = this._typicalItem ? this._typicalItem.height : 0;
			}

			var itemCount:int = items.length;
			var tileWidth:Number = this._useVirtualLayout ? calculatedTypicalItemWidth : 0;
			var tileHeight:Number = this._useVirtualLayout ? calculatedTypicalItemHeight : 0;
			//a virtual layout assumes that all items are the same size as
			//the typical item, so we don't need to measure every item in
			//that case
			if(!this._useVirtualLayout)
			{
				for(var i:int = 0; i < itemCount; i++)
				{
					var item:DisplayObject = items[i];
					if(!item)
					{
						continue;
					}
					if(item is ILayoutDisplayObject && !ILayoutDisplayObject(item).includeInLayout)
					{
						continue;
					}
					var itemWidth:Number = item.width;
					var itemHeight:Number = item.height;
					if(itemWidth > tileWidth)
					{
						tileWidth = itemWidth;
					}
					if(itemHeight > tileHeight)
					{
						tileHeight = itemHeight;
					}
				}
			}
			if(tileWidth < 0)
			{
				tileWidth = 0;
			}
			if(tileHeight < 0)
			{
				tileHeight = 0;
			}
			if(this._useSquareTiles)
			{
				if(tileWidth > tileHeight)
				{
					tileHeight = tileWidth;
				}
				else if(tileHeight > tileWidth)
				{
					tileWidth = tileHeight;
				}
			}
			var horizontalTileCount:int = (width - this._paddingLeft - this._paddingRight + this._horizontalGap) / (tileWidth + this._horizontalGap);
			if(horizontalTileCount < 1)
			{
				horizontalTileCount = 1;
			}
			else if(this._requestedColumnCount > 0 && horizontalTileCount > this._requestedColumnCount)
			{
				horizontalTileCount = this._requestedColumnCount;
			}
			if(this._paging !== Direction.NONE)
			{
				var verticalTileCount:int = (height - this._paddingTop - this._paddingBottom + this._verticalGap) / (tileHeight + this._verticalGap);
				if(verticalTileCount < 1)
				{
					verticalTileCount = 1;
				}
				var perPage:Number = horizontalTileCount * verticalTileCount;
				var pageIndex:int = index / perPage;
				if(this._paging === Direction.HORIZONTAL)
				{
					result.x = pageIndex * width;
					result.y = 0;
				}
				else
				{
					result.x = 0;
					result.y = pageIndex * height;
				}
			}
			else
			{
				var resultY:Number = this._paddingTop + ((tileHeight + this._verticalGap) * int(index / horizontalTileCount));
				if(nearest)
				{
					var bottomPosition:Number = resultY - (height - tileHeight);
					if(scrollY >= bottomPosition && scrollY <= resultY)
					{
						//keep the current scroll position because the item is already
						//fully visible
						resultY = scrollY;
					}
					else
					{
						var topDifference:Number = Math.abs(resultY - scrollY);
						var bottomDifference:Number = Math.abs(bottomPosition - scrollY);
						if(bottomDifference < topDifference)
						{
							resultY = bottomPosition;
						}
					}
				}
				else
				{
					resultY -= Math.round((height - tileHeight) / 2);
				}
				result.x = 0;
				result.y = resultY;
			}
			return result;
		}

		/**
		 * @private
		 */
		protected function calculateHorizontalTileCount(tileWidth:Number,
			explicitWidth:Number, maxWidth:Number, paddingLeftAndRight:Number,
			horizontalGap:Number, requestedColumnCount:int, totalItemCount:int):int
		{
			if(requestedColumnCount > 0 && this._distributeWidths)
			{
				return requestedColumnCount;
			}
			var tileCount:int;
			if(explicitWidth === explicitWidth) //!isNaN
			{
				//in this case, the exact width is known
				tileCount = (explicitWidth - paddingLeftAndRight + horizontalGap) / (tileWidth + horizontalGap);
				if(requestedColumnCount > 0 && tileCount > requestedColumnCount)
				{
					return requestedColumnCount;
				}
				if(tileCount > totalItemCount)
				{
					tileCount = totalItemCount;
				}
				if(tileCount < 1)
				{
					//we must have at least one tile per row
					tileCount = 1;
				}
				return tileCount;
			}

			//in this case, the width is not known, but it may have a maximum
			if(requestedColumnCount > 0)
			{
				tileCount = requestedColumnCount;
			}
			else
			{
				tileCount = totalItemCount;
			}

			var maxTileCount:int = int.MAX_VALUE;
			if(maxWidth === maxWidth && //!isNaN
				maxWidth < Number.POSITIVE_INFINITY)
			{
				maxTileCount = (maxWidth - paddingLeftAndRight + horizontalGap) / (tileWidth + horizontalGap);
				if(maxTileCount < 1)
				{
					//we must have at least one tile per row
					maxTileCount = 1;
				}
			}
			if(tileCount > maxTileCount)
			{
				tileCount = maxTileCount;
			}
			if(tileCount < 1)
			{
				//we must have at least one tile per row
				tileCount = 1;
			}
			return tileCount;
		}

		/**
		 * @private
		 */
		protected function calculateVerticalTileCount(tileHeight:Number,
			explicitHeight:Number, maxHeight:Number, paddingTopAndBottom:Number,
			verticalGap:Number, requestedRowCount:int, totalItemCount:int,
			horizontalTileCount:int, distributeHeights:Boolean):int
		{
			//using the horizontal tile count, calculate how many rows would be
			//required for the total number of items if there were no restrictions.
			var defaultVerticalTileCount:int = Math.ceil(totalItemCount / horizontalTileCount);
			if(distributeHeights)
			{
				if(requestedRowCount > 0 && defaultVerticalTileCount > requestedRowCount)
				{
					return requestedRowCount;
				}
				return defaultVerticalTileCount;
			}

			var verticalTileCount:int;
			if(explicitHeight === explicitHeight) //!isNaN
			{
				//in this case, the exact height is known
				verticalTileCount = (explicitHeight - paddingTopAndBottom + verticalGap) / (tileHeight + verticalGap);
				if(requestedRowCount > 0 && verticalTileCount > requestedRowCount)
				{
					return requestedRowCount;
				}
				if(verticalTileCount > defaultVerticalTileCount)
				{
					verticalTileCount = defaultVerticalTileCount;
				}
				if(verticalTileCount < 1)
				{
					//we must have at least one tile per row
					verticalTileCount = 1;
				}
				return verticalTileCount;
			}

			//in this case, the height is not known, but it may have a maximum
			if(requestedRowCount > 0)
			{
				verticalTileCount = requestedRowCount;
			}
			else
			{
				verticalTileCount = defaultVerticalTileCount;
			}

			var maxVerticalTileCount:int = int.MAX_VALUE;
			if(maxHeight === maxHeight && //!isNaN
				maxHeight < Number.POSITIVE_INFINITY)
			{
				maxVerticalTileCount = (maxHeight - paddingTopAndBottom + verticalGap) / (tileHeight + verticalGap);
				if(maxVerticalTileCount < 1)
				{
					//we must have at least one tile per row
					maxVerticalTileCount = 1;
				}
			}
			if(verticalTileCount > maxVerticalTileCount)
			{
				verticalTileCount = maxVerticalTileCount;
			}
			if(verticalTileCount < 1)
			{
				//we must have at least one tile per row
				verticalTileCount = 1;
			}
			return verticalTileCount;
		}
	}
}