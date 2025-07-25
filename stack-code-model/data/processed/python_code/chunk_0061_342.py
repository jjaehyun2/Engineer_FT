package ddt.view.common.church
{
   import com.pickgliss.events.FrameEvent;
   import com.pickgliss.ui.ComponentFactory;
   import com.pickgliss.ui.LayerManager;
   import com.pickgliss.ui.controls.alert.BaseAlerFrame;
   import com.pickgliss.ui.vo.AlertInfo;
   import ddt.manager.LanguageMgr;
   import ddt.manager.SoundManager;
   import flash.display.Bitmap;
   import flash.events.Event;
   
   public class ChurchDialogueUnmarried extends BaseAlerFrame
   {
       
      
      private var _bg:Bitmap;
      
      private var _alertInfo:AlertInfo;
      
      public function ChurchDialogueUnmarried()
      {
         super();
         this.initialize();
      }
      
      protected function initialize() : void
      {
         cancelButtonStyle = "core.simplebt";
         submitButtonStyle = "core.simplebt";
         this._alertInfo = new AlertInfo();
         this._alertInfo.showSubmit = false;
         this._alertInfo.cancelLabel = LanguageMgr.GetTranslation("close");
         this._alertInfo.moveEnable = false;
         info = this._alertInfo;
         this.escEnable = true;
         this._bg = ComponentFactory.Instance.creatBitmap("asset.church.UnmarriedAsset");
         this._bg.x = -7;
         addToContent(this._bg);
         addEventListener(FrameEvent.RESPONSE,this.onFrameResponse);
      }
      
      private function onFrameResponse(param1:FrameEvent) : void
      {
         switch(param1.responseCode)
         {
            case FrameEvent.CANCEL_CLICK:
            case FrameEvent.CLOSE_CLICK:
            case FrameEvent.ESC_CLICK:
            case FrameEvent.ENTER_CLICK:
            case FrameEvent.SUBMIT_CLICK:
               SoundManager.instance.play("008");
               this.dispose();
         }
      }
      
      public function show() : void
      {
         LayerManager.Instance.addToLayer(this,LayerManager.GAME_DYNAMIC_LAYER,true,LayerManager.BLCAK_BLOCKGOUND);
      }
      
      override public function dispose() : void
      {
         super.dispose();
         removeEventListener(FrameEvent.RESPONSE,this.onFrameResponse);
         if(this._bg)
         {
            if(this._bg.parent)
            {
               this._bg.parent.removeChild(this._bg);
            }
            this._bg.bitmapData.dispose();
            this._bg.bitmapData = null;
         }
         this._bg = null;
         if(parent)
         {
            parent.removeChild(this);
         }
         dispatchEvent(new Event(Event.CLOSE));
      }
   }
}