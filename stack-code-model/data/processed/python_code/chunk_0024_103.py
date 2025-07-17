/**
 * Created by Administrator on 2015/8/12.
 */
package gui3D
{
	import away3d.cameras.lenses.PerspectiveLens;
	import away3d.containers.View3D;
	import away3d.controllers.HoverController;
	import away3d.lights.PointLight;

	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;
	import flash.geom.Vector3D;
	import flash.utils.getTimer;

	import gui3D.interf.IAShape;
	import gui3D.shapes.SelectBox;
	import gui3D.tool.AxisIndicator;

	import guiFlex.ui.RightToolUI;

	import universal.manager.DragBoxManager;
	import universal.manager.KeyboardManager;
	import universal.manager.SelectBoxManager;
	import universal.manager.ShapeFactoryManager;
	import universal.manager.StageMouseManager;
	import universal.pattern.event.GameDispatcher;
	import universal.pattern.event.GameEvent;
	import universal.pattern.event.GameEventConst;

	/**
	 *3d几何主类
	 */
	public class Geometry3D extends Sprite
	{
		private var _mainView:View3D;
		private var _light:PointLight;
		private var _axisIndicator:AxisIndicator;
		private var _hoverControl:HoverController;
		private var _moveCamera:Boolean = true;
		private var _lastX:Number = 0;
		private var _lastY:Number = 0;
		private var _scale:Number = 2000;
		private var _plane:String = "xyz";//平移方向
		private var _selectBox:SelectBox;

		//场景模型向量表
		private var _shapeVec:Vector.<IAShape>;
		private var _currentTime:uint = 0;

		//默认按当前帧频刷新
		public static const FRAME_RATE:int = 60;
		public var _realTime:uint = 0;

		public function Geometry3D()
		{
			if (stage)
			{
				init();
			}
			else
			{
				addEventListener(Event.ADDED_TO_STAGE, init);
			}
		}

		private function init(e:Event = null):void
		{
			stage.align = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.NO_SCALE;
			removeEventListener(Event.ADDED_TO_STAGE, init);
			StageMouseManager.getInstance.init(stage);
			_shapeVec = new Vector.<IAShape>();

			_mainView = new View3D();
			_mainView.antiAlias = 4;
			_mainView.backgroundColor = 0x333333;
			addChild(_mainView);

			var perspectiveLens:PerspectiveLens = new PerspectiveLens();
			perspectiveLens.far = 800000;
			_mainView.camera.lens = perspectiveLens;

			//点光
			_light = new PointLight();
			_light.y = 2000;
			_light.z = -1700;
			_light.x = 1000;
			_light.color = 0xFFFFFF;
			_light.diffuse = .5;
			_light.specular = .3;

			_mainView.scene.addChild(_light);
			_selectBox = new SelectBox();
			_mainView.scene.addChild(_selectBox);

			//轴线及网格指示器
			_axisIndicator = new AxisIndicator(_mainView.scene);
			_axisIndicator.visible = true;

			_hoverControl = new HoverController(_mainView.camera, _axisIndicator.trident, -210, 20);
			_hoverControl.distance = _scale;


			// setting camera target
			_hoverControl.lookAtPosition = new Vector3D();

			addEventListener(Event.ENTER_FRAME, onRender, false, 0, true);
			stage.addEventListener(Event.RESIZE, onResize, false, 0, true);
			DragBoxManager.getInstance.init(_mainView);
			ShapeFactoryManager.getInstance.initGeometry3D(this);

			_mainView.addEventListener(MouseEvent.MOUSE_DOWN, mouseDownHandler);
			_mainView.stage.addEventListener(MouseEvent.MOUSE_UP, onStageUP, false, 0, true);
			_mainView.addEventListener(MouseEvent.MOUSE_WHEEL, mouseWheelHandler);
			_mainView.addEventListener(MouseEvent.CLICK, onMainViewClick, false, 0, true);
			StageMouseManager.getInstance.keyUpFunc = onKeyUpEvt;
			addGameEvent();
			onResize();
			this.focusRect = false;
		}

		private function onMainViewClick(event:MouseEvent):void
		{
			stage.focus = stage;
		}

		private function onKeyUpEvt(e:KeyboardEvent):void
		{
			if (stage && stage.focus && stage.focus == stage)
			{
				KeyboardManager.getInstance.handlerKeyUpEvent(e);
			}
		}

		private function addGameEvent():void
		{
			GameDispatcher.addEventListener(GameEventConst.DOWN_ITEM, handlerDownItem, false, 0, true);
			GameDispatcher.addEventListener(GameEventConst.DRAG_SELECT_ITEM, handlerDragSelectItem, false, 0, true);
			GameDispatcher.addEventListener(GameEventConst.HIDE_SHOW_AUXILIARYLINE, handlerShowHide, false, 0, true);
			GameDispatcher.addEventListener(GameEventConst.CREATE_SHAPE, handlerCreateShape, false, 0, true);
			GameDispatcher.addEventListener(GameEventConst.DELETE_SHAPE, handlerDeleteShape, false, 0, true);
		}

		private function handlerDeleteShape(event:GameEvent):void
		{
			var deleteType:int = event.param.type;
			var currentSelectModel:IAShape = SelectBoxManager.getInstance.selectShape;
			if (deleteType == 1)
			{
				if (currentSelectModel && _shapeVec && _shapeVec.length)
				{
					var pos:int = _shapeVec.indexOf(currentSelectModel);
					if (pos > -1)
					{
						_shapeVec.splice(pos, 1);
					}
				}
			} else if (deleteType == 2)
			{
				if (_shapeVec && _shapeVec.length)
				{
					_shapeVec.forEach(function (element:IAShape, index:int, vec:Vector.<IAShape>):void
					{
						element.destroy();
						element = null;
					});
					_shapeVec.length = 0;
				}
			}
			if (_selectBox)
			{
				_selectBox.setVisible(false);
			}
			if (currentSelectModel)
			{
				currentSelectModel.destroy();
				currentSelectModel = null;
			}
			RightToolUI.getInstance.resetData();
		}

		/*
		 *  创建图形
		 * */
		private function handlerCreateShape(event:GameEvent):void
		{
			var shape:IAShape = ShapeFactoryManager.getInstance.createShape(event.param.type);
			if (shape)
			{
				_shapeVec.push(shape);
				_selectBox.setTarget(shape);
			}
		}

		private function handlerShowHide(event:GameEvent):void
		{
			if (_axisIndicator)
			{
				_axisIndicator.visible = event.param.value;
			}
		}

		private function handlerDragSelectItem(event:GameEvent):void
		{
			_plane = event.param.type;
		}

		private function handlerDownItem(event:GameEvent):void
		{
			if (_plane == "xyz")
			{
				return;
			}
			_moveCamera = false;
		}

		private function mouseWheelHandler(event:MouseEvent):void
		{
			if (_moveCamera)
			{
				var dist:Number = _hoverControl.distance / 25;
				if (event.delta > 0)
				{
					_scale -= dist;
				}
				else
				{
					_scale += dist;
				}
				if (_scale > 40000)
				{
					_scale = 40000;
				}
				if (_scale < 100)
				{
					_scale = 100;
				}
				_hoverControl.distance = _scale;
			}
		}

		private function mouseDownHandler(event:MouseEvent):void
		{
			if (_moveCamera)
			{
				_mainView.stage.addEventListener(MouseEvent.MOUSE_MOVE, mouseMoveHandler);
				_lastX = _mainView.mouseX;
				_lastY = _mainView.mouseY;
			}
		}

		private function mouseMoveHandler(ev:MouseEvent):void
		{
			if (_moveCamera)
			{
				//移动摄像机
				var dx:Number = _mainView.mouseX - _lastX;
				var dy:Number = _mainView.mouseY - _lastY;

				_hoverControl.panAngle += dx;
				_hoverControl.tiltAngle += dy;

				light.x = _mainView.camera.x + 200;
				light.y = _mainView.camera.y + 200;
				light.z = _mainView.camera.z + 100;

				_lastX = _mainView.mouseX;
				_lastY = _mainView.mouseY;
			}
			else
			{
				//移动 3D 小球
				GameDispatcher.dispatchEvent(GameEventConst.MOVE_DRAG_ITEM);
			}
		}

		private function onStageUP(ev:MouseEvent):void
		{
			_mainView.stage.removeEventListener(MouseEvent.MOUSE_MOVE, mouseMoveHandler);
			_moveCamera = true;
		}

		private function onResize(event:Event = null):void
		{
			_mainView.width = stage.stageWidth;
			_mainView.height = stage.stageHeight;
			GameDispatcher.dispatchEvent(GameEventConst.STAGE_RESIZE, {
				width: stage.stageWidth,
				height: stage.stageHeight
			});
		}

		private function onRender(e:Event):void
		{
			if (getTimer() - _currentTime > FRAME_RATE)
			{
				//实时渲染
				_mainView.render();

				if (_shapeVec && _shapeVec.length)
				{
					var currentSelect:IAShape = SelectBoxManager.getInstance.selectShape;
					_shapeVec.forEach(function (element:IAShape, index:int, vec:Vector.<IAShape>):void
					{
						element.render(_realTime);
					});
				}
				_currentTime = getTimer();
			}
			_realTime = getTimer();
		}

		public function get mainView():View3D
		{
			return _mainView;
		}

		public function get light():PointLight
		{
			return _light;
		}

		public function get selectBox():SelectBox
		{
			return _selectBox;
		}

		public function get shapeVec():Vector.<IAShape>
		{
			return _shapeVec;
		}

		public function destroy():void
		{
			removeEventListener(Event.ENTER_FRAME, onRender);
			stage.removeEventListener(Event.RESIZE, onResize);

			GameDispatcher.removeEventListener(GameEventConst.DOWN_ITEM, handlerDownItem);
			GameDispatcher.removeEventListener(GameEventConst.DRAG_SELECT_ITEM, handlerDragSelectItem);
			GameDispatcher.removeEventListener(GameEventConst.HIDE_SHOW_AUXILIARYLINE, handlerShowHide);
			GameDispatcher.removeEventListener(GameEventConst.CREATE_SHAPE, handlerCreateShape);
			GameDispatcher.removeEventListener(GameEventConst.DELETE_SHAPE, handlerDeleteShape);

			if (_light)
			{
				if (_light.parent)
				{
					_light.parent.removeChild(_light);
				}
				_light = null;
			}

			if (_axisIndicator)
			{
				_axisIndicator.destroy();
				_axisIndicator = null;
			}

			_hoverControl && (_hoverControl = null);

			if (_selectBox)
			{
				if (_selectBox.parent)
				{
					_selectBox.parent.removeChild(_selectBox);
				}
				_selectBox.destroy();
				_selectBox = null;
			}

			if (_shapeVec)
			{
				_shapeVec.forEach(function (element:IAShape, index:int, vector:Vector.<IAShape>):void
				{
					element.destroy();
					element = null;
				});
				_shapeVec.length = 0;
				_shapeVec = null;
			}

			if (_mainView)
			{
				if (_mainView.stage)
				{
					_mainView.stage.removeEventListener(MouseEvent.MOUSE_MOVE, mouseMoveHandler);
					_mainView.stage.removeEventListener(MouseEvent.MOUSE_UP, onStageUP);
				}
				_mainView.removeEventListener(MouseEvent.MOUSE_DOWN, mouseDownHandler);
				_mainView.removeEventListener(MouseEvent.MOUSE_WHEEL, mouseWheelHandler);
				_mainView.removeEventListener(MouseEvent.CLICK, onMainViewClick);

				if (contains(_mainView))
				{
					removeChild(_mainView);
				}
				_mainView = null;
			}

			StageMouseManager.getInstance.destroy();
			KeyboardManager.getInstance.destroy();
			DragBoxManager.getInstance.destroy();
			ShapeFactoryManager.getInstance.destroy();
			SelectBoxManager.getInstance.destroy();
			_instance = null;
		}

		private static var _instance:Geometry3D = null;

		public static function get getInstance():Geometry3D
		{
			if (_instance == null)
			{
				_instance = new Geometry3D();
			}
			return _instance;
		}
	}
}