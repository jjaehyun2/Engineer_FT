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

package mx.messaging.messages
{

import flash.utils.IDataOutput;
import flash.utils.IExternalizable;

[RemoteClass(alias="DSK")]

/**
 * @private
 */
public class AcknowledgeMessageExt extends AcknowledgeMessage implements IExternalizable
{
    //--------------------------------------------------------------------------
    //
    // Constructor
    // 
    //--------------------------------------------------------------------------

    public function AcknowledgeMessageExt(message:AcknowledgeMessage=null)
    {
        super();
        _message = message;
    }

    override public function writeExternal(output:IDataOutput):void
    {
        if (_message != null)
            _message.writeExternal(output);
        else
            super.writeExternal(output);
    }

    /**
     *  The unique id for the message.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3 
     */
    override public function get messageId():String
    {
        /* If we are wrapping another message, use its messageId */
        if (_message != null)
            return _message.messageId;

        return super.messageId;
    }

    private var _message:AcknowledgeMessage;
}

}