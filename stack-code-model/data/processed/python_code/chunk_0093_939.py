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
 
package org.spicefactory.lib.command.base {

import org.spicefactory.lib.command.SuspendableCommand;
import org.spicefactory.lib.command.events.CommandEvent;
import org.spicefactory.lib.logging.LogContext;
import org.spicefactory.lib.logging.Logger;
	
/**
 * Abstract base implementation of the CancellableCommand interface. 
 * 
 * <p>A subclass of AbstractCancellableCommand is expected
 * to override the <code>doStart</code>, <code>doCancel</code>, <code>doSuspend</code> and <code>doResume</code>
 * methods and perform the necessary operations, and then call <code>complete</code>
 * when the operation is done (or <code>error</code> when the command fails to complete successfully).</p>
 * 
 * @author Jens Halm
 */
public class AbstractSuspendableCommand extends AbstractCancellableCommand implements SuspendableCommand {
	
	
	private static var logger:Logger = LogContext.getLogger(AbstractSuspendableCommand);
	
	
	private var _suspended : Boolean;

	
	/**
	 * Creates a new instance.
	 * 
	 * @param description a description of this command
	 */
	public function AbstractSuspendableCommand (description:String = null) {
		super(description);
	}
		
	
	/**
	 * @inheritDoc
	 */
	public function get suspended () : Boolean {
		return _suspended;
	}
	
	/**
	 * @inheritDoc
	 */
	public function suspend () : void {
		if (!active) {
			logger.error("Attempt to suspend inactive command '{0}'", this);
			return;
		}
		if (suspended) {
			logger.error("Attempt to suspend command '{0}' which is already suspended", this);
			return;
		}
		_suspended = true;
		doSuspend();
		dispatchEvent(new CommandEvent(CommandEvent.SUSPEND));
	}
	
	/**
	 * @inheritDoc
	 */
	public function resume () : void {
		if (!suspended) {
			logger.error("Attempt to resume command '{0}' which is not suspended", this);
			return;
		}
		_suspended = false;
		doResume();
		dispatchEvent(new CommandEvent(CommandEvent.RESUME));		
	}
	
	/**
	 * Invoked when this command gets suspended. 
	 * Subclasses should override this method and suspend the actual operation
	 * this command performs.
	 */	
	protected function doSuspend () : void {
		/* base implementation does nothing */
	}

	/**
	 * Invoked when this command gets resumed.  
	 * Subclasses should override this method and resume the suspended operation
	 * this command performs.
	 */	
	protected function doResume () : void {
		/* base implementation does nothing */
	}
	
	
}
}