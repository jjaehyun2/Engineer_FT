package org.ro.view.table {
import mx.controls.LinkButton;

import org.ro.view.ImageRepository;

public class ObjectIconRenderer extends IconRenderer {

    private var labelButton:LinkButton;

    public function ObjectIconRenderer() {
        super();
        labelButton = new LinkButton();
        labelButton.top = 4;
        labelButton.left = 20;
        labelButton.height = 16;
        this.addElement(labelButton);
    }

    override public function set data(value:Object):void {
        //TODO use icon retrieved from server
        var defaultIcon:Class = ImageRepository.PencilIcon;
        iconButton.setStyle("icon", defaultIcon);

        if (value.object != null || value.object != undefined) {
            labelButton.label = value.object.label;
            labelButton.setStyle("textAlign", "left");
            labelButton.setStyle("textDecoration", "underline");
        }
        
    }

}
}