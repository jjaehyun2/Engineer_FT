/**
 * Created by Administrator on 2015/8/13.
 */
package universal.manager
{
	import away3d.containers.View3D;
	import away3d.tools.utils.Drag3D;

	import flash.geom.Vector3D;

	import gui3D.interf.IAShape;

	import universal.pattern.event.GameDispatcher;
	import universal.pattern.event.GameEvent;
	import universal.pattern.event.GameEventConst;

	/*
	 * 拖拽管理器
	 * */
	public class DragBoxManager
	{
		private var _drag:Drag3D;

		public function DragBoxManager()
		{
		}

		public function init(view3d:View3D):void
		{
			_drag = new Drag3D(view3d, null, Drag3D.PLANE_XY);
			GameDispatcher.addEventListener(GameEventConst.MOVE_DRAG_ITEM, handlerMoveDragItem, false, 0, true);
			GameDispatcher.addEventListener(GameEventConst.DOWN_ITEM, handlerDOWN_ITEM, false, 0, true);
			GameDispatcher.addEventListener(GameEventConst.DRAG_SELECT_ITEM, handlerDragSelectItem, false, 0, true);
		}

		private function handlerDragSelectItem(event:GameEvent):void
		{
			if (event.param.type != "xyz")
			{
				_drag.plane = event.param.type;
			}
		}

		private function handlerDOWN_ITEM(event:GameEvent):void
		{
			if (_drag)
			{
				_drag.object3d = event.param.item;
			}
		}

		private function handlerMoveDragItem(event:GameEvent):void
		{
			if (_drag)
			{
				_drag.updateDrag();

				var shape:IAShape = _drag.object3d as IAShape;
				var position:Vector3D = shape.position;
				if (position.x != shape.x)
				{
					position.x = shape.x;
				}
				if (position.y != shape.y)
				{
					position.y = shape.y;
				}
				if (position.z != shape.z)
				{
					position.z = shape.z;
				}
				shape.position = position;
				GameDispatcher.dispatchEvent(GameEventConst.UPDATE_PROPERTY, {item: _drag.object3d});
			}
		}

		public function destroy():void
		{
			GameDispatcher.removeEventListener(GameEventConst.MOVE_DRAG_ITEM, handlerMoveDragItem);
			GameDispatcher.removeEventListener(GameEventConst.DOWN_ITEM, handlerDOWN_ITEM);
			GameDispatcher.removeEventListener(GameEventConst.DRAG_SELECT_ITEM, handlerDragSelectItem);
			if (_drag)
			{
				_drag.object3d = null;
				_drag = null;
			}
			_instance = null;
		}

		private static var _instance:DragBoxManager = null;

		public static function get getInstance():DragBoxManager
		{
			if (_instance == null)
			{
				_instance = new DragBoxManager();
			}
			return _instance;
		}
	}
}