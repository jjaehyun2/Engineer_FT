package modifier{

import mx.events.PropertyChangeEvent;

//Abstract class

public class Modifier implements IUpdater {

    protected var successor:IUpdater;

    public function Modifier(suc:IUpdater) {
        setSuccessor(suc);
    }

    public function setSuccessor(successor:IUpdater):void {
        this.successor = successor;
    }

    public function update(val:PropertyChangeEvent):void {
        successor.update(val);
    }


}
}