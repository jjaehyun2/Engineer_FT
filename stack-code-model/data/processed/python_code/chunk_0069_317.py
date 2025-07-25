package visuals.ui.elements.booster
{
   import com.playata.framework.display.Sprite;
   import com.playata.framework.display.lib.flash.FlashDisplayObjectContainer;
   import com.playata.framework.display.lib.flash.FlashSprite;
   import flash.display.MovieClip;
   
   public class SymbolBoosterType2Strength1Generic extends Sprite
   {
       
      
      private var _nativeObject:SymbolBoosterType2Strength1 = null;
      
      public function SymbolBoosterType2Strength1Generic(param1:MovieClip = null)
      {
         if(param1)
         {
            _nativeObject = param1 as SymbolBoosterType2Strength1;
         }
         else
         {
            _nativeObject = new SymbolBoosterType2Strength1();
         }
         super(null,FlashSprite.fromNative(_nativeObject));
         var _loc2_:FlashDisplayObjectContainer = _sprite as FlashDisplayObjectContainer;
      }
      
      public function setNativeInstance(param1:SymbolBoosterType2Strength1) : void
      {
         FlashSprite.setNativeInstance(_sprite,param1);
         _nativeObject = param1;
         syncInstances();
      }
      
      public function syncInstances() : void
      {
      }
   }
}