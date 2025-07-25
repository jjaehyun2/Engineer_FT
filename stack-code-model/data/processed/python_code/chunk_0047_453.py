package visuals.ui.elements.mail
{
   import com.playata.framework.display.Sprite;
   import com.playata.framework.display.lib.flash.FlashDisplayObjectContainer;
   import com.playata.framework.display.lib.flash.FlashLabel;
   import com.playata.framework.display.lib.flash.FlashLabelArea;
   import com.playata.framework.display.lib.flash.FlashSprite;
   import com.playata.framework.display.ui.controls.ILabel;
   import com.playata.framework.display.ui.controls.ILabelArea;
   import flash.display.MovieClip;
   import visuals.ui.base.SymbolIconButtonDeleteGeneric;
   import visuals.ui.base.SymbolUiButtonDefaultCheckedGeneric;
   
   public class SymbolMailboxRequestLineGeneric extends Sprite
   {
       
      
      private var _nativeObject:SymbolMailboxRequestLine = null;
      
      public var txtInfo:ILabelArea = null;
      
      public var txtTitle:ILabel = null;
      
      public var btnAccept:SymbolUiButtonDefaultCheckedGeneric = null;
      
      public var btnDecline:SymbolIconButtonDeleteGeneric = null;
      
      public function SymbolMailboxRequestLineGeneric(param1:MovieClip = null)
      {
         if(param1)
         {
            _nativeObject = param1 as SymbolMailboxRequestLine;
         }
         else
         {
            _nativeObject = new SymbolMailboxRequestLine();
         }
         super(null,FlashSprite.fromNative(_nativeObject));
         var _loc2_:FlashDisplayObjectContainer = _sprite as FlashDisplayObjectContainer;
         txtInfo = FlashLabelArea.fromNative(_nativeObject.txtInfo);
         txtTitle = FlashLabel.fromNative(_nativeObject.txtTitle);
         btnAccept = new SymbolUiButtonDefaultCheckedGeneric(_nativeObject.btnAccept);
         btnDecline = new SymbolIconButtonDeleteGeneric(_nativeObject.btnDecline);
      }
      
      public function setNativeInstance(param1:SymbolMailboxRequestLine) : void
      {
         FlashSprite.setNativeInstance(_sprite,param1);
         _nativeObject = param1;
         syncInstances();
      }
      
      public function syncInstances() : void
      {
         FlashLabelArea.setNativeInstance(txtInfo,_nativeObject.txtInfo);
         FlashLabel.setNativeInstance(txtTitle,_nativeObject.txtTitle);
         if(_nativeObject.btnAccept)
         {
            btnAccept.setNativeInstance(_nativeObject.btnAccept);
         }
         if(_nativeObject.btnDecline)
         {
            btnDecline.setNativeInstance(_nativeObject.btnDecline);
         }
      }
   }
}