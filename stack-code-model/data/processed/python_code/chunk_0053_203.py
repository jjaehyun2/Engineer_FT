package flash.display {
	import flash.geom.Rectangle;
	import flash.text.TextSnapshot;
	import flash.events.Event;
	public class Stage extends DisplayObjectContainer {
		public function get align():String;
		public function set align(value:String):void;
		public function set cacheAsBitmap(value:Boolean):void;
		public function get displayState():String;
		public function set displayState(value:String):void;
		public function get focus():InteractiveObject;
		public function set focus(value:InteractiveObject):void;
		public function get frameRate():Number;
		public function set frameRate(value:Number):void;
		public function get fullScreenHeight():uint;
		public function get fullScreenSourceRect():Rectangle;
		public function set fullScreenSourceRect(value:Rectangle):void;
		public function get fullScreenWidth():uint;
		public function get height():Number;
		public function set height(value:Number):void;
		public function get mouseChildren():Boolean;
		public function set mouseChildren(value:Boolean):void;
		public function get numChildren():int;
		public function get quality():String;
		public function set quality(value:String):void;
		public function get scaleMode():String;
		public function set scaleMode(value:String):void;
		public function get showDefaultContextMenu():Boolean;
		public function set showDefaultContextMenu(value:Boolean):void;
		public function get stageFocusRect():Boolean;
		public function set stageFocusRect(value:Boolean):void;
		public function get stageHeight():int;
		public function set stageHeight(value:int):void;
		public function get stageWidth():int;
		public function set stageWidth(value:int):void;
		public function get tabChildren():Boolean;
		public function set tabChildren(value:Boolean):void;
		public function set tabEnabled(value:Boolean):void;
		public function get textSnapshot():TextSnapshot;
		public function get width():Number;
		public function set width(value:Number):void;
		public override function addChild(child:DisplayObject):DisplayObject;
		public override function addChildAt(child:DisplayObject, index:int):DisplayObject;
		public override function addEventListener(type:String, listener:Function, useCapture:Boolean = false, priority:int = 0, useWeakReference:Boolean = false):void;
		public override function dispatchEvent(event:Event):Boolean;
		public override function hasEventListener(type:String):Boolean;
		public function invalidate():void;
		public function isFocusInaccessible():Boolean;
		public override function removeChildAt(index:int):DisplayObject;
		public override function setChildIndex(child:DisplayObject, index:int):void;
		public override function swapChildrenAt(index1:int, index2:int):void;
		public override function willTrigger(type:String):Boolean;
	}
}