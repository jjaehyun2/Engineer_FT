package com.company.assembleegameclient.objects {
   import com.company.assembleegameclient.game.GameSprite;
   import com.company.assembleegameclient.ui.panels.Panel;
   import com.company.assembleegameclient.ui.tooltip.TextToolTip;
   import com.company.assembleegameclient.ui.tooltip.ToolTip;
   import io.decagames.rotmg.pets.panels.YardUpgraderPanel;
   
   public class YardUpgrader extends GameObject implements IInteractiveObject {
       
      
      public function YardUpgrader(param1:XML) {
         super(param1);
         isInteractive_ = true;
      }
      
      public function getTooltip() : ToolTip {
         return new TextToolTip(3552822,10197915,"ClosedGiftChest.title","TextPanel.giftChestIsEmpty",200);
      }
      
      public function getPanel(param1:GameSprite) : Panel {
         return new YardUpgraderPanel(param1,objectType_);
      }
   }
}