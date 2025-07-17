/*
 * Copyright (c) 2012 the original author or authors
 *
 * Permission is hereby granted to use, modify, and distribute this file
 * in accordance with the terms of the license agreement accompanying it.
 */
package org.robotlegs.utilities.undoablecommand.interfaces
{
	import flash.events.IEventDispatcher;
	/**
	 * ICommandHistory interface
	 */
	public interface ICommandHistory
	{

		function clear() : void;


		function undo(levels : int = 1) : void;


		function redo(levels : int = 1) : void;


		function add(command : IUndoableCommand) : void;


		function isAdded( command : IUndoableCommand ):Boolean;
		
		
		function get canUndo() : Boolean;


		function get canRedo() : Boolean;


		function get undoLevels() : int;


		function get redoLevels() : int;
		
		
		function get eventDispatcher():IEventDispatcher;
		
		
	}
}