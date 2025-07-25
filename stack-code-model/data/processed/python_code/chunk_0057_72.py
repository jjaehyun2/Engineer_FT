/*
 * Copyright 2008-2009 the original author or authors.
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

package org.spicefactory.parsley.core.messaging.impl {

import org.spicefactory.lib.logging.LogContext;
import org.spicefactory.lib.logging.Logger;
import org.spicefactory.parsley.core.scope.ScopeManager;

/**
 * Represents a reference to a message dispatcher function. To be used in MXML and XML configuration.
 * 
 * @author Jens Halm
 */
public class MessageDispatcher {
	
	
	private static const log:Logger = LogContext.getLogger(MessageDispatcher);
	
	
	private var scopeManager:ScopeManager;
	private var scope:String;
	private var enabled:Boolean = true;
	
	private var owner:Object;
	
	
	/**
	 * Creates a new instance.
	 * 
	 * @param scopeManager the scope manager the message should be dispatched through
	 * @param scope the scope the message should be dispatched to
	 * @param owner the owner of this dispatcher 
	 */
	function MessageDispatcher (scopeManager:ScopeManager, scope:String = null, owner:Object = null) {
		this.scopeManager = scopeManager;
		this.scope = scope;
		this.owner = owner;
	}
	
	
	/**
	 * Dispatches the specified message through the ScopeManager associated with this reference.
	 * 
	 * @param message the message to dispatch
	 * @param selector the selector to use if it cannot be determined from the message instance itself
	 */
	public function dispatchMessage (message:Object, selector:* = undefined) : void {
		if (!enabled) {
			var ownerDesc:String = (owner) ? owner.toString() : "<unknown>";
			log.warn("Attempt to use message dispatcher for {0} after it has been disabled", ownerDesc);
			return;
		}
		if (scope == null) {
			scopeManager.dispatchMessage(message, selector);
		}
		else {
			scopeManager.getScope(scope).dispatchMessage(message, selector);
		}
	}
	
	/**
	 * Disables this dispatcher so that calls to dispatchMessage get ignored.
	 */
	public function disable () : void {
		enabled = false;
		scope = null;
		scopeManager = null;
	}
	
	
}
}