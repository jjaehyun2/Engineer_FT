package org.ro.to {

import org.flexunit.Assert;
import org.ro.URLS;

public class ServiceTest {
    public function ServiceTest() {
    }

    [Test(description="parse result of invoking url")]
    public function testSimpleObjectMenu():void {
        var service:Service = new Service(URLS.SO_MENU);
        Assert.assertEquals("Simple Objects", service.title);
        var actions:Vector.<Invokeable> = service.getMembers();
        Assert.assertEquals(3, actions.length);

        Assert.assertTrue(includesId(actions, "listAll"));
        Assert.assertTrue(includesId(actions, "findByName"));
        Assert.assertTrue(includesId(actions, "create"));

        // jsonObj contains '"members": {}' not '"members": []' 
        // in AS this results in an unordered list (Object{}), 
        // but intended is an ordered list (Array[])
        //TODO use object-layout / menu layout instead
    }

    private static function includesId(list:Vector.<Invokeable>, id:String):Boolean {
        for  each (var m:Member in list) {
            if (m.id == id) {
                return true;
            }
        }
        return false;
    }

    [Test(description="parse result of invoking url")]
    public function test_():void {
        var service:Service = new Service(URLS.RESTFUL_SERVICES);
        var values:Vector.<Invokeable> = service.getValues();
        Assert.assertEquals(8, values.length);
    }

}
}