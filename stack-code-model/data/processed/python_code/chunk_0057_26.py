package net.psykosoft.psykopaint2.base.ui.components.list
{

	import flash.display.DisplayObject;
	import flash.utils.Dictionary;
	import flash.utils.describeType;
	import flash.utils.setTimeout;

	import net.psykosoft.psykopaint2.base.ui.components.HSnapScroller;
	import net.psykosoft.psykopaint2.base.ui.components.ICopyableData;
	import net.psykosoft.psykopaint2.base.ui.components.NavigationButton;
	import net.psykosoft.psykopaint2.base.utils.ui.HScrollInteractionManager;
	import net.psykosoft.psykopaint2.base.utils.ui.SnapPositionManager;
	import net.psykosoft.psykopaint2.core.views.components.button.ButtonData;

	import org.osflash.signals.Signal;

	/*
	 * An data driven HSnapScroller that adds snap points at the position of each child.
	 * */
	public class HSnapList extends HSnapScroller
	{
		private var _dataProvider:Vector.<ISnapListData>;
		private var _itemRendererFactory:HSnapListItemRendererFactory;
		private var _dataForRenderer:Dictionary;

		public var itemGap:Number = 0;
		public var randomPositioningRange:Number = 0;

		public var rendererAddedSignal:Signal;
		public var rendererRemovedSignal:Signal;

		public function HSnapList() {
			super();
			rendererAddedSignal = new Signal();
			rendererRemovedSignal = new Signal();
			_itemRendererFactory = new HSnapListItemRendererFactory();
			_dataForRenderer = new Dictionary();
		}

		public function setDataProvider( data:Vector.<ISnapListData> ):void {
			reset();
			_dataProvider = data;
			// Create snap points.
			recalculateSnapPoints();
		}

		override public function dispose():void {

			// Clean up renderers.
			freeAllItemRenderers();
			if( _dataProvider ) {
				var i:uint;
				var len:uint = _dataProvider.length;
				var itemData:ISnapListData;
				for( i = 0; i < len; ++i ) {
					itemData = _dataProvider[ i ];
					if( itemData.itemRenderer ) {
						_container.removeChild( itemData.itemRenderer );
						itemData.itemRenderer = null;
					}
				}
			}
			_dataProvider = null;

			_itemRendererFactory.dispose();
			_itemRendererFactory = null;

			super.dispose();
		}

		public function removeButtonWithId(id:String):void {
			var targetData:ButtonData = getDataForId(id);
			if( !targetData ) return;
			removeButton(targetData.itemRenderer as NavigationButton);
		}

		public function getDataForId(id:String):ButtonData {
			 var targetData:ButtonData;
			if( _dataProvider ) {
				var numData:uint = dataProvider.length;
				for( var i:uint = 0; i < numData; i++ ) {
					var data:ButtonData = dataProvider[ i ] as ButtonData;
					if( id.indexOf( data.id ) != -1 ) {
					    targetData = data;
						break;
					}
				}
			}
			return targetData;
		}

		public function removeButton(btn:NavigationButton):void {

			// Remove the renderer.
			btn.visible = false; // Item renderer should be freed below.

			// Remove the data.
			var data:ButtonData = getDataForRenderer(btn);
			var dataIdx:uint = _dataProvider.indexOf(data);
			_dataProvider.splice(dataIdx, 1);

			// Recalculate positioning of elements.
			_minContentX = 0;
			_maxContentX = 0;
			var xCache:int = _positionManager.position;
			_positionManager.reset();
			recalculateSnapPoints(false);
			updateItemRendererPositionsFromData();
			refreshItemRendererVisibilityAndAssignmentsFromPositions();

			// Restore position.
			_positionManager.position = xCache;
		}

		override public function recalculateSnapPoints(doDock:Boolean = true):void {

//			super.recalculateSnapPoints();

			if( !_dataProvider ) return;

//			trace( this, "invalidateContent() -----------------" );

			// Create snap points for each data item.
			// Items will remember their associated position.
			var i:uint;
			var numItems:uint = _dataProvider.length;
//			trace( this, "numItems: " + numItems );
			var itemData:ISnapListData;
			var itemPositioningMarker:Number = 0;
			for( i = 0; i < numItems; i++ ) {
				itemData = _dataProvider[ i ];
				itemData.itemRendererPosition = itemPositioningMarker + itemData.itemRendererWidth / 2;
				itemPositioningMarker += itemData.itemRendererWidth + itemGap + rand( -randomPositioningRange, randomPositioningRange );
//				trace( this, "placing item: " + itemPositioningMarker );
				evaluateDimensionsFromItemPositionAndWidth( itemData.itemRendererPosition, itemData.itemRendererWidth );
				evaluateNewSnapPointFromPosition( itemData.itemRendererPosition );
			}

			containEdgeSnapPoints();
			if(doDock) dock();

			// Should be commented, just for visualization/debugging.
//			graphics.clear();
			_container.graphics.clear();
//			visualizeVisibleDimensions();
//			visualizeContentDimensions();
//			visualizeSnapPoints();
//			visualizeDataPositionsAndDimensions();

//			trace("invalidated");

			refreshItemRendererVisibilityAndAssignmentsFromPositions();
		}

		override public function reset():void {

			// Release all current item renderers.
			freeAllItemRenderers();
			_dataProvider = null;

			super.reset();
		}

		private function rand( min:Number, max:Number ):Number {
			return (max - min) * Math.random() + min;
		}

		override protected function onUpdate():void {
			if( _dataProvider ) {
				refreshItemRendererVisibilityAndAssignmentsFromPositions();
			}
		}

		// ---------------------------------------------------------------------
		// Data provider.
		// ---------------------------------------------------------------------

		public function get dataProvider():Vector.<ISnapListData> {
			return _dataProvider;
		}

		// ---------------------------------------------------------------------
		// Item renderer updates.
		// ---------------------------------------------------------------------

		public function refreshItemRendererVisibilityAndAssignmentsFromPositions():void {

			if( !_dataProvider ) return;

//			trace("refreshItemRendererVisibilityAndAssignmentsFromPositions ------");

			var i:uint;
			var numItems:uint;
			var itemRenderer:DisplayObject;
			var itemData:ISnapListData;

			// Which items should *become* visible?
			numItems = _dataProvider.length;
			var indicesOfItemsThatBecomeVisible:Vector.<uint> = new Vector.<uint>();
			var indicesOfItemsThatBecomeInvisible:Vector.<uint> = new Vector.<uint>();
			for( i = 0; i < numItems; i++ ) {
				itemData = _dataProvider[ i ];
				var shouldBeVisible:Boolean = shouldItemBeVisibleAtCurrentScrollPosition( itemData );
				var isCurrentlyVisible:Boolean = itemData.isDataItemVisible;
				if( !isCurrentlyVisible && shouldBeVisible ) {
//					trace( i + " becoming visible" );
					indicesOfItemsThatBecomeVisible.push( i );
					itemData.isDataItemVisible = true;
				}
				else if( isCurrentlyVisible && !shouldBeVisible ) {
//					trace( i + " becoming invisible" );
					indicesOfItemsThatBecomeInvisible.push( i );
					itemData.isDataItemVisible = false;
				}
			}

			// Decommission item renderers from items that are becoming invisible.
			numItems = indicesOfItemsThatBecomeInvisible.length;
			for( i = 0; i < numItems; i++ ) {

				itemData = _dataProvider[ indicesOfItemsThatBecomeInvisible[ i ] ];

				// Dissociate item renderer from data and mark it as available.
				itemRenderer = itemData.itemRenderer;
				freeItemRenderer( itemRenderer );
				itemData.itemRenderer = null;
			}

			// Assign renderers to items that are becoming visible.
			numItems = indicesOfItemsThatBecomeVisible.length;
			for( i = 0; i < numItems; i++ ) {

				itemData = _dataProvider[ indicesOfItemsThatBecomeVisible[ i ] ];

				// Retrieve an item renderer.
				itemRenderer = getNewItemRendererForData( itemData );
				itemData.itemRenderer = itemRenderer;
				_dataForRenderer[ itemRenderer ] = itemData;
				rendererAddedSignal.dispatch( itemRenderer );

				// Configure renderer from data properties.
				//copyAllPropertiesFromObjectAToObjectB( itemData, itemRenderer );
				(itemRenderer as ICopyableData).copyData( itemData as ICopyableData );
				
				// Add it to display.
				itemRenderer.x = itemData.itemRendererPosition;
//				trace("x: " + itemRenderer.x);
				itemRenderer.y = itemData.itemRendererWidth / 2;
				itemRenderer.visible = true;
//				itemRenderer.alpha = 0.25;
				if( itemRenderer.parent != _container ) {
					_container.addChild( itemRenderer );
				}

				if( itemData.onItemRendererAssigned != null) {
					itemData.onItemRendererAssigned( itemRenderer );
				}
			}
		}

		private function updateItemRendererPositionsFromData():void {
//			trace("updateItemRendererPositionsFromData -----");
			var numItems:int = _dataProvider.length;
			var itemData:ISnapListData;
			var itemRenderer:DisplayObject;
			for(var i:int = 0; i < numItems; i++ ) {
				itemData = _dataProvider[i];
				itemRenderer = itemData.itemRenderer;
				if(itemRenderer) {
					itemRenderer.x = itemData.itemRendererPosition;
					itemRenderer.y = itemData.itemRendererWidth / 2;
//					itemRenderer.visible = true;
//					trace("x: " + itemRenderer.x);
					_container.graphics.beginFill( 0xFF0000 );
					_container.graphics.drawCircle( itemRenderer.x, itemRenderer.y, 10 );
					_container.graphics.endFill();
				}
			}
		}

		private function shouldItemBeVisibleAtCurrentScrollPosition( itemData:ISnapListData ):Boolean {
			var px:Number = _container.x + itemData.itemRendererPosition;
			var hw:Number = itemData.itemRendererWidth * 0.5;
			return px + hw >= 0 && px - hw <= _visibleWidth;
		}

		// ---------------------------------------------------------------------
		// Item renderers.
		// ---------------------------------------------------------------------

		public function getDataForRenderer( renderer:DisplayObject ):ButtonData {
			return _dataForRenderer[ renderer ];
		}

		private function getNewItemRendererForData( data:ISnapListData ):DisplayObject {
			var renderer:DisplayObject = _itemRendererFactory.getItemRendererOfType( data.itemRendererType );
			return renderer;
		}

		private function freeItemRenderer( renderer:DisplayObject ):void {

			var data:ISnapListData = _dataForRenderer[ renderer ];

			if( data.onItemRendererReleased != null ) {
				data.onItemRendererReleased( renderer );
			}

			_dataForRenderer[ renderer ] = null;
			rendererRemovedSignal.dispatch( renderer );
			_itemRendererFactory.markItemRendererAsAvailable( renderer );
			renderer.visible = false;
		}

		private function freeAllItemRenderers():void {
			if( _dataProvider ) {
				var i:uint;
				var len:uint = _dataProvider.length;
				var itemData:ISnapListData;
				for( i = 0; i < len; ++i ) {
					itemData = _dataProvider[ i ];
					if( itemData.itemRenderer ) {
						freeItemRenderer( itemData.itemRenderer );
					}
				}
			}
		}

		public function get itemRenderers():Vector.<DisplayObject> {
			return _itemRendererFactory.itemRenderers;
		}

		// ---------------------------------------------------------------------
		// Moving data between item renderers and data items.
		// ---------------------------------------------------------------------

		public function updateItemRendererAssociatedData( itemRenderer:DisplayObject, propertyName:String = "" ):void {
			var data:ISnapListData = _dataForRenderer[ itemRenderer ];
			if( data ) {
				//if( propertyName == "" ) copyAllPropertiesFromObjectAToObjectB( itemRenderer, data );
				//else copyPropertyFromObjectAToObjectB( propertyName, itemRenderer, data );
				if( propertyName == "" )(data as ICopyableData).copyData( itemRenderer as ICopyableData );
				else (data as ICopyableData).copyDataProperty(itemRenderer as ICopyableData, propertyName);
			}
		}

		public function updateItemRenderersFromData():void {
			var i:uint;
			var numItems:uint;
			numItems = _dataProvider.length;
			for( i = 0; i < numItems; i++ ) {
				var data:ISnapListData = _dataProvider[ i ];
				if( data.itemRenderer ) {
					//copyAllPropertiesFromObjectAToObjectB( data, data.itemRenderer );
					(data.itemRenderer as ICopyableData).copyData(data as ICopyableData);
					
				}
			}
		}

		/*
		private function copyAllPropertiesFromObjectAToObjectB( objectA:*, objectB:* ):void {

			//trace( this, "copying properties from " + objectA + " to " + objectB );

			// Obtain object a's public interface description in xml.
			var objectDescriptor:XML = describeType( objectA );
			var propertyList:XMLList = objectDescriptor.variable;

			// Sweep object a's properties and check if it has properties that object b also has.
			// If so, set.
			var i:uint;
			var numProperties:uint = propertyList.length();
			for( i = 0; i < numProperties; i++ ) {
				var propertyName:String = propertyList[ i ].@name;
				copyPropertyFromObjectAToObjectB( propertyName, objectA, objectB );
			}
		}

		private function copyPropertyFromObjectAToObjectB( propertyName:String, objectA:*, objectB:* ):void {
			if( objectB.hasOwnProperty( propertyName ) ) {
				trace( objectA,objectB, "copying property [" + propertyName + "]" );
				objectB[ propertyName ] = objectA[ propertyName ];
			}
		}
		*/
		
		// ---------------------------------------------------------------------
		// Visualization utils.
		// ---------------------------------------------------------------------

		private function visualizeDataPositionsAndDimensions():void {
			var i:uint;
			var len:uint = _dataProvider.length;
			var itemData:ISnapListData;
			_container.graphics.lineStyle( 1, 0xFF0000, 1 );
			for( i = 0; i < len; ++i ) {
				itemData = _dataProvider[ i ];
				var hw:Number = itemData.itemRendererWidth / 2;
				var px:Number = itemData.itemRendererPosition - hw;
				_container.graphics.drawRect( px, 0, itemData.itemRendererWidth, itemData.itemRendererWidth );
			}
		}
		
		
	}
}