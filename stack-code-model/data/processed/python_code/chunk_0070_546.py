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

package mx.modules 
{

import flash.utils.ByteArray;

import mx.core.IFlexModuleFactory;
import mx.events.Request;

/**
 *  The ModuleManager class centrally manages dynamically loaded modules.
 *  It maintains a mapping of URLs to modules.
 *  A module can exist in a state where it is already loaded
 *  (and ready for use), or in a not-loaded-yet state.
 *  The ModuleManager dispatches events that indicate module status.
 *  Clients can register event handlers and then call the 
 *  <code>load()</code> method, which dispatches events when the factory is ready
 *  (or immediately, if it was already loaded).
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class ModuleManager
{
    include "../core/Version.as";

    //--------------------------------------------------------------------------
    //
    //  Class methods
    //
    //--------------------------------------------------------------------------

    /**
     *  Get the IModuleInfo interface associated with a particular URL.
     *  There is no requirement that this URL successfully load,
     *  but the ModuleManager returns a unique IModuleInfo handle for each unique URL.
     *  
     *  @param url A URL that represents the location of the module.
     *  
     *  @return The IModuleInfo interface associated with a particular URL.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public static function getModule(url:String):IModuleInfo
    {
        return getSingleton().getModule(url);
    }

    /**
     *  See if the referenced object is associated with (or, in the managed
     *  ApplicationDomain of) a known IFlexModuleFactory implementation.
     *  
     *  @param object The object that the ModuleManager tries to create.
     * 
     *  @return Returns the IFlexModuleFactory implementation, or <code>null</code>
     *  if the object type cannot be created from the factory.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public static function getAssociatedFactory(
                                object:Object):IFlexModuleFactory
    {
        return getSingleton().getAssociatedFactory(object);
    }

    /**
     *  @private
     *  Typed as Object, for now. Ideally this should be IModuleManager.
     */
    private static function getSingleton():Object
    {
        if (!ModuleManagerGlobals.managerSingleton)
            ModuleManagerGlobals.managerSingleton = new ModuleManagerImpl();

        return ModuleManagerGlobals.managerSingleton;
    }
}

}

import flash.display.Loader;
import flash.events.ErrorEvent;
import flash.events.Event;
import flash.events.EventDispatcher;
import flash.events.IOErrorEvent;
import flash.events.ProgressEvent;
import flash.events.SecurityErrorEvent;
import flash.net.URLRequest;
import flash.system.ApplicationDomain;
import flash.system.LoaderContext;
import flash.system.Security;
import flash.system.SecurityDomain;
import flash.utils.ByteArray;
import flash.utils.Dictionary;
import flash.utils.getDefinitionByName;
import flash.utils.getQualifiedClassName;

import mx.core.IFlexModuleFactory;
import mx.events.ModuleEvent;
import mx.modules.IModuleInfo;

////////////////////////////////////////////////////////////////////////////////
//
//  Helper class: ModuleManagerImpl
//
////////////////////////////////////////////////////////////////////////////////
import mx.events.Request;

/**
 *  @private
 *  ModuleManagerImpl is the Module Manager singleton,
 *  hidden from direct access by the ModuleManager class.
 *  See the documentation for ModuleManager for the details on this class.
 */
class ModuleManagerImpl extends EventDispatcher
{
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
    public function ModuleManagerImpl()
    {
        super();
    }

    //--------------------------------------------------------------------------
    //
    //  Variables
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     */
    private var moduleDictionary:Dictionary = new Dictionary(true);

    //--------------------------------------------------------------------------
    //
    //  Methods
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     */
    public function getAssociatedFactory(object:Object):IFlexModuleFactory
    {
        var className:String = getQualifiedClassName(object);
        
        for (var m:Object in moduleDictionary)
        {
            var info:ModuleInfo = m as ModuleInfo;

            if (!info.ready)
                continue;

            var domain:ApplicationDomain = info.applicationDomain;
            
            if (domain.hasDefinition(className))
            {
                var cls:Class = Class(domain.getDefinition(className));
                if (cls && (object is cls))
                    return info.factory;
            }
        }

        return null;
    }

