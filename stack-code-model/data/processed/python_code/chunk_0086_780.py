/*
 * Copyright (c) 2007-2009 the original author or authors
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
package as3reflect {

	import flash.utils.describeType;
	import flash.utils.getDefinitionByName;

	/**
	 * Provides information about the characteristics of a class or an interface.
	 * These are the methods, accessors (getter/setter), variables and constants,
	 * but also if the class is <code>dynamic</code> and <code>final</code>.
	 *
	 * <p>Note that information about an object cannot be retrieved by calling the
	 * <code>Type</code> constructor. Instead use one of the following static
	 * methods:</p>
	 *
	 * <p>In case of an instance:
	 * <code>var type:Type = Type.forInstance(myInstance);</code>
	 * </p>
	 *
	 * <p>In case of a <code>Class</code> variable:
	 * <code>var type:Type = Type.forClass(MyClass);</code>
	 * </p>
	 *
	 * <p>In case of a classname:
	 * <code>var type:Type = Type.forName("MyClass");</code>
	 * </p>
	 *
	 * @author Christophe Herreman, Martino Piccinato
	 */
	public class Type extends MetaDataContainer {

		public static const UNTYPED:Type = new Type();
		public static const VOID:Type = new Type();
		public static const PRIVATE:Type = new Type();

		private static var _cache:Object = {};

		private var _name:String;
		private var _fullName:String;
		private var _isDynamic:Boolean;
		private var _isFinal:Boolean;
		private var _isStatic:Boolean;
		private var _constructor:Constructor;
		private var _methods:Array;
		private var _accessors:Array;
		private var _staticConstants:Array;
		private var _constants:Array;
		private var _staticVariables:Array;
		private var _variables:Array;
		private var _fields:Array;
		private var _class:Class;

		/**
		 * Creates a new <code>Type</code> instance.
		 */
		public function Type() {
			super();
			_methods = new Array();
			_accessors = new Array();
			_staticConstants = new Array();
			_constants = new Array();
			_staticVariables = new Array();
			_variables = new Array();
			_fields = new Array();
		}

		/**
		 * Returns a <code>Type</code> object that describes the given instance.
		 *
		 * @param instance the instance from which to get a type description
		 */
		public static function forInstance(instance:*):Type {
			var result:Type;
			var clazz:Class = ClassUtils.forInstance(instance);
			if (clazz != null) {
				result = Type.forClass(clazz);
			}
			return result;
		}

		/**
		 * Returns a <code>Type</code> object that describes the given classname.
		 *
		 * @param name the classname from which to get a type description
		 */
		public static function forName(name:String):Type {
			var result:Type;
			/*if(name.indexOf("$")!=-1){
				return Type.PRIVATE;
			}*/
			switch (name) {
				case "void":
				result = Type.VOID;
				break;
				case "*":
				result = Type.UNTYPED;
				break;
				default:
				try {
					result = Type.forClass(Class(getDefinitionByName(name)));
				}
				catch (e:ReferenceError) {
					trace("Type.forName error: " + e.message + " The class '" + name + "' is probably an internal class or it may not have been compiled.");
				}

			}
			return result;
		}

		/**
		 * Returns a <code>Type</code> object that describes the given class.
		 *
		 * @param clazz the class from which to get a type description
		 */
		public static function forClass(clazz:Class):Type {
			var result:Type;
			var fullyQualifiedClassName:String = ClassUtils.getFullyQualifiedName(clazz);

			if (_cache[fullyQualifiedClassName]) {
				result = _cache[fullyQualifiedClassName];
			}
			else {
				var description:XML = _getTypeDescription(clazz);
				result = new Type();
				// add the Type to the cache before assigning any values to prevent looping
				_cache[fullyQualifiedClassName] = result;
				result.fullName = fullyQualifiedClassName;
				result.name = ClassUtils.getNameFromFullyQualifiedName(fullyQualifiedClassName);
				result.clazz = clazz;
				result.isDynamic = description.@isDynamic;
				result.isFinal = description.@isFinal;
				result.isStatic = description.@isStatic;
				result.constructor = TypeXmlParser.parseConstructor(result, description.factory.constructor);
				result.accessors = TypeXmlParser.parseAccessors(result, description);
				result.methods = TypeXmlParser.parseMethods(result, description);
				result.staticConstants = TypeXmlParser.parseMembers(Constant, description.constant, result, true);
				result.constants = TypeXmlParser.parseMembers(Constant, description.factory.constant, result, false);
				result.staticVariables = TypeXmlParser.parseMembers(Variable, description.variable, result, true);
				result.variables = TypeXmlParser.parseMembers(Variable, description.factory.variable, result, false);
				TypeXmlParser.parseMetaData(description.factory[0].metadata, result);
			}

			return result;
		}

		/**
		 * Returns the <code>Method</code> object for the method in this type
		 * with the given name.
		 *
		 * @param name the name of the method
		 */
		public function getMethod(name:String):Method {
			var result:Method;
			for each (var method:Method in methods) {
				if (method.name == name) {
				result = method;
				break;
				}
			}
			return result;
		}

		/**
		 * Returns the <code>Field</code> object for the field in this type
		 * with the given name.
		 *
		 * @param name the name of the field
		 */
		public function getField(name:String):Field {
			var result:Field;
			for each (var field:Field in fields) {
				if (field.name == name) {
				result = field;
				break;
				}
			}
			return result;
		}

		public function get name():String { return _name; }
		public function set name(value:String):void { _name = value; }

		public function get fullName():String { return _fullName; }
		public function set fullName(value:String):void { _fullName = value; }

		public function get clazz():Class { return _class; }
		public function set clazz(value:Class):void { _class = value; }

		public function get isDynamic():Boolean { return _isDynamic; }
		public function set isDynamic(value:Boolean):void { _isDynamic = value; }

		public function get isFinal():Boolean { return _isFinal; }
		public function set isFinal(value:Boolean):void { _isFinal = value; }

		public function get isStatic():Boolean { return _isStatic; }
		public function set isStatic(value:Boolean):void { _isStatic = value; }
	
		public function get constructor():Constructor { return _constructor; }
		public function set constructor(constructor:Constructor):void { _constructor = constructor; }
	
		public function get accessors():Array { return _accessors; }
		public function set accessors(value:Array):void { _accessors = value; }

		public function get methods():Array { return _methods; }
		public function set methods(value:Array):void { _methods = value; }

		public function get staticConstants():Array { return _staticConstants; }
		public function set staticConstants(value:Array):void { _staticConstants = value; }

		public function get constants():Array { return _constants; }
		public function set constants(value:Array):void { _constants = value; }

		public function get staticVariables():Array { return _staticVariables; }
		public function set staticVariables(value:Array):void { _staticVariables = value; }

		public function get variables():Array { return _variables; }
		public function set variables(value:Array):void { _variables = value; }

		public function get fields():Array {
			return accessors.concat(staticConstants).concat(constants).concat(staticVariables).concat(variables);
		}

		/**
		 * Get XML clazz description as given by flash.utils.describeType
		 * using a workaround for bug http://bugs.adobe.com/jira/browse/FP-183
		 * that in certain cases do not allow to retrieve complete constructor
		 * description.
		 */
		private static function _getTypeDescription(clazz:Class):XML {
			var description:XML = describeType(clazz);
				
			// Workaround for bug http://bugs.adobe.com/jira/browse/FP-183
			var constructorXML:XMLList = description.factory.constructor;
				
			if (constructorXML && constructorXML.length() > 0) {
				var parametersXML:XMLList = constructorXML[0].parameter;
				if (parametersXML && parametersXML.length() > 0) {
					// Instantiate class with all null arguments.
					var args:Array = [];
					for (var n:int = 0; n < parametersXML.length(); n++) {
						args.push(null);
					}
					// As the constructor may throw Errors on null arguments arguments 
					// surround it with a try/catch block
					try {
						ClassUtils.newInstance(clazz, args);
					} catch (e:Error) {
						// Do nothing (here is not a problem to hide the Error as we just need to
						// instantiate the class once to have complete constructor
						// parameters information
					}
						
					description = describeType(clazz);
				}
			}
			
			return description;
		}
	
	}
}

