package my.patterns.runwaymodels {
import my.patterns.decorators.AbstractDresser;

//Abstract class for a walking model
public class Model {
    protected var whatToWear:String;

    public function getDressed():String {
        return whatToWear;
    }

    public function wear(dresserClass:Class):Model
    {
        return new dresserClass(this) as Model;
    }
}
}