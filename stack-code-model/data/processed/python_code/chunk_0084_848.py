package {

import flash.display.GradientType;
import flash.display.Sprite;
import flash.display.StageAlign;
import flash.display.StageScaleMode;
import flash.events.TimerEvent;
import flash.events.TouchEvent;
import flash.text.TextField;
import flash.ui.Multitouch;
import flash.ui.MultitouchInputMode;
import flash.utils.Timer;

[SWF(width=320, height=460, frameRate=24, backgroundColor=0xEB7F00)]
public class UnresponsiveTouch extends Sprite
{
    public function UnresponsiveTouch()
    {
        super();

        stage.scaleMode = StageScaleMode.NO_SCALE;
        stage.align = StageAlign.TOP_LEFT;

        var textField:TextField = new TextField();
        textField.text = "Hello, World";
        addChild(textField);

        Multitouch.inputMode = MultitouchInputMode.TOUCH_POINT;
        stage.addEventListener(TouchEvent.TOUCH_BEGIN, touchBeginHandler);
    }

    private function touchBeginHandler(event:TouchEvent):void
    {
        var touch:Sprite = new Sprite();
        touch.x = event.stageX;
        touch.y = event.stageY;
        touch.graphics.beginGradientFill(GradientType.RADIAL, [0x39B449, 0x39B449], [1.0, 0.0], [0, 255]);
        touch.graphics.drawCircle(0, 0, 50);
        touch.graphics.endFill();
        addChild(touch);

        var timer:Timer = new Timer(1000, 1);
        timer.addEventListener(TimerEvent.TIMER_COMPLETE, function(event:TimerEvent):void
        {
            timer.removeEventListener(TimerEvent.TIMER_COMPLETE, arguments.callee);

            removeChild(touch);
        });
        timer.start();
    }
}
}