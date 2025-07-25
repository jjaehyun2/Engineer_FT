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
package org.springextensions.actionscript.ioc.factory.process.impl.factory {
	import org.as3commons.async.operation.IOperation;
	import org.as3commons.logging.api.ILogger;
	import org.as3commons.logging.api.getClassLogger;
	import org.springextensions.actionscript.ioc.factory.IObjectFactory;
	import org.springextensions.actionscript.ioc.factory.process.IObjectPostProcessor;


	/**
	 *
	 * @author Roland Zwaga
	 */
	public class RegisterObjectPostProcessorsFactoryPostProcessor extends AbstractOrderedFactoryPostProcessor {

		private static var logger:ILogger = getClassLogger(RegisterObjectPostProcessorsFactoryPostProcessor);

		/**
		 * Creates a new <code>RegisterObjectPostProcessorsFactoryPostProcessor</code> instance.
		 *
		 */
		public function RegisterObjectPostProcessorsFactoryPostProcessor(orderPosition:int) {
			super(orderPosition);
		}

		/**
		 * Retrieves all instances of type <code>IObjectPostProcessor</code> from the specified <code>IObjectFactory</code> and registers
		 * them with the same <code>IObjectFactory</code>.
		 * @param objectFactory
		 * @return
		 */
		override public function postProcessObjectFactory(objectFactory:IObjectFactory):IOperation {
			if (objectFactory.objectDefinitionRegistry != null) {
				var objectNames:Vector.<String> = objectFactory.objectDefinitionRegistry.getObjectDefinitionNamesForType(IObjectPostProcessor);
				for each (var name:String in objectNames) {
					logger.debug("Registering object postprocessor '{0}'", [name]);
					objectFactory.addObjectPostProcessor(IObjectPostProcessor(objectFactory.getObject(name)));
				}
			}
			return null;
		}
	}
}