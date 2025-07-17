package
{
   import flash.display.DisplayObject;
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.events.ProgressEvent;
   import flash.utils.getDefinitionByName;
   import flash.text.TextField;
 
   [SWF(width="800", height="480", frameRate="20", backgroundColor="0x000000", quality="high", scale="noscale")]
   public class Preloader extends MovieClip
   {
 
       public var loadingBar:LoadingBar = new LoadingBar();
 
       public function Preloader()
       {
           addEventListener(Event.ENTER_FRAME, checkFrame);
           loaderInfo.addEventListener(ProgressEvent.PROGRESS, progress);
           loadingBar.x = stage.stageWidth / 2;
           loadingBar.y = stage.stageHeight / 2;
           addChild(loadingBar);
       }
 
       private function progress(e: ProgressEvent):void
       {
           loadingBar.loadingBar.mask.scaleX = stage.loaderInfo.bytesLoaded/stage.loaderInfo.bytesTotal;
       }
 
       private function checkFrame(e:Event):void
       {
           if (currentFrame == totalFrames)
           {
               removeEventListener(Event.ENTER_FRAME, checkFrame);                
               startup();
           }
       }
 
       private function startup():void
       {
           removeChild(loadingBar);
           stop();
           loaderInfo.removeEventListener(ProgressEvent.PROGRESS, progress);
           var mainClass:Class = getDefinitionByName("Main") as Class;
           addChild(new mainClass() as DisplayObject);
       }
 
   }
 
}