/**
 * Copyright 2010 The original author or authors.
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *   http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.as3commons.collections.framework.core {
	import org.as3commons.collections.Map;
	import org.as3commons.collections.framework.IIterator;
	import org.as3commons.collections.mocks.MapMock;
	import org.as3commons.collections.testhelpers.AbstractIteratorTestCase;
	import org.as3commons.collections.testhelpers.UniqueMapKey;
	import org.as3commons.collections.units.iterators.IMapIteratorTests;

	/**
	 * @author Jens Struwe 23.03.2010
	 */
	public class MapIteratorTest extends AbstractIteratorTestCase {

		/*
		 * AbstractIteratorTest
		 */

		override public function createCollection() : * {
			return new MapMock();
		}

		override public function fillCollection(items : Array) : void {
			Map(collection).clear();
			for each (var item : * in items) {
				Map(collection).add(UniqueMapKey.key, item);
			}
		}

		override public function getIterator(index : uint = 0) : IIterator {
			return Map(collection).iterator(index);
		}

		override public function toArray() : Array {
			return Map(collection).toArray();
		}

		/*
		 * Units
		 */

		/*
		 * MapIterator tests
		 */

		public function test_mapIterator() : void {
			new IMapIteratorTests(this).runAllTests();
		}

	}
}