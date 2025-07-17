package wrapperSuite.tests
{
  import luaAlchemy.lua_wrapper;

  import net.digitalprimates.fluint.tests.TestCase;

  public class CommonTestCaseWrapper extends BaseTestCase
  {
    protected var luaState:uint;

    override protected function setUp():void
    {
      luaState = lua_wrapper.luaInitializeState();
    }

    override protected function tearDown():void
    {
      trace("CommonTestCaseWrapper::tearDown(): begin");
      try
      {
        lua_wrapper.luaClose(luaState);
      }
      catch (errObject:Error)
      {
        trace("CommonTestCaseWrapper::tearDown(): error " + errObject.message);
        throw errObject;
      }
      trace("CommonTestCaseWrapper::tearDown(): end");
    }

    protected function doString(
        script:String,
        expected:Array,
        verifyLength:Boolean = true
      ):void
    {
      var stack:Array = lua_wrapper.luaDoString(luaState, script);
      checkLuaResult(expected, stack, verifyLength);
    }

    protected function doStringAsync(
        timeout:Number,
        script:String,
        expected:Array,
        verifyLength:Boolean = true
      ):void
    {
      var settings:Object = new Object();
      settings.expected = expected;
      settings.verifyLength = verifyLength;
      var handler:Function = asyncHandler(
          asyncCallback,
          timeout,
          settings,
          timeOutCallback
        );
      lua_wrapper.luaDoStringAsync(
          function(stack:Array):void
          {
            settings.stack = stack;
            handler(stack, settings);
          },
          luaState,
          script
        );
    }

    protected function doFileAsync(
        timeout:Number,
        filename:String,
        expected:Array,
        verifyLength:Boolean = true
      ):void
    {
      var settings:Object = new Object();
      settings.expected = expected;
      settings.verifyLength = verifyLength;
      var handler:Function = asyncHandler(
          asyncCallback,
          timeout,
          settings,
          timeOutCallback
        );
      lua_wrapper.doFileAsync(
          function(stack:Array):void
          {
            settings.stack = stack;
            handler(stack, settings);
          },
          luaState,
          filename
        );
    }

    protected function asyncCallback(
        stack:Array,
        settings:Object
      ):void
    {
      checkLuaResult(
          settings.expected,
          stack,
          settings.verifyLength
        );
    }

    protected function timeOutCallback(settings:Object):void
    {
      if (settings.stack) // TODO: WTF?!
      {
        checkLuaResult(
            settings.expected,
            settings.stack,
            settings.verifyLength
          );
      }
      else
      {
        fail("timed out");
      }
    }
  }
}