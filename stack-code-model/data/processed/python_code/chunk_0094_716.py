package com.company.assembleegameclient.ui.options {
import com.company.assembleegameclient.parameters.Parameters;
import com.company.util.MoreColorUtil;

import flash.events.Event;

import kabam.rotmg.text.view.stringBuilder.StringBuilder;

public class ChoiceOption extends BaseOption {


    public function ChoiceOption(_arg_1:String, _arg_2:Vector.<StringBuilder>, _arg_3:Array, _arg_4:String, _arg_5:String, _arg_6:Function, _arg_7:uint = 16777215) {
        super(_arg_1, _arg_4, _arg_5);
        desc_.setColor(_arg_7);
        tooltip_.tipText_.setColor(_arg_7);
        this.callback_ = _arg_6;
        this.choiceBox_ = new ChoiceBox(_arg_2, _arg_3, Parameters.data[paramName_], _arg_7);
        this.choiceBox_.addEventListener("change", this.onChange);
        addChild(this.choiceBox_);
    }
    private var callback_:Function;
    private var choiceBox_:ChoiceBox;

    override public function refresh():void {
        this.choiceBox_.setValue(Parameters.data[paramName_]);
    }

    public function refreshNoCallback():void {
        this.choiceBox_.setValue(Parameters.data[paramName_], false);
    }

    public function enable(_arg_1:Boolean):void {
        transform.colorTransform = !!_arg_1 ? MoreColorUtil.darkCT : MoreColorUtil.identity;
        mouseEnabled = !_arg_1;
        mouseChildren = !_arg_1;
    }

    private function onChange(_arg_1:Event):void {
        Parameters.data[paramName_] = this.choiceBox_.value();
        if (this.callback_ != null) {
            this.callback_();
        }
        Parameters.save();
    }
}
}