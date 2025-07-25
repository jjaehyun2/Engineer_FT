package com.company.assembleegameclient.ui {
import com.company.assembleegameclient.objects.GameObject;
import com.company.assembleegameclient.objects.ObjectLibrary;
import com.company.assembleegameclient.objects.Player;
import com.company.assembleegameclient.util.PlayerUtil;
import com.company.util.MoreColorUtil;

import flash.display.Bitmap;
import flash.display.Sprite;
import flash.filters.DropShadowFilter;
import flash.geom.ColorTransform;

import kabam.rotmg.text.view.TextFieldDisplayConcrete;
import kabam.rotmg.text.view.stringBuilder.TemplateBuilder;

import org.osflash.signals.Signal;

public class GameObjectListItem extends Sprite {


    public function GameObjectListItem(_arg_1:uint, _arg_2:Boolean, _arg_3:GameObject, _arg_4:Boolean = false) {
        super();
        this.positionClassBelow = _arg_4;
        this.isLongVersion = _arg_2;
        this.color = _arg_1;
        this.portrait = new Bitmap();
        this.portrait.x = -4;
        this.portrait.y = !!_arg_4 ? -1 : -4;
        addChild(this.portrait);
        this.text = new TextFieldDisplayConcrete().setSize(13).setColor(_arg_1).setHTML(_arg_2);
        if (!_arg_2) {
            this.text.setTextWidth(66).setTextHeight(20).setBold(true);
        }
        this.text.x = 32;
        this.text.y = 6;
        this.text.filters = [new DropShadowFilter(0, 0, 0)];
        addChild(this.text);
        this.textReady = this.text.textChanged;
        this.draw(_arg_3);
    }
    public var portrait:Bitmap;
    public var isLongVersion:Boolean;
    public var go:GameObject;
    public var textReady:Signal;
    private var text:TextFieldDisplayConcrete;
    private var builder:TemplateBuilder;
    private var color:uint;
    private var objname:String;
    private var _type:int;
    private var level:int;
    private var positionClassBelow:Boolean;

    public function draw(_arg_1:GameObject, _arg_2:ColorTransform = null):void {
        var _local3:Boolean = this.isClear();
        this.go = _arg_1;
        visible = _arg_1 != null;
        if (visible && (this.hasChanged() || _local3)) {
            this.redraw();
            transform.colorTransform = _arg_2 || MoreColorUtil.identity;
        }
    }

    public function clear():void {
        this.go = null;
        visible = false;
    }

    public function isClear():Boolean {
        return this.go == null && !visible;
    }

    private function hasChanged():Boolean {
        var _local1:Boolean = this.go.name_ != this.objname || this.go.level_ != this.level || this.go.objectType_ != this._type;
        _local1 && this.updateData();
        return _local1;
    }

    private function updateData():void {
        this.objname = this.go.name_;
        this.level = this.go.level_;
        this._type = this.go.objectType_;
    }

    private function redraw():void {
        this.portrait.bitmapData = this.go.getPortrait();
        this.text.setStringBuilder(this.prepareText());
        this.text.setColor(this.getDrawColor());
        this.text.update();
    }

    private function prepareText():TemplateBuilder {
        this.builder = this.builder || new TemplateBuilder();
        if (this.isLongVersion) {
            this.applyLongTextToBuilder();
        } else if (this.isNameDefined()) {
            this.builder.setTemplate(this.objname);
        } else {
            this.builder.setTemplate(ObjectLibrary.typeToDisplayId_[this._type]);
        }
        return this.builder;
    }

    private function applyLongTextToBuilder():void {
        var _local1:* = null;
        var _local2:* = {};
        if (this.isNameDefined()) {
            if (this.positionClassBelow) {
                _local1 = "<b>{name}</b>\n({type}{level})";
            } else {
                _local1 = "<b>{name}</b> ({type}{level})";
            }
            _local2.name = this.go.name_;
            _local2.type = ObjectLibrary.typeToDisplayId_[this._type];
            _local2.level = this.level < 1 ? "" : " " + this.level;
        } else {
            _local1 = "<b>{name}</b>";
            _local2.name = ObjectLibrary.typeToDisplayId_[this._type];
        }
        this.builder.setTemplate(_local1, _local2);
    }

    private function isNameDefined():Boolean {
        return this.go.name_ != null && this.go.name_ != "";
    }

    private function getDrawColor():int {
        var _local1:Player = this.go as Player;
        if (_local1) {
            return PlayerUtil.getPlayerNameColor(_local1);
        }
        return this.color;
    }
}
}