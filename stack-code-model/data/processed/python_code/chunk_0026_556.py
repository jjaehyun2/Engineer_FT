package com.company.assembleegameclient.ui {
import com.company.util.GraphicsUtil;

import flash.display.GraphicsPath;
import flash.display.GraphicsPathWinding;
import flash.display.GraphicsSolidFill;
import flash.display.IGraphicsData;
import flash.display.Shape;

public class LineBreakDesign extends Shape {
    private var designGraphicsData_:Vector.<IGraphicsData>;

    public function LineBreakDesign(width:int, color:uint) {
        this.designFill_ = new GraphicsSolidFill(16777215, 1);
        this.designPath_ = new GraphicsPath(new Vector.<int>(), new Vector.<Number>(), GraphicsPathWinding.NON_ZERO);
        this.designGraphicsData_ = new <IGraphicsData>[this.designFill_, this.designPath_, GraphicsUtil.END_FILL];
        super();
        this.setWidthColor(width, color);
    }
    private var designFill_:GraphicsSolidFill;
    private var designPath_:GraphicsPath;

    public function setWidthColor(width:int, color:uint):void {
        graphics.clear();
        this.designFill_.color = color;
        GraphicsUtil.clearPath(this.designPath_);
        GraphicsUtil.drawDiamond(0, 0, 4, this.designPath_);
        GraphicsUtil.drawDiamond(width, 0, 4, this.designPath_);
        GraphicsUtil.drawRect(0, -1, width, 2, this.designPath_);
        graphics.drawGraphicsData(this.designGraphicsData_);
    }
}
}