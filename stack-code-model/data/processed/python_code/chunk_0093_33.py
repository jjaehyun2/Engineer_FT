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
package org.springextensions.actionscript.ioc.config.impl.xml.parser.impl.nodeparser {
	import org.as3commons.logging.api.ILogger;
	import org.as3commons.logging.api.getClassLogger;
	import org.springextensions.actionscript.ioc.config.impl.RuntimeObjectReference;
	import org.springextensions.actionscript.ioc.config.impl.xml.parser.IXMLObjectDefinitionsParser;
	import org.springextensions.actionscript.ioc.config.impl.xml.parser.impl.XMLObjectDefinitionsParser;

	/**
	 * Parses an reference node.
	 *
	 * @author Christophe Herreman
	 * @author Erik Westra
	 */
	public class RefNodeParser extends AbstractNodeParser {

		private static const logger:ILogger = getClassLogger(RefNodeParser);

		/**
		 * Constructs the RefNodeParser.
		 *
		 * @param xmlObjectDefinitionsParser  The definitions parser using this NodeParser
		 *
		 * @see org.springextensions.actionscript.ioc.factory.xml.parser.support.XMLObjectDefinitionsParser.#REF_ELEMENT
		 */
		public function RefNodeParser(xmlObjectDefinitionsParser:IXMLObjectDefinitionsParser) {
			super(xmlObjectDefinitionsParser, XMLObjectDefinitionsParser.REF_ELEMENT);
		}

		/**
		 * @inheritDoc
		 */
		override public function parse(node:XML):* {
			var id:String = node.toString();
			logger.debug("Creating runtime object reference to definition '{0}'", [id]);
			return new RuntimeObjectReference(id);
		}
	}
}