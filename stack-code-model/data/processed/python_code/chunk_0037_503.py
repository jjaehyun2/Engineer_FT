package com.epolyakov.async.tasks
{
	import com.epolyakov.async.mocks.MockResult;
	import com.epolyakov.mock.Mock;

	import flash.events.Event;

	import org.flexunit.asserts.assertFalse;
	import org.flexunit.asserts.assertTrue;
	import org.flexunit.async.Async;

	/**
	 * @author Evgeniy Polyakov
	 */
	public class FramesTaskTests
	{
		[Before]
		public function Before():void
		{
			Mock.clear();
		}

		[Test(async, timeout=500)]
		public function await_ShouldWaitWithTheGivenDelay():void
		{
			var result:MockResult = new MockResult();
			var args:Object = {};
			var task:FramesTask = new FramesTask(2);

			task.await(args, result);

			Async.delayCall(this, function ():void
			{
				assertTrue(task.active);
				Mock.verify().total(0);
			}, 1);
			Async.handleEvent(this, result, Event.COMPLETE, function (...rest):void
			{
				assertFalse(task.active);
				Mock.verify().that(result.onReturn(args, task))
						.verify().total(1);
			}, 300);
			Async.failOnEvent(this, result, Event.CANCEL, 400);
		}

		[Test(async, timeout=500)]
		public function cancel_ShouldClearTimeout():void
		{
			var result:MockResult = new MockResult();
			var args:Object = {};
			var task:FramesTask = new FramesTask(2);

			task.await(args, result);

			Async.delayCall(this, function ():void
			{
				assertTrue(task.active);
				Mock.verify().total(0);

				task.cancel();

				assertFalse(task.active);
				Mock.verify().total(0);
			}, 1);
			Async.failOnEvent(this, result, Event.COMPLETE, 400);
			Async.failOnEvent(this, result, Event.CANCEL, 400);
		}

		[Test]
		public function await_zeroDelay_ShouldReturnImmediately():void
		{
			var result:MockResult = new MockResult();
			var args:Object = {};
			var task:FramesTask = new FramesTask(0);

			task.await(args, result);

			Mock.verify().that(result.onReturn(args, task))
					.verify().total(1);
		}

		[Test]
		public function await_negativeDelay_ShouldReturnImmediately():void
		{
			var result:MockResult = new MockResult();
			var args:Object = {};
			var task:FramesTask = new FramesTask(-1);

			task.await(args, result);

			assertFalse(task.active);
			Mock.verify().that(result.onReturn(args, task))
					.verify().total(1);
		}

		[Test]
		public function cancel_ShouldNotThrow():void
		{
			var task:FramesTask = new FramesTask(100);
			task.cancel();
		}
	}
}