    /**
     *  @private
     */
    public function getModule(url:String):IModuleInfo
    {
        var info:ModuleInfo = null;

        for (var m:Object in moduleDictionary)
        {
            var mi:ModuleInfo = m as ModuleInfo;
            if (moduleDictionary[mi] == url)
            {
                info = mi;
                break;
            }
        }

        if (!info)
        {
            info = new ModuleInfo(url);
            moduleDictionary[info] = url;
        }

        return new ModuleInfoProxy(info);
    }
}

////////////////////////////////////////////////////////////////////////////////
//
//  Helper class: ModuleInfo
//
////////////////////////////////////////////////////////////////////////////////


/**
 *  @private
 *  The ModuleInfo class encodes the loading state of a module.
 *  It isn't used directly, because there needs to be only one single
 *  ModuleInfo per URL, even if that URL is loaded multiple times,
 *  yet individual clients need their own dedicated events dispatched
 *  without re-dispatching to clients that already received their events.
 *  ModuleInfoProxy holds the public IModuleInfo implementation
 *  that can be externally manipulated.
 */
class ModuleInfo extends EventDispatcher
{
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
    public function ModuleInfo(url:String)
    {
        super();

        _url = url;
    }

    //--------------------------------------------------------------------------
    //
    //  Variables
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     */
    private var factoryInfo:FactoryInfo;

    /**
     *  @private
     */
    private var loader:Loader;

    /**
     *  @private
     */
    private var numReferences:int = 0;

    /**
     *  @private
     */
    private var parentModuleFactory:IFlexModuleFactory;
    
    //--------------------------------------------------------------------------
    //
    //  Properties
    //
    //--------------------------------------------------------------------------

    //----------------------------------
    //  applicationDomain
    //----------------------------------

    /**
     *  @private
     */
    public function get applicationDomain():ApplicationDomain
    {
        return factoryInfo ? factoryInfo.applicationDomain : null;
    }

    //----------------------------------
    //  error
    //----------------------------------

    /**
     *  @private
     *  Storage for the error property.
     */
    private var _error:Boolean = false;

    /**
     *  @private
     */
    public function get error():Boolean
    {
        return _error;
    }

    //----------------------------------
    //  factory
    //----------------------------------

    /**
     *  @private
     */
    public function get factory():IFlexModuleFactory
    {
        return factoryInfo ? factoryInfo.factory : null;
    }

    //----------------------------------
    //  loaded
    //----------------------------------

    /**
     *  @private
     *  Storage for the loader property.
     */
    private var _loaded:Boolean = false;

    /**
     *  @private
     */
    public function get loaded():Boolean
    {
        return _loaded;
    }

    //----------------------------------
    //  ready
    //----------------------------------

    /**
     *  @private
     *  Storage for the ready property.
     */
    private var _ready:Boolean = false;

    /**
     *  @private
     */
    public function get ready():Boolean
    {
        return _ready;
    }

    //----------------------------------
    //  setup
    //----------------------------------

    /**
     *  @private
     *  Storage for the setup property.
     */
    private var _setup:Boolean = false;

    /**
     *  @private
     */
    public function get setup():Boolean
    {
        return _setup;
    }

    //----------------------------------
    //  size
    //----------------------------------

    /**
     *  @private
     */
    public function get size():int
    {
        return factoryInfo ? factoryInfo.bytesTotal : 0;
    }

    //----------------------------------
    //  url
    //----------------------------------

    /**
     *  @private
     *  Storage for the url property.
     */
    private var _url:String;

    /**
     *  @private
     */
    public function get url():String
    {
        return _url;
    }

