package pl.cdaction.controller
{
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.geom.Point;
	import flash.text.TextField;
	
	import pl.cdaction.common.Constants;
	import pl.cdaction.view.customizable.ICustomizable;
	import pl.cdaction.view.grid.GridObject;
	import pl.cdaction.view.grid.GridView;

	public class GridTouchController
	{
		private var _gridView : GridView;
		
		private var _isDragging : Boolean;
		private var _obj : GridObject;
		private var _startPos : Point;
		
		
		public function GridTouchController( gridView : GridView )
		{
			_gridView = gridView;
			
			init();
		}
		
		private function init() : void
		{
			_isDragging = false;
			_startPos = new Point();
			
			_gridView.addEventListener(Event.ADDED_TO_STAGE, handleAddedToStage);
		}
		
		protected function handleAddedToStage(event : Event) : void
		{
			_gridView.removeEventListener(Event.ADDED_TO_STAGE, handleAddedToStage);
			_gridView.stage.addEventListener(MouseEvent.MOUSE_UP, onMouseUp);
		}
		
		
		public function registerGridObj(gridObj : GridObject) : void
		{
			gridObj.addEventListener(MouseEvent.MOUSE_DOWN, onMouseDown);
		}
		
		public function unregisterGridObj(gridObj : GridObject) : void
		{
			gridObj.removeEventListener(MouseEvent.MOUSE_DOWN, onMouseDown);
		}
		
		
		protected function onMouseDown(event : MouseEvent) : void
		{
			if(event.currentTarget is GridObject && event.target.name == "header")
			{
				startDraggingGridObject( event.currentTarget as GridObject );
			}
			
			if(event.target is TextField && event.target.name == "tfCustomizable")
			{
				if(event.target.parent is ICustomizable)
				{
					_gridView.sigCustomizeMe.dispatch(event.target.parent);
				}
			}
		}
		
		private function startDraggingGridObject(obj : GridObject) : void
		{
			_obj = obj;
			_obj.mouseEnabled = _obj.mouseChildren = false;
			_obj.alpha = 0.4;
			_startPos.x = _obj.x;
			_startPos.y = _obj.y;
			_gridView.addChild(_obj);
			
			_gridView.addEventListener(Event.ENTER_FRAME, onEnterFrame);
			_isDragging = true;
		}
		
		protected function onEnterFrame(event : Event) : void
		{
			_obj.x = _gridView.mouseX;
			_obj.y = _gridView.mouseY;
		}
		
		
		protected function onMouseUp(event : MouseEvent) : void
		{
			if(_isDragging)
			{
				_gridView.removeEventListener(Event.ENTER_FRAME, onEnterFrame);
				_isDragging = false;
				
				if(_obj)
				{
					stopDraggingGridObject();
				}
			}
		}
		
		private function stopDraggingGridObject() : void
		{
			var currIndex : int = _gridView.getItemIndex(_obj);
			if(_gridView.totalItems == 1 || currIndex == -1)
			{
				_obj.x = _startPos.x;
				_obj.y = _startPos.y;
			}
			else
			{
				var itemsInRow : int = Math.floor( _gridView.stage.stageWidth / (Constants.GRID_OBJECT_WIDTH + Constants.GRID_ITEMS_GAP) );
				var destX : int = Math.max(0, Math.floor( (_gridView.mouseX + Constants.GRID_OBJECT_WIDTH * 0.5 + Constants.GRID_ITEMS_GAP) / (Constants.GRID_OBJECT_WIDTH + Constants.GRID_ITEMS_GAP) ));
				var destY : int = Math.max(0, Math.floor( _gridView.mouseY / (Constants.GRID_OBJECT_HEIGHT + Constants.GRID_ITEMS_GAP) ));
				var destIndex : int = destY * itemsInRow + destX;
				
				if(currIndex == destIndex)
				{
					_obj.x = _startPos.x;
					_obj.y = _startPos.y;
				}
				else
				{
					_gridView.moveGridItem(currIndex, destIndex < currIndex ? destIndex : destIndex - 1, _obj);
				}
			}
			
			_obj.mouseEnabled = _obj.mouseChildren = true;
			_obj.alpha = 1;
			_obj = null;
		}
		
		
		public function destroy() : void
		{
			_gridView.removeEventListener(Event.ENTER_FRAME, onEnterFrame);
			_gridView.stage.removeEventListener(MouseEvent.MOUSE_UP, onMouseUp);
			_gridView = null;
			_obj = null;
			_startPos = null;
		}
	}
}