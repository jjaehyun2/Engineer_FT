package org.ro.utils {
import mx.controls.ToolTip;

public class HtmlToolTip extends ToolTip {
    public function HtmlToolTip() {
        super();
    }

    override protected function commitProperties():void {
        super.commitProperties();
        textField.htmlText = text;
    }

}
}