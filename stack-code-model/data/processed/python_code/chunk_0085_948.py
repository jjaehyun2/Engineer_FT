////////////////////////////////////////////////////////////////////////////////
//
//  ADOBE SYSTEMS INCORPORATED
//  Copyright 2005-2006 Adobe Systems Incorporated
//  All Rights Reserved.
//
//  NOTICE: Adobe permits you to use, modify, and distribute this file
//  in accordance with the terms of the license agreement accompanying it.
//
////////////////////////////////////////////////////////////////////////////////

package mx.managers
{

import flash.display.DisplayObject;
import flash.geom.Point;
import mx.core.IChildList;
import mx.core.mx_internal;

use namespace mx_internal;

[ExcludeClass]

/**
 *  @private
 *  A SystemManager has various types of children,
 *  such as the Application, popups, 
 *  tooltips, and custom cursors.
 *  You can access the just the custom cursors through
 *  the <code>cursors</code> property,
 *  the tooltips via <code>toolTips</code>, and
 *  the popups via <code>popUpChildren</code>.  Each one returns
 *  a SystemChildrenList which implements IChildList.  The SystemManager's
 *  IChildList methods return the set of children that aren't popups, tooltips
 *  or cursors.  To get the list of all children regardless of type, you
 *  use the rawChildrenList property which returns this SystemRawChildrenList.
 */
public class SystemRawChildrenList implements IChildList
{
    include "../core/Version.as";

	//--------------------------------------------------------------------------
	//
	//  Constructor
	//
	//--------------------------------------------------------------------------

	/**
	 *  Constructor.
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function SystemRawChildrenList(owner:SystemManager)
	{
		super();

		this.owner = owner;
	}

	//--------------------------------------------------------------------------
	//
	//  Properties
	//
	//--------------------------------------------------------------------------

	/**
	 *  @private
	 */
	private var owner:SystemManager;

	//--------------------------------------------------------------------------
	//
	//  Methods
	//
	//--------------------------------------------------------------------------

	/**
	 *  @copy mx.core.IChildList#numChildren
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function get numChildren():int
	{
		return owner.$numChildren;
	}

	/**
	 *  @copy mx.core.IChildList#getChildAt
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
  	public function getChildAt(index:int):DisplayObject
  	{
		return owner.rawChildren_getChildAt(index);
  	}

	/**
	 *  @copy mx.core.IChildList#addChild
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function addChild(child:DisplayObject):DisplayObject
  	{
		return owner.rawChildren_addChild(child);
  	}
	
	/**
	 *  @copy mx.core.IChildList#addChildAt
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function addChildAt(child:DisplayObject, index:int):DisplayObject
  	{
		return owner.rawChildren_addChildAt(child,index);
  	}
	
	/**
	 *  @copy mx.core.IChildList#removeChild
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function removeChild(child:DisplayObject):DisplayObject
  	{
		return owner.rawChildren_removeChild(child);
  	}
	
	/**
	 *  @copy mx.core.IChildList#removeChildAt
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function removeChildAt(index:int):DisplayObject
  	{
		return owner.rawChildren_removeChildAt(index);
  	}
	
	/**
	 *  @copy mx.core.IChildList#getChildByName
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
  	public function getChildByName(name:String):DisplayObject
  	{
		return owner.rawChildren_getChildByName(name);
	}
	
	/**
	 *  @copy mx.core.IChildList#getChildIndex
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
  	public function getChildIndex(child:DisplayObject):int
  	{
		return owner.rawChildren_getChildIndex(child);
  	}
	
	/**
	 *  @copy mx.core.IChildList#setChildIndex
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function setChildIndex(child:DisplayObject, newIndex:int):void
  	{
		owner.rawChildren_setChildIndex(child, newIndex);
  	}
	
	/**
	 *  @copy mx.core.IChildList#getObjectsUnderPoint
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function getObjectsUnderPoint(point:Point):Array
	{
		return owner.rawChildren_getObjectsUnderPoint(point);
	}
	
	/**
	 *  @copy mx.core.IChildList#contains
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function contains(child:DisplayObject):Boolean
	{
		return owner.rawChildren_contains(child);
	}
}

}