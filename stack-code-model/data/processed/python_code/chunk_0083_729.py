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

import flash.events.ErrorEvent;
import flash.events.Event;
import flash.events.IEventDispatcher;
import flash.events.IOErrorEvent;
import flash.events.ProgressEvent;
import flash.system.ApplicationDomain;
import mx.events.ResourceEvent;
import mx.events.RSLEvent;
import mx.resources.IResourceManager;

[ExcludeClass]

/**
 *	@private
 *
 *  Preloads a resource module during frame 1, from an URL that was
 *  specified in the application's parameters["resourceModuleURLs"].
 *
 *  The Preloader uses RSLListLoader to sequentially load
 *  cross-domain RSLs, regular RSLs, and resource modules.
 *  Each of these is represented by an RSLItem in a queue
 *  processed by RSLListLoader.
 *  The class names ResourceModuleRSLItem, RSLItem, RSLListLoader,
 *  and RSLEvent are slightly misleading in that a resource module
 *  isn't really an RSL.
 */
public class ResourceModuleRSLItem extends RSLItem
{
    include "../core/Version.as";

	//--------------------------------------------------------------------------
	//
	//  Class variables
	//
	//--------------------------------------------------------------------------

    /**
	 *  @private
     */	
	public static var resourceManager:IResourceManager;

	//--------------------------------------------------------------------------
	//
	//  Constructor
	//
	//--------------------------------------------------------------------------

    /**
	 *  @private
     */	
	public function ResourceModuleRSLItem(url:String, appDomain:ApplicationDomain)
	{
		super(url);
		this.appDomain = appDomain;
	}

	//--------------------------------------------------------------------------
	//
	//  Variables
	//
	//--------------------------------------------------------------------------

	private var appDomain:ApplicationDomain;

	//--------------------------------------------------------------------------
	//
	//  Overridden methods
	//
	//--------------------------------------------------------------------------
	
	/**
	 * 
	 *  Preloads a resource module
     * 
     *  @param progressHandler Receives ProgressEvent.PROGRESS events, may be null
	 *
     *  @param completeHandler Receives Event.COMPLETE events, may be null
	 *
     *  @param ioErrorHandler Receives IOErrorEvent.IO_ERROR events, may be null
	 *
     *  @param securityErrorHandler Receives SecurityErrorEvent.SECURITY_ERROR events, may be null
	 *
     *  @param rslErrorHandler Receives RSLEvent.RSL_ERROR events, may be null
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	override public function load(progressHandler:Function,
                                  completeHandler:Function,
	                              ioErrorHandler:Function,
	                              securityErrorHandler:Function,
	                              rslErrorHandler:Function):void 
	{
	    chainedProgressHandler = progressHandler;
	    chainedCompleteHandler = completeHandler;
	    chainedIOErrorHandler = ioErrorHandler;
	    chainedSecurityErrorHandler = securityErrorHandler;
	    chainedRSLErrorHandler = rslErrorHandler;
	    
		if (!resourceManager)
		{
			// do this to prevent dependency on ResourceManager
			if (appDomain.hasDefinition("mx.resources::ResourceManager"))
			{
				var resourceManagerClass:Class = 
					Class(appDomain.getDefinition("mx.resources::ResourceManager"));
				resourceManager = 
					IResourceManager(resourceManagerClass["getInstance"]());
			}
			else
				return;
		}

		
		var eventDispatcher:IEventDispatcher =
			resourceManager.loadResourceModule(url);
		
		eventDispatcher.addEventListener(
			ResourceEvent.PROGRESS, itemProgressHandler);
			
		eventDispatcher.addEventListener(
			ResourceEvent.COMPLETE, itemCompleteHandler);
			
		eventDispatcher.addEventListener(
			ResourceEvent.ERROR, resourceErrorHandler);
	}
		
	//--------------------------------------------------------------------------
	//
	//  Overridden event handlers
	//
	//--------------------------------------------------------------------------

	/**
	 *  @private
	 */
	private function resourceErrorHandler(event:ResourceEvent):void
	{
		var errorEvent:IOErrorEvent = new IOErrorEvent(IOErrorEvent.IO_ERROR);
		errorEvent.text = event.errorText;

		super.itemErrorHandler(errorEvent);
	}
}

}