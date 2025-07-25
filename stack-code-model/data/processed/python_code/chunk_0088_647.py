package visuals.ui.elements.buttons
{
   import com.playata.framework.display.Sprite;
   import com.playata.framework.display.lib.flash.FlashDisplayObjectContainer;
   import com.playata.framework.display.lib.flash.FlashLabel;
   import com.playata.framework.display.lib.flash.FlashSprite;
   import com.playata.framework.display.ui.controls.ILabel;
   import flash.display.MovieClip;
   
   public class SymbolButtonSmallTabTabbedWhiteGeneric extends Sprite
   {
       
      
      private var _nativeObject:SymbolButtonSmallTabTabbedWhite = null;
      
      public var symbolButtonSmallTabTabbedBackgroundWhite:SymbolButtonSmallTabTabbedBackgroundWhiteGeneric = null;
      
      public var caption:ILabel = null;
      
      public function SymbolButtonSmallTabTabbedWhiteGeneric(param1:MovieClip = null)
      {
         if(param1)
         {
            _nativeObject = param1 as SymbolButtonSmallTabTabbedWhite;
         }
         else
         {
            _nativeObject = new SymbolButtonSmallTabTabbedWhite();
         }
         super(null,FlashSprite.fromNative(_nativeObject));
         var _loc2_:FlashDisplayObjectContainer = _sprite as FlashDisplayObjectContainer;
         symbolButtonSmallTabTabbedBackgroundWhite = new SymbolButtonSmallTabTabbedBackgroundWhiteGeneric(_nativeObject.symbolButtonSmallTabTabbedBackgroundWhite);
         caption = FlashLabel.fromNative(_nativeObject.caption);
      }
      
      public function setNativeInstance(param1:SymbolButtonSmallTabTabbedWhite) : void
      {
         FlashSprite.setNativeInstance(_sprite,param1);
         _nativeObject = param1;
         syncInstances();
      }
      
      public function syncInstances() : void
      {
         if(_nativeObject.symbolButtonSmallTabTabbedBackgroundWhite)
         {
            symbolButtonSmallTabTabbedBackgroundWhite.setNativeInstance(_nativeObject.symbolButtonSmallTabTabbedBackgroundWhite);
         }
         FlashLabel.setNativeInstance(caption,_nativeObject.caption);
      }
   }
}