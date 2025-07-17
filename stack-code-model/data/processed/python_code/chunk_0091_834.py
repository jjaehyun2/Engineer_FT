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

package org.spicefactory.lib.command.adapter {
import org.spicefactory.lib.command.CommandExecutor;
	
/**
 * Represents an adapter for a command type that does not implement
 * one of the command interfaces.
 * 
 * @author Jens Halm
 */
public interface CommandAdapter extends CommandExecutor {
	
	/**
	 * The target executed by this adapter.
	 */
	function get target () : Object;
	
}
}