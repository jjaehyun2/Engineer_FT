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

/**
 *  The IFactory interface defines the interface that factory classes
 *  such as ClassFactory must implement.
 *  An object of type IFactory is a "factory object" which Flex uses
 *  to generate multiple instances of another class, each with identical
 *  properties.
 *
 *  <p>For example, a DataGridColumn has an <code>itemRenderer</code> of type
 *  IFactory; it calls <code>itemRenderer.newInstance()</code> to create
 *  the cells for a particular column of the DataGrid.</p>
 *
 *  @see mx.core.ClassFactory
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public interface IFactory
{
	//--------------------------------------------------------------------------
	//
	//  Methods
	//
	//--------------------------------------------------------------------------

	/**
	 *  Creates an instance of some class (determined by the class that
	 *  implements IFactory).
	 *
	 *  @return The newly created instance.
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	function newInstance():*;
}

}