/*
 * Copyright 2011 the original author or authors.
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
package org.spicefactory.lib.command.model {
/**
 * @author Jens Halm
 */
public class CommandModel {
	
	private var _value: Object;
	private var _injected: Boolean;
	
	function CommandModel (value: Object) {
		_value = value;
	}
	
	public function get value (): Object {
		return _value;
	}
	
	public function markAsInjected (): void {
		_injected = true;
	}
	
	public function get injected (): Boolean {
		return _injected;
	}
	
}
}