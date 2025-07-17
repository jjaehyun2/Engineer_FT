package org.ro.handler {
import org.ro.core.Globals;
import org.ro.layout.Layout;

public class LayoutHandler extends AbstractHandler implements IResponseHandler {
    public function LayoutHandler() {
    }

    public override function canHandle(jsonObj:Object):Boolean {
        var rows:Object = jsonObj.row;
        return (rows != null && rows.length > 0);
    }

    public override function doHandle(jsonObj:Object):void {
        var layout:Layout = new Layout(jsonObj);
        logEntry.object = layout;
    }

}
}