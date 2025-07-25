/*
 * Copyright 2010 the original author or authors.
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

package org.spicefactory.lib.xml.mapper.metadata {
import org.spicefactory.lib.xml.mapper.MetadataMapperBuilder;
import org.spicefactory.lib.xml.mapper.MetadataMapperDecorator;

[Metadata(name="Ignore", types="property")]
/**
 * Represents a Metadata tag that can be used on properties that should not be mapped.
 *
 * @author Jens Halm
 */
public class IgnoreDecorator implements MetadataMapperDecorator {

	
	
	[Target]
	/**
	 * The name of the property.
	 */
	public var property:String;
	
	/**
	 * @inheritDoc
	 */
	public function decorate (builder:MetadataMapperBuilder) : void {
		builder.ignoreProperty(property);
	}
	
	
}
}