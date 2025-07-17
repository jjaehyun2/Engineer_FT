package my.patterns.decorators {
import my.patterns.runwaymodels.Model;

public class Bow extends AbstractDresser {
    public function Bow(model:Model) {
        super(model);
    }
    override public function getDressed():String {
        return model.getDressed() + "~bow";
    }
}
}