package pub.media {
import mx.controls.Image;

import uidocument.commons.api.document.Element;
import mx.events.PropertyChangeEvent;

public class Still extends Image implements IUpdater  {

    public function Still(element:Element) {
        super();
        this.x = element.getPosition().getX();
        this.y = element.getPosition().getY();
        this.load(element.getPropertyByName("url")[1]);
    }

    public function update(val:PropertyChangeEvent):void {
        this[val.property] = "" + val.newValue;
    }

}

}