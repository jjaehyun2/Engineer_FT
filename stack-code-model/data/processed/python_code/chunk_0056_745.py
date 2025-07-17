//@todo remove listener
package uidocument.commons.api.document.property{

import mx.events.*;
import modifiers.*

[Bindable]
public class BindablePropertyObject extends ExtendedObject implements IUpdatable, IProperty {

    public var name:String;
    public var value:String;
    public var modifiers:String;

    public function BindablePropertyObject(name:String="", value:String="", modifiers:String="") {
        super();
        this.name = name;
        this.value = value;
        this.modifiers = modifiers;
    }


    public function addListener(property:IProperty, setter:IUpdatable):void {
        var currentSetter:IUpdatable = setter;
        currentSetter = new PropertyNameModifier(currentSetter, property.getName());
        if (property.getModifiers().length != 0) {
            var mod:Array = property.getModifiers().split(":");
            for (var i:Number = 0; i < mod.length; i++) {

                currentSetter = ModifierFactory.createModifier(mod[i].toString(),currentSetter);

            }

        }
        this.addEventListener(PropertyChangeEvent.PROPERTY_CHANGE, currentSetter.update);
        currentSetter.update(new PropertyChangeEvent(PropertyChangeEvent.PROPERTY_CHANGE, false, false, PropertyChangeEventKind.UPDATE, name, "", value, this));
    }

    public function removeListener(property:BindablePropertyObject, setter:IUpdatable):void {
        this.removeEventListener(PropertyChangeEvent.PROPERTY_CHANGE, setter.update);
    }

    public function update(val:PropertyChangeEvent):void {
        this.value = ""+val.newValue;
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
        return "Name:"+this.getName+",Value:"+this.getValue()+",Modifiers:"+this.getModifiers();
    }
}
}