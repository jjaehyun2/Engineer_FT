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

package mx.collections.errors
{

import mx.rpc.IResponder;

/**
 *  This error is thrown when retrieving an item from a collection view
 *  requires an asynchronous call. This error occurs when the backing data 
 *  is provided from a remote source and the data is not yet available locally.
 * 
 *  <p>If the receiver of this error needs notification when the requested item
 *  becomes available (that is, when the asynchronous call completes), it must
 *  use the <code>addResponder()</code> method and specify  
 *  an object that  supports the <code>mx.rpc.IResponder</code>
 *  interface to respond when the item is available.
 *  The <code>mx.collections.ItemResponder</code> class implements the 
 *  IResponder interface and supports a <code>data</code> property.</p>
 *
 *  @see mx.collections.ItemResponder
 *  @see mx.rpc.IResponder
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class ItemPendingError extends Error
{
    include "../../core/Version.as";

	//--------------------------------------------------------------------------
	//
	//  Constructor
	//
	//--------------------------------------------------------------------------

    /**
	 *  Constructor.
	 *
	 *  <p>Called by the Flex Framework when a request is made 
	 *  for an item that isn't local.</p>
	 *
	 *  @param message A message providing information about the error cause.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function ItemPendingError(message:String)
    {
        super(message);
    }

	//--------------------------------------------------------------------------
	//
	//  Properties
	//
	//--------------------------------------------------------------------------

	//----------------------------------
	// responder
	//----------------------------------

    /**
	 *  @private
	 */
	private var _responders:Array;

    /**
     *  An array of IResponder handlers that will be called when
     *  the asynchronous request completes.
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function get responders():Array
	{
		return _responders;
	}

	//--------------------------------------------------------------------------
	//
	//  Methods
	//
	//--------------------------------------------------------------------------

	/**
	 *  <code>addResponder</code> adds a responder to an Array of responders. 
     *  The object assigned to the responder parameter must implement the 
     *  mx.rpc.IResponder interface.
	 *
	 *  @param responder A handler which will be called when the asynchronous request completes.
	 * 
	 *  @see	mx.rpc.IResponder
	 *  @see	mx.collections.ItemResponder
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
	public function addResponder(responder:IResponder):void
	{
		if (!_responders)
			_responders = [];

		_responders.push(responder);
	}
}

}