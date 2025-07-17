package my.patterns.decorators {
import my.patterns.runwaymodels.Model;

//The Decorator: Abstract class
public class AbstractDresser extends Model {
    public function AbstractDresser(model:Model) {
        this.model = model;
    }

    protected var model:Model;

    override public function getDressed():String {
        return whatToWear;
    }
}
}