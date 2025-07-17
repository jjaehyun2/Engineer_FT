package my.patterns.decorators {
import my.patterns.runwaymodels.Model;

public class Muff extends Model {
    override public function getDressed():String {
        return "~muff";
    }
}
}