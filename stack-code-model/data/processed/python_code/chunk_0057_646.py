package org.ro.layout {

import mx.containers.HBox;
import mx.containers.VBox;

import org.flexunit.Assert;
import org.ro.URLS;

public class LayoutTest {
    public function LayoutTest() {
    }

    [Test(description="parse result of invoking url")]
    public function testObjectLayout():void {
        //when
        var lo:Layout = new Layout(URLS.SO_OBJECT_LAYOUT);
        // then
        var properties:Vector.<PropertyLayout> = lo.getProperties();
        Assert.assertEquals(2, properties.length);
        Assert.assertEquals("name", properties[0].getId());
        Assert.assertEquals("notes", properties[1].getId());
    }

    [Test(description="parse result of invoking url (FixtureScript)")]
    public function testFsObjectLayout():void {
        // given
        var lo:Layout = new Layout(URLS.FR_OBJECT_LAYOUT);
        // when
        var properties:Vector.<PropertyLayout> = lo.getProperties();
        // then
        Assert.assertEquals(4, properties.length);
        Assert.assertEquals("className", properties[0].getId());
        Assert.assertEquals("fixtureScriptClassName", properties[1].getId());
        Assert.assertEquals("key", properties[2].getId());
        Assert.assertEquals("object", properties[3].getId());
        //TODO where do these labels come from?

        // (1) property.link.href "http://localhost:8080/restful/objects/isisApplib.FixtureResult/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPG1lbWVudG8-PGtleT5kb21haW4tYXBwLWRlbW8vcGVyc2lzdC1hbGwvaXRlbS01PC9rZXk-PG9iamVjdC5ib29rbWFyaz5zaW1wbGUuU2ltcGxlT2JqZWN0OjExNDwvb2JqZWN0LmJvb2ttYXJrPjwvbWVtZW50bz4=/properties/className"
        // (2) links[describedBy].href -> 
        // (3) http://localhost:8080/restful/domain-types/isisApplib.FixtureResult/properties/className -> extensions.friendlyName
        // (4) 
    }

    [Test(description="parse result of invoking url")]
    public function testBuildObjectLayout():void {
        //when
        var lo:Layout = new Layout(URLS.SO_OBJECT_LAYOUT);
        // layout.rows[1].cols[1].col.tabGroup[0]
        //ensure tabgroup is TabNavigator

        // then
        var ui:VBox = lo.build();
        Assert.assertEquals(2, ui.getChildren().length);

        //TODO IMPROVE expected values depend on 'debugInfo' applied in Layout classes 
        var row1:VBox = ui.getChildren()[1];
        Assert.assertEquals(3, row1.getChildren().length);

        var h2:HBox = row1.getChildren()[1];
        Assert.assertEquals(3, h2.getChildren().length);
    }
    
}
}