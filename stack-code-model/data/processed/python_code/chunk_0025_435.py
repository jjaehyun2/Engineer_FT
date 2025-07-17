package modifier{

import mx.events.PropertyChangeEvent;

public class PropertyNameModifier extends Modifier {

    private var name:String;

    public function PropertyNameModifier(suc:IUpdater,name:String) {
        super(suc);
        this.name = name;
    }

    override public function update(val:PropertyChangeEvent):void {
        val.property = name;
        successor.update(val);
    }
}
}