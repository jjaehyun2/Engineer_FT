package pl.cdaction.view.grid
{
	import flash.display.Sprite;
	
	import org.osflash.signals.Signal;
	
	import pl.cdaction.common.Constants;
	import pl.cdaction.controller.GridTouchController;
	
	public class GridView extends Sprite
	{
		private var _sigCustomizeMe : Signal;
		private var _gridItems : Vector.<GridObject>;
		private var _touchController : GridTouchController;
		
		
		public function GridView()
		{
			init();
		}
		
		private function init() : void
		{
			_sigCustomizeMe = new Signal();
			_gridItems = new Vector.<GridObject>();
			_touchController = new GridTouchController(this);
		}
		
		public function addEmpty() : void
		{
			var gridObj : GridObject = new GridObject( _gridItems.length );
			
			var itemsInRow : int = Math.floor( stage.stageWidth / (Constants.GRID_OBJECT_WIDTH + Constants.GRID_ITEMS_GAP) );
			
			gridObj.x = (totalItems % itemsInRow) * (Constants.GRID_OBJECT_WIDTH + Constants.GRID_ITEMS_GAP);
			gridObj.y = Math.floor( totalItems / itemsInRow ) * (Constants.GRID_OBJECT_HEIGHT + Constants.GRID_ITEMS_GAP);
			addChild(gridObj);
			
			_gridItems.push(gridObj);
			_touchController.registerGridObj( gridObj );
		}
		
		public function addCustomized(label : String, pageL : Object, pageR : Object) : void
		{
			var gridObj : GridObject = new GridObject( _gridItems.length );
			addChild(gridObj);
			
			if(label)
				gridObj.setLabel( label );
			
			gridObj.setLeftPageContent( pageL as Array );
			gridObj.setRightPageContent( pageR as Array );
			
			_gridItems.push(gridObj);
			_touchController.registerGridObj( gridObj );
		}
		
		public function handleResize() : void
		{
			if(_gridItems.length > 0)
			{
				var itemsInRow : int = Math.floor( stage.stageWidth / (Constants.GRID_OBJECT_WIDTH + Constants.GRID_ITEMS_GAP) );
				
				var i : int = 0;
				for each(var gridObj : GridObject in _gridItems)
				{
					gridObj.x = (i % itemsInRow) * (Constants.GRID_OBJECT_WIDTH + Constants.GRID_ITEMS_GAP);
					gridObj.y = Math.floor( i / itemsInRow ) * (Constants.GRID_OBJECT_HEIGHT + Constants.GRID_ITEMS_GAP);
					gridObj.updateIndex( i );
					i++;
				}
			}
		}
		
		public function moveGridItem(currIndex:int, destIndex:int, obj:GridObject):void
		{
			_gridItems.splice( currIndex, 1 );
			_gridItems.splice( destIndex, 0, obj );
			
			handleResize();
		}
		
		
		public function getItemIndex(obj:GridObject) : int
		{
			return _gridItems.indexOf(obj);
		}
		
		public function get totalItems() : int
		{
			return _gridItems.length;
		}
		
		public function get sigCustomizeMe() : Signal
		{
			return _sigCustomizeMe;
		}
		
		
		public function getAllItemsAsObject() : Object
		{
			var mainObj : Object = {};
			mainObj.totalItems = totalItems;
			
			var objectsArray : Array = [];
			
			for each(var gridObj:GridObject in _gridItems)
			{
				var obj : Object = {};
				
				var label : String = gridObj.getLabel();
				if(label != "")
					obj.label = label;
				
				obj.pageL = gridObj.getLeftPageContent();
				obj.pageR = gridObj.getRightPageContent();
				
				objectsArray.push( obj );
			}
			
			
			if(objectsArray.length > 0)
				mainObj.gridObjects = objectsArray;
			
			return mainObj;
		}
		
		
		public function destroy() : void
		{
			_sigCustomizeMe.removeAll();
			
			for each(var gridObj : GridObject in _gridItems)
			{
				_touchController.unregisterGridObj( gridObj );
				gridObj.destroy();
			}
			_gridItems.length = 0;
			
			_touchController.destroy();
			_touchController = null;
		}
	}
}