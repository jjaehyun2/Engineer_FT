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
 *  ComponentDescriptor is the base class for the UIComponentDescriptor class,
 *  which encapsulates the information that you specified in an MXML tag
 *  for an instance of a visual component.
 *  In Flex, non-visual components are treated differently and do not
 *  have descriptors, but in a future version the ComponentDescriptor
 *  base class may be used for them as well.
 *
 *  <p>Most of the tags in an MXML file describe a tree of UIComponent objects.
 *  For example, the <code>&lt;mx:Application&gt;</code> tag represents a
 *  UIComponent object, and its child containers and controls are all
 *  UIComponent objects.</p>
 *
 *  <p>The MXML compiler compiles each of these MXML tags into a
 *  UIComponentDescriptor instance.
 *  To be precise, the MXML compiler autogenerates an ActionScript
 *  data structure which is a tree of UIComponentDescriptor objects.</p>
 *
 *  <p>At runtime, the <code>createComponentsFromDescriptors()</code> method
 *  of the Container class uses the information in the UIComponentDescriptor
 *  objects in the container's <code>childDescriptors</code> array to create
 *  the actual UIComponent objects that are the container's children,
 *  plus deeper descendants as well.
 *  Depending on the value of the container's <code>creationPolicy</code>,
 *  property, the descendants might be created at application startup,
 *  when some part of the component is about to become visible,
 *  or when the application developer manually calls
 *  the <code>createComponentsFromDescriptors()</code> method.</p>
 *
 *  <p>You do not typically create ComponentDescriptor or UIComponentDescriptor
 *  instances yourself; you can access the ones that the MXML compiler
 *  autogenerates, via the <code>childDescriptors</code> array
 *  of the Container class.</p>
 *
 *  @see mx.core.UIComponentDescriptor
 *  @see mx.core.Container#childDescriptors
 *  @see mx.core.Container#creationPolicy
 *  @see mx.core.Container#createComponentsFromDescriptors()
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */ 
public class ComponentDescriptor
{
    //include "../core/Version.as";

    //--------------------------------------------------------------------------
    //
    //  Constructor
    //
    //--------------------------------------------------------------------------