    //--------------------------------------------------------------------------
    //
    //  Methods
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     */
    public function load(applicationDomain:ApplicationDomain = null,
                         securityDomain:SecurityDomain = null,
                         bytes:ByteArray = null,
                         moduleFactory:IFlexModuleFactory = null):void
    {
        if (_loaded)
            return;

        _loaded = true;

        parentModuleFactory = moduleFactory;
        
        // If bytes are supplied, then load the bytes instead of loading
        // from the url.
        if (bytes)
        {
            loadBytes(applicationDomain, bytes);
            return;
        }
    
        if (_url.indexOf("published://") == 0)
            return;

        var r:URLRequest = new URLRequest(_url);

        var c:LoaderContext = new LoaderContext();
        c.applicationDomain =
            applicationDomain ?
            applicationDomain :
            new ApplicationDomain(ApplicationDomain.currentDomain);

        // setting securityDomain is not allowed on non-REMOTE sandboxes
        if (securityDomain != null && Security.sandboxType == Security.REMOTE)
            c.securityDomain = securityDomain;

        loader = new Loader();

        loader.contentLoaderInfo.addEventListener(
            Event.INIT, initHandler);
        loader.contentLoaderInfo.addEventListener(
            Event.COMPLETE, completeHandler);
        loader.contentLoaderInfo.addEventListener(
            ProgressEvent.PROGRESS, progressHandler);
        loader.contentLoaderInfo.addEventListener(
            IOErrorEvent.IO_ERROR, errorHandler);
        loader.contentLoaderInfo.addEventListener(
            SecurityErrorEvent.SECURITY_ERROR, errorHandler);
        
        loader.load(r, c);
    }

    /**
     *  @private
     */
    private function loadBytes(applicationDomain:ApplicationDomain, bytes:ByteArray):void
    {
        var c:LoaderContext = new LoaderContext();
        c.applicationDomain =
            applicationDomain ?
            applicationDomain :
            new ApplicationDomain(ApplicationDomain.currentDomain);

        // If the AIR flag is available then set it to true so we can
        // load the module without a security error.
        if ("allowLoadBytesCodeExecution" in c)
            c["allowLoadBytesCodeExecution"] = true;
        
        loader = new Loader();

        loader.contentLoaderInfo.addEventListener(
            Event.INIT, initHandler);
        loader.contentLoaderInfo.addEventListener(
            Event.COMPLETE, completeHandler);
        loader.contentLoaderInfo.addEventListener(
            IOErrorEvent.IO_ERROR, errorHandler);
        loader.contentLoaderInfo.addEventListener(
            SecurityErrorEvent.SECURITY_ERROR, errorHandler);

        loader.loadBytes(bytes, c);
    }

    /**
     *  @private
     */
    public function resurrect():void
    {
        // If the module is not ready then don't try to resurrect it.
        // You can only resurrect a module that is in the ready state.
        // We return here and do not destroy the current state because
        // we may have started loading a module that is not yet ready.
        if (!_ready)
            return;
        
        //trace("Module[", url, "] resurrect");
        
        if (!factoryInfo)
        {
            if (_loaded)
                dispatchEvent(new ModuleEvent(ModuleEvent.UNLOAD));

            loader = null;
            _loaded = false;
            _setup = false;
            _ready = false;
            _error = false;
        }
    }

    /**
     *  @private
     */
    public function release():void
    {
        // If the module is ready, then keep it in the 
        // module dictionary.
        if (!_ready)
        {
            // Otherwise we just drop it
            unload();
        }
    }

    /**
     *  @private
     */

