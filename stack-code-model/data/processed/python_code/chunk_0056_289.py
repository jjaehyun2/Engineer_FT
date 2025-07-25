package io.decagames.rotmg.supportCampaign.tab.tiers.button {
import com.company.assembleegameclient.ui.tooltip.TextToolTip;

import flash.events.MouseEvent;

import io.decagames.rotmg.supportCampaign.data.SupporterCampaignModel;
import io.decagames.rotmg.supportCampaign.signals.TierSelectedSignal;
import io.decagames.rotmg.supportCampaign.signals.UpdateCampaignProgress;

import kabam.rotmg.core.signals.HideTooltipsSignal;
import kabam.rotmg.core.signals.ShowTooltipSignal;
import kabam.rotmg.tooltips.HoverTooltipDelegate;

import robotlegs.bender.bundles.mvcs.Mediator;

public class TierButtonMediator extends Mediator {


    public function TierButtonMediator() {
        super();
    }
    [Inject]
    public var view:TierButton;
    [Inject]
    public var model:SupporterCampaignModel;
    [Inject]
    public var updatePointsSignal:UpdateCampaignProgress;
    [Inject]
    public var showTooltipSignal:ShowTooltipSignal;
    [Inject]
    public var hideTooltipSignal:HideTooltipsSignal;
    [Inject]
    public var selectedSignal:TierSelectedSignal;
    private var toolTip:TextToolTip = null;
    private var hoverTooltipDelegate:HoverTooltipDelegate;
    private var remainingPoints:int;

    override public function initialize():void {
        this.updatePointsSignal.add(this.onPointsUpdate);
        this.view.addEventListener("click", this.onClickHandler);
        this.selectedSignal.add(this.onTierSelected);
        this.view.removeToolTipSignal.add(this.clearToolTip);
        this.updateTooltip();
    }

    override public function destroy():void {
        this.updatePointsSignal.remove(this.onPointsUpdate);
        this.view.removeEventListener("click", this.onClickHandler);
        this.view.removeToolTipSignal.remove(this.clearToolTip);
        this.selectedSignal.remove(this.onTierSelected);
        this.clearToolTip();
    }

    private function onPointsUpdate():void {
        this.updateTooltip();
    }

    private function updateTooltip():void {
        this.remainingPoints = this.model.ranks[this.view.tier - 1] - this.model.points;
        if (this.view.label && (this.view.status == 0 || this.view.status == 1)) {
            this.clearToolTip();
            if (this.remainingPoints <= 0) {
                this.toolTip = new TextToolTip(0x363636, 4958208, "Rank " + this.view.tier, "Claim your Gifts!", 3 * 60);
            } else {
                this.toolTip = new TextToolTip(0x363636, 0x9b9b9b, "Rank " + this.view.tier, this.remainingPoints.toString() + " Bonus Points remaining ", 3 * 60);
            }
            this.hoverTooltipDelegate = new HoverTooltipDelegate();
            this.hoverTooltipDelegate.setShowToolTipSignal(this.showTooltipSignal);
            this.hoverTooltipDelegate.setHideToolTipsSignal(this.hideTooltipSignal);
            this.hoverTooltipDelegate.setDisplayObject(this.view.label);
            this.hoverTooltipDelegate.tooltip = this.toolTip;
        } else if (this.view.status == 2) {
            this.clearToolTip();
        }
    }

    private function onTierSelected(_arg_1:int):void {
        if (this.view.tier == _arg_1 && !this.view.selected) {
            this.view.selected = true;
        }
        if (this.view.tier != _arg_1 && this.view.selected) {
            this.view.selected = false;
        }
    }

    private function clearToolTip():void {
        if (this.hoverTooltipDelegate) {
            this.toolTip = null;
            this.hoverTooltipDelegate.removeDisplayObject();
            this.hoverTooltipDelegate = null;
        }
    }

    private function onClickHandler(_arg_1:MouseEvent):void {
        if (!this.view.selected) {
            this.view.selected = true;
            this.selectedSignal.dispatch(this.view.tier);
        }
    }
}
}