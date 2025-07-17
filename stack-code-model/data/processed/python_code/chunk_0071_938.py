package uidocument.commons.api.document.property {
public class PropertyObject implements IProperty {

    public var name:String;
    public var value:String;
    public var modifiers:String;

    public function PropertyObject(name:String, value:String, modifiers:String="") {
        this.name = name;
        this.value = value;
        this.modifiers = modifiers;
    }

    public function getName():String {
        return this.name;
    }

    public function setName(name:String):void {
        this.name = name;
    }

    public function getValue():String {
        return this.value;
    }

    public function setValue(value:String):void {
        this.value = value;
    }

    public function getModifiers():String {
        return this.modifiers;
    }

    public function setModifiers(modifiers:String):void {
        this.modifiers = modifiers;
    }

    public function toString():String {
        return "Name:"+this.getName()+",Value:"+this.getValue()+",Modifiers:"+this.getModifiers();
    }

    public function addListener(property:IProperty, component:IUpdatable):void {
    }
}
}