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
package
{
	/**
	 * @externs
	 */
	COMPILE::JS
	public class dialogPolyfill
	{
		/** 
         * <inject_html>
         * <script src="https://cdnjs.cloudflare.com/ajax/libs/dialog-polyfill/0.4.9/dialog-polyfill.min.js"></script>
         * <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/dialog-polyfill/0.4.9/dialog-polyfill.min.css">
         * </inject_html>
		 */
		public function dialogPolyfill(){}
		 
		public static function registerDialog(dialog:Element):void {}
	}
}