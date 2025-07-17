/**
 * Created by nguye on 1/23/2016.
 */
package some.external.lib {
import mx.core.IVisualElement;

import spark.components.Group;

public class BoardItem extends Group{
    public function drawLine(x1:Number, x2:Number, y1:Number, y2:Number):void
    {
        //Abstract, do nothing
    }

    public function drawText(msg:String):void
    {
        //Abstract, do nothing
    }
}
}