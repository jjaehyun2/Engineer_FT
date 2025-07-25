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

package com.sangupta.as3utils.filefilter {
	
	import flash.filesystem.File;

	/**
	 * An implementation of <code>FileFilter</code> that selects all files
	 * that are directories.
	 * 
	 * @author sangupta
	 * @since 1.0
	 */
	public class DirectoryFileFilter implements IFileFilter {
		
		/**
		 * Create a new instance of <code>DirectoryFileFilter</code>.
		 * 
		 */
		public function DirectoryFileFilter() {
			super();
		}
		
		/**
		 * Test whether the supplied file fulfills the criteria of this filter.
		 * 
		 * @param the file to be tested against
		 * 
		 * @return <code>true</code> if the file can be accepted by the filter,
		 * <code>false</code> otherwise.
		 */
		public function accept(file:File):Boolean {
			if(file.isDirectory) {
				return true;
			}
			
			return false;
		}
	}
}