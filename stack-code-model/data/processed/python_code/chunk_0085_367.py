//////////////////////////////////////////////////////////////////////////////////////
//
//  Copyright 2012 Freshplanet (http://freshplanet.com | opensource@freshplanet.com)
//  
//  Licensed under the Apache License, Version 2.0 (the "License");
//  you may not use this file except in compliance with the License.
//  You may obtain a copy of the License at
//  
//    http://www.apache.org/licenses/LICENSE-2.0
//  
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.
//  
//////////////////////////////////////////////////////////////////////////////////////

package com.github.lheberlie
{

import flash.events.EventDispatcher;
import flash.events.StatusEvent;
import flash.external.ExtensionContext;

public class MyANE extends EventDispatcher
{
    private static var _instance:MyANE;

    private var extCtx:ExtensionContext = null;

    public function MyANE()
    {
        if (!_instance)
        {
            extCtx = ExtensionContext.createExtensionContext("com.github.lheberlie.MyANE", null);
            if (extCtx != null)
            {
                extCtx.addEventListener(StatusEvent.STATUS, onStatus);
            }
            else
            {
                trace('[MyANE] Error - Extension Context is null.');
            }
            _instance = this;
        }
        else
        {
            throw Error('This is a singleton, use getInstance(), do not call the constructor directly.');
        }
    }

    public static function getInstance():MyANE
    {
        return _instance ? _instance : new MyANE();
    }


    /**
     * Example function.
     * Define your own API and use extCtx.call() to communicate with the native part of the ANE.
     */
    public function isSupported():Boolean
    {
        return extCtx.call('isSupported');
    }


    /**
     * Status events allow the native part of the ANE to communicate with the ActionScript part.
     * We use event.code to represent the type of event, and event.level to carry the data.
     */
    private function onStatus(event:StatusEvent):void
    {
        if (event.code == "LOGGING")
        {
            trace('[MyANE] ' + event.level);
        }
    }
}
}