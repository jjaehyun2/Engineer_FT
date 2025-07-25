package de.viaboxx.flexboxx {
import mx.graphics.GradientEntry;

import org.flexunit.assertThat;
import org.hamcrest.collection.array;
import org.hamcrest.object.equalTo;
import org.hamcrest.object.notNullValue;

import org.hamcrest.object.nullValue;

import spark.filters.DropShadowFilter;

[RunWith("org.flexunit.runners.Parameterized")]
public class FilterDescriptionTest {

    public function FilterDescriptionTest() {
        //empty constructor
    }

    public static function propertyNames():Array {
        return [
            ["alpha"],
            ["angle"]
        ];
    }

    public static function propertyTypes():Array {
        return [
            ["alpha", Number],
            ["color", uint],
            ["knockout", Boolean]
        ];
    }

    [Test(dataProvider="propertyNames")]
    public function dropShadowDescriptionPropertyNameIsCorrect(propertyName:String):void {
        assertThat(FilterDescription.forFilter(new DropShadowFilter()).getProperty(propertyName).name, equalTo(propertyName));
    }


    [Test(dataProvider="propertyTypes")]
    public function dropShadowDescriptionDatatypeIsCorrect(propertyName:String, expectedType:Class):void {
        assertThat(FilterDescription.forFilter(new DropShadowFilter()).getProperty(propertyName).dataType, equalTo(expectedType));
    }

    [Test]
    public function filterDescriptionContainsRightClassName():void {
        assertThat(FilterDescription.forFilter(new DropShadowFilter()).className, equalTo("DropShadowFilter"));
    }

    [Test]
    public function iteratingOverFilterDescriptionsWorks():void {
        var desc:FilterDescription = FilterDescription.forFilter(new TestFilter()),
                properties:Array = [];
        desc.forEachProperty(function callme(item:Property):void {
            properties.push(item.name);
        });
        assertThat(properties, array(equalTo("a"), equalTo("b"), equalTo("c")));
    }

    [Test]
    public function minMaxValuesFromMetadataAreCorrect():void {
        var desc:FilterDescription = FilterDescription.forFilter(new TestFilter());
        assertThat(desc.getProperty("b").minValue, equalTo(0.1));
        assertThat(desc.getProperty("b").maxValue, equalTo(1.0));

    }

    [Test]
    public function minMaxValuesFromMetadataAreCorrectForInteger():void {
        var desc:FilterDescription = FilterDescription.forFilter(new TestFilter());
        assertThat(desc.getProperty("a").minValue, equalTo(1));
        assertThat(desc.getProperty("a").maxValue, equalTo(100));
    }

    //    [Test]
    //    public function extractTypeInfo():void {
    //        assertThat("",equalTo(describeType(new GradientBevelFilter())))
    //    }

    [Test]
    public function gradientEntriesPropertyFound():void {
        var desc:FilterDescription = FilterDescription.forFilter(new TestGradientEntryFilter());
        assertThat(desc.getProperty("entries"), notNullValue());
    }

    [Test]
    public function gradientEntriesPropertyClassIsArray():void {
        var desc:FilterDescription = FilterDescription.forFilter(new TestGradientEntryFilter());
        assertThat(desc.getProperty("entries").dataType, equalTo(Array));
    }

    [Test]
    public function arrayEntryTypeIsCorrect():void {
        var desc:FilterDescription = FilterDescription.forFilter(new TestGradientEntryFilter());
        assertThat(desc.getProperty("entries").arrayType, equalTo(GradientEntry));
    }

    [Test]
    public function addingPropertiesManuallyWorks():void {
        var desc:FilterDescription = FilterDescription.forFilter(new TestFilter());
        var property:Property = new Property("id", String);
        desc.addProperty(property);
        assertThat(desc.getProperty("id"), equalTo(property));
    }

    [Test]
    public function readOnlyPropertiesAreOmitted():void {
        var desc:FilterDescription = FilterDescription.forFilter(new TestReadOnlyProperty());
        assertThat(desc.getProperty("automationEnabled"), nullValue());
    }

    [Test]
    public function writeOnlyPropertiesAreOmitted():void {
        var desc:FilterDescription = FilterDescription.forFilter(new TestWriteOnlyProperty());
        assertThat(desc.getProperty("writeOnly"), nullValue());
    }

}
}

import flash.filters.BitmapFilter;

import mx.filters.IBitmapFilter;

class TestFilter implements IBitmapFilter {

    private var _a:int, _b:Number, _c:Boolean;

    [Inspectable(minValue="1", maxValue="100")]
    public function get a():int {
        return _a;
    }


    public function set a(a:int) {
    }

    public function get c():Boolean {
        return _c;
    }

    public function set c(c:Boolean) {
    }

    [Inspectable(minValue="0.1", maxValue="1.0")]
    [Inspectable]
    public function get b():Number {
        return _b;
    }

    public function set b(b:Number) {
    }

    public function clone():BitmapFilter {
        return null;
    }
}


class TestGradientEntryFilter implements IBitmapFilter {

    private var _entries:Array;

    [Inspectable(category="General", arrayType="mx.graphics.GradientEntry")]
    public function get entries():Array {
        return _entries;
    }


    public function set entries(arr:Array):void {
    }

    public function clone():BitmapFilter {
        return null;
    }
}

class TestReadOnlyProperty {

    // r/o property for testing purposes.
    public function get automationEnabled():Boolean {
        return true;
    }
}

class TestWriteOnlyProperty {

    // w/o property for testing purposes.
    public function set writeOnly(a:Boolean):void {

    }
}