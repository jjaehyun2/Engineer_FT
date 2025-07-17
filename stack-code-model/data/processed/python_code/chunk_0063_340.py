/**
 * Created by Administrator on 2015/8/14.
 */
package gui3D.shapes
{
	import away3d.containers.ObjectContainer3D;
	import away3d.primitives.WireframeCube;

	import constants.ShapeType;

	import gui3D.interf.IAShape;

	import universal.manager.SelectBoxManager;
	import universal.pattern.event.GameDispatcher;
	import universal.pattern.event.GameEvent;
	import universal.pattern.event.GameEventConst;

	/**
	 * 3d物品显示选中框
	 * */
	public class SelectBox extends ObjectContainer3D
	{
		private var _width:Number = 100;
		private var _height:Number = 100;
		private var _depth:Number = 100;
		private var _color:uint = 0xff0000;
		private var _thick:Number = 1.0;

		private var _wireFrame:WireframeCube;
		private var _target:IAShape;

		public function SelectBox()
		{
			super();
			mouseChildren = false;
			mouseEnabled = false;
			_wireFrame = new WireframeCube(_width, _height, _depth, _color, _thick);
			addChild(_wireFrame);
			setVisible(false);
			addEvent();
		}

		private function addEvent():void
		{
			GameDispatcher.addEventListener(GameEventConst.UPDATE_PROPERTY, handlerUpdatePosition, false, 0, true);
			GameDispatcher.addEventListener(GameEventConst.DOWN_ITEM, handlerDownItem, false, 0, true);
		}

		private function handlerDownItem(event:GameEvent):void
		{
			setTarget(event.param.item);
		}

		private function handlerUpdatePosition(event:GameEvent):void
		{
			refresh();
		}

		public function setTarget(shapeBase:IAShape):void
		{
			if (_target)
			{
				_target.stopListen();
				_target = null;
			}
			setVisible(true);
			_target = shapeBase;
			GameDispatcher.dispatchEvent(GameEventConst.UPDATE_PROPERTY, {item: _target});
			_target.startListen();
			refresh();
			SelectBoxManager.getInstance.selectShape = _target;
		}

		public function updateWidth(width:Number):void
		{
			if (_wireFrame.width != width)
			{
				_wireFrame.width = width;
			}
		}

		public function updateHeight(height:Number):void
		{
			if (_wireFrame.height != height)
			{
				_wireFrame.height = height;
			}
		}

		public function updateDepth(depth:Number):void
		{
			if (_wireFrame.depth != depth)
			{
				_wireFrame.depth = depth;
			}
		}

		/**
		 * 刷新属性
		 * */
		public function refresh():void
		{
			if (_target)
			{
				x = _target.x;
				y = _target.y;
				z = _target.z;

				var type:int = _target.type;
				if (type == ShapeType.CONE_TYPE)
				{
					updateWidth(_target.radius * 2 + 50);
					updateHeight(_target.height + 50);
					updateDepth(_target.radius * 2 + 50);
				} else if (type == ShapeType.CUBE_TYPE)
				{
					updateWidth(_target.width + 50);
					updateHeight(_target.height + 50);
					updateDepth(_target.depth + 50);
				} else if (type == ShapeType.CYLINDER_TYPE)
				{
					updateWidth(_target.radius * 2 + 50);
					updateHeight(_target.height + 50);
					updateDepth(_target.radius * 2 + 50);
				} else if (type == ShapeType.SHHERE_TYPE)
				{
					updateWidth(_target.radius * 2 + 50);
					updateHeight(_target.radius * 2 + 50);
					updateDepth(_target.radius * 2 + 50);
				}

				scaleX = _target.scaleX;
				scaleY = _target.scaleY;
				scaleZ = _target.scaleZ;
			}
		}

		public function setVisible(bool:Boolean):void
		{
			this.visible = bool;
		}

		public function destroy():void
		{
			GameDispatcher.removeEventListener(GameEventConst.UPDATE_PROPERTY, handlerUpdatePosition);
			GameDispatcher.removeEventListener(GameEventConst.DOWN_ITEM, handlerDownItem);
			if (_wireFrame)
			{
				if (contains(_wireFrame))
				{
					removeChild(_wireFrame);
				}
				_wireFrame.dispose();
				_wireFrame = null;
			}
			setVisible(false);
			_target = null;
		}
	}
}