    private function clearLoader():void
    {
        if (loader)
        {
            if (loader.contentLoaderInfo)
            {
                loader.contentLoaderInfo.removeEventListener(
                    Event.INIT, initHandler);
                loader.contentLoaderInfo.removeEventListener(
                    Event.COMPLETE, completeHandler);
                loader.contentLoaderInfo.removeEventListener(
                    ProgressEvent.PROGRESS, progressHandler);
                loader.contentLoaderInfo.removeEventListener(
                    IOErrorEvent.IO_ERROR, errorHandler);
                loader.contentLoaderInfo.removeEventListener(
                    SecurityErrorEvent.SECURITY_ERROR, errorHandler);
            }

            try
            {
                if (loader.content)
                {
                    loader.content.removeEventListener("ready", readyHandler);
                    loader.content.removeEventListener("error", moduleErrorHandler);
                }
            }
            catch(error:Error)
            {
                // we might get unloaded because of a security error
                // which will disallow access to loader.content
                // so if we get an error here, just ignore it.
            }


            if (_loaded)
            {
                try
                {
                    loader.close();
                }
                catch(error:Error)
                {
                }
            }

            try
            {
                loader.unload();
            }
            catch(error:Error)
            {
            }

            loader = null;
        }
    }
    /**
     *  @private
     */
    public function unload():void
    {
        clearLoader();

        if (_loaded)
            dispatchEvent(new ModuleEvent(ModuleEvent.UNLOAD));

        factoryInfo = null;
        parentModuleFactory = null;
        _loaded = false;
        _setup = false;
        _ready = false;
        _error = false;
    }

    /**
     *  @private
     */
    public function publish(factory:IFlexModuleFactory):void
    {
        if (factoryInfo)
            return; // can't re-publish without unloading.

        if (_url.indexOf("published://") != 0)
            return;

        factoryInfo = new FactoryInfo();
        factoryInfo.factory = factory;
        _loaded = true;
        _setup = true;
        _ready = true;
        _error = false;

        dispatchEvent(new ModuleEvent(ModuleEvent.SETUP));
        dispatchEvent(new ModuleEvent(ModuleEvent.PROGRESS));
        dispatchEvent(new ModuleEvent(ModuleEvent.READY));
    }

    /**
     *  @private
     */
    public function addReference():void
    {
        ++numReferences;
    }

    /**
     *  @private
     */
    public function removeReference():void
    {
        --numReferences;
        if (numReferences == 0)
            release();
    }

    //--------------------------------------------------------------------------
    //
    //  Event handlers
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     */
    public function initHandler(event:Event):void
    {
        //trace("child load of " + _url + " fired init");

        factoryInfo = new FactoryInfo();

        try
        {
            factoryInfo.factory = loader.content as IFlexModuleFactory;
        }
        catch(error:Error)
        {
        }

        if (!factoryInfo.factory)
        {
            var moduleEvent:ModuleEvent = new ModuleEvent(
                ModuleEvent.ERROR, event.bubbles, event.cancelable);
            moduleEvent.bytesLoaded = 0;
            moduleEvent.bytesTotal = 0;
            moduleEvent.errorText = "SWF is not a loadable module";
            dispatchEvent(moduleEvent);
            return;
        }

        loader.content.addEventListener("ready", readyHandler);
        loader.content.addEventListener("error", moduleErrorHandler);
        loader.content.addEventListener(Request.GET_PARENT_FLEX_MODULE_FACTORY_REQUEST, 
                                        getFlexModuleFactoryRequestHandler, false, 0, true);            

        try
        {
            factoryInfo.applicationDomain =
                loader.contentLoaderInfo.applicationDomain;
        }
        catch(error:Error)
        {
        }
        _setup = true;

        dispatchEvent(new ModuleEvent(ModuleEvent.SETUP));
    }

    /**
     *  @private
     */
    public function progressHandler(event:ProgressEvent):void
    {
        var moduleEvent:ModuleEvent = new ModuleEvent(
            ModuleEvent.PROGRESS, event.bubbles, event.cancelable);
        moduleEvent.bytesLoaded = event.bytesLoaded;
        moduleEvent.bytesTotal = event.bytesTotal;
        dispatchEvent(moduleEvent);
    }

    /**
     *  @private
     */
    public function completeHandler(event:Event):void
    {
        //trace("child load of " + _url + " is complete");

        var moduleEvent:ModuleEvent = new ModuleEvent(
            ModuleEvent.PROGRESS, event.bubbles, event.cancelable);
        moduleEvent.bytesLoaded = loader.contentLoaderInfo.bytesLoaded;
        moduleEvent.bytesTotal = loader.contentLoaderInfo.bytesTotal;
        dispatchEvent(moduleEvent);
    }

