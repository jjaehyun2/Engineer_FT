/*
* Copyright 2007-2011 the original author or authors.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*      http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/
package org.springextensions.actionscript.ioc.error {


	public class ObjectFactoryError extends Error {

		public static const FACTORY_NOT_READY:String = "objectFactoryNotReady";
		public static const CANNOT_INSTANTIATE_INTERFACE:String = "cannotInstantiateInterface";

		public function ObjectFactoryError(message:*="", id:*=0) {
			super(message, id);
		}
	}
}