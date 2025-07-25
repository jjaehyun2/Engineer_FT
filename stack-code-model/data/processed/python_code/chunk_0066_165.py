/*
 * Copyright 2008 the original author or authors.
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
 
package org.spicefactory.lib.reflect.metadata {

[Metadata(types="property")] 
/**
 * Represents a metadata tag that marks a property as the default property.
 * These will be mapped for attributes in metadata tags where no key is specified
 * (e.g. <code>[SomeTag("someValue")]</code>.
 * 
 * @author Jens Halm
 */
public class DefaultProperty {
	
}

}