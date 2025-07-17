/*
 * Copyright (c) 2012 the original author or authors
 *
 * Permission is hereby granted to use, modify, and distribute this file
 * in accordance with the terms of the license agreement accompanying it.
 */
package org.robotlegs.utilities.undoablecommand.commands
{

	import org.robotlegs.mvcs.Command;
	import org.robotlegs.utilities.undoablecommand.interfaces.ICommandHistory;

	/**
	 * Map this command to the HistoryEvent.STEP_BACKWARD event to trigger an undo action.
	 * Provided for convenience.
	 */
	public class ClearHistoryCommand extends Command
	{

		[Inject]
		public var commandHistory : ICommandHistory;


		override public function execute() : void
		{
			commandHistory.clear();
		}
	}
}