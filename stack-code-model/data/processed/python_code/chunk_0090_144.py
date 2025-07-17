/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.flexunit.asserts {
	import org.flexunit.Assert;

	/**
	 * Alias for org.flexunit.Assert assertNull method
	 * 
	 * @param rest
	 * 			Accepts an argument of type Object.
	 * 			If two arguments are passed the first argument must be a String
	 * 			and will be used as the error message.
	 * 			
	 * 			<code>assertNull( String, Object );</code>
	 * 			<code>assertNull( Object );</code>
	 * 
	 * @see org.flexunit.Assert assertNull
	 */
	public function assertNull(... rest):void {
		Assert.assertNull.apply( null, rest );
	}
}