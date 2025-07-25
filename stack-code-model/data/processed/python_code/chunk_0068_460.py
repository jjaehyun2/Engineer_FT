package visuals.ui.elements.battle
{
   import com.playata.framework.display.Sprite;
   import com.playata.framework.display.lib.flash.FlashDisplayObjectContainer;
   import com.playata.framework.display.lib.flash.FlashSprite;
   import flash.display.MovieClip;
   
   public class SymbolBattleAvatarEmoteIconSwirl2Generic extends Sprite
   {
       
      
      private var _nativeObject:SymbolBattleAvatarEmoteIconSwirl2 = null;
      
      public function SymbolBattleAvatarEmoteIconSwirl2Generic(param1:MovieClip = null)
      {
         if(param1)
         {
            _nativeObject = param1 as SymbolBattleAvatarEmoteIconSwirl2;
         }
         else
         {
            _nativeObject = new SymbolBattleAvatarEmoteIconSwirl2();
         }
         super(null,FlashSprite.fromNative(_nativeObject));
         var _loc2_:FlashDisplayObjectContainer = _sprite as FlashDisplayObjectContainer;
      }
      
      public function setNativeInstance(param1:SymbolBattleAvatarEmoteIconSwirl2) : void
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