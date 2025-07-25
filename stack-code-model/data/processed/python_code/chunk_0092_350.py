package kabam.lib.console.view {
import kabam.lib.console.model.Console;
import kabam.lib.console.signals.ConsoleLogSignal;

import robotlegs.bender.bundles.mvcs.Mediator;

public final class ConsoleInputMediator extends Mediator {

    private static const ERROR_PATTERN:String = "[0xFF3333:error - \"${value}\" not found]";

    private static const ACTION_PATTERN:String = "[0xFFEE00:${value}]";

    public function ConsoleInputMediator() {
        super();
    }

    [Inject]
    public var view:ConsoleInputView;
    [Inject]
    public var console:Console;
    [Inject]
    public var log:ConsoleLogSignal;

    override public function initialize():void {
        addViewListener("ConsoleEvent.INPUT", this.onInput, ConsoleEvent);
        addViewListener("ConsoleEvent.GET_PREVIOUS", this.onGetPrevious, ConsoleEvent);
        addViewListener("ConsoleEvent.GET_NEXT", this.onGetNext, ConsoleEvent);
    }

    override public function destroy():void {
        removeViewListener("ConsoleEvent.INPUT", this.onInput, ConsoleEvent);
        removeViewListener("ConsoleEvent.GET_PREVIOUS", this.onGetPrevious, ConsoleEvent);
        removeViewListener("ConsoleEvent.GET_NEXT", this.onGetNext, ConsoleEvent);
    }

    private function logInput(_arg_1:String):void {
        if (this.console.hasAction(_arg_1)) {
            this.logAction(_arg_1);
        } else {
            this.logError(_arg_1);
        }
    }

    private function logAction(_arg_1:String):void {
        var _local2:Array = _arg_1.split(" ");
        _local2[0] = "[0xFFEE00:${value}]".replace("${value}", _local2[0]);
        this.log.dispatch(_local2.join(" "));
    }

    private function logError(_arg_1:String):void {
        var _local2:String = "[0xFF3333:error - \"${value}\" not found]".replace("${value}", _arg_1);
        this.log.dispatch(_local2);
    }

    private function onInput(_arg_1:ConsoleEvent):void {
        var _local2:String = _arg_1.data;
        this.logInput(_local2);
        this.console.execute(_local2);
    }

    private function onGetPrevious(_arg_1:ConsoleEvent):void {
        this.view.text = this.console.getPreviousAction();
    }

    private function onGetNext(_arg_1:ConsoleEvent):void {
        this.view.text = this.console.getNextAction();
    }
}
}