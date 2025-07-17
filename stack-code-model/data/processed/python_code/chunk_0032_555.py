package modifiers{

import mx.events.PropertyChangeEvent;

public class LowercaseModifier extends Modifier {

    public function LowercaseModifier(suc:IUpdatable) {
        super(suc);
    }

    override public function update(val:PropertyChangeEvent):void {
        val.newValue = val.newValue.toString().toLocaleLowerCase();
        successor.update(val);
    }
}
}