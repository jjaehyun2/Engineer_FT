///////////////////////////////////////////////////////////
//  IShape.as
//  Macromedia ActionScript Implementation of the Interface IShape
//  Generated by Enterprise Architect
//  Created on:      01-Apr-2008 8:09:24 AM
//  Original author: alessandro crugnola
///////////////////////////////////////////////////////////

package com.aviary.geom
{
	import __AS3__.vec.Vector;
	
	import com.aviary.display.IShapeContainer;
	import com.aviary.geom.controls.IHandle;
	import com.aviary.geom.path.IPath;
	import com.aviary.sdk.storage.eggfile.IEGGNode;
	
	import flash.display.Graphics;
	import flash.geom.Rectangle;
	import flash.utils.ByteArray;

	/**
	 * An IShape interface is the base interface for vector objects like Paths, Vector
	 * drawings, Text
	 * @author alessandro crugnola
	 * @version 1.0
	 * @created 01-Apr-2008 8:09:25 AM
	 */
	public interface IShape
	{
		function get path_commands( ): Vector.<int>;
		function get path_data( ): Vector.<Number>;
		
		function get container(): IShapeContainer;
		function get eggNode( ): IEGGNode;
		function set eggNode( value: IEGGNode ): void;
		function get uid( ): String;
		function set uid( value: String ): void;
		function get type( ): String;
		function set container(value:IShapeContainer): void;
		function get allowMultipleHandleSelection(): Boolean;
		function get locked( ): Boolean;
		function set locked( value: Boolean ): void;
		function get boundingBox(): Rectangle;
		function get handles(): Vector.<IHandle>;
		function get colorRect(): Rectangle;
		function set colorRect( value: Rectangle ): void;
		
		/**
		 * Invalidate the current shape/path and force the recreation of the bounding box
		 * Rectangle
		 * @see boundingBox
		 * @see flash.geom.Rectangle
		 */
		function invalidate(): void;
		function generatePath(): IPath;
		function render( g: Graphics ): void;
		function getHandleByUid( value: String ): IHandle;
		function decodeColorRect( data: ByteArray ): Rectangle;
		function toString( ): String;
		function decode( node: IEGGNode ): void;
		function encode( ): IEGGNode;		
		
	}//end IShape

}