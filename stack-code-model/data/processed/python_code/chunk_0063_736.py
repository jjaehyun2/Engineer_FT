package flexUnitTests.as3.mongo.wire.cursor
{
	import ab.flex.utils.flexunit.signals.AsyncSignalHandler;
	import ab.flex.utils.flexunit.signals.AsyncSignalHandlerEvent;

	import as3.mongo.db.document.Document;
	import as3.mongo.wire.cursor.Cursor;
	import as3.mongo.wire.messages.database.OpReply;
	import as3.mongo.wire.messages.database.OpReplyLoader;

	import flash.net.Socket;
	import flash.utils.ByteArray;

	import mockolate.mock;
	import mockolate.nice;
	import mockolate.runner.MockolateRule;

	import org.flexunit.asserts.assertEquals;
	import org.flexunit.asserts.assertNotNull;
	import org.flexunit.asserts.assertTrue;
	import org.osflash.signals.Signal;
	import org.serialization.bson.Int64;

	public class Cursor_opReplyLoaderSignalsTests
	{
		[Rule]
		public var mocks:MockolateRule       = new MockolateRule();

		[Mock(inject = "false", type = "nice")]
		public var mockOpReplyLoader:OpReplyLoader;

		[Mock(inject = "true", type = "nice")]
		public var mockSocket:Socket;

		private var _cursor:Cursor;
		private var _testLoadedSignal:Signal = new Signal(OpReply);

		[Before]
		public function setUp():void
		{
			mockOpReplyLoader = nice(OpReplyLoader, null, [mockSocket]);
			mock(mockOpReplyLoader).getter("LOADED").returns(_testLoadedSignal);
			_cursor = new Cursor(mockOpReplyLoader);
		}

		[After]
		public function tearDown():void
		{
			_cursor = null;
		}

		[Test(async)]
		public function loadedSignal_onFirstLoadedSignalDispatched_opReplyNumberReturnedStored():void
		{
			var testOpReply:TestOpReply = new TestOpReply(100, mockSocket);
			testOpReply.numberReturned = 5;

			new AsyncSignalHandler(this, _testLoadedSignal, _checkTotalDocumentsLoaded, 5000, testOpReply);

			_testLoadedSignal.dispatch(testOpReply);
		}

		private function _checkTotalDocumentsLoaded(event:AsyncSignalHandlerEvent, passThrough:Object=null):void
		{
			const testOpReply:TestOpReply = passThrough as TestOpReply;
			assertEquals(testOpReply.numberReturned, _cursor.totalDocumentsLoaded);
		}

		[Test(async)]
		public function loadedSignal_onLoadedSignalDispatched_cursorReadySignalIsDispatched():void
		{
			var testOpReply:TestOpReply = new TestOpReply(100, mockSocket);
			testOpReply.numberReturned = 5;

			new AsyncSignalHandler(this, _cursor.cursorReady, _handleCursorReady, 5000, testOpReply);

			_testLoadedSignal.dispatch(testOpReply);
		}

		private function _handleCursorReady(event:AsyncSignalHandlerEvent, passThrough:Object=null):void
		{
			assertTrue(event.getSignalArgument(0) is Cursor);
		}

		[Test(async)]
		public function loadedSignal_onFirstLoadedSignalDispatched_cursorIdIsSet():void
		{
			var testOpReply:TestOpReply = new TestOpReply(100, mockSocket);
			testOpReply.numberReturned = 5;
			const byteArray:ByteArray   = new ByteArray()
			byteArray.writeInt(0);
			byteArray.writeInt(0);
			byteArray.position = 0;
			testOpReply.cursorID = new Int64(byteArray);

			new AsyncSignalHandler(this, _testLoadedSignal, _checkCursorId, 5000, testOpReply);

			_testLoadedSignal.dispatch(testOpReply);
		}

		private function _checkCursorId(event:AsyncSignalHandlerEvent, passThrough:Object=null):void
		{
			const testOpReply:TestOpReply = passThrough as TestOpReply;
			assertEquals(testOpReply.cursorID, _cursor.cursorID);
		}
	}
}