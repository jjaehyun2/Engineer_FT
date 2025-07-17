package
{
   import Array;
   
   import GraffitiTouchUnitTests.GraffitiTouchSuite;
   
   import flash.display.Sprite;
   import flash.display.StageAlign;
   import flash.display.StageAspectRatio;
   import flash.display.StageScaleMode;
   
   import flexunit.flexui.FlexUnitTestRunnerUIASMobile;
   
   public class FlexUnitApplication extends Sprite
   {
      public function FlexUnitApplication()
      {
         stage.align = StageAlign.TOP_LEFT;
         stage.scaleMode = StageScaleMode.NO_BORDER;
         stage.setAspectRatio(StageAspectRatio.PORTRAIT);
         onCreationComplete();
      }
      
      private function onCreationComplete():void
      {
         var testRunner:FlexUnitTestRunnerUIASMobile=new FlexUnitTestRunnerUIASMobile(stage.fullScreenWidth, stage.fullScreenHeight);
         testRunner.portNumber=8765; 
         this.addChild(testRunner); 
         testRunner.runWithFlexUnit4Runner(currentRunTestSuite(), "GraffitiTouchTests");
      }
      
      public function currentRunTestSuite():Array
      {
         var testsToRun:Array = new Array();
         testsToRun.push(GraffitiTouchUnitTests.GraffitiTouchSuite);
         return testsToRun;
      }
   }
}