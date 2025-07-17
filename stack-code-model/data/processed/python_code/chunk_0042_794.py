package com.illuzor.circles.tools {
	
	import com.illuzor.circles.constants.PointType;
	import flash.geom.Point;
	import starling.display.Sprite;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class ControllerBase {
		
		protected var circleSize:uint;
		protected var centerPoint:Point;
		protected var stageWidth:uint;
		protected var stageHeight:uint;
		protected var container:Sprite;
		
		public function ControllerBase(container:Sprite, circleSize:uint) {
			this.circleSize = circleSize;
			this.container = container;
			stageWidth = container.stage.stageWidth;
			stageHeight = container.stage.stageHeight;
			centerPoint = new Point(stageWidth >> 1, stageHeight >> 1);
		}
		
		protected function getPoint(pointType):Point {
			switch (pointType) {
				case PointType.CENTER_TOP:
					return new Point(centerPoint.x, centerPoint.y - circleSize * 1.5);
				break;
				case PointType.LEFT_TOP:
					return new Point(centerPoint.x - circleSize * 1.5, centerPoint.y - circleSize * 1.5)
				break;
				case PointType.LEFT_BOTTOM:
					return new Point(centerPoint.x - circleSize * 1.5, centerPoint.y + circleSize * 1.5);
				break;
				case PointType.RIGHT_TOP:
					return new Point(centerPoint.x + circleSize * 1.5, centerPoint.y - circleSize * 1.5)
				break;
				case PointType.RIGHT_BOTTOM:
					return new Point(centerPoint.x + circleSize * 1.5, centerPoint.y + circleSize * 1.5)
				break;
				case PointType.RIGHT_TOP_ASIDE:
					return new Point(stageWidth + circleSize/2, centerPoint.y - circleSize * 1.5);
				break;
				case PointType.LEFT_TOP_ASIDE:
					return new Point( -circleSize / 2, centerPoint.y - circleSize * 1.5);
				break;
				case PointType.RIGHT_BOTTOM_ASIDE:
					return new Point(stageWidth + circleSize/2, centerPoint.y + circleSize * 1.5);
				break;
				case PointType.LEFT_BOTTOM_ASIDE:
					return new Point(-circleSize/2, centerPoint.y + circleSize * 1.5);
				break;
			}
			return new Point();
		}
		
		protected function getClockwiseNext(currentPoint:Point):Point {
			var newPoint:Point;
			
			if (currentPoint.equals(getPoint(PointType.LEFT_TOP))) {
				newPoint = getPoint(PointType.RIGHT_TOP);
			} else if (currentPoint.equals(getPoint(PointType.RIGHT_TOP))) {
				newPoint = getPoint(PointType.RIGHT_BOTTOM);
			} else if (currentPoint.equals(getPoint(PointType.RIGHT_BOTTOM))) {
				newPoint = getPoint(PointType.LEFT_BOTTOM);
			} else if (currentPoint.equals(getPoint(PointType.LEFT_BOTTOM))) {
				newPoint = getPoint(PointType.LEFT_TOP);
			}
			return newPoint;
		}
		
		protected function getCounterclockwiseNext(currentPoint:Point):Point {
			var newPoint:Point;
			if (currentPoint.equals(getPoint(PointType.LEFT_TOP))) {
				newPoint = getPoint(PointType.LEFT_BOTTOM);
			} else if (currentPoint.equals(getPoint(PointType.RIGHT_TOP))) {
				newPoint = getPoint(PointType.LEFT_TOP);
			} else if (currentPoint.equals(getPoint(PointType.RIGHT_BOTTOM))) {
				newPoint = getPoint(PointType.RIGHT_TOP);
			} else if (currentPoint.equals(getPoint(PointType.LEFT_BOTTOM))) {
				newPoint = getPoint(PointType.RIGHT_BOTTOM);
			}
			return newPoint;
		}
		
	}
}