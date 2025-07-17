package org.ro.core {
import mx.controls.Alert;

public class Utils {

    public static function endsWith(obj:String, qry:String):Boolean {
        var qLen:uint = qry.length;
        var oLen:uint = obj.length;
        if (qLen > oLen) {
            return false;
        }
        var end:String = obj.substr(oLen - qLen, oLen);
        return (end == qry);
    }

    public static function camelCase(input:String):String {
        var firstChar:String = input.charAt(0).toUpperCase();
        var output:String = firstChar + input.substr(1, input.length);
        return output;
    }

    public static function deCamel(input:String):String {
        var output:String = "";
        var c:String;
        for (var i:uint = 0; i < input.length; i++) {
            c = input.charAt(i);
            if (i == 0) {
                output += c.toUpperCase();
            } else {
                if (c.toUpperCase() == c) {
                    c = " " + c;
                }
                output += c;
            }
        }
        return output;
    }

    public static function isEmptyObject(obj:Object):Boolean {
        return JSON.stringify(obj) === '{}';
    }

    // https://stackoverflow.com/questions/15816008/in-as3-how-to-check-if-two-json-objects-are-equal
    public static function areEqual(a:Object, b:Object):Boolean {
        if (a === null || a is Number || a is Boolean || a is String) {
            // Compare primitive values.
            return a === b;
        } else {
            var p:*;
            for (p in a) {
                // Check if a and b have different values for p.
                if (!areEqual(a[p], b[p])) {
                    return false;
                }
            }
            for (p in b) {
                // Check if b has a value which a does not.
                if (!a[p]) {
                    return false;
                }
            }
            return true;
        }
        return false;
    }

    public static function replace(json:Object, oldKey:String, newKey:String):Object {
        var origin:String = JSON.stringify(json);
        if (origin.indexOf(oldKey) > 0) {
            var answer:String = origin.replace(oldKey, newKey);
            return JSON.parse(answer);
        }
        return json;
    }

    public static function getSelfHref(value:Object):String {
        var links:Array = value.links; // rel==self
        for each (var l:Object in links) {
            if (l.rel == "self") {
                return l.href;
            }
        }
        return null;
    }

    //TODO unify with getSelfHref, eventually use Builder pattern / fluent Interface 
    // (.fromString(response).linkNamed(SELF|UP|LAYOUT)
    public static function getUpHref(response:String):String {
        var object:Object = JSON.parse(response);
        var links:Array;
        var val:Object = object.value;
        if (val is Array) {
            links = val as Array;
        }
        if (links == null) {
            links = object.links;
        }
        for each (var l:Object in links) {
            if (l.rel == "up") {
                return l.href;
            }
        }
        return null;
    }

    public static function toJsonObject(jsonStr:String):Object {
        var jsonObject:Object;
        try {
            jsonObject = JSON.parse(jsonStr);
        } catch (err:Error) {
            Alert.show("Error: " + err.message);
        }
        finally {
            // Code that runs whether an error was thrown. This code can clean 
            // up after the error, or take steps to keep the application running. 
        }
        return jsonObject;
    }

    public static function toJsonString(jsonObj:Object):String {
        var jsonStr:String;
        try {
            jsonStr = JSON.stringify(jsonObj);
        } catch (err:Error) {
            Alert.show("Error: " + err.message);
        }
        finally {
            // Code that runs whether an error was thrown. This code can clean 
            // up after the error, or take steps to keep the application running. 
        }
        return jsonStr;
    }

    public static function htmlTip(jsonObj:Object):String {
        var str:String = JSON.stringify(jsonObj, null, 4);
        var xml:XML = XML(str);
        return xml;
    }

}
}