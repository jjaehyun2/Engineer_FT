﻿package kabam.rotmg.ui.view {
import com.company.assembleegameclient.game.AGameSprite;
import com.company.assembleegameclient.game.GameSprite;
import com.company.assembleegameclient.map.GradientOverlay;
import com.company.assembleegameclient.map.HurtOverlay;
import com.company.assembleegameclient.objects.GameObject;
import com.company.assembleegameclient.objects.Player;
import com.company.assembleegameclient.parameters.Parameters;
import com.company.assembleegameclient.ui.TradePanel;
import com.company.assembleegameclient.ui.panels.InteractPanel;
import com.company.assembleegameclient.ui.panels.itemgrids.EquippedGrid;
import com.company.assembleegameclient.util.TextureRedrawer;
import com.company.util.GraphicsUtil;
import com.company.util.SpriteUtil;

import flash.display.DisplayObject;
import flash.display.GraphicsPath;
import flash.display.GraphicsSolidFill;
import flash.display.IGraphicsData;
import flash.display.Sprite;
import flash.events.Event;
import flash.geom.ColorTransform;
import flash.geom.Point;
import flash.utils.getTimer;

import kabam.rotmg.assets.EmbeddedAssets.EmbeddedAssets;
import kabam.rotmg.game.view.components.TabStripView;
import kabam.rotmg.messaging.impl.incoming.TradeAccepted;
import kabam.rotmg.messaging.impl.incoming.TradeChanged;
import kabam.rotmg.messaging.impl.incoming.TradeStart;
import kabam.rotmg.minimap.view.MiniMapImp;

public class HUDView extends Sprite implements UnFocusAble {

    private const BG_POSITION:Point = new Point(0, 0);
    private const MAP_POSITION:Point = new Point(4, 4);
    private const CHARACTER_DETAIL_PANEL_POSITION:Point = new Point(0, 198);
    private const STAT_METERS_POSITION:Point = new Point(12, 230);
    private const EQUIPMENT_INVENTORY_POSITION:Point = new Point(14, 304);
    private const TAB_STRIP_POSITION:Point = new Point(7, 346);
    private const INTERACT_PANEL_POSITION:Point = new Point(0, 500);
    private const GRADIENT_OVERLAY_POSITION:Point = new Point(-10, 0);
    private const DARKNESS_Y_POSITION:Point = new Point(-175, -50); // x: center, y: offset
    private const DARKNESS_X_POSITION:int = -600;
    private const HURT_OVERLAY_POSITION:Point = new Point(-600, 0);
    private const BREATH_CT:ColorTransform = new ColorTransform(0xFF / 0xFF, 55 / 0xFF, 0 / 0xFF, 0);

    private var background:CharacterWindowBackground;
    private var miniMap:MiniMapImp;
    private var equippedGrid:EquippedGrid;
    private var statMeters:StatMetersView;
    private var characterDetails:CharacterDetailsView;
    private var equippedGridBG:Sprite;
    private var player:Player;
    private var gradientOverlay:GradientOverlay;
    private var darkness:DisplayObject;
    private var hurtOverlay_:HurtOverlay;
    public var tabStrip:TabStripView;
    public var interactPanel:InteractPanel;
    public var tradePanel:TradePanel;

    public function HUDView() {
        this.createAssets();
        this.addAssets();
        this.positionAssets();
    }

    private function createAssets():void {
        this.background = new CharacterWindowBackground();
        this.miniMap = new MiniMapImp(192, 192);
        this.tabStrip = new TabStripView();
        this.characterDetails = new CharacterDetailsView();
        this.statMeters = new StatMetersView();
        this.gradientOverlay = new GradientOverlay();
        this.hurtOverlay_ = new HurtOverlay();
        this.darkness = new EmbeddedAssets.DarknessBackground();
        this.darkness.alpha = 0.95;
    }

    private function addAssets():void {
        addChild(this.background);
        addChild(this.miniMap);
        addChild(this.tabStrip);
        addChild(this.characterDetails);
        addChild(this.statMeters);
        addChild(this.gradientOverlay);
        addChild(this.hurtOverlay_);
    }

    private function positionAssets():void {
        this.background.x = this.BG_POSITION.x;
        this.background.y = this.BG_POSITION.y;
        this.miniMap.x = this.MAP_POSITION.x;
        this.miniMap.y = this.MAP_POSITION.y;
        this.tabStrip.x = this.TAB_STRIP_POSITION.x;
        this.tabStrip.y = this.TAB_STRIP_POSITION.y;
        this.characterDetails.x = this.CHARACTER_DETAIL_PANEL_POSITION.x;
        this.characterDetails.y = this.CHARACTER_DETAIL_PANEL_POSITION.y;
        this.statMeters.x = this.STAT_METERS_POSITION.x;
        this.statMeters.y = this.STAT_METERS_POSITION.y;
        this.gradientOverlay.x = this.GRADIENT_OVERLAY_POSITION.x;
        this.gradientOverlay.y = this.GRADIENT_OVERLAY_POSITION.y;
        this.darkness.x = this.DARKNESS_X_POSITION;
        this.hurtOverlay_.x = this.HURT_OVERLAY_POSITION.x;
        this.hurtOverlay_.y = this.HURT_OVERLAY_POSITION.y;
    }

    public function setPlayerDependentAssets(_arg1:GameSprite):void {
        this.player = _arg1.map.player_;
        this.createEquippedGridBackground();
        this.createEquippedGrid();
        this.createInteractPanel(_arg1);
    }

    private function createInteractPanel(_arg1:GameSprite):void {
        this.interactPanel = new InteractPanel(_arg1, this.player, 200, 100);
        this.interactPanel.x = this.INTERACT_PANEL_POSITION.x;
        this.interactPanel.y = this.INTERACT_PANEL_POSITION.y;
        addChild(this.interactPanel);
    }

    private function createEquippedGrid():void {
        this.equippedGrid = new EquippedGrid(this.player, this.player.slotTypes_, this.player);
        this.equippedGrid.x = this.EQUIPMENT_INVENTORY_POSITION.x;
        this.equippedGrid.y = this.EQUIPMENT_INVENTORY_POSITION.y;
        this.equippedGrid.filters = [TextureRedrawer.OUTLINE_FILTER];
        addChild(this.equippedGrid);
    }

    private function createEquippedGridBackground():void {
        var _local3:Vector.<IGraphicsData>;
        var _local1:GraphicsSolidFill = new GraphicsSolidFill(0x676767, 1);
        var _local2:GraphicsPath = new GraphicsPath(new Vector.<int>(), new Vector.<Number>());
        _local3 = new <IGraphicsData>[_local1, _local2, GraphicsUtil.END_FILL];
        GraphicsUtil.drawCutEdgeRect(0, 0, 178, 46, 6, [1, 1, 1, 1], _local2);
        this.equippedGridBG = new Sprite();
        this.equippedGridBG.x = (this.EQUIPMENT_INVENTORY_POSITION.x - 3);
        this.equippedGridBG.y = (this.EQUIPMENT_INVENTORY_POSITION.y - 3);
        this.equippedGridBG.graphics.drawGraphicsData(_local3);
        this.equippedGridBG.graphics.endFill();
        this.equippedGridBG.filters = [TextureRedrawer.OUTLINE_FILTER];
        addChild(this.equippedGridBG);
    }

    public function draw():void {
        if (this.equippedGrid) {
            this.equippedGrid.draw();
        }
        if (this.interactPanel) {
            this.interactPanel.draw();
        }

        // draw breath overlay
        if (player != null && player.breath_ >= 0 && player.breath_ < Parameters.BREATH_THRESH) {
            var bMult:Number = (Parameters.BREATH_THRESH - player.breath_) / Parameters.BREATH_THRESH;
            var btMult:Number = Math.abs(Math.sin(getTimer() / 300)) * 0.75;
            BREATH_CT.alphaMultiplier = bMult * btMult;
            hurtOverlay_.transform.colorTransform = BREATH_CT;
            hurtOverlay_.visible = true;
        }
        else {
            hurtOverlay_.visible = false;
        }

        // draw darkness
        if (player && player.isDarkness()) {
            this.darkness.y = Parameters.data_.centerOnPlayer ? DARKNESS_Y_POSITION.x : DARKNESS_Y_POSITION.y;
            addChild(this.darkness);
        }
        else {
            if (contains(this.darkness)) {
                removeChild(this.darkness);
            }
        }
    }

    public function startTrade(_arg1:AGameSprite, _arg2:TradeStart):void {
        if (!this.tradePanel) {
            this.tradePanel = new TradePanel(_arg1, _arg2);
            this.tradePanel.y = 200;
            this.tradePanel.addEventListener(Event.CANCEL, this.onTradeCancel);
            addChild(this.tradePanel);
            this.setNonTradePanelAssetsVisible(false);
        }
    }

    private function setNonTradePanelAssetsVisible(_arg1:Boolean):void {
        this.characterDetails.visible = _arg1;
        this.statMeters.visible = _arg1;
        this.tabStrip.visible = _arg1;
        this.equippedGrid.visible = _arg1;
        this.equippedGridBG.visible = _arg1;
        this.interactPanel.visible = _arg1;
    }

    public function tradeDone():void {
        this.removeTradePanel();
    }

    public function tradeChanged(_arg1:TradeChanged):void {
        if (this.tradePanel) {
            this.player.isTrading = true;
            this.tradePanel.setYourOffer(_arg1.offer_);
        }
    }

    public function tradeAccepted(_arg1:TradeAccepted):void {
        if (this.tradePanel) {
            this.player.isTrading = true;
            this.tradePanel.youAccepted(_arg1.myOffer_, _arg1.yourOffer_);
        }
    }

    private function onTradeCancel(_arg1:Event):void {
        this.removeTradePanel();
    }

    private function removeTradePanel():void {
        if (this.tradePanel) {
            SpriteUtil.safeRemoveChild(this, this.tradePanel);

            this.player.isTrading = false;
            this.tradePanel.removeEventListener(Event.CANCEL, this.onTradeCancel);
            this.tradePanel = null;

            this.setNonTradePanelAssetsVisible(true);
        }
    }

    public function setMiniMapFocus(object:GameObject):void {
        this.miniMap.setFocus(object);
    }

}
}