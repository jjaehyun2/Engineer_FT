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
package org.apache.royale.mdl.supportClasses
{
	import org.apache.royale.html.Group;

    COMPILE::JS
    {
        import org.apache.royale.core.WrappedHTMLElement;
		import org.apache.royale.html.util.addElementToWrapper;
        import org.apache.royale.core.CSSClassList;
    }

	/**
	 *  The CardInner class is a base class for all Card inner containers.
	 *
	 *  @langversion 3.0
	 *  @playerversion Flash 10.2
	 *  @playerversion AIR 2.6
	 *  @productversion Royale 0.8
	 */
	public class CardInner extends Group
	{
		/**
		 *  constructor.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.8
		 */
		public function CardInner()
		{
			super();

            COMPILE::JS
            {
                _classList = new CSSClassList();
            }
		}

        COMPILE::JS
        private var _classList:CSSClassList;

		private var _border:Boolean = false;
        /**
		 *  A boolean flag to activate "mdl-card--border" effect selector.
		 *  Adds a border to the card section that it's applied to.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.8
		 */
        public function get border():Boolean
        {
            return _border;
        }
        public function set border(value:Boolean):void
        {
            if (_border != value)
            {
                _border = value;

                COMPILE::JS
                {
                    var classVal:String = "mdl-card--border";
                    value ? _classList.add(classVal) : _classList.remove(classVal);
                    setClassName(computeFinalClassNames());
                }
            }
        }

		private var _expand:Boolean = false;
        /**
		 *  A boolean flag to activate "mdl-card--expand" effect selector.
		 *  Makes the container grows all available space. Is flex css dependant
		 *  It seems it will be deprecated in new MDL versions.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.8
		 */
        public function get expand():Boolean
        {
            return _expand;
        }

        public function set expand(value:Boolean):void
        {
            if (_expand != value)
            {
                _expand = value;

                COMPILE::JS
                {
                    var classVal:String = "mdl-card--expand";
                    value ? _classList.add(classVal) : _classList.remove(classVal);
                    setClassName(computeFinalClassNames());
                }
            }
        }

        COMPILE::JS
        override protected function computeFinalClassNames():String
        {
            return _classList.compute() + super.computeFinalClassNames();
        }
	}
}