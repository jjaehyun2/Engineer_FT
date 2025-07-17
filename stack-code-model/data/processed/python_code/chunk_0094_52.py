/**
 * Created by nguye on 1/30/2016.
 */
package my.pattern {
import some.useful.classes.LineGroup;
import some.useful.classes.TextGroup;

public class MyFacade extends BoardItem {
    private var lineGroup:LineGroup;
    private var textGroup:TextGroup;

    public function MyFacade() {
        lineGroup = new LineGroup();
        textGroup = new TextGroup();
        this.addElement(lineGroup);
        this.addElement(textGroup);
    }

    override public function drawLine(x1:Number, x2:Number, y1:Number, y2:Number):void
    {
        lineGroup.draw(x1,x2,y1,y2);
    }

    override public function drawText(msg:String):void
    {
        textGroup.draw(msg);
    }
}
}