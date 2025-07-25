package visuals.ui.elements.tutorial
{
   import com.playata.framework.display.MovieClip;
   import com.playata.framework.display.lib.flash.FlashDisplayObjectContainer;
   import com.playata.framework.display.lib.flash.FlashMovieClip;
   
   public class SymbolTutorialArrowGeneric extends com.playata.framework.display.MovieClip
   {
       
      
      private var _nativeObject:SymbolTutorialArrow = null;
      
      public var message:SymbolTutorialMessageBoxGeneric = null;
      
      public var arrow:SymbolTutorialArrowAnimationGeneric = null;
      
      public function SymbolTutorialArrowGeneric(param1:flash.display.MovieClip = null)
      {
         if(param1)
         {
            _nativeObject = param1 as SymbolTutorialArrow;
         }
         else
         {
            _nativeObject = new SymbolTutorialArrow();
         }
         super(null,FlashMovieClip.fromNative(_nativeObject));
         var _loc2_:FlashDisplayObjectContainer = _sprite as FlashDisplayObjectContainer;
         message = new SymbolTutorialMessageBoxGeneric(_nativeObject.message);
         arrow = new SymbolTutorialArrowAnimationGeneric(_nativeObject.arrow);
      }
      
      public function setNativeInstance(param1:SymbolTutorialArrow) : void
      {
         FlashMovieClip.setNativeInstance(_movieClip,param1);
         _nativeObject = param1;
         syncInstances();
      }
      
      override public function play() : void
      {
         super.play();
         syncInstances();
      }
      
      override public function stop() : void
      {
         super.stop();
         syncInstances();
      }
      
      override public function gotoAndStop(param1:Object) : void
      {
         super.gotoAndStop(param1);
         syncInstances();
      }
      
      override public function gotoAndPlay(param1:Object) : void
      {
         _movieClip.gotoAndPlay(param1);
         syncInstances();
      }
      
      public function syncInstances() : void
      {
         if(_nativeObject.message)
         {
            message.setNativeInstance(_nativeObject.message);
         }
         if(_nativeObject.arrow)
         {
            arrow.setNativeInstance(_nativeObject.arrow);
         }
      }
   }
}