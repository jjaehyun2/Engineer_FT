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

package mx.binding
{

import flash.events.Event;
import mx.core.IRepeaterClient;
import mx.core.mx_internal;

use namespace mx_internal;

[ExcludeClass]

/**
 *  @private
 */
public class RepeatableBinding extends Binding
{
    include "../core/Version.as";

	//--------------------------------------------------------------------------
	//
	//  Constructor
	//
	//--------------------------------------------------------------------------

    /**
     *  Create a Binding object
	 *
     *  @param document The document that is the target of all of this work.
	 *
     *  @param srcFunc The function that returns us the value
	 *  to use in this Binding.
	 *
     *  @param destFunc The function that will take a value
	 *  and assign it to the destination.
	 *
     *  @param destString The destination represented as a String.
	 *  We can then tell the ValidationManager to validate this field.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function RepeatableBinding(document:Object, srcFunc:Function,
									  destFunc:Function, destString:String)
    {
        super(document, srcFunc, destFunc, destString);
    }

	//--------------------------------------------------------------------------
	//
	//  Overridden methods
	//
	//--------------------------------------------------------------------------

    /**
     *  Execute the binding.
     *  Call the source function and get the value we'll use.
     *  Then call the destination function passing the value as an argument.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    override public function execute(o:Object = null):void
    {
        if (isExecuting)
            return;

        isExecuting = true;
    
        // o is an array index, a single instance of a UIComponent,
		// a Repeater, or is null.
        // If it is a number it is because a Watcher fired
		// and we are being passed the cloneIndex
        // If it is defined as an Object, it is because the Binding Manager
		// just called executeBindings() on that particular instance,
		// and passed it in.
        // If it is null (now unlikely for RepeatableBinding) a watcher
		// has just fired and we will execute this RepeatableBinding
		// on all repeated instances of the object specified by
		// the _destString of this RepeatableBinding.
        // For example, if the _destString is "b.label", we update
        // all instances with id "b", which we locate via their indexed
        // id references on the document, such as b[2][4].
        var id:String;
        if (!o)
        {
            id = destString.substring(0, destString.indexOf("."));
            o = document[id];
        }
        else if (typeof(o) == "number")
        {
            id = destString.substring(0, destString.indexOf("."));
            var components:Array = document[id] as Array;
            if (components)
                o = components[o];
            else
                o = null;
        }

        if (o)
            recursivelyProcessIDArray(o);
   
        isExecuting = false;
    }

	//--------------------------------------------------------------------------
	//
	//  Methods
	//
	//--------------------------------------------------------------------------

    /**
	 *  @private
	 */
	private function recursivelyProcessIDArray(o:Object):void
    {
        // o is either a scalar id reference (to a UIComponent or a Repeater)
        // or an array, perhaps multi-dimensional, of id references

        if (o is Array)
        {
            var array:Array = o as Array;
			var n:int = array.length;
            for (var i:int = 0; i < n; i++)
            {
                recursivelyProcessIDArray(array[i]);
            }
        }
        else if (o is IRepeaterClient)
        {
            var client:IRepeaterClient = IRepeaterClient(o);

            wrapFunctionCall(this, function():void
            {
                var value:Object = wrapFunctionCall(this, srcFunc, null, client.instanceIndices, client.repeaterIndices);

                if (BindingManager.debugDestinationStrings[destString])
                {
                    trace("RepeatableBinding: destString = " + destString + ", srcFunc result = " + value);
                }

                destFunc(value, client.instanceIndices);
            },
            o);
        }
    }

	//--------------------------------------------------------------------------
	//
	//  Event handlers
	//
	//--------------------------------------------------------------------------

    /**
     *  The only reason a Binding listens to an event
	 *  is because it wants a signal to execute
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function eventHandler(event:Event):void
    {
        if (isHandlingEvent)
            return;
        isHandlingEvent = true;

        execute();

        isHandlingEvent = false;
    }
}

}