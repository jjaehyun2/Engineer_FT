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

import flash.display.MovieClip;
import flash.display.Loader;
import flash.events.Event;
import flash.system.ApplicationDomain;
import flash.system.LoaderContext;
import flash.utils.ByteArray;

/**
 *  Dispatched after the SWF asset has been fully loaded.
 *
 *  @eventType flash.events.Event.COMPLETE
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Event(name="complete", type="flash.events.Event")]

/**
 *  MovieClipLoaderAsset is a subclass of the MovieClipAsset class
 *  which represents SWF files that you embed in a Flex application.
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class MovieClipLoaderAsset extends MovieClipAsset
								  implements IFlexAsset, IFlexDisplayObject
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
	public function MovieClipLoaderAsset()
	{
		super();

		var loaderContext:LoaderContext = new LoaderContext();
		loaderContext.applicationDomain = new
			ApplicationDomain(ApplicationDomain.currentDomain);
		
		// in AIR...
		// when embedding a SWF using @Embed, you are actively asking for the SWF
		// to be executed, otherwise the SWF will fail loading due to
		// Loader.allowLoadBytesCodeExecution.
		//
		// this property prevents accidentally loading a potentially dangerous
		// SWF into the application sandbox.
		//
		// since this property is indirectly accessed, this should be revisited
		// after AIR 1.x, as it may become deprecated 
		if ("allowLoadBytesCodeExecution" in loaderContext)
			loaderContext["allowLoadBytesCodeExecution"] = true;

		loader = new Loader();
		loader.contentLoaderInfo.addEventListener(Event.COMPLETE,
												  completeHandler);
		loader.loadBytes(movieClipData, loaderContext);
		addChild(loader);
	}

	//--------------------------------------------------------------------------
	//
	//  Variables
	//
	//--------------------------------------------------------------------------
	
	/**
	 *  @private
	 */
	private var loader:Loader = null;
	 
	/**
	 *  @private
	 */
	private var initialized:Boolean = false;
	
	/**
	 *  @private
	 */
	private var requestedWidth:Number;
	
	/**
	 *  @private
	 */
	private var requestedHeight:Number;
	
	/**
	 *  Backing storage for the <code>measuredWidth</code> property.
	 *  Subclasses should set this value in the constructor.
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	protected var initialWidth:Number = 0;
	
	/**
	 *  Backing storage for the <code>measuredHeight</code> property.
	 *  Subclasses should set this value in the constructor.
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	protected var initialHeight:Number = 0;

	//--------------------------------------------------------------------------
	//
	//  Overridden properties
	//
	//--------------------------------------------------------------------------

	//----------------------------------
	//  height
	//----------------------------------

	/**
	 *  @private
	 */
	override public function get height():Number
	{
		if (!initialized)
			return initialHeight;
		
		return super.height;
	}
	
	/**
	 *  @private
	 */
	override public function set height(value:Number):void
	{
		if (!initialized)
			requestedHeight = value;
		else
			loader.height = value;
	}
	
	//----------------------------------
	//  measuredHeight
	//----------------------------------

	/**
	 *  @private
	 *  The default height, in pixels.
	 */
	override public function get measuredHeight():Number
	{
		return initialHeight;
	}

	//----------------------------------
	//  measuredWidth
	//----------------------------------

	/**
	 *  @private
	 *  The default width, in pixels.
	 */
	override public function get measuredWidth():Number
	{
		return initialWidth;
	}
	
	//----------------------------------
	//  width
	//----------------------------------

	/**
	 *  @private
	 */
	override public function get width():Number
	{
		if (!initialized)
			return initialWidth;
		
		return super.width;
	}
	
	/**
	 *  @private
	 */
	override public function set width(value:Number):void
	{
		if (!initialized)
			requestedWidth = value;
		else
			loader.width = value;
	}

	//--------------------------------------------------------------------------
	//
	//  Properties
	//
	//--------------------------------------------------------------------------

	//----------------------------------
	//  movieClipData
	//----------------------------------

	/**
	 *  A ByteArray containing the inner content.
	 *  Overridden in subclasses.
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function get movieClipData():ByteArray
	{
		return null;
	}

	//--------------------------------------------------------------------------
	//
	//  Event handlers
	//
	//--------------------------------------------------------------------------

	/**
	 *  @private
	 *  The event handler for the <code>complete</code> event.
	 */
	private function completeHandler(event:Event):void
	{
		initialized = true;
		
		initialWidth = loader.contentLoaderInfo.width;
		initialHeight = loader.contentLoaderInfo.height;
		
		if (!isNaN(requestedWidth))
			loader.width = requestedWidth;
		
		if (!isNaN(requestedHeight))
			loader.height = requestedHeight;
		
		// Forward the event
		dispatchEvent(event);
	}
}

}