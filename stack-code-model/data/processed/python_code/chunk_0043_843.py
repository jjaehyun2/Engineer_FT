/*
 * Copyright 2011 the original author or authors.
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
package org.spicefactory.parsley.xml.tag.command {

import org.spicefactory.parsley.command.tag.link.LinkResultTypeTag;

[XmlMapping(elementName="link-result-type")]
/**
 * Links a specific result value
 * to the the target command specified by this tag.
 * 
 * @author Jens Halm
 */
public class XmlLinkResultTypeTag extends LinkResultTypeTag {
	
	
	[Attribute("to")]
	/**
	 * The id of the command to execute in case the condition
	 * specified by this tag is met.
	 */
	public var toId:String;
	
	
	/**
	 * @private
	 */
	protected override function get targetKey () : Object {
		return toId;
	}
	
	
}
}