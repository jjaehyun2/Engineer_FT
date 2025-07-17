package org.ro.core.event {
import mx.rpc.events.FaultEvent;
import mx.rpc.events.ResultEvent;
import mx.rpc.http.mxml.HTTPService;

import org.ro.core.Globals;
import org.ro.to.Invokeable;
import org.ro.to.Link;

/**
 * The name is somewhat misleading, see: https://en.wikipedia.org/wiki/XMLHttpRequest
 */
public class XmlHttpRequest extends HTTPService {
    private static var log:EventLog = EventLog.getInstance();

    protected function xhrFaultHandler(event:FaultEvent):void {
        log.fault(url, event.fault.faultString);
    }

    protected function xhrResultHandler(event:ResultEvent):void {
        var jsonString:String = event.result.toString();
        var logEntry:LogEntry = log.end(url, jsonString);
        Globals.dispatcher.handle(logEntry);
    }

    public function XmlHttpRequest() {
        super.useProxy = false;
        addEventListener(FaultEvent.FAULT, xhrFaultHandler);
        addEventListener(ResultEvent.RESULT, xhrResultHandler);
    }

    public function invoke(inv:Invokeable, obs:ILogEventObserver):void {
        cancel();
        super.url = inv.getHref();
        if (log.isCached(url)) {
            log.update(url);
        }
        super.method = inv.getMethod();
        var credentials:String = Globals.session.getCredentials();
        super.headers = {Authorization: "Basic " + credentials};
        super.headers["Accept"] = "application/json";
        super.contentType = "application/json";
        if (super.method == Invokeable.POST) {
            var l:Link = inv as Link;
            var body:String = l.getArgumentsAsJsonString();
            send(body);
        } else {
            send();
        }
        log.start(url, method, body, obs);
    }

}
}