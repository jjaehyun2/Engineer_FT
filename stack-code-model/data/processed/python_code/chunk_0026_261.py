////////////////////////////////////////////////////////////////////////////////
//
//  Licensed to the Apache Software Foundation (ASF) under one or more
//  contributor license agreements.  See the NOTICE file distributed with
//  this work for additional information regarding copyright ownership.
//  The ASF licenses this file to You under the Apache License, Version 2.0
//  (the "License"); you may not use this file except in compliance with
//  the License.  You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.
//
////////////////////////////////////////////////////////////////////////////////

package mx.core
{
	
import flash.display.DisplayObject;
import flash.utils.Dictionary;
import flash.events.EventDispatcher;
import flash.events.IEventDispatcher;
	
import mx.events.DynamicEvent;
import mx.managers.ISystemManager;
	
/**
 *  A SWFBridgeGroup represents all of the sandbox bridges that an 
 *  application needs to communicate with its parent and children.
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class SWFBridgeGroup extends EventDispatcher implements ISWFBridgeGroup
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
     *  @param owner The DisplayObject that owns this group.
     *  This should be the SystemManager of an application.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
	public function SWFBridgeGroup(owner:ISystemManager)
	{
        super();

		_groupOwner = owner;
	}
	
	//--------------------------------------------------------------------------
	//
	//  Variables
	//
	//--------------------------------------------------------------------------

    //----------------------------------
    //  groupOwner
    //----------------------------------
	
    /**
	 *  @private
     *  The DisplayObject that owns this group.
	 */
	private var _groupOwner:ISystemManager;
	
	/**
	 *  @private
	 *  Allows communication with children that are in different sandboxes.
	 *  The sandbox bridge is used as a hash to find the display object.
	 */
	private var _childBridges:Dictionary;
	
 	//--------------------------------------------------------------------------
	//
	//  Properties: ISWFBridgeGroup
	//
	//--------------------------------------------------------------------------

    //----------------------------------
    //  parentBridge
    //----------------------------------
	
    /**
     *  @private
     */
    private var _parentBridge:IEventDispatcher;
	
    /**
     *  Allows communication with the parent
     *  if the parent is in a different sandbox.
     *  May be <code>null</code> if the parent is in the same sandbox
     *  or this is the top-level root application.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
	public function get parentBridge():IEventDispatcher
	{
		return _parentBridge;
	}

    /**
     *  @private
     */	
	public function set parentBridge(bridge:IEventDispatcher):void
	{
		_parentBridge = bridge;
	}
	
	//--------------------------------------------------------------------------
	//
	//  Methods: ISWFBridgeGroup
	//
	//--------------------------------------------------------------------------
	
	/**
	 *  @inheritDoc
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function addChildBridge(bridge:IEventDispatcher, bridgeProvider:ISWFBridgeProvider):void
	{
		if (!_childBridges)
			_childBridges = new Dictionary();

		_childBridges[bridge] = bridgeProvider;

		var event:DynamicEvent = new DynamicEvent("addChildBridge");
		event.bridge = bridge;
		event.bridgeProvider = bridgeProvider;
		dispatchEvent(event);
	}

	/**
	 *  @inheritDoc
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function removeChildBridge(bridge:IEventDispatcher):void
	{
		if (!_childBridges || !bridge)
			return;
		
		for (var iter:Object in _childBridges)
		{
			if (iter == bridge)
				delete _childBridges[iter];
		}

		var event:DynamicEvent = new DynamicEvent("removeChildBridge");
		event.bridge = bridge;
		dispatchEvent(event);
	}

	/**
	 *  @inheritDoc
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function getChildBridgeProvider(bridge:IEventDispatcher):ISWFBridgeProvider
	{
		if (!_childBridges)
			return null;
			
		return ISWFBridgeProvider(_childBridges[bridge]);
	}
	
	/**
	 *  @inheritDoc
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function getChildBridges():Array
	{
		var bridges:Array = [];
		
        for (var iter:Object in _childBridges)
		{
			bridges.push(iter);
		}	
		
		return bridges;
	}

	/**
	 *  @inheritDoc
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function containsBridge(bridge:IEventDispatcher):Boolean
	{
		if (parentBridge && parentBridge == bridge)
			return true;
			
		for (var iter:Object in _childBridges)
		{
			if (bridge == iter)
				return true;	
		}
				
		return false;
	}
}

}