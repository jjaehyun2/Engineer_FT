/**
 *
 * as3utils - ActionScript Utility Classes
 * Copyright (C) 2011, Sandeep Gupta
 * http://www.sangupta.com/projects/as3utils
 *
 * The file is licensed under the the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */

package com.sangupta.as3utils {
	
	/**
	 * Helper class for working with <code>Array</code> class.
	 * 
	 * @author <a href="http://www.sangupta.com">Sandeep Gupta</a>
	 * @since 1.0
	 */
	public class ArrayUtils	{
		
		/**
		 * <code>ArrayUtils</code> instances should NOT be constructed in standard programming.
		 */
		public function ArrayUtils() {
			super();
		}

		/**
		 * Method that checks whether the given <code>object</code> is present
		 * in the array using strict === equality.
		 * 
		 * @param array the array to be searched
		 * 
		 * @object the object to be looked for
		 * 
		 * @return <code>true</code> if the item exists inside the array, <code>false</code>
		 * otherwise.
		 */
		public static function has(array:Array, object:Object):Boolean {
			if(array == null || object == null) {
				return false;
			}
			
			for each(var obj:Object in array) {
				if(obj === object) {
					return true;
				}
			}
			
			return false;
		}
		
		/**
		 * Method that checks whether the given <code>object</code> is present
		 * in the array using normal == equality.
		 * 
		 * @param array the array in which the existence of item is to be tested
		 * 
		 * @param object the object to be looked for
		 * 
		 * @return <code>true</code> if the item exists inside the array, <code>false</code>
		 * otherwise.
		 */
		public static function contains(array:Array, object:Object):Boolean {
			if(array == null || object == null) {
				return false;
			}
			
			for each(var obj:Object in array) {
				if(obj == object) {
					return true;
				}
			}
			
			return false;
		}
		
		/**
		 * Remove the given item from the array. The method is <code>null</code>
		 * safe. 
		 * 
		 * @param array the array from which the item is to be removed
		 * 
		 * @object the item to be removed
		 */
		public static function removeItem(array:Array, object:Object):void {
			if(object != null) {
				if(AssertUtils.isNotEmptyArray(array)) {
					for(var index:Number = 0; index < array.length; index++) {
						var item:Object = array[index];
						if(item === object) {
							array.splice(index, 1);
							break;
						}
					}
				}
			}
		}
		
		/**
		 * Remove all elements from the given array.
		 */
		public static function clear(array:Array):void {
			if(array != null) {
				array.splice(0, array.length);
			}
		}

	}
}