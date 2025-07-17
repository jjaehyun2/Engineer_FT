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
package org.apache.royale.icons
{
    import org.apache.royale.core.StyledUIBase;
    import org.apache.royale.core.IIcon;
    import org.apache.royale.utils.StringUtil;

    COMPILE::JS
    {
        import org.apache.royale.core.WrappedHTMLElement;
        import org.apache.royale.html.util.addElementToWrapper;
    }

    /**
     *  FontIconBase is the base class to provide most common features 
     *  for all kinds of text based icons
     *
     *  @langversion 3.0
     *  @playerversion Flash 10.2
     *  @playerversion AIR 2.6
     *  @productversion Royale 0.9.3
     */
    public class FontIconBase extends StyledUIBase implements IIcon
    {
        /**
         *  constructor.
         *
         *  @langversion 3.0
         *  @playerversion Flash 10.2
         *  @playerversion AIR 2.6
         *  @productversion Royale 0.9.3
         */
        public function FontIconBase()
        {
            super();
            
            typeNames = "";
        }

        COMPILE::JS
        protected var textNode:Text;

        /**
         * @royaleignorecoercion org.apache.royale.core.WrappedHTMLElement
		 * @royaleignorecoercion HTMLElement
         * @royaleignorecoercion Text
         */
        COMPILE::JS
        override protected function createElement():WrappedHTMLElement
        {
			var i:WrappedHTMLElement = addElementToWrapper(this,'i');
            
            textNode = document.createTextNode(iconText) as Text;
            i.appendChild(textNode); 

            positioner = element;
            
            return i;
        }

        /**
         *  the icon text that matchs with font icon.
         *  override in extending classes
         *
         *  @langversion 3.0
         *  @playerversion Flash 10.2
         *  @playerversion AIR 2.6
         *  @productversion Royale 0.9.3
         */
        protected function get iconText():String
        {
            return "";
        }

        private var _material:Boolean;
        /**
         *  add class name "material-icons" since in IE11 this font only
         *  works with that class name strangely. it seems we can avoid this 
         *  self-hosting the fonts @see https://google.github.io/material-design-icons/
         *  but we must think if this is or not the right way.
         *
         *  @langversion 3.0
         *  @playerversion Flash 10.2
         *  @playerversion AIR 2.6
         *  @productversion Royale 0.9.3
         */
        public function get material():Boolean
        {
            return _material;
        }
        public function set material(value:Boolean):void
        {
            if (_material != value)
            {
                _material = value;

                typeNames = StringUtil.removeWord(typeNames, " material-icons");
                typeNames += " material-icons";

                COMPILE::JS
                {
                    if (parent)
                        setClassName(computeFinalClassNames()); 
                }
            }
        }

        private var _size:Number = 24;
        /**
         *  Activate "size-XX" size class selector. Although the icons in the 
         *  font can be scaled to any size, recommended sizes are 18, 24, 36 or 48px.
         *
         *  The default being 24px.
         *
         *  @langversion 3.0
         *  @playerversion Flash 10.2
         *  @playerversion AIR 2.6
         *  @productversion Royale 0.8
         */
        public function get size():Number
        {
            return _size;
        }
        public function set size(value:Number):void
        {
            if (_size != value)
            {
                COMPILE::JS
                {
                    removeClass("size-" + _size);
                    _size = value;
                    addClass("size-" + _size);
                }
            }
        }

        private var _dark:Boolean;
        /**
         *  Activate "dark" class selector.
         *
         *  @langversion 3.0
         *  @playerversion Flash 10.2
         *  @playerversion AIR 2.6
         *  @productversion Royale 0.9.3
         */
        public function get dark():Boolean
        {
            return _dark;
        }

        public function set dark(value:Boolean):void
        {
            if (_dark != value)
            {
                _dark = value;

                toggleClass("dark", _dark);
            }
        }

        private var _light:Boolean;
        /**
         *  Activate "light" class selector.
         *
         *  @langversion 3.0
         *  @playerversion Flash 10.2
         *  @playerversion AIR 2.6
         *  @productversion Royale 0.9.3
         */
        public function get light():Boolean
        {
            return _light;
        }
        public function set light(value:Boolean):void
        {
            if (_light != value)
            {
                _light = value;

                toggleClass("light", _light);
            }
        }

        private var _inactive:Boolean;
        /**
         *  Activate "inactive" class selector.
         *  To show the icon as inactive
         *
         *  @langversion 3.0
         *  @playerversion Flash 10.2
         *  @playerversion AIR 2.6
         *  @productversion Royale 0.9.3
         */
        public function get inactive():Boolean
        {
            return _inactive;
        }
        public function set inactive(value:Boolean):void
        {
            if (_inactive != value)
            {
                _inactive = value;

                toggleClass("inactive", _inactive);
            }
        }
    }
}