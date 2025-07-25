package wrapperSuite.tests
{
  import luaAlchemy.LuaAlchemy;

  import flash.utils.ByteArray;

  import mx.containers.Canvas;
  import mx.utils.ObjectUtil;

  import net.digitalprimates.fluint.tests.TestCase;

  // TODO: Hack! This suite is just copy-pasted from TestSugar.as
  //       Generalize code instead!
  //
  public class TestSugarAutoconvert extends SugarLuaAlchemyTestCase
  {
    public function testSugarIsLoaded():void
    {
      var script:String = ( <![CDATA[
        assert(as3.class ~= nil)
      ]]> ).toString();

      doString(script, [true])
    }

    public function testAS3AutoconversionSettings():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        assert(as3.isas3value(as3.class.Array.new().length))

        as3.enable_sugar_autoconversion()

        assert(as3.is_sugar_autoconversion_enabled())
        assert(not as3.isas3value(as3.class.Array.new().length))

        as3.disable_sugar_autoconversion()

        assert(not as3.is_sugar_autoconversion_enabled())
        assert(as3.isas3value(as3.class.Array.new().length))

        as3.enable_sugar_autoconversion(true)

        assert(as3.is_sugar_autoconversion_enabled())
        assert(not as3.isas3value(as3.class.Array.new().length))

        as3.enable_sugar_autoconversion(false)

        assert(not as3.is_sugar_autoconversion_enabled())
        assert(as3.isas3value(as3.class.Array.new().length))
      ]]> ).toString();

      doString(script, [true]);
    }

    public function testNewInstance():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local v = as3.class.wrapperSuite.tests.TestWrapperHelper.new()
        return as3.type(v)
      ]]> ).toString();

      doString(script, [true, "wrapperSuite.tests::TestWrapperHelper"]);
    }

    public function testSetGetInstance():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local v = as3.class.wrapperSuite.tests.TestWrapperHelper.new()
        v.string2 = "hello"
        return as3.tolua(v.string2)
      ]]> ).toString();

      doString(script, [true, "hello"]);
    }

    public function testCallInstanceNoReturn():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local v = as3.class.wrapperSuite.tests.TestWrapperHelper.new()
        v.setNameAge("OldDude", 999)
        return as3.tolua(v.nameAge)
      ]]> ).toString();

      doString(script, [true, "Name: OldDude age: 999"]);
    }

    public function testCallInstanceNoReturnMultibyte():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local v = as3.class.wrapperSuite.tests.TestWrapperHelper.new()
        v.setNameAge("Александр Сергеевич ПУШКИН", 38)
        return as3.tolua(v.nameAge)
      ]]> ).toString();

      doString(script, [true, "Name: Александр Сергеевич ПУШКИН age: 38"]);
    }

    public function testCallInstanceReturnNumber():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local v = as3.class.wrapperSuite.tests.TestWrapperHelper.new()
        return v.addTwoNumbers(13, 5)
      ]]> ).toString();

      doString(script, [true, 18]);
    }

    public function testClassStaticClass():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.tolua(as3.class.wrapperSuite.tests.TestWrapperHelper.class().TEST_WRAPPER_HELPER_EVENT)
      ]]> ).toString();

      doString(script, [true, "TestWrapperHelperEvent"]);
    }

    public function testClassStaticNoClass():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.tolua(as3.class.wrapperSuite.tests.TestWrapperHelper.TEST_WRAPPER_HELPER_EVENT)
      ]]> ).toString();

      doString(script, [true, "TestWrapperHelperEvent"]);
    }

    public function testClassVar():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local v = as3.class.String.class()
        return as3.type(v)
      ]]> ).toString();

      doString(script, [true, "String"]);
    }

    public function testClassStaticFunctionWithReturnClass():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local r = as3.class.wrapperSuite.tests.TestWrapperHelper.class().staticNameAge("Bubba Joe Bob Brain", 7)
        return as3.tolua(r)
      ]]> ).toString();

      doString(script, [true, "Name: Bubba Joe Bob Brain age: 7"]);
    }

    public function testClassStaticFunctionWithReturnNoClass():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local r = as3.class.wrapperSuite.tests.TestWrapperHelper.staticNameAge("Bubba Joe Bob Brain", 7)
        return as3.tolua(r)
      ]]> ).toString();

      doString(script, [true, "Name: Bubba Joe Bob Brain age: 7"]);
    }

    public function testClassSetStaticVarClass():void
    {
      TestWrapperHelper.staticString = "Some String"
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local oldStr = as3.tolua(as3.class.wrapperSuite.tests.TestWrapperHelper.class().staticString)
        as3.class.wrapperSuite.tests.TestWrapperHelper.class().staticString = "A New String"
        local newStr = as3.tolua(as3.class.wrapperSuite.tests.TestWrapperHelper.class().staticString)
        return oldStr, newStr
      ]]> ).toString();

      doString(script, [true, "Some String", "A New String"]);
    }

    public function testClassSetStaticVarNoClass():void
    {
      TestWrapperHelper.staticString = "Some String"
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local oldStr = as3.tolua(as3.class.wrapperSuite.tests.TestWrapperHelper.staticString)
        as3.class.wrapperSuite.tests.TestWrapperHelper.staticString = "A New String"
        local newStr = as3.tolua(as3.class.wrapperSuite.tests.TestWrapperHelper.staticString)
        return oldStr, newStr
      ]]> ).toString();

      doString(script, [true, "Some String", "A New String"]);
    }

    public function testClassStaticFunctionNoReturnClass():void
    {
      TestWrapperHelper.staticString = "Start String"
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local oldStr = as3.tolua(as3.class.wrapperSuite.tests.TestWrapperHelper.class().staticString)
        as3.class.wrapperSuite.tests.TestWrapperHelper.class().setStaticString("Totally different string")
        local newStr = as3.tolua(as3.class.wrapperSuite.tests.TestWrapperHelper.class().staticString)
        return oldStr, newStr
      ]]> ).toString();

      doString(script, [true, "Start String", "Totally different string"]);
    }

    public function testClassStaticFunctionNoReturnNoClass():void
    {
      TestWrapperHelper.staticString = "Start String"
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local oldStr = as3.tolua(as3.class.wrapperSuite.tests.TestWrapperHelper.staticString)
        as3.class.wrapperSuite.tests.TestWrapperHelper.setStaticString("Totally different string")
        local newStr = as3.tolua(as3.class.wrapperSuite.tests.TestWrapperHelper.staticString)
        return oldStr, newStr
      ]]> ).toString();

      doString(script, [true, "Start String", "Totally different string"]);
    }

    /*
    // TODO: Need a better test case.
    //       This is broken due to auto-conversion to string
    public function testNamespaceFunction():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.type(as3.namespace.flash.utils.getQualifiedClassName("foo"))
      ]]> ).toString();

      doString(script, [true, "String"]);
    }
    */

    public function testOnClose():void
    {
      TestWrapperHelper.staticString = "Start String"
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        as3.onclose(
          function()
            as3.class.wrapperSuite.tests.TestWrapperHelper.staticString = "Closed"
          end)
      ]]> ).toString();

      doString(script, [true]);
      assertEquals("Start String", TestWrapperHelper.staticString);

      myLuaAlchemy.close()
      assertEquals("Closed", TestWrapperHelper.staticString);
    }

    public function testMakePrinter():void
    {
      var printer:Object = new Object();
      printer.text = "First line\n";
      myLuaAlchemy.setGlobal("printer", printer);

      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        print = as3.makeprinter(printer)
        print("Second line", 1, nil, 2, false)
      ]]> ).toString();

      doString(script, [true]);

      assertEquals("First line\nSecond line\t1\tnil\t2\tfalse\n", printer.text);
    }

    public function testPrintS():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.prints("Second line", 1, nil, 2, false)
      ]]> ).toString();

      doString(script, [true, "Second line\t1\tnil\t2\tfalse"]);
    }

    /*
    // TODO: Need a better test case.
    //       This is broken due to auto-conversion to string
    public function testChainSugarCalls():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.class.String.new("Test Chain").toUpperCase().toLowerCase()
      ]]> ).toString();

      doString(script, [true, "test chain"]);
    }
    */

    public function testNewStillReturnsAS3():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        assert(as3.isas3value(as3.class.String.new("Test Chain")))
      ]]> ).toString();

      doString(script, [true]);
    }

    /*
    // TODO: Need a better test case.
    //       This is broken due to auto-conversion to string
    public function testChainSugarCallGet():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        assert(
            as3.class.String.new("Test Chain").toUpperCase().length == 10          )
      ]]> ).toString();

      doString(script, [true]);
    }
    */

    /*
    // TODO: Need a better test case here, with object property,
    //       so that it would not get autoconverted.
    public function testChainSugarCallsOnGet():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.class.Array.new().length.toString()
      ]]> ).toString();

      doString(script, [true, "0"]);
    }
    */
    public function testToObjectSimpleTypes():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return
          as3.toobject(),
          as3.toobject(nil),
          as3.toobject(false),
          as3.toobject(42),
          as3.toobject("LuaAlchemy"),
          as3.toobject(coroutine.create(function() end)),
          as3.toobject(newproxy()),
          as3.toobject(as3.new("Number", 1))
      ]]> ).toString();

      doString(
          script,
          [
            true,
            null,
            null,
            false,
            42,
            "LuaAlchemy",
            "thread", // TODO: Should be black box
            "userdata", // TODO: Should be black box
            1
          ]
        );
    }

    public function testToObjectFunction():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.toobject(function() return 42 end)
      ]]> ).toString();

      var stack:Array = myLuaAlchemy.doString(script);

      assertEquals("stack length", 2, stack.length);
      assertTrue("success", stack[0]);
      assertTrue("returned Function", stack[1] is Function)

      assertEquals("return check", 42, stack[1]())
    }

    public function testToObjectEmptyTable():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.toobject({})
      ]]> ).toString();

      var stack:Array = myLuaAlchemy.doString(script);

      var expected:Object = new Object;
      var obj:Object = stack[1];

      assertEquals("stack length", 2, stack.length);
      assertTrue("success", stack[0]);
      assertTrue("returned Object", stack[1] is Object)

      assertTrue("return check", ObjectUtil.compare(expected, obj) == 0)
    }

    public function testToObjectSimpleTable():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.toobject({ a = 1, b = "c" })
      ]]> ).toString();

      var stack:Array = myLuaAlchemy.doString(script);

      var expected:Object = new Object;
      expected.a = 1;
      expected.b = "c";

      assertEquals("stack length", 2, stack.length);
      assertTrue("success", stack[0]);
      assertTrue("returned Object", stack[1] is Object)

      var obj:Object = stack[1];

      assertTrue("return check", ObjectUtil.compare(expected, obj) == 0)
    }

    public function testToObjectNestedTable():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.toobject({ a = { b = "c" } })
      ]]> ).toString();

      var stack:Array = myLuaAlchemy.doString(script);

      var expected:Object = new Object;
      expected.a = new Object;
      expected.a.b = "c"

      assertEquals("stack length", 2, stack.length);
      assertTrue("success", stack[0]);
      assertTrue("returned Object", stack[1] is Object)

      var obj:Object = stack[1];

      assertTrue("return check", ObjectUtil.compare(expected, obj) == 0)
    }

    public function testToObjectTableReference():void
    {
      // Note the way this is different from recursive table case
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local t = { b = "c" }
        return as3.toobject({ a = t, z = t })
      ]]> ).toString();

      var stack:Array = myLuaAlchemy.doString(script);

      var expected:Object = new Object;
      expected.a = new Object;
      expected.a.b = "c"
      expected.z = new Object;
      expected.z.b = "c"

      assertEquals("stack length", 2, stack.length);
      assertTrue("success", stack[0]);
      assertTrue("returned Object", stack[1] is Object)

      var obj:Object = stack[1];

      assertTrue("return check", ObjectUtil.compare(expected, obj) == 0)
      assertTrue(
          "tables references are separated",
          obj.a !== obj.b
        )
    }

    public function testToObjectBadKey():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.toobject({ [function() end] = 2 })
      ]]> ).toString();

      doString(script, [false, "builtin://lua_alchemy/as3/toobject.lua:19: unsupported key type\nstack traceback:\n\t[C]: in function 'error'\n\tbuiltin://lua_alchemy/as3/toobject.lua:19: in function <builtin://lua_alchemy/as3/toobject.lua:7>\n\t(tail call): ?\n\t(tail call): ?"]);
    }

    public function testToObjectNoNumericKeyConversion():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.toobject({ [1] = 2 })
      ]]> ).toString();

      doString(script, [false, "builtin://lua_alchemy/as3/toobject.lua:19: unsupported key type\nstack traceback:\n\t[C]: in function 'error'\n\tbuiltin://lua_alchemy/as3/toobject.lua:19: in function <builtin://lua_alchemy/as3/toobject.lua:7>\n\t(tail call): ?\n\t(tail call): ?"]);
    }

    public function testToObjectRecursion():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local t = {}
        t.t = t
        return as3.toobject(t)
      ]]> ).toString();

      doString(script, [false, "builtin://lua_alchemy/as3/toobject.lua:22: recursion detected\nstack traceback:\n\t[C]: in function 'assert'\n\tbuiltin://lua_alchemy/as3/toobject.lua:22: in function 'impl'\n\tbuiltin://lua_alchemy/as3/toobject.lua:25: in function <builtin://lua_alchemy/as3/toobject.lua:7>\n\t(tail call): ?\n\t(tail call): ?"]);
    }

    public function testToArraySimpleTypes():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return
          as3.toarray(),
          as3.toarray(nil),
          as3.toarray(false),
          as3.toarray(42),
          as3.toarray("LuaAlchemy"),
          as3.toarray(coroutine.create(function() end)),
          as3.toarray(newproxy()),
          as3.toarray(as3.new("Number", 1))
      ]]> ).toString();

      doString(
          script,
          [
            true,
            null,
            null,
            false,
            42,
            "LuaAlchemy",
            "thread", // TODO: Should be black box
            "userdata", // TODO: Should be black box
            1
          ]
        );
    }

    public function testToArrayFunction():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.toarray(function() return 42 end)
      ]]> ).toString();

      var stack:Array = myLuaAlchemy.doString(script);

      assertEquals("stack length", 2, stack.length);
      assertTrue("success", stack[0]);
      assertTrue("returned Function", stack[1] is Function)

      assertEquals("return check", 42, stack[1]())
    }

    public function testToArrayEmptyTable():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.toarray({})
      ]]> ).toString();

      var stack:Array = myLuaAlchemy.doString(script);

      var expected:Array = new Array;
      var obj:Array = stack[1];

      assertEquals("stack length", 2, stack.length);
      assertTrue("success", stack[0]);
      assertTrue("returned Array", stack[1] is Array)

      assertTrue("return check", ObjectUtil.compare(expected, obj) == 0)
    }

    public function testToArraySimpleTable():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.toarray({ [1] = 1, [2] = "c" })
      ]]> ).toString();

      var stack:Array = myLuaAlchemy.doString(script);

      var expected:Array = new Array;
      expected[0] = 1;
      expected[1] = "c";

      assertEquals("stack length", 2, stack.length);
      assertTrue("success", stack[0]);
      assertTrue("returned Array", stack[1] is Array)

      var obj:Array = stack[1];

      assertTrue("return check", ObjectUtil.compare(expected, obj) == 0)
    }

    public function testToArrayTableHoles():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.toarray({ [1] = "one", [1000] = 1 })
      ]]> ).toString();

      var stack:Array = myLuaAlchemy.doString(script);

      var expected:Array = new Array;
      expected[0] = "one";
      // key 1000 is ignored per ipairs rules

      assertEquals("stack length", 2, stack.length);
      assertTrue("success", stack[0]);
      assertTrue("returned Array", stack[1] is Array)

      var obj:Array = stack[1];

      assertTrue("return check", ObjectUtil.compare(expected, obj) == 0)
    }

    public function testToArrayNestedTable():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.toarray({ [1] = { [1] = "c" } })
      ]]> ).toString();

      var stack:Array = myLuaAlchemy.doString(script);

      var expected:Array = new Array;
      expected[0] = new Array;
      expected[0][0] = "c"

      assertEquals("stack length", 2, stack.length);
      assertTrue("success", stack[0]);
      assertTrue("returned Array", stack[1] is Array)

      var obj:Array = stack[1];

      assertTrue("return check", ObjectUtil.compare(expected, obj) == 0)
    }

    public function testToArrayTableReference():void
    {
      // Note the way this is different from recursive table case
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local t = { [1] = "c" }
        return as3.toarray({ [1] = t, [2] = t })
      ]]> ).toString();

      var stack:Array = myLuaAlchemy.doString(script);

      var expected:Array = new Array;
      expected[0] = new Array;
      expected[0][0] = "c"
      expected[1] = new Array;
      expected[1][0] = "c"

      assertEquals("stack length", 2, stack.length);
      assertTrue("success", stack[0]);
      assertTrue("returned Array", stack[1] is Array)

      var obj:Array = stack[1];

      assertTrue("return check", ObjectUtil.compare(expected, obj) == 0)
      assertTrue(
          "tables references are separated",
          obj[0] !== obj[1]
        )
    }

    public function testToArrayBadKeyIgnored():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.toarray({ [1] = "one", [function() end] = 2 })
      ]]> ).toString();

      var stack:Array = myLuaAlchemy.doString(script);

      var expected:Array = new Array;
      expected[0] = "one";

      assertEquals("stack length", 2, stack.length);
      assertTrue("success", stack[0]);
      assertTrue("returned Array", stack[1] is Array)

      var obj:Array = stack[1];

      assertTrue("return check", ObjectUtil.compare(expected, obj) == 0)
     }

    public function testToArrayNoStringKeyConversion():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        return as3.toarray({ [1] = "one", ["2"] = "two" })
      ]]> ).toString();

      var stack:Array = myLuaAlchemy.doString(script);

      var expected:Array = new Array;
      expected[0] = "one";
      // key "2" (note it is a string) is ignored per ipairs() rules

      assertEquals("stack length", 2, stack.length);
      assertTrue("success", stack[0]);
      assertTrue("returned Array", stack[1] is Array)

      var obj:Array = stack[1];

      assertTrue("return check", ObjectUtil.compare(expected, obj) == 0)
    }

    public function testToArrayRecursion():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local t = {}
        t[1] = t
        return as3.toarray(t)
      ]]> ).toString();

      doString(script, [false, "builtin://lua_alchemy/as3/toobject.lua:49: recursion detected\nstack traceback:\n\t[C]: in function 'assert'\n\tbuiltin://lua_alchemy/as3/toobject.lua:49: in function 'impl'\n\tbuiltin://lua_alchemy/as3/toobject.lua:52: in function <builtin://lua_alchemy/as3/toobject.lua:42>\n\t(tail call): ?\n\t(tail call): ?"]);
    }

    public function testPrintOverload():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        print("LuaAlchemy", true, nil, 42)
      ]]> ).toString();

      // TODO: How to detect that as3.trace() was actually called?

      doString(script, [true]);
    }

    // TODO: Test advanced functionality when flyield() issue would be resolved
    public function testLoadfileOverload():void
    {
      var file:String = ( <![CDATA[
        MY_GLOBAL_VARIABLE = 42
        return 7
        ]]> ).toString();
      var luaAsset:ByteArray = new ByteArray();
      luaAsset.writeUTFBytes(file);

      myLuaAlchemy.supplyFile("builtin://myFile.lua", luaAsset);

      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        assert(MY_GLOBAL_VARIABLE == nil)
        local fn = assert(loadfile("myFile.lua"))
        assert(MY_GLOBAL_VARIABLE == nil)
        assert(fn() == 7)
        assert(MY_GLOBAL_VARIABLE == 42)
      ]]> ).toString();

      doString(script, [true]);
    }

    // TODO: Test advanced functionality when flyield() issue would be resolved
    public function testDofileOverload():void
    {
      var file:String = ( <![CDATA[
        MY_GLOBAL_VARIABLE = 42
        return 7
        ]]> ).toString();
      var luaAsset:ByteArray = new ByteArray();
      luaAsset.writeUTFBytes(file);

      myLuaAlchemy.supplyFile("builtin://myFile.lua", luaAsset);

      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        assert(MY_GLOBAL_VARIABLE == nil)
        assert(dofile("myFile.lua") == 7)
        assert(MY_GLOBAL_VARIABLE == 42)
      ]]> ).toString();

      doString(script, [true]);
    }

    public function testAS3AutoconversionNumber():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local v = as3.class.wrapperSuite.tests.TestWrapperHelper.new()

        -- Sanity checks
        assert(as3.tolua(v.forty) == 40, "forty: tolua value")
        assert(as3.tolua(v.two) == 2, "two: tolua value")

        assert(as3.isas3value(v), "v is as3 value")
        assert(not as3.isas3value(v.forty), "forty is not as3 value")
        assert(not as3.isas3value(v.two), "forty is not as3 value")

        assert(type(v.forty) == "number", "forty is a Lua number")
        assert(type(v.two) == "number", "two is a Lua number")

        assert(v.forty == 40, "forty: raw equality")
        assert(v.two == 2, "two: raw equality")
        assert(v.forty + v.two == 42, "forty + two works")
        assert(v.forty + 2 == 42, "forty + 2 works")
        assert(40 + v.two == 42, "40 + two works")
      ]]> ).toString();

      doString(script, [true]);
    }

    public function testAS3AutoconversionCallObject():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        assert(
            as3.class.wrapperSuite.tests.TestWrapperHelper.new().addTwoNumbers(
                40, 2
              )
            == 42,
            "call returns number"
          )
      ]]> ).toString();

      doString(script, [true]);
    }

    public function testAS3AutoconversionCallStatic():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        assert(
            as3.class.wrapperSuite.tests.TestWrapperHelper.staticNameAge(
                "Yoda", 900
              )
            == "Name: Yoda age: 900",
            "static call returns string"
          )
      ]]> ).toString();

      doString(script, [true]);
    }

    public function testAS3AutoconversionCallNamespace():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        assert(
            as3.namespace.flash.utils.getQualifiedClassName("foo") == "String",
            "namespace call returns Lua value"
          )
      ]]> ).toString();

      doString(script, [true]);
    }

    public function testAS3AutoconversionStaticClassMember():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        as3.class.wrapperSuite.tests.TestWrapperHelper.setStaticString("A")

        assert(
            as3.class.wrapperSuite.tests.TestWrapperHelper.staticString
              == "A",
            "static string is Lua value"
          )
      ]]> ).toString();

      doString(script, [true]);
    }

    public function testAS3AutoconversionBadStaticClassMember():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        assert(
            -- Just triggering __index
            as3.class.wrapperSuite.tests.TestWrapperHelper.badmembername ~= { }
          )
      ]]> ).toString();

      doString(script, [true]);
    }

    public function testAS3AutoconversionBadClassName():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        assert(
            as3.class.badclassname ~= { } -- Just triggering __index
          )

        assert(
            as3.class.badclassname.whoa ~= { } -- Just triggering __index
          )
      ]]> ).toString();

      doString(script, [true]);
    }

    public function testAS3AutoconversionString():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local v = as3.class.wrapperSuite.tests.TestWrapperHelper.new()

        v.string1 = "forty"
        v.string2 = "two"

        assert(v.string1 == "forty", "string1 is a lua value")
        assert(v.string2 == "two", "string2 is a lua value")

        assert(v.concat1And2() == "fortytwo", "function call returns string")

        assert(
            v.string1 .. " " .. v.string2 == "forty two", "concat works"
          )
      ]]> ).toString();

      doString(script, [true]);
    }

    public function testFunctionValue():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local v = as3.class.wrapperSuite.tests.TestWrapperHelper.new()

        local f = assert(v.getFortyTwoFn())

        assert(as3.isas3value(f))

        assert(f() == 42)
        assert(f() == 42) -- again
      ]]> ).toString();

      doString(script, [true]);
    }

    public function testIterator():void
    {
      var script:String = ( <![CDATA[
        assert(not as3.is_sugar_autoconversion_enabled())
        as3.enable_sugar_autoconversion()

        local v = as3.class.wrapperSuite.tests.TestWrapperHelper.new()

        v.vec.push("forty")
        v.vec.push("two")

        do
          local t = { }
          for val in v.listIter() do
            t[#t + 1] = val
          end

          assert(#t == 2)
          assert(t[1] == "forty")
          assert(t[2] == "two")
        end

        -- Repeat to ensure that iterator works ok
        do
          local t = { }
          for val in v.listIter() do
            t[#t + 1] = val:reverse()

            for val in v.listIter() do
              t[#t + 1] = val
            end
          end

          assert(#t == 6)
          assert(t[1] == "ytrof")
          assert(t[2] == "forty")
          assert(t[3] == "two")
          assert(t[4] == "owt")
          assert(t[5] == "forty")
          assert(t[6] == "two")
        end
      ]]> ).toString();

      doString(script, [true]);
    }
  }
}