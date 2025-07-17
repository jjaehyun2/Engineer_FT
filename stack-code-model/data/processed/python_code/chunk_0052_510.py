package org.ro {
import flash.events.TimerEvent;
import flash.utils.Timer;

import org.flexunit.Assert;
import org.flexunit.async.Async;
import org.ro.core.Globals;
import org.ro.core.Utils;
import org.ro.core.event.LogEntry;
import org.ro.to.Invokeable;
import org.ro.to.Link;

/**
 * This is an integration test that requires SimpleApp running on http://localhost:8080
 *
 * @item Iterate over all Objects defined in class URLS,
 * @item check if the href 'self' can be invoked and
 * @item compare the response of invoking 'self' with what is hardcoded
 */
public class UrlsTest {
    private var timer:Timer;
    private var link:Link;
    private var object:Object;

    public function UrlsTest() {
    }

    [Before]
    public function setUp():void {
        timer = new Timer(100, 1);
        Globals.login("http://localhost:8080", "sven", "pass");
        /*        urls = {};
                addUrl(URLS.FR_OBJECT);
                addUrl(URLS.FR_OBJECT_BAZ);
                addUrl(URLS.FR_OBJECT_LAYOUT);
                addUrl(URLS.FR_OBJECT_PROPERTY);
                addUrl(URLS.FR_PROPERTY_DESCRIPTION);
                addUrl(URLS.SO_0);
                addUrl(URLS.SO_LIST_ALL);
                addUrl(URLS.SO_LIST_ALL_INVOKE);
                addUrl(URLS.SO_LIST_ALL_OBJECTS);
                addUrl(URLS.SO_MENU);
                addUrl(URLS.SO_OBJECT_LAYOUT);
                addUrl(URLS.RESTFUL_SERVICES); */
    }

    [After]
    public function tearDown():void {
        if (timer) {
            timer.stop();
        }
        timer = null;
    }

    protected static function handleTimeout(passThroughData:Object):void {
        Assert.fail("Timeout reached before event");
    }

    [Test(async, description="parse result of invoking object url")]
    public function testUrl1():void {
        object = URLS.RESTFUL_SERVICES;
        var href:String = Utils.getSelfHref(object);
        initLink(href);

        var asyncHandler:Function = Async.asyncHandler(this, handleLinkComplete, 500, null, handleTimeout);
        timer.addEventListener(TimerEvent.TIMER_COMPLETE, asyncHandler, false, 0, true);
        timer.start();
    }

    private function initLink(href:String):void {
        link = new Link();
        link.setHref(href);
        link.setMethod(Invokeable.GET);
        link.invoke();
    }

    public function handleLinkComplete(event:TimerEvent, passThroughData:Object):void {
        var href:String = link.getHref();
        var logEntry:LogEntry = Globals.logFind(href);
        var resp:String = logEntry.retrieveResponse();
        //TODO handle authentication problem: logEntry.fault="Security error accessing url"
        //  http://localhost:8080/crossdomain.xml
        if (logEntry.fault == null) {
            var observed:Object = JSON.parse(resp);
            //pass over String to Services
            var expected:Object = object;
            var b:Boolean = Utils.areEqual(expected, observed);
            Assert.assertTrue(b);        }
        else {
            trace(logEntry.fault);
        }
    }

}
}