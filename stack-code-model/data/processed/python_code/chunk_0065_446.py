package org.ro.core.model {
import org.ro.core.Utils;
import org.ro.view.ImageRepository;

/**
 * Wrapps the adapted object and adds an operation that renders the adaptee as a clickable link in the UI.
 * @see: https://en.wikipedia.org/wiki/Adapter_pattern
 */
dynamic public class ObjectAdapter implements Visible {
    private var _adaptee:Adaptable;
    private var _type:String;
    private var _icon:Class;
    private var _label:String;

    public function ObjectAdapter(adaptee:Adaptable,
                                  label:String = null,
                                  typeSpec:String = null,
                                  icon:Class = null) {
        _adaptee = adaptee;
        _label = label;
        _type = typeSpec;
        _icon = icon;
        if (_type == null) {
            _type = "String";
        }
        if (_icon == null) {
            _icon = ImageRepository.ObjectIcon;
        }
        if (_label == null) {
            _label = "label not set";
        }
        initPropertyAccessors();
    }

    public function toString():String {
        return "[" + _label + " -> " + _type + "]";
    }

    // add properties of the adaptee to the adapter dynamically
    public function initPropertyAccessors():void {
        //first pass: add properties
        const s:String = JSON.stringify(_adaptee);
        const o:Object = JSON.parse(s);
        fromObject(o);
        //second pass: set values from adaptee
        fromAdaptee(o);
    }

    private function fromObject(obj:Object):void {
        for (var prop:String in obj) {
            this[prop] = obj[prop];
        }
    }

    private function fromAdaptee(obj:Object):void {
        var value:Object;
        for (var prop:String in obj) {
            value = _adaptee[prop];
            this[prop] = value;
        }
    }

    public function get adaptee():Adaptable {
        return _adaptee;
    }

    public function getIcon():Class {
        return _icon;
    }

    public function get label():String {
        return _label;
    }

    public function tag():String {
        var tag:String = "";
        if (this.hasOwnProperty("name")) {
            tag = this.name;
        } else if (this.hasOwnProperty("className")) {
            tag = this.className;
        } else {
            tag = "noNameNorClassname";
        }
        tag = Utils.deCamel(tag);
        return tag;
    }

}
}