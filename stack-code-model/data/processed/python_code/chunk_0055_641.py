package com.company.assembleegameclient.ui.tooltip {
import flash.utils.Dictionary;

import kabam.rotmg.text.view.stringBuilder.AppendingLineBuilder;

public class SlotComparisonResult {

    public function SlotComparisonResult() {
        super();
        this.lineBuilder = new AppendingLineBuilder();
        this.processedTags = new Dictionary(true);
    }
    public var lineBuilder:AppendingLineBuilder;
    public var processedTags:Dictionary;
}
}