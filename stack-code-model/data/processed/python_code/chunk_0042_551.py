﻿package com.company.assembleegameclient.ui {
import com.company.assembleegameclient.parameters.Parameters;
import com.company.assembleegameclient.util.TextureRedrawer;

import flash.display.Bitmap;
import flash.display.Sprite;
import flash.events.Event;
import flash.events.MouseEvent;
import flash.events.TimerEvent;
import flash.filters.DropShadowFilter;
import flash.utils.Timer;

import kabam.rotmg.assets.EmbeddedAssets.EmbeddedAssets_progressBarLarge_shapeEmbed_;
import kabam.rotmg.text.view.TextFieldDisplayConcrete;
import kabam.rotmg.text.view.stringBuilder.LineBuilder;
import kabam.rotmg.text.view.stringBuilder.StaticStringBuilder;

import org.osflash.signals.Signal;

public class StatusBar extends Sprite {

    public static var barTextSignal:Signal = new Signal(Boolean);

    public var w_:int;
    public var h_:int;
    public var color_:uint;
    public var backColor_:uint;
    public var pulseBackColor:uint;
    public var textColor_:uint;
    public var val_:Number = -1;
    public var max_:Number = -1;
    public var boost_:int = -1;
    public var maxMax_:int = -1;
    public var level_:int = 0;
    private var labelText_:TextFieldDisplayConcrete;
    private var labelTextStringBuilder_:LineBuilder;
    private var valueText_:TextFieldDisplayConcrete;
    private var valueTextStringBuilder_:StaticStringBuilder;
    private var boostText_:TextFieldDisplayConcrete;
    private var multiplierText:TextFieldDisplayConcrete;
    public var multiplierIcon:Sprite;
    private var colorSprite:Sprite;
    private var defaultForegroundColor:Number;
    private var defaultBackgroundColor:Number;
    public var mouseOver_:Boolean = false;
    private var isPulsing:Boolean = false;
    private var repetitions:int;
    private var direction:int = -1;
    private var speed:Number = 0.1;
    private var enablePercentage:Boolean;

    public function StatusBar(width:int, height:int, foregroundColor:uint, backgroundColor:uint, textKey:String = null, drawShape:Boolean = true, valueSize:int = 14, percentage:Boolean = false) {
        this.enablePercentage = percentage;
        this.colorSprite = new Sprite();
        super();
        addChild(this.colorSprite);
        this.w_ = width + 2;
        this.h_ = height;
        this.defaultForegroundColor = (this.color_ = foregroundColor);
        this.defaultBackgroundColor = (this.backColor_ = backgroundColor);
        this.textColor_ = 0xFFFFFF;
        if (((!((textKey == null))) && (!((textKey.length == 0))))) {
            this.labelText_ = new TextFieldDisplayConcrete().setSize(12).setColor(this.textColor_);
            this.labelText_.setBold(true);
            this.labelTextStringBuilder_ = new LineBuilder().setParams(textKey);
            this.labelText_.setStringBuilder(this.labelTextStringBuilder_);
            this.centerVertically(this.labelText_);
            this.labelText_.filters = [new DropShadowFilter(0, 0, 0)];
            this.labelText_.x = 2;
            addChild(this.labelText_);
        }
        this.valueText_ = new TextFieldDisplayConcrete().setSize(valueSize).setColor(0xFFFFFF);
        this.valueText_.setBold(true);
        this.valueText_.filters = [new DropShadowFilter(0, 0, 0)];
        this.centerVertically(this.valueText_);
        this.valueTextStringBuilder_ = new StaticStringBuilder();
        this.boostText_ = new TextFieldDisplayConcrete().setSize(12).setColor(this.textColor_);
        this.boostText_.setBold(true);
        this.boostText_.alpha = 0.6;
        this.centerVertically(this.boostText_);
        this.boostText_.filters = [new DropShadowFilter(0, 0, 0)];
        this.multiplierIcon = new Sprite();
        this.multiplierIcon.x = (this.w_ - 60);
        this.multiplierIcon.y = -3;
        this.multiplierIcon.graphics.beginFill(0xFF00FF, 0);
        this.multiplierIcon.graphics.drawRect(0, 0, 20, 20);
        this.multiplierIcon.addEventListener(MouseEvent.MOUSE_OVER, this.onMultiplierOver);
        this.multiplierIcon.addEventListener(MouseEvent.MOUSE_OUT, this.onMultiplierOut);
        this.multiplierText = new TextFieldDisplayConcrete().setSize(12).setColor(0xFFFF00);
        this.multiplierText.setBold(true);
        this.multiplierText.setStringBuilder(new StaticStringBuilder("+50% EXP"));
        this.multiplierText.filters = [new DropShadowFilter(0, 0, 0)];
        this.multiplierIcon.addChild(this.multiplierText);
        if (!Parameters.data_.toggleBarText) {
            addEventListener(MouseEvent.ROLL_OVER, this.onMouseOver);
            addEventListener(MouseEvent.ROLL_OUT, this.onMouseOut);
        }
        barTextSignal.add(this.setBarText);
        if (drawShape)
            this.drawProgressBarShape();
    }

    private var bitmap_:Bitmap;

    private function drawProgressBarShape():void {
        this.bitmap_ = new Bitmap();
        this.bitmap_.bitmapData = new EmbeddedAssets_progressBarLarge_shapeEmbed_().bitmapData;
        addChild(this.bitmap_);
    }

    public function centerVertically(_arg1:TextFieldDisplayConcrete):void {
        _arg1.setVerticalAlign(TextFieldDisplayConcrete.MIDDLE);
        _arg1.y = (this.h_ / 2) - 1;
    }

    private function onMultiplierOver(_arg1:MouseEvent):void {
        dispatchEvent(new Event("MULTIPLIER_OVER"));
    }

    private function onMultiplierOut(_arg1:MouseEvent):void {
        dispatchEvent(new Event("MULTIPLIER_OUT"));
    }

    public function draw(value:Number, max:Number, boost:int, maxMax:int = -1, level:int = 0):void {
        if (max > 0) {
            value = Math.min(max, Math.max(0, value));
        }
        if ((((((((value == this.val_)) && ((max == this.max_)))) && ((boost == this.boost_)))) && ((maxMax == this.maxMax_)))) {
            return;
        }
        this.val_ = value;
        this.max_ = max;
        this.boost_ = boost;
        this.maxMax_ = maxMax;
        this.level_ = level;
        this.internalDraw();
    }

    public function setLabelText(_arg1:String, _arg2:Object = null):void {
        this.labelTextStringBuilder_.setParams(_arg1, _arg2);
        this.labelText_.setStringBuilder(this.labelTextStringBuilder_);
    }

    private function setTextColor(_arg1:uint):void {
        this.textColor_ = _arg1;
        if (this.boostText_ != null) {
            this.boostText_.setColor(this.textColor_);
        }
        this.valueText_.setColor(this.textColor_);
    }

    public function setBarText(_arg1:Boolean):void {
        this.mouseOver_ = false;
        if (_arg1) {
            removeEventListener(MouseEvent.ROLL_OVER, this.onMouseOver);
            removeEventListener(MouseEvent.ROLL_OUT, this.onMouseOut);
        }
        else {
            addEventListener(MouseEvent.ROLL_OVER, this.onMouseOver);
            addEventListener(MouseEvent.ROLL_OUT, this.onMouseOut);
        }
        this.internalDraw();
    }

    private function internalDraw():void {
        graphics.clear();
        this.colorSprite.graphics.clear();
        var _local1:uint = 0xFFFFFF;
        if (this.boost_ > 0) {
            _local1 = 6206769;
        }
        if (this.textColor_ != _local1) {
            this.setTextColor(_local1);
        }
        graphics.beginFill(this.backColor_);
        graphics.drawRect(0, 0, this.w_, this.h_);
        graphics.endFill();
        if (this.isPulsing) {
            this.colorSprite.graphics.beginFill(this.pulseBackColor);
            this.colorSprite.graphics.drawRect(0, 0, this.w_, this.h_);
        }
        this.colorSprite.graphics.beginFill(this.color_);
        if (this.max_ > 0) {
            this.colorSprite.graphics.drawRect(0, 0, (this.w_ * (this.val_ / this.max_)), this.h_);
        }
        else {
            this.colorSprite.graphics.drawRect(0, 0, this.w_, this.h_);
        }
        this.colorSprite.graphics.endFill();
        this.colorSprite.filters = [TextureRedrawer.OUTLINE_FILTER];
        if (contains(this.valueText_)) {
            removeChild(this.valueText_);
        }
        if (contains(this.boostText_)) {
            removeChild(this.boostText_);
        }
        if (((Parameters.data_.toggleBarText) || (((this.mouseOver_) && ((this.h_ > 4)))))) {
            this.drawWithMouseOver();
        }
    }

    public function drawWithMouseOver():void {
        var _local2:int;
        var _local1:String = "";

        if (this.enablePercentage)
            this.valueText_.setStringBuilder(this.valueTextStringBuilder_.setString(Parameters.formatValue((this.val_ / this.max_) * 100, 2) + "%"));
        else
            this.valueText_.setStringBuilder(this.valueTextStringBuilder_.setString(("" + this.val_)));

        if (!contains(this.valueText_)) {
            this.valueText_.mouseEnabled = false;
            this.valueText_.mouseChildren = false;
            addChild(this.valueText_);
        }
        if (this.boost_ != 0) {
            this.boostText_.setStringBuilder(this.valueTextStringBuilder_.setString((((" (" + (((this.boost_ > 0)) ? "+" : "")) + this.boost_.toString()) + ")")));
            if (!contains(this.boostText_)) {
                this.boostText_.mouseEnabled = false;
                this.boostText_.mouseChildren = false;
                addChild(this.boostText_);
            }
            this.valueText_.x = ((this.w_ / 2) - ((this.valueText_.width + this.boostText_.width) / 2));
            this.boostText_.x = (this.valueText_.x + this.valueText_.width);
        }
        else {
            this.valueText_.x = ((this.w_ / 2) - (this.valueText_.width / 2));
            if (contains(this.boostText_)) {
                removeChild(this.boostText_);
            }
        }
    }

    public function showMultiplierText():void {
        this.multiplierIcon.mouseEnabled = false;
        this.multiplierIcon.mouseChildren = false;
        addChild(this.multiplierIcon);
        this.startPulse(3, this.color_, 0xFFFFFF);
    }

    public function hideMultiplierText():void {
        if (this.multiplierIcon.parent) {
            removeChild(this.multiplierIcon);
        }
    }

    public function startPulse(_arg1:Number, _arg2:Number, _arg3:Number):void {
        this.isPulsing = true;
        this.color_ = _arg2;
        this.pulseBackColor = _arg3;
        this.repetitions = _arg1;
        this.internalDraw();
        addEventListener(Event.ENTER_FRAME, this.onPulse);
    }
    private function onPulse(_arg1:Event):void {
        if ((((this.colorSprite.alpha > 1)) || ((this.colorSprite.alpha < 0)))) {
            this.direction = (this.direction * -1);
            if (this.colorSprite.alpha > 1) {
                this.repetitions--;
                if (!this.repetitions) {
                    this.isPulsing = false;
                    this.color_ = this.defaultForegroundColor;
                    this.backColor_ = this.defaultBackgroundColor;
                    this.colorSprite.alpha = 1;
                    this.internalDraw();
                    removeEventListener(Event.ENTER_FRAME, this.onPulse);
                }
            }
        }
        this.colorSprite.alpha = (this.colorSprite.alpha + (this.speed * this.direction));
    }

    private function onMouseOver(_arg1:MouseEvent):void {
        this.mouseOver_ = true;
        this.internalDraw();
    }

    private function onMouseOut(_arg1:MouseEvent):void {
        this.mouseOver_ = false;
        this.internalDraw();
    }


}
}