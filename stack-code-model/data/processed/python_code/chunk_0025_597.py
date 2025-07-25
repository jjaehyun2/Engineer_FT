package visuals.ui.dialogs
{
   import com.playata.framework.display.Sprite;
   import com.playata.framework.display.lib.flash.FlashDisplayObjectContainer;
   import com.playata.framework.display.lib.flash.FlashLabel;
   import com.playata.framework.display.lib.flash.FlashLabelArea;
   import com.playata.framework.display.lib.flash.FlashSprite;
   import com.playata.framework.display.lib.flash.FlashTextInput;
   import com.playata.framework.display.ui.controls.ILabel;
   import com.playata.framework.display.ui.controls.ILabelArea;
   import com.playata.framework.display.ui.controls.ITextInput;
   import flash.display.MovieClip;
   import visuals.ui.base.SymbolUiButtonWideGeneric;
   import visuals.ui.base.SymbolUiCheckboxGeneric;
   import visuals.ui.elements.backgrounds.SymbolSlice9BackgroundDialogGeneric;
   import visuals.ui.elements.buttons.SymbolButtonCloseGeneric;
   import visuals.ui.elements.stream.SymbolPanelStreamInputBackgroundGeneric;
   
   public class SymbolDialogOptInMarketingGeneric extends Sprite
   {
       
      
      private var _nativeObject:SymbolDialogOptInMarketing = null;
      
      public var dialogBackground:SymbolSlice9BackgroundDialogGeneric = null;
      
      public var txtDialogTitle:ILabel = null;
      
      public var txtInfo:ILabelArea = null;
      
      public var txtEmailCaption:ILabel = null;
      
      public var backgroundInputEmail:SymbolPanelStreamInputBackgroundGeneric = null;
      
      public var inputEmail:ITextInput = null;
      
      public var rbtnYes:SymbolUiCheckboxGeneric = null;
      
      public var txtYes:ILabelArea = null;
      
      public var rbtnNo:SymbolUiCheckboxGeneric = null;
      
      public var txtNo:ILabelArea = null;
      
      public var btnConfirm:SymbolUiButtonWideGeneric = null;
      
      public var btnClose:SymbolButtonCloseGeneric = null;
      
      public function SymbolDialogOptInMarketingGeneric(param1:MovieClip = null)
      {
         if(param1)
         {
            _nativeObject = param1 as SymbolDialogOptInMarketing;
         }
         else
         {
            _nativeObject = new SymbolDialogOptInMarketing();
         }
         super(null,FlashSprite.fromNative(_nativeObject));
         var _loc2_:FlashDisplayObjectContainer = _sprite as FlashDisplayObjectContainer;
         dialogBackground = new SymbolSlice9BackgroundDialogGeneric(_nativeObject.dialogBackground);
         txtDialogTitle = FlashLabel.fromNative(_nativeObject.txtDialogTitle);
         txtInfo = FlashLabelArea.fromNative(_nativeObject.txtInfo);
         txtEmailCaption = FlashLabel.fromNative(_nativeObject.txtEmailCaption);
         backgroundInputEmail = new SymbolPanelStreamInputBackgroundGeneric(_nativeObject.backgroundInputEmail);
         inputEmail = FlashTextInput.fromNative(_nativeObject.inputEmail);
         rbtnYes = new SymbolUiCheckboxGeneric(_nativeObject.rbtnYes);
         txtYes = FlashLabelArea.fromNative(_nativeObject.txtYes);
         rbtnNo = new SymbolUiCheckboxGeneric(_nativeObject.rbtnNo);
         txtNo = FlashLabelArea.fromNative(_nativeObject.txtNo);
         btnConfirm = new SymbolUiButtonWideGeneric(_nativeObject.btnConfirm);
         btnClose = new SymbolButtonCloseGeneric(_nativeObject.btnClose);
      }
      
      public function setNativeInstance(param1:SymbolDialogOptInMarketing) : void
      {
         FlashSprite.setNativeInstance(_sprite,param1);
         _nativeObject = param1;
         syncInstances();
      }
      
      public function syncInstances() : void
      {
         if(_nativeObject.dialogBackground)
         {
            dialogBackground.setNativeInstance(_nativeObject.dialogBackground);
         }
         FlashLabel.setNativeInstance(txtDialogTitle,_nativeObject.txtDialogTitle);
         FlashLabelArea.setNativeInstance(txtInfo,_nativeObject.txtInfo);
         FlashLabel.setNativeInstance(txtEmailCaption,_nativeObject.txtEmailCaption);
         if(_nativeObject.backgroundInputEmail)
         {
            backgroundInputEmail.setNativeInstance(_nativeObject.backgroundInputEmail);
         }
         FlashTextInput.setNativeInstance(inputEmail,_nativeObject.inputEmail);
         if(_nativeObject.rbtnYes)
         {
            rbtnYes.setNativeInstance(_nativeObject.rbtnYes);
         }
         FlashLabelArea.setNativeInstance(txtYes,_nativeObject.txtYes);
         if(_nativeObject.rbtnNo)
         {
            rbtnNo.setNativeInstance(_nativeObject.rbtnNo);
         }
         FlashLabelArea.setNativeInstance(txtNo,_nativeObject.txtNo);
         if(_nativeObject.btnConfirm)
         {
            btnConfirm.setNativeInstance(_nativeObject.btnConfirm);
         }
         if(_nativeObject.btnClose)
         {
            btnClose.setNativeInstance(_nativeObject.btnClose);
         }
      }
   }
}