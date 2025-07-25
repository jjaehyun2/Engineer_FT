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
package mx.display
{
    import org.apache.royale.events.EventDispatcher;
    import mx.core.UIComponent;

    public class LoaderInfo extends EventDispatcher
    {
        private var _loader:Loader;

        public function LoaderInfo(loaderValue:Loader)
        {
            super();
            _loader = loaderValue;
        }

	public function get content():UIComponent
	    {
		    return _loader.content;
	    }

        public function get loader():Loader
        {
        	return _loader;
        }

        public function get width():int
        {
            // TODO this should be the nominal width, whatever that means
            return _loader.content.width;
        }

        public function get height():int
        {
            // TODO this should be the nominal height, whatever that means
            return _loader.content.height;
        }
		
		public var _url:String = "";
		public function get url():String {
			return _url;
		}

    }
}