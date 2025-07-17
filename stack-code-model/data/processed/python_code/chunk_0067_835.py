package org.ro.view {
import flash.geom.Rectangle;

import mx.controls.MenuBar;
import mx.controls.menuClasses.IMenuBarItemRenderer;
import mx.core.IFlexDisplayObject;

/**
 * Only required in order to change the Icon offset (from 10 -> x)
 * copied from mx.control.MenuBar
 * probably to be removed if a more modern MenuBar implementation is used
 */
public class MenuBarAdapter extends MenuBar {
    
    private var MARGIN_WIDTH:int = 0;

    protected function setMarginWidth(x:int):void {
        MARGIN_WIDTH = x;
    }

    override protected function measure():void {
        super.measure();
        var len:int = menuBarItems.length;
        measuredWidth = 0;

        // measured height is at least 22
        measuredHeight = DEFAULT_MEASURED_MIN_HEIGHT;
        for (var i:int = 0; i < len; i++) {
            measuredWidth += menuBarItems[i].getExplicitOrMeasuredWidth();
            measuredHeight = Math.max(
                    measuredHeight, menuBarItems[i].getExplicitOrMeasuredHeight());
        }

        if (len > 0)
            measuredWidth += 2 * MARGIN_WIDTH;
        else // else give it a default width, MARGIN_WIDTH = 10.
            measuredWidth = DEFAULT_MEASURED_MIN_WIDTH; // setting it slightly more than the width

        measuredMinWidth = measuredWidth;
        measuredMinHeight = measuredHeight;
    }

    private var background:IFlexDisplayObject;

    override protected function updateDisplayList(unscaledWidth:Number,
                                                  unscaledHeight:Number):void {
        super.updateDisplayList(unscaledWidth, unscaledHeight);

        var lastX:Number = MARGIN_WIDTH;
        var lastW:Number = 0;
        var len:int = menuBarItems.length;

        var clipContent:Boolean = false;
        var hideItems:Boolean = (unscaledWidth == 0 || unscaledHeight == 0);

        for (var i:int = 0; i < len; i++) {
            var item:IMenuBarItemRenderer = menuBarItems[i];

            item.setActualSize(item.getExplicitOrMeasuredWidth(), unscaledHeight);
 //           item.visible = !hideItems;

            lastX = item.x = lastX + lastW;
            lastW = item.width;

            if (!hideItems &&
                    (item.getExplicitOrMeasuredHeight() > unscaledHeight ||
                            (lastX + lastW) > unscaledWidth)) {
                clipContent = true;
            }
        }

        if (background) {
            background.setActualSize(unscaledWidth, unscaledHeight);
            background.visible = !hideItems;
        }

        // Set a scroll rect to handle clipping.
        scrollRect = clipContent ? new Rectangle(0, 0,
                unscaledWidth, unscaledHeight) : null;
    }

}
}