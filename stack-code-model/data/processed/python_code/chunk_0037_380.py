package visualComponents {
	
	import components.Timeout;
	import core.TPMovieClip;
	import flash.display.MovieClip;
	import flash.geom.ColorTransform;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import states.AnimationSizeStates;
	import core.TPStage;
	
	/**
	 * ...
	 * @author notSafeForDev
	 */
	public class Borders {
		
		private var element : TPMovieClip;
		
		private var color : Number;
		
		private var containerWidth : Number;
		private var containerHeight : Number;
		private var containerAspectRatio : Number;
		private var containerMaxDimension : Number;
		
		private var highlightBorderTimeout : Number;
		
		public function Borders(_parent : TPMovieClip, _color : Number) {
			element = TPMovieClip.create(_parent, "borders");
			
			color = _color;
			
			containerWidth = TPStage.stageWidth;
			containerHeight = TPStage.stageHeight;
			containerAspectRatio = containerWidth / containerHeight;
			containerMaxDimension = Math.max(containerWidth, containerHeight);
			
			AnimationSizeStates.listen(this, onAnimationSizeStatesChange, [AnimationSizeStates.width, AnimationSizeStates.height]);
		}
		
		private function onAnimationSizeStatesChange() : void {
			update(AnimationSizeStates.width.value / AnimationSizeStates.height.value);
			
			if (AnimationSizeStates.isUsingInitialSize.value == true) {
				return;
			}
			
			Timeout.clear(highlightBorderTimeout);
			
			var highlightColorTransform : ColorTransform = new ColorTransform();
			highlightColorTransform.redOffset = 100;
			highlightColorTransform.alphaMultiplier = 0.5;
			element.colorTransform = highlightColorTransform;
			
			highlightBorderTimeout = Timeout.set(this, doneHighlightingBorders, 500);
		}
		
		private function doneHighlightingBorders() : void {
			element.colorTransform = new ColorTransform();
		}
		
		private function update(_visibleAreaAspectRatio : Number) : void {
			var shouldShowTopAndBottomBorders : Boolean = _visibleAreaAspectRatio > containerAspectRatio;
			
			var topBorderHeight : Number = 0;
			var sideBorderWidth : Number = 0;
			
			if (shouldShowTopAndBottomBorders == true) {
				topBorderHeight = (containerHeight - (containerWidth / _visibleAreaAspectRatio)) * 0.5;
			} else {
				sideBorderWidth = (containerWidth - (containerHeight * _visibleAreaAspectRatio)) * 0.5;
			}
			
			var outsideRect : Rectangle = new Rectangle(
				-containerMaxDimension, 
				-containerMaxDimension, 
				containerWidth + containerMaxDimension * 2, 
				containerHeight + containerMaxDimension * 2
			);
			
			var insideRect : Rectangle = new Rectangle(
				sideBorderWidth, 
				topBorderHeight, 
				containerWidth - sideBorderWidth * 2, 
				containerHeight - topBorderHeight * 2
			);
			
			element.graphics.clear();
			element.graphics.beginFill(color);
			element.graphics.drawRect(outsideRect.x, outsideRect.y, outsideRect.width, insideRect.y - outsideRect.y); // Top
			element.graphics.drawRect(outsideRect.x, insideRect.y, insideRect.x - outsideRect.x, insideRect.height); // Left
			element.graphics.drawRect(insideRect.right, insideRect.y, outsideRect.right - insideRect.right, insideRect.height); // Right
			element.graphics.drawRect(outsideRect.x, insideRect.bottom, outsideRect.width, insideRect.y - outsideRect.y); // Top
		}
	}
}