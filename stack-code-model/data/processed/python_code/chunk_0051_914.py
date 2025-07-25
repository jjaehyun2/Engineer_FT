////////////////////////////////////////////////////////////////////////////////
//
//  MATTBOLT.BLOGSPOT.COM
//  Copyright(C) 2010 Matt Bolt
//
//  Licensed under the Apache License, Version 2.0 (the "License");
//  you may not use this file except in compliance with the License.
//  You may obtain a copy of the License at:
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

package com.mattbolt.grits.net {

    //----------------------------------
    //  imports
    //----------------------------------

    import flash.events.IEventDispatcher;
    import flash.net.ServerSocket;


    //----------------------------------
    //  imports
    //----------------------------------

    /**
     * @eventType com.mattbolt.grits.events.GritsTransportEvent.DELIVERY
     */
    [Event(name="delivery", type="com.mattbolt.grits.events.GritsTransportEvent")]

    /**
     * @eventType com.mattbolt.grits.events.GritsServerEvent.OPENED_CONNECTION
     */
    [Event(name="openedConnection", type="com.mattbolt.grits.events.GritsServerEvent")]

    /**
     * @eventType com.mattbolt.grits.events.GritsServerEvent.CLOSED_CONNECTION
     */
    [Event(name="closedConnection", type="com.mattbolt.grits.events.GritsServerEvent")]


    /**
     * This interface defines an implementation prototype for the driving server instance
     * for grits.
     *
     * @author Matt Bolt [mbolt35&#64;gmail.com]
     */
    public interface IGritsServer extends IEventDispatcher {

        //--------------------------------------------------------------------------
        //
        //  Methods
        //
        //--------------------------------------------------------------------------

        /**
         * This method initializes and opens the server for connections.
         */
        function start():void;

        /**
         * This method stops the log server.
         */
        function stop():void;


        //--------------------------------------------------------------------------
        //
        //  Properties
        //
        //--------------------------------------------------------------------------

        /**
         * This property contains the <code>ServerSocket</code> instance used to control
         * the connections.
         */
        function get server():ServerSocket;
    }

}