    /**
     *  @private
     */
    public function errorHandler(event:ErrorEvent):void
    {
        _error = true;

        var moduleEvent:ModuleEvent = new ModuleEvent(
            ModuleEvent.ERROR, event.bubbles, event.cancelable);
        moduleEvent.bytesLoaded = 0;
        moduleEvent.bytesTotal = 0;
        moduleEvent.errorText = event.text;
        dispatchEvent(moduleEvent);

        //trace("child load of " + _url + " generated an error " + event);
    }

    /**
     *  @private
     */
    public function getFlexModuleFactoryRequestHandler(request:Request):void
    {
        request.value = parentModuleFactory;
    }
    
    /**
     *  @private
     */
    public function readyHandler(event:Event):void
    {
        //trace("child load of " + _url + " is ready");

        _ready = true;

        factoryInfo.bytesTotal = loader.contentLoaderInfo.bytesTotal;

        var moduleEvent:ModuleEvent = new ModuleEvent(ModuleEvent.READY);
        moduleEvent.bytesLoaded = loader.contentLoaderInfo.bytesLoaded;
        moduleEvent.bytesTotal = loader.contentLoaderInfo.bytesTotal;

        clearLoader();

        dispatchEvent(moduleEvent);
    }
    
    /**
     *  @private
     */
    public function moduleErrorHandler(event:Event):void
    {
        //trace("Error: child load of " + _url + ");

        _ready = true;

        factoryInfo.bytesTotal = loader.contentLoaderInfo.bytesTotal;

        clearLoader();

        var errorEvent:ModuleEvent;
        
        if (event is ModuleEvent)
            errorEvent = ModuleEvent(event);
        else
            errorEvent = new ModuleEvent(ModuleEvent.ERROR);
             
        dispatchEvent(errorEvent);
    }    
}

////////////////////////////////////////////////////////////////////////////////
//
//  Helper class: FactoryInfo
//
////////////////////////////////////////////////////////////////////////////////

/**
 *  @private
 *  Used for weak dictionary references to a GC-able module.
 */
class FactoryInfo
{
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
    public function FactoryInfo()
    {
        super();
    }

    //--------------------------------------------------------------------------
    //
    //  Properties
    //
    //--------------------------------------------------------------------------

    //----------------------------------
    //  factory
    //----------------------------------

    /**
     *  @private
     */
    public var factory:IFlexModuleFactory;

    //----------------------------------
    //  applicationDomain
    //----------------------------------

    /**
     *  @private
     */
    public var applicationDomain:ApplicationDomain;

    //----------------------------------
    //  bytesTotal
    //----------------------------------

    /**
     *  @private
     */
    public var bytesTotal:int = 0;
}

////////////////////////////////////////////////////////////////////////////////
//
//  Helper class: ModuleInfoProxy
//
////////////////////////////////////////////////////////////////////////////////

/**
 *  @private
 *  ModuleInfoProxy implements IModuleInfo and allows each caller of load()
 *  to have their own dedicated module events, while still using the same
 *  backing load state.
 */
class ModuleInfoProxy extends EventDispatcher implements IModuleInfo
{
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
    public function ModuleInfoProxy(info:ModuleInfo)
    {
        super();

        this.info = info;

        info.addEventListener(ModuleEvent.SETUP, moduleEventHandler, false, 0, true);
        info.addEventListener(ModuleEvent.PROGRESS, moduleEventHandler, false, 0, true);
        info.addEventListener(ModuleEvent.READY, moduleEventHandler, false, 0, true);
        info.addEventListener(ModuleEvent.ERROR, moduleEventHandler, false, 0, true);
        info.addEventListener(ModuleEvent.UNLOAD, moduleEventHandler, false, 0, true);
    }

