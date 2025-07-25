package Ankama_GameUiCore.ui
{
   import com.ankamagames.berilia.api.UiApi;
   import com.ankamagames.berilia.components.Label;
   import com.ankamagames.berilia.components.TextureBitmap;
   import com.ankamagames.berilia.types.graphic.ButtonContainer;
   import com.ankamagames.berilia.types.graphic.GraphicContainer;
   import com.ankamagames.berilia.utils.ComponentHookList;
   import com.ankamagames.dofus.kernel.sound.enum.SoundEnum;
   import com.ankamagames.dofus.kernel.sound.enum.SoundTypeEnum;
   import com.ankamagames.dofus.misc.lists.ShortcutHookListEnum;
   import com.ankamagames.dofus.uiApi.SoundApi;
   import com.ankamagames.jerakine.logger.Log;
   import com.ankamagames.jerakine.logger.Logger;
   import flash.utils.getQualifiedClassName;
   
   public class KISPreventAndSanctionPopup
   {
      
      protected static const _log:Logger = Log.getLogger(getQualifiedClassName(KISPreventAndSanctionPopup));
       
      
      [Api(name="SoundApi")]
      public var soundApi:SoundApi;
      
      [Api(name="UiApi")]
      public var uiApi:UiApi;
      
      public var mainCtr:GraphicContainer;
      
      public var window_popup:GraphicContainer;
      
      public var lbl_title_window_popup:Label;
      
      public var lbl_sanctionHeader:Label;
      
      public var lbl_sanctionReasons:Label;
      
      public var lbl_ban:Label;
      
      public var tx_separator:TextureBitmap;
      
      public var lbl_preventHeader:Label;
      
      public var btn_close_window_popup:ButtonContainer;
      
      public var lbl_preventReasons:Label;
      
      public var lbl_footer:Label;
      
      public var btn_ok:ButtonContainer;
      
      public var lbl_rules:Label;
      
      public function KISPreventAndSanctionPopup()
      {
         super();
      }
      
      public function main(params:Array) : void
      {
         this.showPreventAndSanctionPopup(params[0],params[1],params[2]);
         this.btn_ok.soundId = SoundEnum.OK_BUTTON;
         this.uiApi.addComponentHook(this.btn_ok,ComponentHookList.ON_RELEASE);
         this.uiApi.addComponentHook(this.mainCtr,ComponentHookList.ON_RELEASE);
         this.uiApi.addShortcutHook(ShortcutHookListEnum.CLOSE_UI,this.onShortcut);
         this.uiApi.me().setOnTop();
         this.lbl_title_window_popup.text = this.lbl_title_window_popup.text.toUpperCase();
         this.lbl_footer.fullWidthAndHeight();
         this.lbl_preventHeader.fullSize(this.lbl_preventHeader.width);
         this.lbl_preventReasons.fullSize(this.lbl_preventReasons.width);
         this.lbl_sanctionHeader.fullSize(this.lbl_sanctionHeader.width);
         this.lbl_sanctionReasons.fullSize(this.lbl_sanctionReasons.width);
         this.lbl_ban.fullSize(this.lbl_ban.width);
         this.lbl_rules.fullSize(this.lbl_rules.width);
         var headersHeight:int = this.lbl_preventHeader.height + this.lbl_sanctionHeader.height;
         var reasonsHeight:int = this.lbl_sanctionReasons.height + this.lbl_preventReasons.height;
         var footerHeight:int = this.lbl_footer.height;
         var banHeight:int = this.lbl_ban.height;
         var totalbodyHeight:int = headersHeight + reasonsHeight + footerHeight + banHeight;
         this.window_popup.height = totalbodyHeight + this.lbl_title_window_popup.height + this.tx_separator.height + Number(this.uiApi.me().getConstant("bottom_margin")) + Number(this.uiApi.me().getConstant("total_margin"));
      }
      
      private function showPreventAndSanctionPopup(preventReasons:Vector.<String>, sanctionReasons:Vector.<String>, banTime:uint) : void
      {
         this.lbl_title_window_popup.text = this.uiApi.getText("ui.pvp.sanction");
         this.lbl_title_window_popup.cssClass = "redcenter";
         this.lbl_ban.text = this.uiApi.getText("ui.pvp.ban",banTime);
         this.lbl_ban.text = this.uiApi.processText(this.lbl_ban.text,"m",banTime == 1,banTime == 0);
         this.lbl_footer.text = this.uiApi.getText("ui.pvp.preventAndRecidivism");
         this.fillReasons(this.lbl_preventReasons,preventReasons);
         this.fillReasons(this.lbl_sanctionReasons,sanctionReasons);
      }
      
      private function fillReasons(lbl:Label, reasons:Vector.<String>) : void
      {
         var reason:String = null;
         var reasonStr:String = null;
         for each(reason in reasons)
         {
            reasonStr = this.uiApi.getText(reason);
            if(reasonStr !== "[UNKNOWN_TEXT_NAME_" + reason + "]")
            {
               lbl.appendText(reasonStr + "\n");
            }
            else
            {
               _log.warn("Le flag " + reason + " envoyé par le serveur n\'a pas de texte AGT associé.");
            }
         }
      }
      
      public function unload() : void
      {
         this.soundApi.playSound(SoundTypeEnum.CLOSE_WINDOW);
      }
      
      private function closeMe() : void
      {
         if(this.uiApi !== null)
         {
            this.uiApi.unloadUi(this.uiApi.me().name);
         }
      }
      
      private function validate() : void
      {
         this.closeMe();
      }
      
      public function onShortcut(shortcutLabel:String) : Boolean
      {
         switch(shortcutLabel)
         {
            case ShortcutHookListEnum.VALID_UI:
               this.validate();
               return true;
            case ShortcutHookListEnum.CLOSE_UI:
               this.closeMe();
               return true;
            default:
               return false;
         }
      }
      
      public function onRelease(target:GraphicContainer) : void
      {
         switch(target)
         {
            case this.mainCtr:
               this.uiApi.me().setOnTop();
               break;
            case this.btn_close_window_popup:
            case this.btn_ok:
               this.validate();
         }
      }
   }
}