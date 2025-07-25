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
package org.apache.royale.html
{
	import org.apache.royale.core.ContainerBase;
	import org.apache.royale.core.IChrome;
	import org.apache.royale.core.IContainer;
	import org.apache.royale.core.IUIBase;
	import org.apache.royale.events.Event;
	
	[DefaultProperty("mxmlContent")]
    
    /**
     *  A Container that has a HorizontalLayout.
     * 
     *  This is effectively the same as the pattern
     *  <code>
     *  <basic:Container xmlns:basic="library://ns.apache.org/royale/basic">
     *    <basic:layout>
     *       <basic:HorizontalLayout />
     *    </basic:layout>
     *  </basic:Container>
     *  </code>
     *  
     *  @toplevel
     *  @langversion 3.0
     *  @playerversion Flash 10.2
     *  @playerversion AIR 2.6
     *  @productversion Royale 0.0
     */    
	public class HContainer extends Container
	{
        /**
         *  Constructor.
         *  
         *  @langversion 3.0
         *  @playerversion Flash 10.2
         *  @playerversion AIR 2.6
         *  @productversion Royale 0.0
         */
		public function HContainer()
		{
			super();
        }
	}
}