//@todo property/properties
package components.actionstore {

import uidocument.commons.api.document.Property;

public class Action {

    private var trigger:String;
    private var action:String;
    private var properties:Property;

    public function Action(trigger:String,action:String,properties:Property) {
        this.trigger = trigger;
        this.action  = action;
        this.properties = properties;
    }

    public function getTrigger():String {
        return trigger;
    }

    public function setTrigger(trigger:String):void {
        this.trigger = trigger;
    }

    public function getAction():String {
        return action;
    }

    public function setAction(trigger:String):void {
        this.action = action;
    }

    public function getProperties():Property {
        return properties;
    }

    public function setProperties(properties:Property):void {
        this.properties = properties;
    }
}
}