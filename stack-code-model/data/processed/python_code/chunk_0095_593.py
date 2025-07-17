package org.ro.handler {
import org.flexunit.Assert;
import org.ro.URLS;
import org.ro.core.DisplayManager;
import org.ro.core.Globals;
import org.ro.core.Menu;
import org.ro.core.event.ListObserver;
import org.ro.core.event.LogEntry;
import org.ro.core.model.ObjectList;

public class ListHandlerTest {

    public function ListHandlerTest() {
    }

    [Test(description="handover json from service ")]
    public function testService():void {
        // given
        var m:Menu = new Menu(0);
        DisplayManager.setMenu(m);
        // when
        var le:LogEntry = new LogEntry("", "GET", null);
        le.response = JSON.stringify(URLS.SO_LIST_ALL_INVOKE);
        Globals.dispatcher.handle(le);
        var lo:ListObserver = le.observer as ListObserver;
        var t1:ObjectList = lo.getList();
        // then
        Assert.assertNotNull(t1);
    }

}
}