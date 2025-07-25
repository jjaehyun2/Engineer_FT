/**
 * Copyright 2011 The original author or authors.
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
package org.as3commons.ui.layout.shortcut {

	import org.as3commons.ui.layout.HGroup;
	import org.as3commons.ui.layout.framework.core.init.LayoutInitializer;

	/**
	 * Shortcut to create a <code>HGroup</code> layout.
	 * 
	 * @param args List of layout items and configuration parameters.
	 * @author Jens Struwe 18.03.2011
	 */
	public function hgroup(...args) : HGroup {
		var h : HGroup = new HGroup();
		new LayoutInitializer().init(h, args);
		return h;
	}
}