package org.ro.view {
import mx.containers.Box;
import mx.containers.FormItem;
import mx.controls.Label;
import mx.core.UIComponent;

import org.ro.core.Utils;

import spark.components.Button;

public class UIUtil {

    public static function decorate(uic:UIComponent, className:String, jsonObj:Object):void {
        // toolTip has no effect for HBox, VBox
        uic.toolTip = Utils.htmlTip(jsonObj);
        if (uic is Box) {
            var lbl:Label = new Label();
            lbl.text = className;
            uic.addChild(lbl);
        }

        uic.setStyle("borderThickness", 2);
        uic.setStyle("borderColor", "black");
        uic.setStyle("borderSides", "left top right bottom");
        uic.setStyle("borderStyle", "inset");
        uic.percentWidth = 75;
        uic.percentHeight = 75;
    }

    public static function buildFormItem(label:String):FormItem {
        var fi:FormItem = new FormItem();
        fi.direction = "horizontal";
        fi.setStyle("horizontalAlign", "left");
        fi.label = label;
        return fi;
    }

    public static function buildButton(label:String, iconClass:Class):Button {
        var btn:Button = new Button();
        btn.label = label;
        return btn;
    }

}
}