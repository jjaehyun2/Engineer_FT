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

import flash.display.Loader;
import flash.events.Event;
import flash.events.ErrorEvent;
import flash.events.ProgressEvent;
import flash.events.IOErrorEvent;
import flash.events.SecurityErrorEvent;
import flash.net.URLRequest;
import flash.system.LoaderContext;
import flash.system.ApplicationDomain;
import flash.system.LoaderContext;
import flash.system.Security;
import flash.system.SecurityDomain;
import flash.utils.ByteArray;

import mx.events.RSLEvent;
import mx.utils.LoaderUtil;

[ExcludeClass]

/**
 *  @private
 *  RSL Item Class
 * 
 *  Contains properties to describe the RSL and methods to help load the RSL.
 */
public class RSLItem
{
    include "../core/Version.as";
 
    //--------------------------------------------------------------------------
    //
    //  Properties
    //
    //--------------------------------------------------------------------------

    //----------------------------------
    //  urlRequest
    //----------------------------------

    /**
     *  @private
     *  Only valid after loading has started
     */
    public var urlRequest:URLRequest;

    //----------------------------------
    //  total
    //----------------------------------

    /**
     *  @private
     */
    public var total:uint = 0;
    
    //----------------------------------
    //  loaded
    //----------------------------------

    /**
     *  @private
     */
    public var loaded:uint = 0;

    //----------------------------------
    //  rootURL
    //----------------------------------

    /**
     *  @private
     * 
     *  Provides the url used to locate relative RSL urls.
     */ 
    public var rootURL:String;
        

    //--------------------------------------------------------------------------
    //
    //  Variables
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     *  External handlers so the load can be 
     *  observed by the class calling load().
     */
    protected var chainedProgressHandler:Function;    
    protected var chainedCompleteHandler:Function;
    protected var chainedIOErrorHandler:Function;
    protected var chainedSecurityErrorHandler:Function;
    protected var chainedRSLErrorHandler:Function;
    
    /**
     *  @private
     */
    private var completed:Boolean = false;

    /**
     *  @private
     */
    private var errorText:String;
    
    /**
     *  @private
     */
    protected var moduleFactory:IFlexModuleFactory; // application/module loading this RSL.
    
    /**
     *  @private
     */
    protected var url:String;
    
    //--------------------------------------------------------------------------
    //
    //  Constructor
    //
    //--------------------------------------------------------------------------

    /**
     *  Create a RSLItem with a given URL.
     * 
     *  @param url location of RSL to load
     *  @param rootURL provides the url used to locate relative RSL urls. 
     *  @param moduleFactory The module factory that is loading the RSLs. The
     *  RSLs will be loaded into the application domain of the given module factory.
     *  If a module factory is not specified, then the RSLs will be loaded into the 
     *  application domain of where the CrossDomainRSLItem class was first loaded.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function RSLItem(url:String, rootURL:String = null, 
                            moduleFactory:IFlexModuleFactory = null)
    {
        super();

        this.url = url;
        this.rootURL = rootURL;
        this.moduleFactory = moduleFactory;
    }
                    
    //--------------------------------------------------------------------------
    //
    //  Methods
    //
    //--------------------------------------------------------------------------

    /**
     * 
     *  Load an RSL. 
     * 
     *  @param progressHandler Receives ProgressEvent.PROGRESS events.
     *  May be null.
     *
     *  @param completeHandler Receives Event.COMPLETE events.
     *  May be null.
     *
     *  @param ioErrorHandler Receives IOErrorEvent.IO_ERROR events.
     *  May be null.
     *
     *  @param securityErrorHandler
     *  Receives SecurityErrorEvent.SECURITY_ERROR events.
     *  May be null.
     *
     *  @param rslErrorHandler Receives RSLEvent.RSL_ERROR events.
     *  May be null.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function load(progressHandler:Function,
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
        
        var loader:Loader = new Loader();               
        var loaderContext:LoaderContext = new LoaderContext();
        urlRequest = new URLRequest(LoaderUtil.createAbsoluteURL(rootURL, url));
                    
        // The RSLItem needs to listen to certain events.

        loader.contentLoaderInfo.addEventListener(
            ProgressEvent.PROGRESS, itemProgressHandler);
            
        loader.contentLoaderInfo.addEventListener(
            Event.COMPLETE, itemCompleteHandler);
            
        loader.contentLoaderInfo.addEventListener(
            IOErrorEvent.IO_ERROR, itemErrorHandler);
            
        loader.contentLoaderInfo.addEventListener(
            SecurityErrorEvent.SECURITY_ERROR, itemErrorHandler);

        if (moduleFactory != null)
            loaderContext.applicationDomain = moduleFactory.info()["currentDomain"];    
        else 
            loaderContext.applicationDomain = ApplicationDomain.currentDomain;

        loader.load(urlRequest, loaderContext); 
    }
    
    //--------------------------------------------------------------------------
    //
    //  Event handlers
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     */
    public function itemProgressHandler(event:ProgressEvent):void
    {
        // Update the loaded and total properties.
        loaded = event.bytesLoaded;
        total = event.bytesTotal;
        
        // Notify an external listener
        if (chainedProgressHandler != null)
            chainedProgressHandler(event);
    }

    /**
     *  @private
     */
    public function itemCompleteHandler(event:Event):void
    {
        completed = true;
        
        // Notify an external listener
        if (chainedCompleteHandler != null)
            chainedCompleteHandler(event);
    }

    /**
     *  @private
     */
    public function itemErrorHandler(event:ErrorEvent):void
    {
        errorText = decodeURI(event.text);
        completed = true;
        loaded = 0;
        total = 0;
        
        trace(errorText);
        
        // Notify an external listener
        if (event.type == IOErrorEvent.IO_ERROR &&
            chainedIOErrorHandler != null)
        {
            chainedIOErrorHandler(event);
        }
        else if (event.type == SecurityErrorEvent.SECURITY_ERROR && 
                 chainedSecurityErrorHandler != null)
        {
            chainedSecurityErrorHandler(event);
        }
        else if (event.type == RSLEvent.RSL_ERROR && 
                 chainedRSLErrorHandler != null)
        {
            chainedRSLErrorHandler(event);
        }

    }
}

}