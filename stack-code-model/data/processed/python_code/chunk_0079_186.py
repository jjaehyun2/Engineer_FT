package components {

import mx.controls.TextArea;
import mx.events.PropertyChangeEvent;
import components.actionstore.*;

public class Input extends TextArea implements IUpdatable, IActionStore {

    private var actions:ActionStore;

    public function Input() {
        super();
        actions = new ActionStore();
    }

    public function update(val:PropertyChangeEvent):void {
        this[val.property] = "" + val.newValue;
    }

    public function getBehavior(trigger:String):Action {
        return actions.getBehavior(trigger);
    }

    public function addBehavior(action:Action):void {
        actions.addBehavior(action);
    }

    public function removeBehavior(trigger:String):void {
        actions.removeBehavior(trigger);
    }

}
}