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
package org.springextensions.actionscript.ioc.config.property.impl {
	import org.as3commons.lang.Assert;
	import org.as3commons.logging.api.ILogger;
	import org.as3commons.logging.api.getClassLogger;
	import org.springextensions.actionscript.ioc.config.property.IPropertiesProvider;
	import org.springextensions.actionscript.ioc.config.property.IPropertyPlaceholderResolver;
	import org.springextensions.actionscript.ioc.config.property.error.PropertyPlaceholderResolverError;

	/**
	 * Used for resolving property placeholders.<br/>
	 * A property placeholder can be of two forms:<br/>
	 * ${place_holder} or $(place_holder).<br/>
	 * The first is typically used in XML configurations, the second in MXML.
	 * @author Christophe Herreman
	 * @author Roland Zwaga
	 */
	public class PropertyPlaceholderResolver implements IPropertyPlaceholderResolver {

		private static const logger:ILogger = getClassLogger(PropertyPlaceholderResolver);

		public static const NUM_BEGIN_CHARS:uint = 2; // '${' or '$('
		public static const NUM_END_CHARS:uint = 1; // '}' or ')'

		/**
		 * Creates a new <code>PropertyPlaceholderResolver</code> instance.
		 * @param regExp the regular expression used for searching for property placeholders
		 * @param properties the properties
		 * @param ignoreUnresolvablePlaceholders whether or not to ignore (fail silent) unresolvable properties or not (throw error)
		 */
		public function PropertyPlaceholderResolver(regExp:RegExp=null, properties:IPropertiesProvider=null, ignoreUnresolvablePlaceholders:Boolean=false) {
			this.regExp = regExp;
			this.propertiesProvider = properties;
			this.ignoreUnresolvablePlaceholders = ignoreUnresolvablePlaceholders;
		}

		private var _ignoreUnresolvablePlaceholders:Boolean;
		private var _propertiesProvider:IPropertiesProvider;
		private var _regExp:RegExp;

		public function get ignoreUnresolvablePlaceholders():Boolean {
			return _ignoreUnresolvablePlaceholders;
		}

		public function set ignoreUnresolvablePlaceholders(value:Boolean):void {
			if (value != _ignoreUnresolvablePlaceholders) {
				_ignoreUnresolvablePlaceholders = value;
			}
		}

		public function get propertiesProvider():IPropertiesProvider {
			return _propertiesProvider;
		}

		public function set propertiesProvider(value:IPropertiesProvider):void {
			if (value !== _propertiesProvider) {
				_propertiesProvider = value;
			}
		}

		public function get regExp():RegExp {
			return _regExp;
		}

		public function set regExp(value:RegExp):void {
			if (value !== _regExp) {
				_regExp = value;
			}
		}

		/**
		 * Returns the name of the property from a placeholder string.
		 * e.g. ${myProperty} -> myProperty
		 */
		public static function getPropertyName(placeholder:String):String {
			return placeholder.substring(NUM_BEGIN_CHARS, placeholder.length - NUM_END_CHARS);
		}

		/**
		 * Resolves the property placeholders for the given string, using the given regular expression. This method
		 * is used recursively by the resolvePropertyPlaceholder method since this will only do a single
		 * non-recursive replacement.
		 *
		 * @param value the string value for which to replace its placeholders
		 * @param regExp the regular expression used to search for property placeholders
		 * @return the value with its property placeholders resolved
		 */
		public function replacePropertyPlaceholder(value:String, regExp:RegExp, properties:IPropertiesProvider):String {
			Assert.hasText(value, "value argument must have text");
			Assert.notNull(regExp, "regExp argument must not be null");
			properties ||= _propertiesProvider;
			Assert.notNull(properties, "properties argument must not be null");
			var matches:Array = value.match(regExp);
			for each (var match:String in matches) {
				var key:String = getPropertyName(match);
				var newValue:String = properties.getProperty(key);

				// throw error or allow unresolved placeholders
				// note: don't check with !newValue since we also allow empty strings
				if (newValue == null) {
					if (!ignoreUnresolvablePlaceholders) {
						throw new PropertyPlaceholderResolverError("Could not resolve placeholder '" + match + "'");
					}
				} else {
					logger.debug("Replacing '{0}' in '{1}' with '{2}'", [match, value, newValue]);
					value = value.replace(match, newValue);
				}
			}
			return value;
		}

		/**
		 * Resolves the property placeholders in the given value, using the given regular expression. Property
		 * replacement happens recursively to make sure that property placeholders that are replaced by other
		 * property placeholders also get replaced.
		 *
		 * @param value the string value for which to replace its placeholders
		 * @param regEx the regular expression used to search for property placeholders
		 * @return the value with its property placeholders resolved
		 */
		public function resolvePropertyPlaceholders(value:String, regEx:RegExp=null, properties:IPropertiesProvider=null):String {
			if (!value) {
				return value;
			}

			regEx ||= this.regExp;
			properties ||= this.propertiesProvider;

			var newValue:String;

			// try to resolve as long as we match the regular expression
			while (value.search(regEx) > -1) {
				newValue = replacePropertyPlaceholder(value, regEx, properties);

				if (newValue != value) {
					value = newValue;
				} else {
					// the replaced value is equal to the original value
					// this might be in case we have an unresolved placeholder and unresolved placeholders
					// are ignored, so we need to break to prevent an infinite loop
					break;
				}
			}
			return value;
		}
	}
}