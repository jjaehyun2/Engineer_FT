package org.ro.layout {

public class AbstractLayout {
    internal var debugInfo:Object;
    internal var cssClass:String;

    public function AbstractLayout(jsonObj:Object = null) {
        fromObject(jsonObj);
    }

    internal function fromObject(obj:Object):void {
        for (var prop:String in obj) {
            this[prop] = obj[prop];
        }
        debugInfo = obj;
    }

}
}