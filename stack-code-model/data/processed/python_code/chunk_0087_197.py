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
package org.springextensions.actionscript.ioc.factory {

	/**
	 * Error thrown when an object factory cannot find an object definition for the given name.
	 */
	public class NoSuchObjectDefinitionError extends Error {

		/**
		 * Creates a new NoSuchObjectDefinitionError object.
		 *
		 * @param objectName the name of the object definition
		 */
		public function NoSuchObjectDefinitionError(objectName:String) {
			super("No object named '" + objectName + "' is defined.");
			_objectName = objectName;
		}

		private var _objectName:String;

		/**
		 * @return The name of the object defintion that could not be found in the current object factory configuration.
		 */
		public function get objectName():String {
			return _objectName;
		}
	}
}