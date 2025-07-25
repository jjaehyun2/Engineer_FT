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
package org.apache.royale.core
{
    
    import org.apache.royale.core.ClassFactory;
    import org.apache.royale.core.IFactory;
    import org.apache.royale.core.IItemRendererProvider;
    import org.apache.royale.core.ISelectableItemRenderer;
    
    import org.apache.royale.utils.MXMLDataInterpreter;

	[DefaultProperty("mxmlContent")]
    
    /**
     *  The SelectableItemRendererClassFactory class extends the default
     *  ItemRendererClassFactory and adds an ISelectableItemRenderer Bead to
     *  each renderer instance.  That allows renderers to be used
     *  in lists with or without selection.
     * 
     *  @langversion 3.0
     *  @playerversion Flash 10.2
     *  @playerversion AIR 2.6
     *  @productversion Royale 0.0
     */
	public class SelectableItemRendererClassFactory extends ItemRendererClassFactory
	{
        /**
         *  Constructor.
         *  
         *  @langversion 3.0
         *  @playerversion Flash 10.2
         *  @playerversion AIR 2.6
         *  @productversion Royale 0.0
         */
		public function SelectableItemRendererClassFactory()
		{
			super();
		}

        /**
         *  @copy org.apache.royale.core.IBead#strand
         *  
         *  @langversion 3.0
         *  @playerversion Flash 10.2
         *  @playerversion AIR 2.6
         *  @productversion Royale 0.0
         *  @royaleignorecoercion Class
         */
        override public function set strand(value:IStrand):void
        {
            super.strand = value;
            selectableBeadClass = ValuesManager.valuesImpl.getValue(value, "iSelectableItemRenderer") as Class;
        }
        
        private var selectableBeadClass:Class;
        
        /**
         *  @copy org.apache.royale.core.IItemRendererClassFactory#createItemRenderer()
         *  
         *  @langversion 3.0
         *  @playerversion Flash 10.2
         *  @playerversion AIR 2.6
         *  @productversion Royale 0.0
         */
        override public function createItemRenderer():IItemRenderer
        {
            var ir:IItemRenderer = super.createItemRenderer();
	        ir.addBead(new selectableBeadClass());
            return ir;
        }
	}
}