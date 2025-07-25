package visuals.ui.elements.guild
{
   import com.playata.framework.display.Sprite;
   import com.playata.framework.display.lib.flash.FlashDisplayObjectContainer;
   import com.playata.framework.display.lib.flash.FlashSprite;
   import flash.display.MovieClip;
   
   public class SymbolGuildStatBarBackgroundGeneric extends Sprite
   {
       
      
      private var _nativeObject:SymbolGuildStatBarBackground = null;
      
      public function SymbolGuildStatBarBackgroundGeneric(param1:MovieClip = null)
      {
         if(param1)
         {
            _nativeObject = param1 as SymbolGuildStatBarBackground;
         }
         else
         {
            _nativeObject = new SymbolGuildStatBarBackground();
         }
         super(null,FlashSprite.fromNative(_nativeObject));
         var _loc2_:FlashDisplayObjectContainer = _sprite as FlashDisplayObjectContainer;
      }
      
      public function setNativeInstance(param1:SymbolGuildStatBarBackground) : void
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