import as3reflect.Type;
import as3reflect.IMetaDataContainer;
import as3reflect.AccessorAccess;
import as3reflect.Method;
import as3reflect.Parameter;
import as3reflect.Accessor;
import as3reflect.MetaDataArgument;
import as3reflect.MetaData;
import as3reflect.IMember;
import as3reflect.Constructor;

/**
 * Internal xml parser
 */
class TypeXmlParser {
	public static function parseConstructor(type:Type, constructorXML:XMLList):Constructor {
	if (constructorXML.length() > 0) {
		var params:Array = parseParameters(constructorXML[0].parameter);
		return new Constructor(type, params);
	} else {
		return new Constructor(type);
	}
	}	
	public static function parseMethods(type:Type, xml:XML):Array {
		var classMethods:Array = parseMethodsByModifier(type, xml.method, true);
		var instanceMethods:Array = parseMethodsByModifier(type, xml.factory.method, false);
		return classMethods.concat(instanceMethods);
	}
	public static function parseAccessors(type:Type, xml:XML):Array {
		var classAccessors:Array = parseAccessorsByModifier(type, xml.accessor, true);
		var instanceAccessors:Array = parseAccessorsByModifier(type, xml.factory.accessor, false);
		return classAccessors.concat(instanceAccessors);
	}
	public static function parseMembers(memberClass:Class, members:XMLList, declaringType:Type, isStatic:Boolean):Array {
		var result:Array = [];
		for each (var m:XML in members) {
			var member:IMember = new memberClass(m.@name, Type.forName(m.@type), declaringType, isStatic);
			parseMetaData(m.metadata, member);
			result.push(member);
		}
		return result;
	}
	private static function parseMethodsByModifier(type:Type, methodsXML:XMLList, isStatic:Boolean):Array {
		var result:Array = [];
		for each (var methodXML:XML in methodsXML) {
			var params:Array = parseParameters(methodXML.parameter);
			var method:Method = new Method(type, methodXML.@name, isStatic, params, Type.forName(methodXML.@returnType));
			parseMetaData(methodXML.metadata, method);
			result.push(method);
		}
		return result;
	}
	private static function parseParameters(paramsXML:XMLList):Array {
		var params:Array = [];
		for each(var paramXML:XML in paramsXML) {
		var paramType:Type = Type.forName(paramXML.@type);
		var param:Parameter = new Parameter(paramXML.@index, paramType, paramXML.@optional == "true" ? true : false );
		params.push(param);
		}
	
		return params;
	}
	private static function parseAccessorsByModifier(type:Type, accessorsXML:XMLList, isStatic:Boolean):Array {
		var result:Array = [];
		for each (var accessorXML:XML in accessorsXML) {
			var accessor:Accessor = new Accessor(
							accessorXML.@name,
							AccessorAccess.fromString(accessorXML.@access),
							Type.forName(accessorXML.@type),
							Type.forName(accessorXML.@declaredBy),
							isStatic);
			parseMetaData(accessorXML.metadata, accessor);
			result.push(accessor);
		}
		return result;
	}
	/**
	 * Parses MetaData objects from the given metaDataNodes XML data and adds them to the given metaData array.
	 */
	public static function parseMetaData(metaDataNodes:XMLList, metaData:IMetaDataContainer):void {
		for each (var metaDataXML:XML in metaDataNodes) {
			var metaDataArgs:Array = [];
			for each (var metaDataArgNode:XML in metaDataXML.arg) {
				metaDataArgs.push(new MetaDataArgument(metaDataArgNode.@key, metaDataArgNode.@value));
			}
			metaData.addMetaData(new MetaData(metaDataXML.@name, metaDataArgs));
		}
	}
}