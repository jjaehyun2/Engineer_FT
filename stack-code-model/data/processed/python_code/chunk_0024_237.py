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

package {
	
	import com.sangupta.as3utils.ArrayUtilsTest;
	import com.sangupta.as3utils.AssertUtilsTest;
	
	/**
	 *
	 * @author <a href="http://www.sangupta.com">Sandeep Gupta</a>
	 * @since 1.0
	 */
	[Suite]
	[RunWith( "org.flexunit.runners.Suite" )]
	public class AllTests {
		
		public var arrayUtilsTest:ArrayUtilsTest;
		public var assertUtilsTest:AssertUtilsTest;
		
	}
}