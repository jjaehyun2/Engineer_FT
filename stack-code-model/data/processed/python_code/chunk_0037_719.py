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
package org.springextensions.actionscript.stage {
	import org.as3commons.stageprocessing.IStageObjectDestroyer;
	import org.springextensions.actionscript.context.IApplicationContext;
	import org.springextensions.actionscript.context.IApplicationContextAware;

	import flash.display.DisplayObject;

	/**
	 *
	 * @author Roland Zwaga
	 */
	public class DefaultStageObjectDestroyer implements IApplicationContextAware, IStageObjectDestroyer {
		private var _applicationContext:IApplicationContext;

		/**
		 * Creates a new <code>DefaultStageObjectDestroyer</code> instance.
		 */
		public function DefaultStageObjectDestroyer() {
			super();
		}

		public function destroy(displayObject:DisplayObject):DisplayObject {
			if (_applicationContext != null) {
				_applicationContext.destroyObject(displayObject);
				_applicationContext.removeRootView(displayObject);
			}
			return displayObject;
		}

		public function process(displayObject:DisplayObject):DisplayObject {
			return displayObject;
		}

		public function get applicationContext():IApplicationContext {
			return _applicationContext;
		}

		public function set applicationContext(value:IApplicationContext):void {
			_applicationContext = value;
		}
	}
}