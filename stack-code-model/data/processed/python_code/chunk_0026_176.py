package {
  import org.windmill.TestCase;
  public class TestFoo extends TestCase {
    public var order:Array = ['testClick', 'testClickTimeout', 'testWaitCondition', 'testWaitConditionTimeout',
        'testWaitSleep', 'testAssertDisplayObject', 'testWaitDisplayObject', 'testAssertEqualsString',
        'testAssertEqualsNumber', 'testAppPublicInt', 'testAppPublicString', 'testAppPublicArray'];

    public function setup():void {
    }
    public function testClick():void {
      controller.click({id: 'howdyButton'});
    }
    public function testClickTimeout():void {
      controller.click({id: 'howdyButton', timeout: 3000});
    }
    public function testWaitCondition():void {
      var now:Date = new Date();
      var nowTime:Number = now.getTime();
      var thenTime:Number = nowTime + 5000; // Five seconds from now
      waits.forCondition({test: function ():Boolean {
          var dt:Date = new Date();
          var dtTime:Number = dt.getTime();
          // Wait until the current date is greater
          // the thenTime, set above
          return (dtTime > thenTime);
      }});
    }
    public function testWaitConditionTimeout():void {
      waits.forCondition({test: function ():Boolean {
          return false;
      }, timeout: 3000});
    }
    public function testWaitSleep():void {
      waits.sleep({milliseconds: 5000});
    }
    public function testAssertDisplayObject():void {
      asserts.assertDisplayObject({id: 'mainPane'});
    }
    public function testWaitDisplayObject():void {
      waits.forDisplayObject({id: 'mainPanel', timeout: 5000});
    }
    public function testAssertEqualsString():void {
      var foo:String = 'foo';
      asserts.assertEquals('foo', foo);
    }
    public function testAssertEqualsNumber():void {
      var num:int = 2111;
      asserts.assertEquals(2112, num);
    }

    // Test some public properties in the main Flex app class
    public function testAppPublicInt():void {
      var num:int = context.testAppCode.publicInt;
      asserts.assertEquals(2112, num);
    }
    public function testAppPublicString():void {
      var str:String = context.testAppCode.publicString;
      asserts.assertEquals('Geddy Lee', str);
    }
    public function testAppPublicArray():void {
      var arr:Array = context.testAppCode.publicArray;
      asserts.assertEquals('Snow Dog', arr[1]);
    }

    public function teardown():void {
    }
  }
}