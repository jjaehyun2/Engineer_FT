package kabam.rotmg.game.view.components {
import com.company.assembleegameclient.map.mapoverlay.CharacterStatusText;
import com.company.assembleegameclient.objects.GameObject;

public class QueuedStatusText extends CharacterStatusText {


    public function QueuedStatusText(go:GameObject, text:String, color:uint, lifetime:int, offsetTime:int = 0) {
        super(go, text, color, lifetime, offsetTime);
    }
    public var list:QueuedStatusTextList;
    public var next:QueuedStatusText;

    override public function dispose():void {
        this.list.shift();
    }
}
}