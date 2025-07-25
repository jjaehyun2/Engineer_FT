package com.rockdot.plugin.screen.displaylist.view {
	import flash.accessibility.AccessibilityProperties;
	import flash.display.DisplayObject;
	import flash.display.DisplayObjectContainer;
	import flash.display.IBitmapDrawable;
	import flash.display.LoaderInfo;
	import flash.display.Stage;
	import flash.events.IEventDispatcher;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import flash.geom.Transform;

	/**
	 * @author Nils Doehring (nilsdoehring@gmail.com)
	 */
	public interface IDisplayObject extends IBitmapDrawable, IEventDispatcher {
		function get accessibilityProperties() : AccessibilityProperties;
		function set accessibilityProperties(value : AccessibilityProperties) : void;

		function get alpha() : Number;
		function set alpha(value : Number) : void;

		function get blendMode() : String;
		function set blendMode(value : String) : void;

		// FP 10
//		function set blendShader(value : Shader) : void;

		function get cacheAsBitmap() : Boolean;
		function set cacheAsBitmap(value : Boolean) : void;

		function get filters() : Array;
		function set filters(value : Array) : void;

		function getBounds(targetCoordinateSpace : DisplayObject) : Rectangle;
		function getRect(targetCoordinateSpace : DisplayObject) : Rectangle;

		function globalToLocal(point : Point) : Point;

		// FP 10
//		function globalToLocal3D(point : Point) : Vector3D;

		function get height() : Number;
		function set height(value : Number) : void;

		function hitTestObject(obj : DisplayObject) : Boolean;
		function hitTestPoint(x : Number, y : Number, shapeFlag : Boolean = false) : Boolean;

		function get loaderInfo() : LoaderInfo;

		// FP 10
//		function local3DToGlobal(point3d : Vector3D) : Point;

		function localToGlobal(point : Point) : Point;

		function get mask() : DisplayObject;
		function set mask(value : DisplayObject) : void;

		function get mouseX() : Number;
		function get mouseY() : Number;

		function get name() : String;
		function set name(value : String) : void;

		function get opaqueBackground() : Object;
		function set opaqueBackground(value : Object) : void;

		function get parent() : DisplayObjectContainer;

		function get root() : DisplayObject;

		function get rotation() : Number;
		function set rotation(value : Number) : void;

		// FP 10
		function get rotationX() : Number;

		// FP 10
		function set rotationX(value : Number) : void;

		// FP 10
		function get rotationY() : Number;

		// FP 10
		function set rotationY(value : Number) : void;

		// FP 10
		function get rotationZ() : Number;

		// FP 10
		function set rotationZ(value : Number) : void;

		function get scale9Grid() : Rectangle;
		function set scale9Grid(innerRectangle : Rectangle) : void;

		function get scaleX() : Number;
		function set scaleX(value : Number) : void;

		function get scaleY() : Number;
		function set scaleY(value : Number) : void;

		// FP 10
		function get scaleZ() : Number;

		// FP 10
		function set scaleZ(value : Number) : void;

		function get scrollRect() : Rectangle;
		function set scrollRect(value : Rectangle) : void;

		function get stage() : Stage;
		
		function get transform() : Transform;
		function set transform(value : Transform) : void;

		function get visible() : Boolean;
		function set visible(value : Boolean) : void;

		function get width() : Number;
		function set width(value : Number) : void;

		function get x() : Number;
		function set x(value : Number) : void;

		function get y() : Number;
		function set y(value : Number) : void;

		// FP 10
		function get z() : Number;

		// FP 10
		function set z(value : Number) : void;
	}
}