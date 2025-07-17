package com.adobe.webdashboard.view.components
{
	import com.adobe.dashboard.enum.DateRangeEnum;
	import com.adobe.dashboard.util.DateTimeUtil;

	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import flash.text.TextField;
	import flash.text.TextFormat;
	import flash.text.TextFormatAlign;

	import mx.core.UIComponent;

	[Event(name="change", type="flash.events.Event")]

	public class DateSliderComponent extends UIComponent
	{

		public var backgroundColor:uint=0x141414;

		public var borderColor:uint=0x262626;

		public var paddingLeft:int=10;

		public var paddingRight:int=10;


		/**
		 * the type of range being displayed <DateRangeEnum> type
		 */
		private var _dateRange:String=DateRangeEnum.MONTH;

		public function get dateRange():String
		{
			return _dateRange;
		}

		public function set dateRange(value:String):void
		{
			_dateRange=value;
			invalidateDisplayList();
		}

		/**
		 * the beining of the date range the bar represents (note: only tested with one full year range)
		 */
		private var _startDate:Date=new Date(new Date().fullYear, 0, 1);

		public function get startDate():Date
		{
			return _startDate;
		}

		public function set startDate(value:Date):void
		{
			_startDate=value;
			invalidateDisplayList();
		}

		/**
		 * the ending of the date range the bar represents (note: only tested with one full year range)
		 */
		private var _endDate:Date=new Date();

		public function get endDate():Date
		{
			return _endDate;
		}

		public function set endDate(value:Date):void
		{
			_endDate=value;
			invalidateDisplayList();
		}

		/**
		 * the begining of the selected range
		 */
		private var _selectionBeginDate:Date;

		public function get selectionBeginDate():Date
		{
			return _selectionBeginDate;
		}

		public function set selectionBeginDate(value:Date):void
		{
			_selectionBeginDate=value;
			invalidateDisplayList();
		}

		/**
		 * the end of the selected range
		 */
		private var _selectionEndDate:Date

		public function get selectionEndDate():Date
		{
			return _selectionEndDate;
		}

		public function set selectionEndDate(value:Date):void
		{
			_selectionEndDate=value;
			invalidateDisplayList();
		}

		/**
		 * list of lables that appear on the bar
		 */
		protected var labelList:Array=[];

		/**
		 * list of TextField instances that have been created
		 */
		protected var textFieldList:Array=[];

		/**
		 * the instance of the left handle sprite
		 */
		protected var leftHandle:Sprite;

		/**
		 * the instance of the right handle sprite
		 */
		protected var rightHandle:Sprite;

		/**
		 * the bar drawn between the two thumb buttons
		 */
		protected var selectionBar:Sprite;

		/**
		 * the bounds of the dragable area and what the handles are attached to
		 */
		protected var dragTray:Sprite;

		/**
		 * the bar starting position when a drag starts
		 */
		protected var barStartX:Number;

		/**
		 * the left thumb starting position when a drag starts
		 */
		protected var leftStartX:Number;

		/**
		 * the right thumb starting position when a drag starts
		 */
		protected var rightStartX:Number;

		/**
		 * true if any dragging is happening
		 */
		protected var isDragging:Boolean=false;

		/**
		 * true if the bar is being dragged
		 */
		protected var isBarDown:Boolean=false;

		/**
		 * The embeded slider handle image
		 */
		[Embed(source="/assets/images/slider_handle.png")]
		public static const HANDLE:Class;


		/**
		 * Constructor
		 */
		public function DateSliderComponent()
		{
			// Do nothing

		}

		override protected function updateDisplayList(unscaledWidth:Number, unscaledHeight:Number):void
		{
			super.updateDisplayList(unscaledWidth, unscaledHeight);

			// Clear all graphics
			graphics.clear();

			// Remove labels
			removeLabels();

			drawBackground(unscaledWidth, unscaledHeight);

			layoutContents(unscaledWidth, unscaledHeight);
		}

		protected function drawBackground(unscaledWidth:Number, unscaledHeight:Number):void
		{
			graphics.lineStyle(3, borderColor, 1, true);
			graphics.beginFill(backgroundColor, 1);
			graphics.drawRoundRect(0, 0, unscaledWidth, unscaledHeight, 10, 10);
			graphics.endFill();
		}

		protected function layoutContents(unscaledWidth:Number, unscaledHeight:Number):void
		{
			drawHandles();
			drawLabels();

			layoutLabels(unscaledWidth - (paddingLeft + paddingRight), unscaledHeight);
			layoutHandles(unscaledWidth - (paddingLeft + paddingRight), unscaledHeight);
		}

		private function drawHandles():void
		{
			if (!dragTray)
			{
				dragTray=new Sprite();
				dragTray.buttonMode=true;
				dragTray.addEventListener(MouseEvent.CLICK, mouseClickHandler, false, 0, true);
				addChild(dragTray);
			}

			if (!selectionBar)
			{
				selectionBar=new Sprite();
				selectionBar.buttonMode=true;
				selectionBar.addEventListener(MouseEvent.MOUSE_DOWN, selectionBarMouseDownHandler, false, 0, true);
				selectionBar.addEventListener(MouseEvent.CLICK, ignoreMouseClickHandler, false, 0, true);
				dragTray.addChild(selectionBar);
			}

			if (!leftHandle)
			{
				leftHandle=new Sprite();
				leftHandle.addChild(new HANDLE());
				leftHandle.buttonMode=true;
				leftHandle.addEventListener(MouseEvent.MOUSE_DOWN, leftHandleMouseDownHandler, false, 0, true);
				leftHandle.addEventListener(MouseEvent.CLICK, ignoreMouseClickHandler, false, 0, true);
				dragTray.addChild(leftHandle);
			}

			if (!rightHandle)
			{
				rightHandle=new Sprite();
				rightHandle.addChild(new HANDLE());
				rightHandle.buttonMode=true;
				rightHandle.addEventListener(MouseEvent.MOUSE_DOWN, rightHandleMouseDownHandler, false, 0, true);
				rightHandle.addEventListener(MouseEvent.CLICK, ignoreMouseClickHandler, false, 0, true);
				dragTray.addChild(rightHandle);
			}
		}

		protected function layoutHandles(width:Number, height:Number):void
		{
			// Draw the tray
			dragTray.graphics.clear();
			dragTray.graphics.beginFill(0xFFFFFF, 0.0); // turn alpha up for debugging
			dragTray.graphics.drawRect(0, 0, width, height - 14);
			dragTray.graphics.endFill();
			dragTray.x=paddingLeft;
			dragTray.y=10;

			if (!isDragging)
			{
				positionLeftHandle(width, height);
				positionRightHandle(width, height);
			}

			drawSelectionBar();
		}

		protected function drawSelectionBar():void
		{
			var barWidth:int=rightHandle.x - leftHandle.x;
			var barHeight:int=rightHandle.height;

			selectionBar.graphics.clear();
			selectionBar.graphics.beginFill(0xFFC267, 0.5);
			selectionBar.graphics.drawRect(leftHandle.x + (leftHandle.width / 2), leftHandle.y, barWidth, barHeight);
			selectionBar.graphics.endFill();
		}

		protected function positionLeftHandle(width:Number, height:Number):void
		{
			var w:int=width - (paddingLeft + paddingRight)

			var yPos:int=0;
			var xPos:int=0; // Far left

			var segmentWidth:int=width / labelList.length;

			switch (dateRange)
			{
				case DateRangeEnum.MONTH:
				{
					xPos=(selectionBeginDate.month) * segmentWidth;
					break;
				}
				case DateRangeEnum.QUARTER:
				{
					var quarter:int=Math.ceil((selectionBeginDate.month + 1) / 3);
					xPos=(quarter - 1) * (segmentWidth);
					break;
				}
				default:
				{
					break;
				}
			}

			leftHandle.x=xPos - (leftHandle.width / 2);
			leftHandle.y=yPos;
		}

		protected function positionRightHandle(width:Number, height:Number):void
		{
			var w:int=width - (paddingLeft + paddingRight)

			var yPos:int=0;
			var xPos:int=w - rightHandle.width; // Far right

			var segmentWidth:int=width / labelList.length;

			switch (dateRange)
			{
				case DateRangeEnum.MONTH:
				{
					xPos=(selectionEndDate.month + 1) * segmentWidth;
					break;
				}
				case DateRangeEnum.QUARTER:
				{
					var quarter:int=Math.ceil((selectionEndDate.month + 1) / 3);
					xPos=quarter * segmentWidth;
					break;
				}
				default:
				{
					break;
				}
			}

			rightHandle.x=xPos - (rightHandle.width / 2);
			rightHandle.y=yPos;
		}

		protected function drawLabels():void
		{
			switch (dateRange)
			{
				case DateRangeEnum.MONTH:
				{
					labelList=buildMonthLabels();
					break;
				}
				case DateRangeEnum.QUARTER:
				{
					labelList=buildQuarterLabels();
					break;
				}
				case DateRangeEnum.YEAR:
				{
					labelList=buildYearLabels();
					break;
				}
			}
		}

		protected function buildYearLabels():Array
		{
			var a:Array=DateTimeUtil.buildYearList(startDate, endDate);

			var labels:Array=[];
			for each (var date:Date in a)
			{
				labels.push(date.fullYear);
			}
			return labels;
		}

		protected function buildQuarterLabels():Array
		{
			var a:Array=DateTimeUtil.buildQuarterList(startDate, endDate);

			var labels:Array=[];
			for each (var date:Date in a)
			{
				labels.push(DateTimeUtil.formatQuarterName(date));
			}
			return labels;
		}


		protected function buildMonthLabels():Array
		{
			var a:Array=DateTimeUtil.buildMonthList(startDate, endDate);

			var labels:Array=[];
			for each (var date:Date in a)
			{
				labels.push(DateTimeUtil.formatMonthName(date));
			}
			return labels;
		}

		protected function layoutLabels(unscaledWidth:Number, unscaledHeight:Number):void
		{
			if (!labelList || labelList.length == 0)
			{
				return;
			}

			var w:int=unscaledWidth;
			var segmentWidth:int=unscaledWidth / labelList.length;

			textFieldList=[];
			for each (var s:String in labelList)
			{
				// Build the TextField and push into a list
				textFieldList.push(drawLabelTextField(s, segmentWidth));
			}

			var xPos:int=paddingLeft;
			var yPos:int=unscaledHeight / 2;
			for each (var tf:TextField in textFieldList)
			{
				tf.x=xPos;
				tf.y=yPos - ((tf.textHeight + 4) / 2)
				addChild(tf);

				// draw line segment
				drawLineSegment(xPos, 7, segmentWidth);

				// draw tick mark
				drawTickMark(xPos + (segmentWidth / 2), 7);

				// increment x
				xPos+=segmentWidth;
			}
		}

		protected function removeLabels():void
		{
			for each (var tf:TextField in textFieldList)
			{
				removeChild(tf);
				tf=null;
			}
		}

		protected function drawLabelTextField(text:String, width:int):TextField
		{
			var tf:TextField=new TextField();
			tf.defaultTextFormat=new TextFormat("MyriadPro Regular", 11, 0x4D4D4D, null, null, null, null, null, TextFormatAlign.CENTER);
			tf.selectable=false;
			tf.mouseEnabled=false;
			tf.width=width;
			tf.text=text;
			tf.mouseEnabled=false;

			return tf;
		}

		protected function drawTickMark(x:int, y:int):void
		{
			graphics.lineStyle(0, 0, 0);

			graphics.beginFill(0x000000, 1);
			graphics.drawRect(x, y, 1, 5);
			graphics.endFill();
		}

		protected function drawLineSegment(x:int, y:int, width:int):void
		{
			graphics.lineStyle(0, 0, 0);

			graphics.beginFill(0x000000, 1);
			graphics.drawRect(x, y, width, 1);
			graphics.endFill();

			graphics.beginFill(0x1A1A1A, 1);
			graphics.drawRect(x, y + 1, width, 1);
			graphics.endFill();
		}

		protected function updateSelectionDates():void
		{
			var now:Date=new Date();

			var w:int=unscaledWidth - (paddingLeft + paddingRight);

			// Left / Begin
			var leftX:int=leftHandle.x;
			var segmentCount:int=textFieldList.length;
			var segmentWidth:int=w / segmentCount;

			switch (dateRange)
			{
				case DateRangeEnum.MONTH:
				{
					var month:int=0; // zero based monthy
					month=Math.ceil((leftHandle.x + paddingLeft + (segmentWidth / 2)) * segmentCount / w) - 1;
					selectionBeginDate=new Date(now.fullYear, month);

					// Right / End
					month=Math.ceil((rightHandle.x + paddingLeft + (segmentWidth / 2)) * segmentCount / w) - 1;
					selectionEndDate=new Date(now.fullYear, month, 0); // Last day of next month
					break;
				}
				case DateRangeEnum.QUARTER:
				{
					var quarter:int=1; // 1 based quarters (1 - 4)

					// Left / Start
					quarter=Math.ceil((leftHandle.x + paddingLeft + (segmentWidth / 2)) * segmentCount / w);
					selectionBeginDate=DateTimeUtil.getFirstDateOfQuarter(new Date(now.fullYear, (quarter * 3) - 1, 1));

					// Right / End
					quarter=Math.ceil((rightHandle.x + paddingLeft - (segmentWidth / 2)) * segmentCount / w);
					selectionEndDate=DateTimeUtil.getLastDateOfQuarter(new Date(now.fullYear, (quarter * 3) - 1, 1));
					break;
				}
				default:
				{
					break;
				}
			}
		}

		private function updateHandles():void
		{
			// Update the dates based on the current positions
			updateSelectionDates();

			// Snap the handles
			layoutHandles(unscaledWidth - (paddingLeft + paddingRight), unscaledHeight);

			isDragging=false;
			isBarDown=false;

			// Notify parent
			dispatchEvent(new Event(Event.CHANGE, true));
		}


		//
		// Event Handlers
		//

		protected function ignoreMouseClickHandler(event:MouseEvent):void
		{
			// eat it
			event.stopPropagation();
			event.stopImmediatePropagation();
		}

		protected function leftHandleMouseDownHandler(event:MouseEvent):void
		{
			event.stopPropagation();
			event.stopImmediatePropagation();

			if (isDragging || isBarDown)
			{
				return;
			}

			stage.addEventListener(MouseEvent.MOUSE_UP, stageMouseUpHandler, false, 0, true);
			stage.addEventListener(MouseEvent.MOUSE_MOVE, stageMouseMoveHandler, false, 0, true);

			var xBounds:int=-(leftHandle.width / 2);
			var segmentWidth:int=dragTray.width / labelList.length;

			leftHandle.startDrag(true, new Rectangle(xBounds, 0, dragTray.width - (dragTray.width - rightHandle.x) - segmentWidth, 0));
			isDragging=true;
		}

		protected function rightHandleMouseDownHandler(event:MouseEvent):void
		{
			event.stopPropagation();
			event.stopImmediatePropagation();

			if (isDragging || isBarDown)
			{
				return;
			}
			stage.addEventListener(MouseEvent.MOUSE_UP, stageMouseUpHandler, false, 0, true);
			stage.addEventListener(MouseEvent.MOUSE_MOVE, stageMouseMoveHandler, false, 0, true);

			var xBounds:int=-(rightHandle.width / 2);
			var segmentWidth:int=dragTray.width / labelList.length;

			rightHandle.startDrag(true, new Rectangle(xBounds + (leftHandle.x + paddingLeft + segmentWidth), 0, dragTray.width, 0));
			isDragging=true;
		}

		protected function selectionBarMouseDownHandler(event:MouseEvent):void
		{
			event.stopPropagation();
			event.stopImmediatePropagation();

			if (isDragging || isBarDown)
			{
				return;
			}

			stage.addEventListener(MouseEvent.MOUSE_UP, stageMouseUpHandler, false, 0, true);
			stage.addEventListener(MouseEvent.MOUSE_MOVE, stageMouseMoveHandler, false, 0, true);

			barStartX=event.localX;
			leftStartX=leftHandle.x;
			rightStartX=rightHandle.x;

			isDragging=true;
			isBarDown=true;
		}

		protected function stageMouseUpHandler(event:MouseEvent):void
		{
			event.stopPropagation();
			event.stopImmediatePropagation();

			if (stage)
			{
				stage.removeEventListener(MouseEvent.MOUSE_UP, stageMouseUpHandler);
				stage.removeEventListener(MouseEvent.MOUSE_MOVE, stageMouseMoveHandler);
			}

			rightHandle.stopDrag();
			leftHandle.stopDrag();
			selectionBar.stopDrag();

			updateHandles();
		}

		protected function stageMouseMoveHandler(event:MouseEvent):void
		{
			if (isBarDown)
			{
				// stage point
				var stagePoint:Point=new Point(event.stageX, event.stageY);
				var barPoint:Point=dragTray.globalToLocal(stagePoint);

				var delta:int=barStartX - barPoint.x;
				var w:int=unscaledWidth - (paddingLeft + paddingRight);
				var handleWidth:int=leftHandle.width;
				var halfHandleWidth:int=leftHandle.width / 2;

				if (leftStartX - delta >= -halfHandleWidth && leftStartX - delta <= w - halfHandleWidth && rightStartX - delta <= w - halfHandleWidth && rightStartX - delta >= -halfHandleWidth)
				{
					leftHandle.x=leftStartX - delta;
					rightHandle.x=leftHandle.x + selectionBar.width;
				}

				drawSelectionBar();
			}
			else
			{
				layoutHandles(unscaledWidth - (paddingLeft + paddingRight), unscaledHeight);
			}
		}

		protected function mouseClickHandler(event:MouseEvent):void
		{
			var delta:int=rightHandle.x - leftHandle.x;
			var leftX:int=leftHandle.x;
			var rightX:int=rightHandle.x;

			if (event.localX < leftHandle.x)
			{
				leftX=event.localX;
				rightX=leftX + delta;
			}
			else if (event.localX > rightHandle.x)
			{
				rightX=event.localX;
				leftX=rightX - delta;
			}

			leftHandle.x=leftX;
			rightHandle.x=rightX;

			updateHandles();
		}

	}
}