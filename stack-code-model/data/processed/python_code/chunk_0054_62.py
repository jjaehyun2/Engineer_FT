package org.ro.layout {
import mx.containers.Box;
import mx.containers.VBox;

import org.ro.view.UIUtil;

public class RowLayout extends AbstractLayout {
    private static const MAX_SPAN:uint = 12;

    internal var cols:Object;
    internal var metadataError:String;
    internal var id:String;

    internal var columnList:Vector.<ColLayout> = new Vector.<ColLayout>();

    public function RowLayout(jsonObj:Object) {
        if (jsonObj != null) {
            this.fromObject(jsonObj);
            init();
        }
    }

    private function init():void {
        columnList = new Vector.<ColLayout>();
        var l:ColLayout;
        for each(var json:Object in cols) {
            l = new ColLayout(json);
            columnList.push(l);
        }
    }

    public function ensureMaxSpan():Boolean {
        var sum:uint = 0;
        for each(var c:ColLayout in columnList) {
            sum = sum + c.span;
        }
        return MAX_SPAN == sum;
    }

    public function build():VBox {
        var result:VBox = new VBox();
        result.label = "tab: " + id;
        UIUtil.decorate(result, "RowLayout", debugInfo);
        var b:Box;
        for each(var c:ColLayout in columnList) {
            b = c.build();
            result.addChild(b);
        }
        return result;
    }

}
}