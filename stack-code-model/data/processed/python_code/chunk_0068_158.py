package modifiers{

import mx.events.PropertyChangeEvent;

public class UppercaseModifier extends Modifier {

    public function UppercaseModifier(suc:IUpdatable) {
        super(suc);
    }

    override public function update(val:PropertyChangeEvent):void {
        val.newValue = val.newValue.toString().toLocaleUpperCase();
        successor.update(val);
    }
}
}