package universal.manager
{
	import flash.display.Stage;
	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;

	/**
	 * 添加3D环境中舞台公用的一些控制事件
	 * @author ado
	 *
	 */
	public class StageMouseManager
	{
		private var stage:Stage;
		/** 鼠标按下的处理回调函数 */
		public var mouseDownFunc:Function;
		/** 鼠标弹起的处理回调函数 */
		public var mouseUpFunc:Function;
		/** 键盘按下的回调函数 */
		public var keyDownFunc:Function;
		/** 键盘弹起的回调函数 */
		public var keyUpFunc:Function;

		private var _stageDeltaX:Number = 0;
		private var _stageDeltaY:Number = 0;
		//参考X
		private var _referX:Number = 0;
		//参考Y
		private var _referY:Number = 0;

		public function StageMouseManager()
		{
		}

		/**
		 * 移除舞台的时间监听
		 * @param eventType        事件类型
		 * @param listener        事件响应函数
		 * @param useCapture    是否捕捉
		 *
		 */
		public function removeStageEvent(eventType:String,
										 listener:Function,
										 useCapture:Boolean = false):void
		{
			stage.removeEventListener(eventType, listener, useCapture);
		}

		/**
		 * 给舞台添加事件监听
		 * @param eventType        事件类型
		 * @param listener        事件响应函数
		 * @param useCapture    是否捕捉
		 * @param priority        优先级
		 * @param useWeakReference 是否使用弱引用
		 *
		 */
		public function addStageEvent(eventType:String,
									  listener:Function,
									  useCapture:Boolean = false,
									  priority:int = 0,
									  useWeakReference:Boolean = false):void
		{
			stage.addEventListener(eventType, listener, useCapture, priority, useWeakReference);
		}

		/**
		 * 销毁 ：移除事件，清除stage引用
		 *
		 */
		public function destroy():void
		{
			stage.removeEventListener(MouseEvent.MOUSE_DOWN, onMouseDown);
			stage.removeEventListener(MouseEvent.MOUSE_UP, onMouseUp);
			stage.removeEventListener(KeyboardEvent.KEY_DOWN, onKeyDown);
			stage.removeEventListener(KeyboardEvent.KEY_UP, onKeyUp);
			stage = null;

			mouseDownFunc = null;
			mouseUpFunc = null;
			keyDownFunc = null;
			keyUpFunc = null;
		}

		/**
		 * 初始化
		 * @param _stage
		 *
		 */
		public function init(_stage:Stage):void
		{
			stage = _stage;
			initStageEvents();
		}

		private function onMouseDown(e:MouseEvent):void
		{
			_stageDeltaX = 0;
			_stageDeltaY = 0;
			_referX = stage.mouseX;
			_referY = stage.mouseY;
			stage.removeEventListener(MouseEvent.MOUSE_DOWN, onMouseDown);
			stage.addEventListener(MouseEvent.MOUSE_UP, onMouseUp);
			if (mouseDownFunc != null)
				mouseDownFunc(e);
		}

		private function onMouseUp(e:MouseEvent):void
		{
			_stageDeltaX = stage.mouseX - _referX;
			_stageDeltaY = stage.mouseY - _referY;
			stage.addEventListener(MouseEvent.MOUSE_DOWN, onMouseDown);
			stage.removeEventListener(MouseEvent.MOUSE_UP, onMouseUp);
			if (mouseUpFunc != null)
				mouseUpFunc(e);
		}

		/*
		 *  设置焦点为舞台
		 * */
		public function setFocusStage():void
		{
			if (stage)
			{
				if (stage.focus != stage)
				{
					stage.focus = stage;
				}
			}
		}

		private function onKeyDown(e:KeyboardEvent):void
		{
			if (keyDownFunc != null)
				keyDownFunc(e);
		}

		private function onKeyUp(e:KeyboardEvent):void
		{
			if (keyUpFunc != null)
				keyUpFunc(e);
		}

		private function initStageEvents():void
		{
			stage.addEventListener(MouseEvent.MOUSE_DOWN, onMouseDown);
			stage.addEventListener(KeyboardEvent.KEY_DOWN, onKeyDown);
			stage.addEventListener(KeyboardEvent.KEY_UP, onKeyUp);
		}

		/**
		 * 鼠标按下和弹起在舞台上的X方向上的增量
		 * @return
		 *
		 */
		public function get stageDeltaX():Number
		{
			return _stageDeltaX;
		}

		/**
		 * 鼠标按下和弹起在舞台上的Y方向上的增量
		 * @return
		 *
		 */
		public function get stageDeltaY():Number
		{
			return _stageDeltaY;
		}

		private static var _instance:StageMouseManager = null;

		public static function get getInstance():StageMouseManager
		{
			if (_instance == null)
			{
				_instance = new StageMouseManager();
			}
			return _instance;
		}
	}
}