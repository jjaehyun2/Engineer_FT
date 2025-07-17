/*
 * Copyright (c) 2012 the original author or authors
 *
 * Permission is hereby granted to use, modify, and distribute this file
 * in accordance with the terms of the license agreement accompanying it.
 */
package tests
{

	import org.flexunit.asserts.assertEquals;
	import org.flexunit.asserts.assertFalse;
	import org.flexunit.asserts.assertNotNull;
	import org.flexunit.asserts.assertTrue;
	import org.robotlegs.utilities.undoablecommand.CommandHistory;
	import org.robotlegs.utilities.undoablecommand.interfaces.ICommandHistory;

	/**
	 * @private
	 */
	public class TestHistory
	{

		private var history : ICommandHistory;

		private var command1 : MockUndoableCommand;

		private var command2 : MockUndoableCommand;


		[Before]
		public function runBeforeEachTest() : void
		{
			history = new CommandHistory();
			command1 = new MockUndoableCommand();
			command2 = new MockUndoableCommand();
		}


		[After]
		public function runAfterEachTest() : void
		{
			history = null;
			command1 = null;
			command2 = null;
		}


		[Test]
		public function testConstructor() : void
		{
			assertNotNull("constructor fail", history);
		}


		[Test]
		public function testInitialState() : void
		{
			assertFalse("initial state canUndo fails", history.canUndo);
			assertFalse("initial state canRedo fails", history.canRedo);
		}


		[Test]
		public function testAdd() : void
		{
			history.add(command1);
			assertTrue("canUndo fails after add", history.canUndo);
			assertFalse("canRedo fails after add", history.canRedo);
		}


		[Test]
		public function isAdded() : void
		{
			history.add(command1);
			assertTrue("isAdded fails after add", history.isAdded(command1));
		}


		[Test]
		public function isAddedAfterUndo() : void
		{
			history.add(command1);
			history.undo();
			assertTrue("isAdded fails after add", history.isAdded(command1));
		}


		[Test]
		public function addClearsRedo() : void
		{
			history.add(command1);
			history.undo();
			history.add(command2);
			assertEquals("test add clears redo, num redos fails", 0, history.redoLevels);
		}
		

		[Test]
		public function testCantAddNull() : void
		{
			history.add(null);
			assertFalse("canUndo fails after add null", history.canUndo);
		}


		[Test (expects="flash.errors.IllegalOperationError")]
		public function testCantAddCommandTwice() : void
		{
			history.add(command1);
			history.add(command1);
		}


		[Test]
		public function testAddUndo() : void
		{
			history.add(command1);
			history.undo();
			assertFalse("canUndo fails after add, undo", history.canUndo);
			assertTrue("canRedo fails after add, undo", history.canRedo);
			assertEquals("command state fail after add, undo", MockUndoableCommand.UNDONE, command1.state);
		}


		[Test]
		public function testAddUndoRedo() : void
		{
			history.add(command1);
			history.undo();
			history.redo();
			assertTrue("canUndo fails after add, undo, redo", history.canUndo);
			assertFalse("canRedo fails after add, undo, redo", history.canRedo);
			assertEquals("command state fail after add, undo", MockUndoableCommand.DONE, command1.state);
		}


		[Test]
		public function testAddTwo() : void
		{
			history.add(command1);
			history.add(command2);
			assertEquals("num undos fail after add two", 2, history.undoLevels);
		}


		[Test]
		public function testUndoTwo() : void
		{
			history.add(command1);
			history.add(command2);
			history.undo(2);
			assertEquals("num undos fail after add two, undo two", 0, history.undoLevels);
			assertEquals("num redos fail after add two, undo two", 2, history.redoLevels);
		}
		
		[Test]
		public function testClear():void
		{
			history.add(command1);
			history.add(command2);
			history.undo();
			history.clear();
			assertFalse("canUndo fails after clear", history.canUndo);
			assertFalse("canRedo fails after clear", history.canRedo);
		}
	}
}