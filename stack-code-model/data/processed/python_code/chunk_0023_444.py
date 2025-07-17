package my.patterns.decorators {
import my.patterns.runwaymodels.Model;

public class BlueDress extends Model{
    public function BlueDress() {
    }

    override public function getDressed():String {
        return "~bluedress";
    }
}
}