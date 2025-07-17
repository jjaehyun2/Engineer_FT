package org.ro.core.event {
import org.ro.core.DisplayManager;
import org.ro.core.Utils;
import org.ro.core.model.ObjectAdapter;
import org.ro.core.model.ObjectList;
import org.ro.layout.Layout;
import org.ro.to.Link;
import org.ro.to.TObject;

/**
 * Observers are initially created in ResponseHandler(s) and assigned to the respective LogEntry.
 * They may be passed on to additional LogEntries, eg. those corresponding to related Object or Layout URLs.
 */
/** sequence of operations:
 * (0) list
 * (1) FR_OBJECT                TObjectHandler -> invoke()
 * (2) FR_OBJECT_LAYOUT         layoutHandler -> invoke(layout.getProperties()[].getLink()) link can be null?
 * (3) FR_OBJECT_PROPERTY       PropertyHandler -> invoke()
 * (4) FR_PROPERTY_DESCRIPTION  PropertyDescriptionHandler
 */
public class ListObserver implements ILogEventObserver {

    private var list:ObjectList = new ObjectList();
    private var log:EventLog = EventLog.getInstance();

    /* test scope only */
    public function getList():ObjectList {
        return list;
    }

    public function ListObserver() {
    }

    public function update(le:LogEntry):void {
        var json:Object = Utils.toJsonObject(le.response);
        var url:String = le.url;

        if (isList(json)) {
            var size:uint = json.result.value.length;
            list.initSize(size);
        }
        if (isObject(json)) {
            if (list.isFull()) {
                trace("List full, not adding: " + url);
            } else {
                //TODO eventually set/get LogEntry.tObject
                var jsonStr:String = le.response;
                var jsonObj:Object = Utils.toJsonObject(jsonStr);
                var tObj:TObject = new TObject(jsonObj);
                loadLayout(tObj);
                var oa:ObjectAdapter = new ObjectAdapter(tObj);
                list.add(oa);
            }
        }

        if (isLayout(json)) {
            //TODO if le.tObject is already set it should contain Layout
            var l:Layout = new Layout(json);
            list.setLayout(l);
        }
        //TODO are list & layout the only criteria?
        if (list.hasLayout() && list.isFull()) {
            var le:LogEntry = log.find(url);
            var b:Boolean = (le != null) && (le.isView());
            if (b) {
                trace("View already opened: " + url);
            } else {
                //TODO on runFixtureScript this is passed multiple times (but no view opened (which is correct))
                DisplayManager.addView(list); //open
            }
        }
    }

    //TODO eventually move to LogEntry
    private function isList(json:Object):Boolean {
        var b:Boolean = false;
        if (json.resulttype == "list") b = true;
        if (json.memberType == "collection") b = true;
        return b;
    }

    private function isObject(json:Object):Boolean {
        return json.hasOwnProperty("instanceId");
    }

    private function isLayout(json:Object):Boolean {
        return json.hasOwnProperty("row");
    }

    private function loadLayout(tObject:TObject):void {
        var link:Link = tObject.getLayoutLink();
        var href:String = link.getHref();
        var le:LogEntry = log.find(href);
        if (le == null) {
            link.invoke(this);
        }
    }

}
}