    /**
     *  Constructor.
     *
     *  @param descriptorProperties An Object containing name/value pairs
     *  for the properties of the ComponentDescriptor object, such as its
     *  <code>type</code>, <code>id</code>, <code>propertiesFactory</code>
     *  and <code>events</code>.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function ComponentDescriptor(descriptorProperties:Object)
    {
        super();

        for (var p:String in descriptorProperties)
        {
            this[p] = descriptorProperties[p];
        }
    }

    //--------------------------------------------------------------------------
    //
    //  Properties
    //
    //--------------------------------------------------------------------------

    //----------------------------------
    //  document
    //----------------------------------

    /**
     *  A reference to the document Object in which the component
     *  is to be created.
     *
     *  @see mx.core.IUIComponent#document
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var document:Object;

    //----------------------------------
    //  events
    //----------------------------------

    /**
     *  An Object containing name/value pairs for the component's
     *  event handlers, as specified in MXML.
     *
     *  <p>For example, if you write</p>
     *
     *  <pre>
     *  &lt;mx:DataGrid id="dg" initialize="fetchData(); initDataGrid();"  change="changeHandler(event);"/&gt;
     *  </pre>
     *
     *  <p>then the descriptor's <code>events</code> property is the Object</p>
     *
     *  <pre>
     *  { initialize: "__dg_initialize", change: "__dg_change" }
     *  </pre>
     *
     *  <p>The <code>event</code>property is <code>null</code>
     *  if no MXML event handlers were specified for the component</p>
     *
     *  <p>The strings <code>"__dg_initialize"</code>
     *  and <code>"__dg_change"</code> are the names of event handler
     *  methods that the MXML compiler autogenerates.
     *  The body of these methods contain the ActionScript statements
     *  that you specified as the values of the event attributes.
     *  For example, the autogenerated <code>initialize</code> handler is</p>
     *
     *  <pre>
     *  public function __dg_initialize(event:mx.events.FlexEvent):void
     *  {
     *      fetchData();
     *      initDataGrid();
     *  }
     *  </pre>
     *
     *  <p>You should not assume that the autogenerated event handlers
     *  will always be specified by name; this may change in a future
     *  version of Flex.</p>
     *  
     *  <p>This property is used by the Container method
     *  <code>createComponentsFromDescriptors()</code>
     *  to register the autogenerated event handlers
     *  using the <code>addEventListener()</code> method.</p>
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var events:Object;

    //----------------------------------
    //  id
    //----------------------------------

    /**
     *  The identifier for the component, as specified in MXML. 
     *
     *  <p>For example, if you write</p>
     *
     *  <pre>
     *  &lt;mx:TextInput id="firstName" text="Enter your first name here"/&gt;
     *  </pre>
     *
     *  <p>then the descriptor's <code>id</code> property is the String
     *  <code>"firstName"</code>.</p>
     *
     *  <p>The <code>id</code> property is <code>null</code>
     *  if no MXML id was specified for the component.</p>
     *
     *  <p>The value of the <code>id</code> property becomes the name
     *  of a public variable in the MXML document object,
     *  autogenerated by the MXML compiler.
     *  The value of this variable is a reference to the UIComponent object
     *  created from this descriptor.
     *  This is why you can, for example, reference the TextInput control's 
     *  <code>text</code> property as <code>firstName.text</code>
     *  from anywhere within the document containing this TextInput instance.</p>
     *
     *  <p>If an <code>id</code> is specified, and it isn't the empty string,
     *  it also becomes the <code>name</code> of the DisplayObject object.
     *  If an <code>id</code> is not specified or is empty, the DisplayObject
     *  object's <code>name</code> remains an autogenerated string,
     *  such as <code>"Button3"</code>, as returned by the
     *  <code>NameUtil.createUniqueName()</code> method.
     *  The <code>name</code> is used in generating the string returned
     *  by the <code>toString()</code> method.
     *  It can also be used to find the component from its parent
     *  by calling <code>getChildByName()</code>.</p>
     *
     *  @see flash.display.DisplayObject#name
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var id:String;

    //----------------------------------
    //  properties
    //----------------------------------

    /**
     *  @private
     */
    private var _properties:Object;

