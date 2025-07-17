package org.ro.layout {
import mx.containers.Box;
import mx.containers.VBox;

import org.ro.view.UIUtil;

/**
 * Parse layout specification.
 * In case of non-menu layout, build a UIComponent.
 */
public class Layout extends AbstractLayout {

    internal var row:Object; // which actually is a list of rows
    internal var rowList:Vector.<RowLayout>;
    private var properties:Vector.<PropertyLayout>;
    private var propertyLabels:Object = {};

    public function Layout(jsonObj:Object = null) {
        if (jsonObj != null) {
            this.fromObject(jsonObj);
            init();
        }
    }

    private function init():void {
        var props:Array = extractProperties();
        initProperties(props);
        initRows(row);

        //TODO refactor train.wreck.s  
        // var s:Object = findPropertyBy(row, "fieldSet");
        function extractProperties():Array {
            var col:Object = row[1].cols[0].col;
            var TAB_GROUP:String = "tabGroup";
            if (col.hasOwnProperty(TAB_GROUP)) {
                // special case for json1
                col = col.tabGroup[0].tab[0].row[0].cols[0].col;
            }
            var pArr:Array = col.fieldSet[0].property;
            return pArr;
        }
    }

    private function initProperties(props:Array):void {
        this.properties = new Vector.<PropertyLayout>();
        var l:PropertyLayout;
        for each(var json:Object in props) {
            l = new PropertyLayout(json);
            this.properties.push(l);
        }
    }

    private function initRows(row:Object):void {
        this.rowList = new Vector.<RowLayout>();
        var l:RowLayout;
        for each(var json:Object in row) {
            l = new RowLayout(json);
            this.rowList.push(l);
        }
    }

    public function addPropertyLabel(id:String, friendlyName:String):void {
        propertyLabels[id] = friendlyName;
    }

    public function getPropertyLabel(id:String):String {
        return propertyLabels[id];
    }

    public function arePropertyLabelsToBeSet():Boolean {
        var labelSize:uint = propertyLabels.length;
        var propsSize:uint = 0;
        if (null != properties) {
            propsSize = properties.length; 
        }
        return (labelSize < propsSize);
    }

    public function build():VBox {
        var result:VBox = new VBox();
        UIUtil.decorate(result, "Layout", debugInfo);
        var b:Box;
        //TODO iterate over rows, recurse into columns, etc.
        var rowCount:uint = 0;
        for each(var rl:RowLayout in rowList) {
            rowCount = rowCount + 1;
            // the first row contains the object titel and actions (for wicket viewer)
            // this is handled here differently (tab)
            if (rowCount > 1) {
                b = rl.build();
                result.addChild(b);
            }
        }

        return result;
    }

    public function getProperties():Vector.<PropertyLayout> {
        return properties;
    }

// recurse into attributes/fields/properties and 
    private function findPropertyBy(object:Object, name:String):Object {
        if (object.hasOwnProperty(name)) {
            return object[name];
        } else {
            for each(var o:Object in object) {
                if (isCollection(o) || isNamed(o)) {
                    return findPropertyBy(o, name);
                }
            }
        }
        return null;

        function isCollection(o:Object):Boolean {
            if ((o == null) || (o is String)) {
                return false;
            } else {
                return ((o is Object) || (o is Array));
            }
        }

        function isNamed(o:Object):Boolean {
            if ((o == null) || (o is String)) {
                return false;
            } else {
                var TAB_GROUP:String = "tabGroup";
                return ((o.hasOwnProperty("col")) || (o.hasOwnProperty(TAB_GROUP)));
            }
        }
    }

}
}