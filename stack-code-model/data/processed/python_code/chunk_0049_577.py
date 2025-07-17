package my.patterns.decorators {
import my.patterns.runwaymodels.Model;

public class Bow extends Model {
    override public function getDressed():String {
        return "~bow";
    }
}
}