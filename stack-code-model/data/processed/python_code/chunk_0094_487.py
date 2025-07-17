/*
 * Copyright (c) 2012 the original author or authors
 *
 * Permission is hereby granted to use, modify, and distribute this file
 * in accordance with the terms of the license agreement accompanying it.
 */
package org.robotlegs.utilities.undoablecommand.commands
{

	import org.robotlegs.mvcs.Command;
	import org.robotlegs.utilities.undoablecommand.event.HistoryEvent;
	import org.robotlegs.utilities.undoablecommand.interfaces.ICommandHistory;

	import flash.events.Event;

	/**
	 * Map this command to the HistoryEvent.UNDO event to trigger undo action(s).
	 * Provided for convenience.
	 * 
	 * Pass number of undo levels as an integer data argument to the HistoryEvent to perfom multiple undos
	 */
	public class UndoCommand extends Command
	{
		[Inject]
		public var commandHistory : ICommandHistory;

		[Inject]
		public var event : Event;

		public function UndoCommand()
		{
		}


		/**
		 * execute undo 
		 */
		override public function execute() : void
		{
			var levels : int;

			if ( event is HistoryEvent )
			{
				levels = (event as HistoryEvent).levels > 1 ? (event as HistoryEvent).levels : 1;
			}
			else
			{
				levels = 1;
			}

			commandHistory.undo(levels);
		}
	}
}