    /**
     *  An Object containing name/value pairs for the component's properties,
     *  as specified in MXML.
     *
     *  <p>For example, if you write</p>
     *
     *  <pre>
     *  &lt;mx:TextInput width="150" text="Hello"/&gt;
     *  </pre>
     *
     *  <p>then the descriptor's <code>properties</code> property
     *  is the Object</p>
     *
     *  <pre>
     *  { width: 150, text: "Hello" }
     *  </pre>
     *
     *  <p>The <code>properties</code> property is <code>null</code>
     *  if no MXML properties were specified for the component.
     *  In this case, the component will use default property values.</p>
     *
     *  <p> This Object is produced by calling the function specified by the
     *  <code>propertiesFactory</code> property, and then cached
     *  for subsequent access.
     *  However, when a Repeater produces multiple instances of a component
     *  from the same descriptor, a fresh copy of the <code>properties</code>
     *  Object should be produced for each component instance so that they
     *  don't share property values which are Arrays or Object references.
     *  The Repeater accomplishes this by calling the 
     *  <code>invalidateProperties()</code> method on the descriptor.</p>
     *
     *  @see #propertiesFactory
     *  @see #invalidateProperties()
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get properties():Object
    {
        if (_properties)
            return _properties;

        if (propertiesFactory != null)
            _properties = propertiesFactory.call(document);
        
        // Propagate the 'document' property, set by the MXML compiler
        // on the document descriptor, down to all descendant descriptors.
        if (_properties)
        {   
            var cd:Array = _properties.childDescriptors; 
            if (cd)
            {
                var n:int = cd.length;
                for (var i:int = 0; i < n; i++)
                {
                    cd[i].document = document;
                }
            }
        }
        else
        {
            _properties = {};
        }
        
        return _properties;
    }

    //----------------------------------
    //  propertiesFactory
    //----------------------------------

    /**
     *  A Function that returns an Object containing name/value pairs
     *  for the component's properties, as specified in MXML.
     *
     *  <p>For example, if you write</p>
     *  
     *  <pre>
     *  &lt;mx:TextInput width="150" text="Hello"&gt;
     *  </pre>
     *
     *  <p>then the descriptor's <code>propertiesFactory</code> property 
     *  is the Function:</p>
     *
     *  <pre>
     *  function():Object { return { width: 150, text: "Hello" }; }
     *  </pre>
     *
     *  <p>The <code>propertiesFactory</code>property is <code>null</code>
     *  if no MXML properties were specified for the component.
     *  In this case, the component will use default property values.</p>
     *
     *  <p>The reason that <code>propertyFactory</code> is a
     *  Function returning an Object rather than an actual Object
     *  is to allow the tree of ComponentDescriptor objects
     *  to "unfold" incrementally.
     *  If all the descriptors in the descriptor tree for the document
     *  were created at launch time, the time to launch would be greater.</p>
     *
     *  <p>The <code>properties</code> property returns a cached Object
     *  that was produced by this factory function.</p>
     *  
     *  <p>Note: Event handlers such as <code>click="doSomething();"</code>
     *  appear in the <code>events</code> Object,
     *  not in the <code>properties</code> Object.</p>
     *
     *  @see #properties
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var propertiesFactory:Function;

    //----------------------------------
    //  type
    //----------------------------------

    /**
     *  The Class of the component, as specified in MXML.
     *
     *  <p>For example, if you write</p>
     *
     *  <pre>
     *  &lt;mx:TextInput/&gt;
     *  </pre>
     *
     *  <p>then the descriptor's <code>type</code> property
     *  the Class mx.controls.TextInput.</p>
     *
     *  <p>The property is never <code>null</code> for the
     *  ComponentDescriptor objects created by the MXML compiler,
     *  because every MXML tag has a tag name such as mx:TextInput.</p>
     *
     *  <p>The mapping between an MXML tag and its corresponding class
     *  is determined by the XML namespace and the "manifest" file,
     *  if any, that is associated with that namespace.
     *  For example, the standard Flex namespace
     *  <code>http://www.adobe.com/2006/mxml</code>
     *  represented by the mx: prefix is associated (in the flex-config.xml
     *  file) with the manifest file mxml-manifest.xml,
     *  and this file has the tag</p>
     *
     *  <pre>
     *  &lt;component id="TextInput" class="mx.controls.TextInput"/&gt;
     *  </pre>
     *
     *  <p>which maps the tag name mx:TextInput
     *  to the Class mx.controls.TextInput.
     *  Note that the use of a manifest file allows components in single
     *  XML namespace to map to classes in multiple ActionScript packages.</p>
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var type:Class;

    //--------------------------------------------------------------------------
    //
    //  Methods
    //
    //--------------------------------------------------------------------------

    /**
     *  Invalidates the cached <code>properties</code> property.
     *  The next time you read the <code>properties</code> property,
     *  the properties are regenerated from the function specified by the 
     *  value of the <code>propertiesFactory</code> property.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function invalidateProperties():void
    {
        _properties = null;
    }
    
    /**
     *  Returns the string "ComponentDescriptor_" plus the value of the  
     *  <code>id</code> property.
     *
     *  @return The string "ComponentDescriptor_" plus the value of the  
     *  <code>id</code> property.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function toString():String
    {
        return "ComponentDescriptor_" + id;
    }
}

}