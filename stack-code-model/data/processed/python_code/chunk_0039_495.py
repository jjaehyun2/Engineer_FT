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

package mx.messaging
{

import flash.errors.IllegalOperationError;
import flash.events.TimerEvent;
import flash.utils.Timer;
import mx.collections.ArrayCollection;
import mx.core.mx_internal;
import mx.logging.Log;
import mx.events.PropertyChangeEvent;
import mx.messaging.errors.InvalidDestinationError;
import mx.messaging.errors.MessagingError;
import mx.messaging.events.ChannelEvent;
import mx.messaging.events.ChannelFaultEvent;
import mx.messaging.events.MessageEvent;
import mx.messaging.events.MessageFaultEvent;
import mx.messaging.errors.MessagingError;
import mx.messaging.messages.AbstractMessage;
import mx.messaging.messages.AcknowledgeMessage;
import mx.messaging.messages.AsyncMessage;
import mx.messaging.messages.CommandMessage;
import mx.messaging.messages.ErrorMessage;
import mx.messaging.messages.IMessage;

use namespace mx_internal;

/**
 *  A MultiTopicProducer sends messages to a destination with zero or more subtopics.
 *  It is like the regular Producer but it can direct the message to any consumer who
 *  is subscribing to any one of a number of subtopics.  If the consumer is a 
 *  MultiTopicConsumer and that consumer has subscribed to more than on subtopic in the
 *  list of subtopics used by the producer, the consumer only receives the message once.
 *  <p>
 *  The MultiTopicProducer will dispatch a MessageAckEvent or MessageFaultEvent 
 *  for each message they send depending upon whether the outbound message
 *  was sent and processed successfully or not.
 *  </p>
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion BlazeDS 4
 *  @productversion LCDS 3 
 */
public class MultiTopicProducer extends AbstractProducer
{
    //--------------------------------------------------------------------------
    //
    // Constructor
    // 
    //--------------------------------------------------------------------------

    /**
     *  Constructor.
     * 
     *  @example
     *  <listing version="3.0">
     *   function sendMessage():void
     *   {
     *       var producer:MultiTopicProducer = new MultiTopicProducer();
     *       producer.destination = "NASDAQ";
     *       var msg:AsyncMessage = new AsyncMessage();
     *       msg.headers.operation = "UPDATE";
     *       msg.body = {"SYMBOL":50.00};
     *       // only send to subscribers to subtopic "SYMBOL" and "ALLSTOCKS"
     *       msg.addSubtopic("SYMBOL");
     *       msg.addSubtopic("ALLSTOCKS");
     *       producer.send(msg);
     *   }
     *   </listing>
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3 
     */
    public function MultiTopicProducer()
    {
        super();
        _log = Log.getLogger("mx.messaging.MultiTopicProducer");
        _agentType = "MultiTopicProducer";
    }

    //--------------------------------------------------------------------------
    //
    // Variables
    // 
    //--------------------------------------------------------------------------
    
    //----------------------------------
    //  subtopic
    //----------------------------------    

    /**
     *  @private
     */
    private var _subtopics:ArrayCollection = new ArrayCollection();
    
    [Bindable(event="propertyChange")]
    
    /**
     *  Provides access to the list of subtopics used in publishing any messages
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3 
     */
    public function get subtopics():ArrayCollection
    {
        return _subtopics;
    }
    
    /**
     * Provide a new ArrayCollection of Strings each of which define a subtopic
     * for use in publishing the message.  Any consumers subscribed to any of the
     * subtopics will receive these messages.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3 
     */
    public function set subtopics(value:ArrayCollection):void
    {
        if (_subtopics != value)
        {
            var event:PropertyChangeEvent;
            if (value == null)
                value = new ArrayCollection();

            event = PropertyChangeEvent.createUpdateEvent(this, "subtopics", _subtopics, value);
            _subtopics = value;                

            dispatchEvent(event);
        }
    }

    //--------------------------------------------------------------------------
    //
    // Public methods
    // 
    //--------------------------------------------------------------------------

    /**
     * Adds a subtopic to the current list of subtopics for messages sent by this
     * producer.  This is a shortcut to adding this subtopic to the subtopics
     * property.
     *
     * @param subtopic The subtopic to add to the current list of
     * subtopics sent by this producer.
     *
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3 
     */
    public function addSubtopic(subtopic:String):void
    {
        subtopics.addItem(subtopic);
    }

    /**
     * Removes the subtopic from the subtopics property.  Throws an error if the
     * subtopic is not in the list.
     *
     * @param subtopic The subtopic to remove from the subtopics property.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3 
     */
    public function removeSubtopic(subtopic:String):void
    {
        var ix:int = subtopics.getItemIndex(subtopic);
        if (ix == -1)
            throw new MessagingError("Attempt to remove a subtopic from MultiTopicProducer: " + 
                                     subtopic + " which does not exist");
        subtopics.removeItemAt(ix);
    }
    
    //--------------------------------------------------------------------------
    //
    // Protected Methods
    // 
    //--------------------------------------------------------------------------

    /**
     * @private
     */
    override protected function internalSend(message:IMessage, waitForClientId:Boolean = true):void
    {
        // Otherwise, use the default topic
        if (subtopics.length > 0)
            message.headers[AsyncMessage.SUBTOPIC_HEADER] = subtopics;    

        super.internalSend(message, waitForClientId);
    }

    //--------------------------------------------------------------------------
    //
    // Private Methods
    // 
    //--------------------------------------------------------------------------
    
}

}