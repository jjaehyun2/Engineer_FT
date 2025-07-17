package components {

import mx.controls.Label;
import mx.events.PropertyChangeEvent;

public class Text extends Label implements IUpdatable {


    public function Text() {
        super();
    }

    public function update(val:PropertyChangeEvent):void {
        this[val.property] = "" + val.newValue;
    }

}

/*
 public function getBinding(property:String):Updater {
 if (property == "text")
 return new Updater() {
 public function update(value:Object):void {
 this.text = value;
 }
 }
 }
 }
 */

}