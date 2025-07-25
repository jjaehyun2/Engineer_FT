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

package mx.managers
{

import flash.events.IEventDispatcher;

/**
 *  Dispatched when the URL is changed either
 *  by the user interacting with the browser, invoking an
 *  application in AIR, or by setting the property programmatically.
 *
 *  @eventType flash.events.Event.CHANGE
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Event(name="change", type="flash.events.Event")]

/**
 *  Dispatched when the URL is changed
 *  by the browser.
 *
 *  @eventType mx.events.BrowserChangeEvent.BROWSER_URL_CHANGE
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Event(name="browserURLChange", type="mx.events.BrowserChangeEvent")]

/**
 *  Dispatched when the URL is changed
 *  by the application.
 *
 *  @eventType mx.events.BrowserChangeEvent.URL_CHANGE
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Event(name="urlChange", type="mx.events.BrowserChangeEvent")]

/**
 *  The interface that the shared instance of the BrowserManager
 *  implements. Applications listen for events,
 *  call methods, and access properties on the shared instance
 *  which is accessed with the <code>BrowserManager.getInstance()</code> method.
 * 
 *  @see mx.managers.BrowserManager
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public interface IBrowserManager extends IEventDispatcher
{

    /**
     *  The portion of current URL before the '#' as it appears 
     *  in the browser address bar.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function get base():String;

    /**
     *  The portion of current URL after the '#' as it appears 
     *  in the browser address bar. Use the <code>setURLFragment()</code> method to change this value.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function get fragment():String;

    /**
     *  The title of the application as it should appear in the
     *  browser history.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function get title():String;

    /**
     *  The current URL as it appears in the browser address bar.  
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function get url():String;

    /** 
     *  Changes the fragment of the URL after the '#' in the browser.
     *  An attempt will be made to track this URL in the browser's
     *  history.
     *
     *  <p>If the title is set, the old title in the browser is replaced
     *  by the new title.</p>
     *
     *  <p>To store the URL, a JavaScript
     *  method named <code>setBrowserURL()</code> will be called.
     *  The application's HTML wrapper must have that method which
     *  must implement a mechanism for taking this
     *  value and registering it with the browser's history scheme
     *  and address bar.</p>
     *
     *  <p>When set, the <code>APPLICATION_URL_CHANGE</code> event is dispatched. If the event
     *  is cancelled, the <code>setBrowserURL()</code> method will not be called.</p>
     *
     * @param value The new fragment to use after the '#' in the URL.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function setFragment(value:String):void;

    /** 
     *  Changes the text in the browser's title bar.
     *  This method does not affect the browser's history.
     *
     * @param value The new title to use in the browser's title bar.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function setTitle(value:String):void;

    /** 
     *  Initializes the BrowserManager. The BrowserManager will get the initial URL. If it
     *  has a fragment, it will dispatch a <code>BROWSER_URL_CHANGE</code> event.
     *
     *  This method sets the value of the <code>ApplicationGlobals.application.historyManagementEnabled</code>
     *  property to <code>false</code> because the HistoryManager generally interferes with your
     *  application's handling of URL fragments.
     *
     *  @param defaultFragment The fragment to use if no fragment is in the initial URL.
     *  @param defaultTitle The title to use if no fragment is in the initial URL.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function init(value:String = null, title:String = null):void;

    /** 
     *  Initializes the BrowserManager. The HistoryManager calls this method to
     *  prepare the BrowserManager for further calls from the HistoryManager. You cannot use 
     *  the HistoryManager and call the <code>setFragment()</code> method from the application.
     *  As a result, the <code>init()</code> method usually sets 
     *  the value of the <code>ApplicationGlobals.application.historyManagementEnabled</code> property to <code>false</code> to disable
     *  the HistoryManager.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function initForHistoryManager():void;
}

}