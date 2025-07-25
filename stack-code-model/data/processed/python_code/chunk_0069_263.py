package com.company.assembleegameclient.ui.panels {
import com.company.assembleegameclient.game.AGameSprite;
import com.company.assembleegameclient.objects.VaultContainer;

import flash.events.Event;
import flash.filters.DropShadowFilter;

import kabam.rotmg.core.StaticInjectorContext;
import kabam.rotmg.text.view.StaticTextDisplay;
import kabam.rotmg.text.view.stringBuilder.LineBuilder;
import kabam.rotmg.ui.model.HUDModel;
import kabam.rotmg.util.components.LegacyBuyButton;

public class VaultPanel extends Panel {

    private static function countValidItems(param1:Vector.<int>):int {
        var _loc3_:int = 0;
        var _loc2_:int = 0;
        _loc3_ = 0;
        while (_loc3_ < param1.length) {
            if (param1[_loc3_] != -1) {
                _loc2_++;
            }
            _loc3_++;
        }
        return _loc2_;
    }

    public function VaultPanel(param1:AGameSprite, param2:VaultContainer) {
        super(param1);
        var _loc3_:HUDModel = StaticInjectorContext.getInjector().getInstance(HUDModel);
        this.owner = param2;
        this.nameText = new StaticTextDisplay();
        this.nameText.setSize(18).setColor(16777215).setTextWidth(188).setWordWrap(true).setMultiLine(true).setAutoSize("center").setBold(true).setHTML(true);
        this.nameText.setStringBuilder(new LineBuilder().setParams("Vault\n" + countValidItems(_loc3_.vaultContents) + "/" + _loc3_.vaultContents.length).setPrefix("<p align=\"center\">").setPostfix("</p>"));
        this.nameText.filters = [new DropShadowFilter(0, 0, 0)];
        addChild(this.nameText);
        this.upgradeButton = new LegacyBuyButton("Upgrade {cost}", 18, this.owner.price_, 0);
        this.upgradeButton.addEventListener("click", this.onUpgradeClick);
        this.upgradeButton.y = 45;
        this.upgradeButton.x = 25;
        addChild(this.upgradeButton);
    }
    private var owner:VaultContainer;
    private var nameText:StaticTextDisplay;
    private var upgradeButton:LegacyBuyButton;

    override public function draw():void {
    }

    private function onUpgradeClick(param1:Event):void {
        this.gs_.gsc_.buy(this.owner.objectId_, 1);
    }
}
}