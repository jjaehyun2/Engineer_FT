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
package org.springextensions.actionscript.metadata {
	import org.as3commons.metadata.process.IMetadataProcessor;

	/**
	 * Marker interface that indicates an <code>IMetadataProcessor</code> that needs to be invoked in the destruction
	 * phase of an object's lifecycle.
	 * @author Roland Zwaga
	 */
	public interface IMetadataDestroyer extends IMetadataProcessor {

	}
}