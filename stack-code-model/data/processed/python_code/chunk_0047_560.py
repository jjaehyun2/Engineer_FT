﻿package kabam.rotmg.chat.view {
import flash.display.Sprite;
import flash.display.Stage;
import flash.events.Event;
import flash.events.KeyboardEvent;

import kabam.rotmg.account.core.Account;
import kabam.rotmg.account.core.signals.RegisterSignal;
import kabam.rotmg.account.core.view.RegisterPromptDialog;
import kabam.rotmg.account.web.model.AccountData;
import kabam.rotmg.chat.control.ScrollListSignal;
import kabam.rotmg.chat.control.ShowChatInputSignal;
import kabam.rotmg.chat.model.ChatModel;
import kabam.rotmg.chat.model.ChatShortcutModel;
import kabam.rotmg.chat.model.TellModel;
import kabam.rotmg.dialogs.control.CloseDialogsSignal;
import kabam.rotmg.dialogs.control.OpenDialogSignal;
import kabam.rotmg.text.model.TextKey;
import kabam.rotmg.ui.model.HUDModel;

import robotlegs.bender.bundles.mvcs.Mediator;

public class ChatMediator extends Mediator {

    private static const SCROLL_BUFFER_SIZE:int = 10;

    [Inject]
    public var view:Chat;
    [Inject]
    public var model:ChatModel;
    [Inject]
    public var account:Account;
    [Inject]
    public var shortcuts:ChatShortcutModel;
    [Inject]
    public var showChatInput:ShowChatInputSignal;
    [Inject]
    public var scrollList:ScrollListSignal;
    [Inject]
    public var tellModel:TellModel;
    [Inject]
    public var hudModel:HUDModel;
    [Inject]
    public var openDialog:OpenDialogSignal;
    [Inject]
    public var closeDialog:CloseDialogsSignal;
    [Inject]
    public var register:RegisterSignal;
    private var stage:Stage;
    private var scrollDirection:int;
    private var scrollBuffer:int;
    private var listenersAdded:Boolean = false;


    override public function initialize():void {
        this.view.x = this.model.bounds.left;
        this.view.y = this.model.bounds.top;
        this.view.setup(this.model, this.account.isRegistered());
        this.stage = this.view.stage;
        this.addListeners();
        this.showChatInput.add(this.onShowChatInput);
        this.openDialog.add(this.onOpenDialog);
        this.closeDialog.add(this.onCloseDialog);
        this.register.add(this.onRegister);
    }

    private function onOpenDialog(_arg1:Sprite):void {
        this.removeListeners();
    }

    private function onCloseDialog():void {
        this.addListeners();
    }

    private function onShowChatInput(_arg1:Boolean, _arg2:String):void {
        if (_arg1) {
            this.stage.focus = this.view;
            this.listenersAdded = false;
        }
        else {
            this.addListeners();
            this.stage.focus = null;
        }
    }

    private function onRegister(_arg1:AccountData):void {
        if (_arg1.error == null) {
            this.view.removeRegisterBlock();
        }
    }

    override public function destroy():void {
        this.removeListeners();
        this.showChatInput.remove(this.onShowChatInput);
        this.openDialog.remove(this.onOpenDialog);
        this.closeDialog.remove(this.onCloseDialog);
        this.register.remove(this.onRegister);
        this.stage = null;
    }

    private function addListeners():void {
        if (!this.listenersAdded) {
            this.stage.addEventListener(KeyboardEvent.KEY_DOWN, this.onKeyDown);
            this.stage.addEventListener(KeyboardEvent.KEY_UP, this.onKeyUp);
            this.listenersAdded = true;
        }
    }

    private function removeListeners():void {
        if (this.listenersAdded) {
            this.stage.removeEventListener(KeyboardEvent.KEY_DOWN, this.onKeyDown);
            this.stage.removeEventListener(KeyboardEvent.KEY_UP, this.onKeyUp);
            this.stage.removeEventListener(Event.ENTER_FRAME, this.iterate);
            this.listenersAdded = false;
        }
    }

    private function onKeyDown(_arg1:KeyboardEvent):void {
        if (_arg1.keyCode == this.shortcuts.getScrollUp()) {
            this.setupScroll(-1);
        }
        else {
            if (_arg1.keyCode == this.shortcuts.getScrollDown()) {
                this.setupScroll(1);
            }
        }
    }

    private function setupScroll(_arg1:int):void {
        this.scrollDirection = _arg1;
        this.scrollList.dispatch(_arg1);
        this.scrollBuffer = 0;
        this.view.addEventListener(Event.ENTER_FRAME, this.iterate);
    }

    private function iterate(_arg1:Event):void {
        if (this.scrollBuffer++ >= SCROLL_BUFFER_SIZE) {
            this.scrollList.dispatch(this.scrollDirection);
        }
    }

    private function onKeyUp(_arg1:KeyboardEvent):void {
        if (this.listenersAdded) {
            this.checkForInputTrigger(_arg1.keyCode);
        }
        if ((((_arg1.keyCode == this.shortcuts.getScrollUp())) || ((_arg1.keyCode == this.shortcuts.getScrollDown())))) {
            this.view.removeEventListener(Event.ENTER_FRAME, this.iterate);
        }
    }

    private function checkForInputTrigger(_arg1:uint):void {
        if ((((this.stage.focus == null)) || ((_arg1 == this.shortcuts.getTellShortcut())))) {
            if (_arg1 == this.shortcuts.getCommandShortcut()) {
                this.triggerOrPromptRegistration("/");
            }
            else {
                if (_arg1 == this.shortcuts.getChatShortcut()) {
                    this.triggerOrPromptRegistration("");
                }
                else {
                    if (_arg1 == this.shortcuts.getGuildShortcut()) {
                        this.triggerOrPromptRegistration("/g ");
                    }
                    else {
                        if (_arg1 == this.shortcuts.getGlobalChatShortcut()) {
                            this.triggerOrPromptRegistration("/gchat ");
                        } else {
                            if (_arg1 == this.shortcuts.getTellShortcut()) {
                                var _local1:String = this.tellModel.getNext();
                                var _local2:String = ("/tell{FORMATINPUT}").replace("{FORMATINPUT}", (_local1 == null || _local1 == "") ? " " : " " + this.tellModel.getNext() + " ");
                                this.triggerOrPromptRegistration(_local2);
                            }
                        }
                    }
                }
            }
        }
    }

    private function triggerOrPromptRegistration(_arg1:String):void {
        if (this.account.isRegistered()) {
            this.showChatInput.dispatch(true, _arg1);
        }
        else {
            if (((!((this.hudModel.gameSprite == null))) && (this.hudModel.gameSprite.evalIsNotInCombatMapArea()))) {
                this.openDialog.dispatch(new RegisterPromptDialog(TextKey.CHAT_REGISTER_TO_CHAT));
            }
        }
    }


}
}