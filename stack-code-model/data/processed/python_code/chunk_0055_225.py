/**
 * Created with IntelliJ IDEA.
 * User: sboichon
 * Date: 13-11-01
 * Time: 12:26
 * To change this template use File | Settings | File Templates.
 */
package {
import flash.display.DisplayObjectContainer;
import flash.geom.Rectangle;

/** Quick and dirty code to show a simple UI in the sample application ***/
/** Button Layout */
class ButtonLayout
{
    private var buttons:Array;
    private var rect:Rectangle;
    private var padding:Number;
    private var parent:DisplayObjectContainer;

    public function ButtonLayout(rect:Rectangle,padding:Number)
    {
        this.rect=rect;
        this.padding=padding;
        this.buttons=new Array();
    }

    public function addButton(btn:SimpleButton):uint
    {
        return buttons.push(btn);
    }

    public function removeButton(btn:SimpleButton):void
    {
        buttons.splice(buttons.indexOf(btn), 1);
        parent.removeChild(btn);
    }

    private function attach(parent:DisplayObjectContainer):void
    {
        this.parent=parent;
        for each(var btn:SimpleButton in this.buttons)
        {
            parent.addChild(btn);
        }
    }

    private function layout():void
    {
        var btnX:Number=rect.x+padding;
        var btnY:Number=rect.y;
        for each( var btn:SimpleButton in this.buttons)
        {
            btn.height=rect.height/this.buttons.length;
            btn.width=rect.width-(padding*2);
            btnY+=this.padding;
            btn.x=btnX;
            btn.y=btnY;
            btnY+=btn.height;
        }
    }

   public function update(parent:DisplayObjectContainer):void
   {
        this.parent = parent;
        attach(parent);
        layout();
   }
}
}