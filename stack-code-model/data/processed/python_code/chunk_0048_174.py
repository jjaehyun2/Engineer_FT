package org.ro.core.event {
import mx.collections.ArrayList;

import org.ro.core.Utils;

public class Node {

    private var entry:LogEntry;
    public var children:ArrayList;
    public var label:String;

    public function Node(entry:LogEntry) {
        this.entry = entry;
        this.label = entry.url;
    }

    public function addChild(n:Node):void {
        if (children == null) {
            children = new ArrayList();
        }
        children.addItem(n);
    }

    public function getParentUrl():String {
        var result:String;
        if (entry.hasResponse()) {
            var response:String = entry.getResponse();
            result = Utils.getUpHref(response);
        }
        return result;
    }

}
}