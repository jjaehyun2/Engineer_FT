/**
 * User: booster
 * Date: 07/12/14
 * Time: 17:25
 */
package {
import flash.geom.Point;

import starling.display.Quad;
import starling.display.Sprite;
import starling.events.Touch;
import starling.events.TouchEvent;
import starling.events.TouchPhase;
import starling.utils.Color;

public class CameraSprite extends Sprite {
    private var _bgQuad:Quad;
    private var _anchorQuad:Quad;

    public function CameraSprite(width:Number, height:Number, anchorX:Number, anchorY:Number) {
        _bgQuad = new Quad(width, height, Color.BLACK);
        addChild(_bgQuad);

        _anchorQuad = new Quad(0.5, 0.5, Color.WHITE);
        _anchorQuad.alignPivot();
        addChild(_anchorQuad);

        pivotX = anchorX;
        pivotY = anchorY;

        addEventListener(TouchEvent.TOUCH, onTouch);
        useHandCursor = true;
    }

    override public function set pivotX(value:Number):void {
        super.pivotX = value;
        _anchorQuad.x = value;
    }

    override public function set pivotY(value:Number):void {
        super.pivotY = value;
        _anchorQuad.y = value;
    }

    private function onTouch(event:TouchEvent):void {
        var touches:Vector.<Touch> = event.getTouches(this, TouchPhase.MOVED);

        if(touches.length == 0)
            return;

        // one finger touching -> move
        var delta:Point = touches[0].getMovement(parent);
        x += delta.x;
        y += delta.y;
    }

    public override function dispose():void {
        removeEventListener(TouchEvent.TOUCH, onTouch);
        super.dispose();
    }
}
}