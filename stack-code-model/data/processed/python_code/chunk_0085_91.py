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

	import as3reflect.testclasses.ComplexClass;
	import as3reflect.testclasses.PublicClass;
	import as3reflect.testclasses.PublicSubClass;
	
	import flash.utils.describeType;
	
	import flexunit.framework.TestCase;
	
	import mx.logging.LogEventLevel;

	/**
	 * @author Christophe Herreman
	 */
	public class TypeTest extends TestCase {

		public function TypeTest(methodName:String = null) {
			super(methodName);
		}

		public function testForInstanceWithCustomClassInstance():void {
			var instance:PublicClass = new PublicClass();
			var type:Type = Type.forInstance(instance);
			assertEquals(12, type.methods.length);
			assertEquals(2, type.staticConstants.length);
			assertEquals(3, type.staticVariables.length);
			assertEquals(1, type.constants.length);
			assertEquals(4, type.variables.length);
			assertEquals("PublicClass", type.name);
			assertEquals("as3reflect.testclasses::PublicClass", type.fullName);
		}

		public function testForInstanceWithStringInstance():void {
			//var type:Type = Type.forInstance("myString");
		}

		public function testForClassWithNativeAccess():void {
			var type:Type = Type.forClass(Array);
			assertEquals(6, type.staticConstants.length);
			assertEquals(0, type.methods.length);
			assertEquals("Array", type.name);
			assertEquals("Array", type.fullName);
		}

		public function testForClassWithLogEventLevel():void {
			var type:Type = Type.forClass(mx.logging.LogEventLevel);
			var d:XML = describeType(LogEventLevel);
			assertEquals(7, type.staticConstants.length);
			assertEquals(8, type.fields.length);
			var errorConstant:Field = type.getField("ERROR");
			assertEquals(LogEventLevel.ERROR, errorConstant.getValue());
		}
		
		public function testForClass_shouldHaveCorrectDeclaringTypesOnAccessors():void {
			var type:Type = Type.forClass(PublicSubClass);
			for each (var accessor:Accessor in type.accessors) {
				// acc4 is defined in PublicSubClass
				// prototype is defined in Class
				// all other accessors are defined in PublicClass
				if (accessor.name == "acc4") {
					assertEquals("PublicSubClass", accessor.declaringType.name);
				}
				else if (accessor.name == "prototype") {
					assertEquals("Class", accessor.declaringType.name);
				}
				else {
					assertEquals("PublicClass", accessor.declaringType.name);
				}
			}
		}
	
		public function testNoArgumentConstructorClass():void {
		var type:Type = Type.forClass(PublicClass);
		var constructor:Constructor = type.constructor;
		assertNotNull(constructor);
		assertNotNull(constructor.declaringType);
		assertEquals(constructor.declaringType.clazz, PublicClass);
		assertEquals(constructor.parameters.length, 0);
		}
		
		public function testWithArgumentConstructorClass():void {
	
		var type:Type = Type.forClass(ComplexClass);
	
		var constructor:Constructor= type.constructor;
		assertNotNull(constructor);
		assertNotNull(constructor.declaringType);
		assertEquals(constructor.declaringType.clazz, ComplexClass);
		assertEquals(constructor.parameters.length, 3);
			
		var firstParameter:Parameter = constructor.parameters[0];
			
		assertFalse(firstParameter.isOptional);
		assertEquals(1, firstParameter.index);
		assertEquals(String, firstParameter.type.clazz);
		
		var secondParameter:Parameter = constructor.parameters[1];
			
		assertFalse(secondParameter.isOptional);
		assertEquals(2, secondParameter.index);
		assertEquals(Number, secondParameter.type.clazz);
		
		
		var thirdParameter:Parameter = constructor.parameters[2];
	
		assertTrue(thirdParameter.isOptional);
		assertEquals(3, thirdParameter.index);
		assertEquals(Array, thirdParameter.type.clazz);
		}

	}
}