package io.decagames.rotmg.fame {
import com.company.assembleegameclient.ui.tooltip.TextToolTip;

import kabam.rotmg.core.signals.HideTooltipsSignal;
import kabam.rotmg.core.signals.ShowTooltipSignal;
import kabam.rotmg.tooltips.HoverTooltipDelegate;

import robotlegs.bender.bundles.mvcs.Mediator;

public class FameStatsLineMediator extends Mediator {


    public function FameStatsLineMediator() {
        super();
    }
    [Inject]
    public var view:StatsLine;
    [Inject]
    public var showTooltipSignal:ShowTooltipSignal;
    [Inject]
    public var hideTooltipSignal:HideTooltipsSignal;
    private var toolTip:TextToolTip = null;
    private var hoverTooltipDelegate:HoverTooltipDelegate;

    override public function initialize():void {
        if (this.view.tooltipText != "") {
            this.toolTip = new TextToolTip(3552822, 10197915, "", this.view.tooltipText, 200);
            this.hoverTooltipDelegate = new HoverTooltipDelegate();
            this.hoverTooltipDelegate.setShowToolTipSignal(this.showTooltipSignal);
            this.hoverTooltipDelegate.setHideToolTipsSignal(this.hideTooltipSignal);
            this.hoverTooltipDelegate.setDisplayObject(this.view);
            this.hoverTooltipDelegate.tooltip = this.toolTip;
        }
    }

    override public function destroy():void {
        if (this.view.tooltipText != "") {
            this.hoverTooltipDelegate = null;
            this.toolTip = null;
        }
        this.view.clean();
    }
}
}