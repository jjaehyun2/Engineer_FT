package my.patterns.decorators {
import my.patterns.runwaymodels.Model;

public class OrangeDress extends Model {
    override public function getDressed():String {
        return "~orangedress";
    }
}
}