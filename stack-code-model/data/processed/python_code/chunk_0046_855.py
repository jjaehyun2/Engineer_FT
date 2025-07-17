package asunit.runners {

    import asunit.framework.IResult;
    import asunit.framework.LegacyTestIterator;
    import asunit.framework.Result;
    import asunit.framework.TestCase;
    import asunit.support.LegacyTestCase;

    import flash.events.Event;
    import asunit.framework.CallbackBridge;

    public class LegacyRunnerTest extends TestCase {

        private var testRunner:LegacyRunner;

        public function LegacyRunnerTest(methodName:String=null) {
            super(methodName)
        }

        override protected function setUp():void {
            super.setUp();
            LegacyTestCase.callCount = 0;
            testRunner = new LegacyRunner();
        }

        override protected function tearDown():void {
            super.tearDown();
            testRunner = null;
        }

        public function testSimpleSubclass():void {
            var handler:Function = function(event:Event):void {
                assertEquals(0, testRunner.bridge.failureCount);
                assertEquals(2, testRunner.bridge.runCount);
            };
            testRunner.addEventListener(Event.COMPLETE, addAsync(handler));
            testRunner.run(LegacyTestCase);
        }
    }
}