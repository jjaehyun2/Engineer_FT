/**
 * Copyright (c) 2014-present, ErZhuan(coco) Xie
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
package coco.core.popup
{
	import flash.display.DisplayObject;
	import flash.display.Stage;
	import flash.geom.Point;
	
	import coco.core.UIComponent;
	import coco.event.UIEvent;
	
	/**
	 * Pop Up uicomponent
	 */
	[ExcludeClass]
	public class PopUp extends UIComponent
	{
		
		public function PopUp()
		{
			super();
		}
		
		
		//---------------------------------------------------------------------------------------------------------------------
		//
		// Variables
		//
		//---------------------------------------------------------------------------------------------------------------------
		
		public var modal:Boolean;
		public var closeWhenMouseClickOutside:Boolean;
		public var backgroundColor:uint = 0x000000;
		public var backgroundAlpha:Number = .1;
		
		private var _child:DisplayObject;
		
		public function set child(value:DisplayObject):void
		{
			if (_child) // remove old child resize listener
			{
				_child.removeEventListener(UIEvent.RESIZE, child_resizeHandler);
			}
			
			_child = value;
			
			if (_child)// add new child resize listener
			{
				_child.addEventListener(UIEvent.RESIZE, child_resizeHandler);
			}
			
			invalidateDisplayList();
		}
		
		public function get child():DisplayObject
		{
			return _child;
		}
		
		private var _childParent:DisplayObject;
		
		public function set childParent(value:DisplayObject):void
		{
			if (_childParent) // remove old childParent resize listener
			{
				_childParent.removeEventListener(UIEvent.RESIZE, childParent_resizeHandler);
			}
			
			_childParent = value;
			
			if (_childParent)// add new childParent resize listener
			{
				_childParent.addEventListener(UIEvent.RESIZE, childParent_resizeHandler);
			}
			
			invalidateSize();
			invalidateDisplayList();
		}
		
		public function get childParent():DisplayObject
		{
			return _childParent;
		}
		
		private var _center:Boolean;
		
		public function set center(value:Boolean):void
		{
			_center = value;
			
			invalidateDisplayList();
		}
		
		public function get center():Boolean
		{
			return _center;
		}
		
		
		//---------------------------------------------------------------------------------------------------------------------
		//
		// Methods
		//
		//---------------------------------------------------------------------------------------------------------------------
		
		override protected function createChildren():void
		{
			super.createChildren();
			
			if (child)
				addChild(child);
		}
		
		override protected function measure():void
		{
			super.measure();
			
			// set pop x y width
			if (childParent)
			{
				var popUpPoint:Point = childParent.localToGlobal(new Point(0, 0));
				var popUpScale:Object = getScaleXY(childParent)
				x = popUpPoint.x / popUpScale.scaleX;
				y = popUpPoint.y / popUpScale.scaleY;
				measuredWidth = childParent.width;
				measuredHeight = childParent.height;
			}
		}
		
		override protected function updateDisplayList():void
		{
			super.updateDisplayList();
			
			// set child x y
			if (center && child && childParent)
			{
				child.x = (childParent.width - child.width) / 2;
				child.y = (childParent.height - child.height) / 2;
			}
		}
		
		override protected function drawSkin():void
		{
			super.drawSkin();
			
			// draw bg fill
			if (modal)
			{
				graphics.clear();
				graphics.beginFill(backgroundColor, backgroundAlpha);
				graphics.drawRect(0, 0, width, height);
				graphics.endFill();
			}
		}
		
		private function child_resizeHandler(event:UIEvent):void
		{
			invalidateDisplayList();
		}
		
		private function childParent_resizeHandler(event:UIEvent):void
		{
			invalidateSize();
			invalidateDisplayList();
		}
		
		private function getScaleXY(displayObject:DisplayObject):Object {
			var scaleX:Number = 1, scaleY:Number = 1
			while(displayObject && displayObject.parent && !(displayObject.parent is Stage)){
				scaleX = scaleX * displayObject.parent.scaleX
				scaleY = scaleY * displayObject.parent.scaleY
				displayObject = displayObject.parent
			}
			
			return {scaleX: scaleX, scaleY: scaleY}
		}
		
	}
}