    //--------------------------------------------------------------------------
    //
    //  Variables
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     */
    private var info:ModuleInfo;

    /**
     *  @private
     */
    private var referenced:Boolean = false;

    //--------------------------------------------------------------------------
    //
    //  Properties
    //
    //--------------------------------------------------------------------------

    //----------------------------------
    //  data
    //----------------------------------

    /**
     *  @private
     *  Storage for the data property.
     */
    private var _data:Object;

    /**
     *  @private
     */
    public function get data():Object
    {
        return _data;
    }

    /**
     *  @private
     */
    public function set data(value:Object):void
    {
        _data = value;
    }

    //----------------------------------
    //  error
    //----------------------------------

    /**
     *  @private
     */
    public function get error():Boolean
    {
        return info.error;
    }

    //----------------------------------
    //  factory
    //----------------------------------

    /**
     *  @private
     */
    public function get factory():IFlexModuleFactory
    {
        return info.factory;
    }

    //----------------------------------
    //  loaded
    //----------------------------------

    /**
     *  @private
     */
    public function get loaded():Boolean
    {
        return info.loaded;
    }

    //----------------------------------
    //  ready
    //----------------------------------

    /**
     *  @private
     */
    public function get ready():Boolean
    {
        return info.ready;
    }

    //----------------------------------
    //  setup
    //----------------------------------

    /**
     *  @private
     */
    public function get setup():Boolean
    {
        return info.setup;
    }

    //----------------------------------
    //  url
    //----------------------------------

    /**
     *  @private
     */
    public function get url():String
    {
        return info.url;
    }

    //--------------------------------------------------------------------------
    //
    //  Methods
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     */
    public function publish(factory:IFlexModuleFactory):void
    {
        info.publish(factory);
    }

    /**
     *  @private
     */
    public function load(applicationDomain:ApplicationDomain = null,
                         securityDomain:SecurityDomain = null,
                         bytes:ByteArray = null,
                         moduleFactory:IFlexModuleFactory = null):void
    {
        info.resurrect();

        if (!referenced)
        {
            info.addReference();
            referenced = true;
        }

        //trace("Module[", url, "] load");

        if (info.error)
        {
            //trace("Module[", url, "] load is in error state");
            dispatchEvent(new ModuleEvent(ModuleEvent.ERROR));
        }
        else if (info.loaded)
        {
            //trace("Module[", url, "] load is already loaded");

            if (info.setup)
            {
                //trace("Module[", url, "] load is already set up");
                dispatchEvent(new ModuleEvent(ModuleEvent.SETUP));

                if (info.ready)
                {
                    //trace("Module[", url, "] load is already ready");

                    var moduleEvent:ModuleEvent =
                        new ModuleEvent(ModuleEvent.PROGRESS);
                    moduleEvent.bytesLoaded = info.size;
                    moduleEvent.bytesTotal = info.size;
                    dispatchEvent(moduleEvent);

                    dispatchEvent(new ModuleEvent(ModuleEvent.READY));
                }
            }
        }
        else
        {
            info.load(applicationDomain, securityDomain, bytes, moduleFactory);
        }
    }

    /**
     *  @private
     */
    public function release():void
    {
        if (referenced)
        {
            info.removeReference();
            referenced = false;
        }
    }

    /**
     *  @private
     */
    public function unload():void
    {
        info.unload();

        info.removeEventListener(ModuleEvent.SETUP, moduleEventHandler);
        info.removeEventListener(ModuleEvent.PROGRESS, moduleEventHandler);
        info.removeEventListener(ModuleEvent.READY, moduleEventHandler);
        info.removeEventListener(ModuleEvent.ERROR, moduleEventHandler);
        info.removeEventListener(ModuleEvent.UNLOAD, moduleEventHandler);
    }

    //--------------------------------------------------------------------------
    //
    //  Event handlers
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     */
    private function moduleEventHandler(event:ModuleEvent):void
    {
        dispatchEvent(event);
    }
}