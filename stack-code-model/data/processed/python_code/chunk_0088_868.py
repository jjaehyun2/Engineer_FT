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
 *  A ClassFactory instance is a "factory object" which Flex uses
 *  to generate instances of another class, each with identical properties.
 *
 *  <p>You specify a <code>generator</code> class when you construct
 *  the factory object.
 *  Then you set the <code>properties</code> property on the factory object.
 *  Flex uses the factory object to generate instances by calling
 *  the factory object's <code>newInstance()</code> method.</p>
 *
 *  <p>The <code>newInstance()</code> method creates a new instance
 *  of the <code>generator</code> class, and sets the properties specified
 *  by <code>properties</code> in the new instance.
 *  If you need to further customize the generated instances,
 *  you can override the <code>newInstance()</code> method.</p>
 *
 *  <p>The ClassFactory class implements the IFactory interface.
 *  Therefore it lets you create objects that can be assigned to properties 
 *  of type IFactory, such as the <code>itemRenderer</code> property of a List control
 *  or the <code>itemEditor</code> property of a DataGrid control.</p>
 *
 *  <p>For example, suppose you write an item renderer class named 
 *  ProductRenderer containing
 *  a <code>showProductImage</code> property which can be <code>true</code>
 *  or <code>false</code>.
 *  If you want to make a List control use this renderer, and have each renderer
 *  instance display a product image, you would write the following code:</p>
 *
 *  <pre>
 *  var productRenderer:ClassFactory = new ClassFactory(ProductRenderer);
 *  productRenderer.properties = { showProductImage: true };
 *  myList.itemRenderer = productRenderer;</pre>
 *
 *  <p>The List control calls the <code>newInstance()</code> method on the
 *  <code>itemRenderer</code> to create individual instances of ProductRenderer,
 *  each with <code>showProductImage</code> property set to <code>true</code>.
 *  If you want a different List control to omit the product images, you use
 *  the ProductRenderer class to create another ClassFactory
 *  with the <code>properties</code> property set to
 *  <code>{ showProductImage: false }</code>.</p>
 *
 *  <p>Using the <code>properties</code> property to configure the instances
 *  can be powerful, since it allows a single generator class to be used
 *  in different ways.
 *  However, it is very common to create non-configurable generator classes
 *  which require no properties to be set.
 *  For this reason, MXML lets you use the following syntax: </p>
 *
 *  <pre>
 *  &lt;mx:List id="myList" itemRenderer="ProductRenderer"&gt;</pre>
 *
 *  <p>The MXML compiler automatically creates the ClassFactory instance
 *  for you.</p>
 *
 *  @see mx.core.IFactory
 *  @see mx.controls.List
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class ClassFactory implements IFactory
{
    include "../core/Version.as";

	//--------------------------------------------------------------------------
	//
	//  Constructor
	//
	//--------------------------------------------------------------------------

    /**
     *  Constructor.
     *
     *  @param generator The Class that the <code>newInstance()</code> method uses
	 *  to generate objects from this factory object.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function ClassFactory(generator:Class = null)
    {
		super();

    	this.generator = generator;
    }

	//--------------------------------------------------------------------------
	//
	//  Properties
	//
	//--------------------------------------------------------------------------

	//----------------------------------
	//  generator
	//----------------------------------

    /**
     *  The Class that the <code>newInstance()</code> method uses
	 *  to generate objects from this factory object.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var generator:Class;

	//----------------------------------
	//  properties
	//----------------------------------

	/**
	 *	An Object whose name/value pairs specify the properties to be set
	 *  on each object generated by the <code>newInstance()</code> method.
	 *
	 *  <p>For example, if you set <code>properties</code> to
	 *  <code>{ text: "Hello", width: 100 }</code>, then every instance
	 *  of the <code>generator</code> class that is generated by calling
	 *  <code>newInstance()</code> will have its <code>text</code> set to
	 *  <code>"Hello"</code> and its <code>width</code> set to
	 *  <code>100</code>.</p>
	 *
	 *  @default null
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public var properties:Object = null;

	//--------------------------------------------------------------------------
	//
	//  Methods
	//
	//--------------------------------------------------------------------------

	/**
	 *  Creates a new instance of the <code>generator</code> class,
	 *  with the properties specified by <code>properties</code>.
	 *
	 *  <p>This method implements the <code>newInstance()</code> method
	 *  of the IFactory interface.</p>
	 *
	 *  @return The new instance that was created.
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function newInstance():*
	{
		var instance:Object = new generator();

        if (properties != null)
        {
        	for (var p:String in properties)
			{
        		instance[p] = properties[p];
			}
       	}

       	return instance;
	}
}

}