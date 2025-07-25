﻿package com.company.assembleegameclient.ui.guild {
import com.company.assembleegameclient.ui.dialogs.Dialog;
import com.company.assembleegameclient.util.GuildUtil;
import com.company.rotmg.graphics.DeleteXGraphic;
import com.company.util.MoreColorUtil;

import flash.display.Bitmap;
import flash.display.Graphics;
import flash.display.Sprite;
import flash.events.Event;
import flash.events.MouseEvent;
import flash.filters.DropShadowFilter;
import flash.geom.ColorTransform;
import flash.text.TextFieldAutoSize;

import kabam.rotmg.core.StaticInjectorContext;
import kabam.rotmg.dialogs.control.CloseDialogsSignal;
import kabam.rotmg.dialogs.control.OpenDialogSignal;
import kabam.rotmg.text.model.TextKey;
import kabam.rotmg.text.view.TextFieldDisplayConcrete;
import kabam.rotmg.text.view.stringBuilder.LineBuilder;
import kabam.rotmg.text.view.stringBuilder.StaticStringBuilder;

internal class MemberListLine extends Sprite {

    public static const WIDTH:int = 756;
    public static const HEIGHT:int = 32;
    protected static const mouseOverCT:ColorTransform = new ColorTransform(1, (220 / 0xFF), (133 / 0xFF));

    private var name_:String;
    private var rank_:int;
    private var placeText_:TextFieldDisplayConcrete;
    private var nameText_:TextFieldDisplayConcrete;
    private var guildFameText_:TextFieldDisplayConcrete;
    private var guildFameIcon_:Bitmap;
    private var rankIcon_:Bitmap;
    private var rankText_:TextFieldDisplayConcrete;
    private var promoteButton_:Sprite;
    private var demoteButton_:Sprite;
    private var removeButton_:Sprite;

    public function MemberListLine(_arg1:int, _arg2:String, _arg3:int, _arg4:int, _arg5:Boolean, _arg6:int) {
        var _local7:uint;
        super();
        this.name_ = _arg2;
        this.rank_ = _arg3;
        _local7 = 0xB3B3B3;
        if (_arg5) {
            _local7 = 16564761;
        }
        this.placeText_ = new TextFieldDisplayConcrete().setSize(22).setColor(_local7);
        this.placeText_.setStringBuilder(new StaticStringBuilder((_arg1.toString() + ".")));
        this.placeText_.filters = [new DropShadowFilter(0, 0, 0, 1, 8, 8)];
        this.placeText_.x = (60 - this.placeText_.width);
        this.placeText_.y = 4;
        addChild(this.placeText_);
        this.nameText_ = new TextFieldDisplayConcrete().setSize(22).setColor(_local7);
        this.nameText_.setStringBuilder(new StaticStringBuilder(_arg2));
        this.nameText_.filters = [new DropShadowFilter(0, 0, 0, 1, 8, 8)];
        this.nameText_.x = 100;
        this.nameText_.y = 4;
        addChild(this.nameText_);
        this.guildFameText_ = new TextFieldDisplayConcrete().setSize(22).setColor(_local7);
        this.guildFameText_.setAutoSize(TextFieldAutoSize.RIGHT);
        this.guildFameText_.setStringBuilder(new StaticStringBuilder(_arg4.toString()));
        this.guildFameText_.filters = [new DropShadowFilter(0, 0, 0, 1, 8, 8)];
        this.guildFameText_.x = 408;
        this.guildFameText_.y = 4;
        addChild(this.guildFameText_);
        this.guildFameIcon_ = new Bitmap(GuildUtil.guildFameIcon(40));
        this.guildFameIcon_.x = 400;
        this.guildFameIcon_.y = ((HEIGHT / 2) - (this.guildFameIcon_.height / 2));
        addChild(this.guildFameIcon_);
        this.rankIcon_ = new Bitmap(GuildUtil.rankToIcon(_arg3, 20));
        this.rankIcon_.x = 548;
        this.rankIcon_.y = ((HEIGHT / 2) - (this.rankIcon_.height / 2));
        addChild(this.rankIcon_);
        this.rankText_ = new TextFieldDisplayConcrete().setSize(22).setColor(_local7);
        this.rankText_.setStringBuilder(new LineBuilder().setParams(GuildUtil.rankToString(_arg3)));
        this.rankText_.filters = [new DropShadowFilter(0, 0, 0, 1, 8, 8)];
        this.rankText_.setVerticalAlign(TextFieldDisplayConcrete.MIDDLE);
        this.rankText_.x = 580;
        this.rankText_.y = (HEIGHT / 2);
        addChild(this.rankText_);
        if (GuildUtil.canPromote(_arg6, _arg3)) {
            this.promoteButton_ = this.createArrow(true);
            this.addHighlighting(this.promoteButton_);
            this.promoteButton_.addEventListener(MouseEvent.CLICK, this.onPromote);
            this.promoteButton_.x = (670 + 6);
            this.promoteButton_.y = (HEIGHT / 2);
            addChild(this.promoteButton_);
        }
        if (GuildUtil.canDemote(_arg6, _arg3)) {
            this.demoteButton_ = this.createArrow(false);
            this.addHighlighting(this.demoteButton_);
            this.demoteButton_.addEventListener(MouseEvent.CLICK, this.onDemote);
            this.demoteButton_.x = (700 + 6);
            this.demoteButton_.y = (HEIGHT / 2);
            addChild(this.demoteButton_);
        }
        if (GuildUtil.canRemove(_arg6, _arg3)) {
            this.removeButton_ = new DeleteXGraphic();
            this.addHighlighting(this.removeButton_);
            this.removeButton_.addEventListener(MouseEvent.CLICK, this.onRemove);
            this.removeButton_.x = 730;
            this.removeButton_.y = ((HEIGHT / 2) - (this.removeButton_.height / 2));
            addChild(this.removeButton_);
        }
    }

    private function createArrow(_arg1:Boolean):Sprite {
        var _local2:Sprite = new Sprite();
        var _local3:Graphics = _local2.graphics;
        _local3.beginFill(0xFFFFFF);
        _local3.moveTo(-8, -6);
        _local3.lineTo(8, -6);
        _local3.lineTo(0, 6);
        _local3.lineTo(-8, -6);
        if (_arg1) {
            _local2.rotation = 180;
        }
        return (_local2);
    }

    private function addHighlighting(_arg1:Sprite):void {
        _arg1.addEventListener(MouseEvent.MOUSE_OVER, this.onHighlightOver);
        _arg1.addEventListener(MouseEvent.ROLL_OUT, this.onHighlightOut);
    }

    private function onHighlightOver(_arg1:MouseEvent):void {
        var _local2:Sprite = (_arg1.currentTarget as Sprite);
        _local2.transform.colorTransform = mouseOverCT;
    }

    private function onHighlightOut(_arg1:MouseEvent):void {
        var _local2:Sprite = (_arg1.currentTarget as Sprite);
        _local2.transform.colorTransform = MoreColorUtil.identity;
    }

    private function onPromote(_arg1:MouseEvent):void {
        var _local2:String = GuildUtil.rankToString(GuildUtil.promotedRank(this.rank_));
        var _local3:Dialog = new Dialog("", "", TextKey.PROMOTE_LEFTBUTTON, TextKey.PROMOTE_RIGHTBUTTON, "/promote");
        _local3.setTextParams(TextKey.PROMOTE_TEXT, {
            "name": this.name_,
            "rank": _local2
        });
        _local3.setTitleStringBuilder(new LineBuilder().setParams(TextKey.PROMOTE_TITLE, {"name": this.name_}));
        _local3.addEventListener(Dialog.LEFT_BUTTON, this.onCancelDialog);
        _local3.addEventListener(Dialog.RIGHT_BUTTON, this.onVerifiedPromote);
        StaticInjectorContext.getInjector().getInstance(OpenDialogSignal).dispatch(_local3);
    }

    private function onVerifiedPromote(_arg1:Event):void {
        dispatchEvent(new GuildPlayerListEvent(GuildPlayerListEvent.SET_RANK, this.name_, GuildUtil.promotedRank(this.rank_)));
        StaticInjectorContext.getInjector().getInstance(CloseDialogsSignal).dispatch();
    }

    private function onDemote(_arg1:MouseEvent):void {
        var _local2:String = GuildUtil.rankToString(GuildUtil.demotedRank(this.rank_));
        var _local3:Dialog = new Dialog("", "", TextKey.DEMOTE_LEFT, TextKey.DEMOTE_RIGHT, "/demote");
        _local3.setTextParams(TextKey.DEMOTE_TEXT, {
            "name": this.name_,
            "rank": _local2
        });
        _local3.setTitleStringBuilder(new LineBuilder().setParams(TextKey.DEMOTE_TITLE, {"name": this.name_}));
        _local3.addEventListener(Dialog.LEFT_BUTTON, this.onCancelDialog);
        _local3.addEventListener(Dialog.RIGHT_BUTTON, this.onVerifiedDemote);
        StaticInjectorContext.getInjector().getInstance(OpenDialogSignal).dispatch(_local3);
    }

    private function onVerifiedDemote(_arg1:Event):void {
        dispatchEvent(new GuildPlayerListEvent(GuildPlayerListEvent.SET_RANK, this.name_, GuildUtil.demotedRank(this.rank_)));
        StaticInjectorContext.getInjector().getInstance(CloseDialogsSignal).dispatch();
    }

    private function onRemove(_arg1:MouseEvent):void {
        var _local2:Dialog = new Dialog("", "", TextKey.REMOVE_LEFT, TextKey.REMOVE_RIGHT, "/removeFromGuild");
        _local2.setTextParams(TextKey.REMOVE_TEXT, {"name": this.name_});
        _local2.setTitleStringBuilder(new LineBuilder().setParams(TextKey.REMOVE_TITLE, {"name": this.name_}));
        _local2.addEventListener(Dialog.LEFT_BUTTON, this.onCancelDialog);
        _local2.addEventListener(Dialog.RIGHT_BUTTON, this.onVerifiedRemove);
        StaticInjectorContext.getInjector().getInstance(OpenDialogSignal).dispatch(_local2);
    }

    private function onVerifiedRemove(_arg1:Event):void {
        StaticInjectorContext.getInjector().getInstance(CloseDialogsSignal).dispatch();
        dispatchEvent(new GuildPlayerListEvent(GuildPlayerListEvent.REMOVE_MEMBER, this.name_));
    }

    private function onCancelDialog(_arg1:Event):void {
        StaticInjectorContext.getInjector().getInstance(CloseDialogsSignal).dispatch();
    }


}
}