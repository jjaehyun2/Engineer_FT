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

package mx.modules
{

import mx.core.LayoutContainer;

[Frame(factoryClass="mx.core.FlexModuleFactory")]

[Alternative(replacement="spark.modules.Module", since="4.5")]

/**
 *  The base class for MXML-based dynamically-loadable modules. You extend this
 *  class in MXML by using the <code>&lt;mx:Module&gt;</code> tag in an MXML file, as the
 *  following example shows:
 *  
 *  <pre>
 *  &lt;?xml version="1.0"?&gt;
 *  &lt;!-- This module loads an image. --&gt;
 *  &lt;mx:Module  width="100%" height="100%" xmlns:mx="http://www.adobe.com/2006/mxml"&gt;
 *  
 *    &lt;mx:Image source="trinity.gif"/&gt;
 *  
 *  &lt;/mx:Module&gt;
 *  </pre>
 *  
 *  <p>Extending the Module class in ActionScript is the same as using the <code>&lt;mx:Module&gt;</code> tag
 *  in an MXML file. You extend this class if your module interacts with the framework. 
 *  To see an example of an ActionScript class that extends the Module class, create an MXML 
 *  file with the root tag of <code>&lt;mx:Module&gt;</code>. When you compile this file, 
 *  set the value of the <code>keep-generated-actionscript</code> compiler option to <code>true</code>.
 *  The Flex compiler stores the generated ActionScript class in a directory called generated, which
 *  you can look at.</p>
 *  
 *  <p>If your module does not include any framework code, you can create a class that extends 
 *  the ModuleBase class. If you use the ModuleBase class, your module will typically be smaller than 
 *  if you create a module that is based on the Module class because it does not have any framework 
 *  class dependencies.</p>
 *  
 *  @see mx.modules.ModuleBase
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class Module extends LayoutContainer implements IModule
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
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function Module()
    {
        super();
    }
}

}