package kabam.rotmg.core.model {
import com.company.assembleegameclient.map.Map;
import com.company.assembleegameclient.objects.IInteractiveObject;

public class MapModel {

    public function MapModel() {
        super();
    }
    public var currentInteractiveTarget:IInteractiveObject;
    public var currentInteractiveTargetObjectId:int;
    public var currentMap:Map;
}
}