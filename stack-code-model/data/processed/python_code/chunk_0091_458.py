/*
 * Copyright 2009 Marek Brun
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *    
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */
package pl.brun.lib.models.easing {

	/**
	 * created: 2009-11-29
	 * @author Marek Brun
	 */
	public class EdgeEasing extends Easing {

		/** from 0 to 1 */
		public var edge:Number = 1;

		override protected function calculateEasing(input:Number):Number {
			return circHard(input, edge);
		}

		public static function circ(n:Number):Number {
			return -(Math.sqrt(1 - n * n) - 1);
		}

		public static function circHard(n:Number, edge:Number):Number {
			var c:Number = circ(n);
			c -= (c * edge) * (1 - c);
			return c;
		}
	}
}