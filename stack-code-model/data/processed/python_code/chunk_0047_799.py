/**
 * Created by max.rozdobudko@gmail.com on 21.10.2019.
 */
package com.github.airext.keyboard {
import com.github.airext.keyboard.enum.AutoCapitalization;
import com.github.airext.keyboard.enum.AutoCorrection;
import com.github.airext.keyboard.enum.NativeKeyboardType;
import com.github.airext.keyboard.enum.ReturnKeyType;
import com.github.airext.keyboard.enum.SpellChecking;

import flash.events.Event;
import flash.events.EventDispatcher;
import flash.net.registerClassAlias;

public class NativeKeyboardTextParams extends EventDispatcher {

    //--------------------------------------------------------------------------
    //
    //  Static initialization
    //
    //--------------------------------------------------------------------------

    {
        registerClassAlias("com.github.airext.keyboard.NativeKeyboardTextParams", NativeKeyboardTextParams);
    }

    //--------------------------------------------------------------------------
    //
    //  Constructor
    //
    //--------------------------------------------------------------------------

    public function NativeKeyboardTextParams() {
        super();
    }

    //--------------------------------------------------------------------------
    //
    //  Properties
    //
    //--------------------------------------------------------------------------

    //-------------------------------------
    //  text
    //-------------------------------------

    private var _text: String = null;
    [Bindable(event="textChanged")]
    public function get text(): String {
        return _text;
    }

    public function set text(value: String): void {
        if (value == _text) return;
        _text = value;
        dispatchEvent(new Event("textChanged"));
    }

    //-------------------------------------
    //  isSecureTextEntry
    //-------------------------------------

    private var _isSecureTextEntry: Boolean = false;
    [Bindable(event="isSecureTextEntryChanged")]
    public function get isSecureTextEntry(): Boolean {
        return _isSecureTextEntry;
    }

    public function set isSecureTextEntry(value: Boolean): void {
        if (value == _isSecureTextEntry) return;
        _isSecureTextEntry = value;
        dispatchEvent(new Event("isSecureTextEntryChanged"));
    }

    //-------------------------------------
    //  maxCharactersCount
    //-------------------------------------

    private var _maxCharactersCount: int;
    [Bindable(event="maxCharactersCountChanged")]
    public function get maxCharactersCount(): int {
        return _maxCharactersCount;
    }

    public function set maxCharactersCount(value: int): void {
        if (value == _maxCharactersCount) return;
        _maxCharactersCount = value;
        dispatchEvent(new Event("maxCharactersCountChanged"));
    }

    //-------------------------------------
    //  keyboardType
    //-------------------------------------

    private var _keyboardType: NativeKeyboardType;
    [Bindable(event="keyboardTypeChanged")]
    public function get keyboardType(): NativeKeyboardType {
        return _keyboardType || NativeKeyboardType.Default;
    }
    public function set keyboardType(value: NativeKeyboardType): void {
        if (value == _keyboardType) return;
        _keyboardType = value;
        dispatchEvent(new Event("keyboardTypeChanged"));
    }

    //-------------------------------------
    //  returnKeyType
    //-------------------------------------

    private var _returnKeyType: ReturnKeyType;
    [Bindable(event="returnKeyTypeChanged")]
    public function get returnKeyType(): ReturnKeyType {
        return _returnKeyType || ReturnKeyType.Done;
    }
    public function set returnKeyType(value: ReturnKeyType): void {
        if (value == _returnKeyType) return;
        _returnKeyType = value;
        dispatchEvent(new Event("returnKeyTypeChanged"));
    }

    //-------------------------------------
    //  autoCapitalization
    //-------------------------------------

    private var _autoCapitalization: AutoCapitalization;
    [Bindable(event="autoCapitalizationChanged")]
    public function get autoCapitalization(): AutoCapitalization {
        return _autoCapitalization || AutoCapitalization.None;
    }
    public function set autoCapitalization(value: AutoCapitalization): void {
        if (value == _autoCapitalization) return;
        _autoCapitalization = value;
        dispatchEvent(new Event("autoCapitalizationChanged"));
    }

    //-------------------------------------
    //  autoCorrection
    //-------------------------------------

    private var _autoCorrection: AutoCorrection;
    [Bindable(event="autoCorrectionChanged")]
    public function get autoCorrection(): AutoCorrection {
        return _autoCorrection || AutoCorrection.Default;
    }
    public function set autoCorrection(value: AutoCorrection): void {
        if (value == _autoCorrection) return;
        _autoCorrection = value;
        dispatchEvent(new Event("autoCorrectionChanged"));
    }

    //-------------------------------------
    //  spellChecking
    //-------------------------------------

    private var _spellChecking: SpellChecking;
    [Bindable(event="spellCheckingChanged")]
    public function get spellChecking(): SpellChecking {
        return _spellChecking || SpellChecking.Default;
    }
    public function set spellChecking(value: SpellChecking): void {
        if (value == _spellChecking) return;
        _spellChecking = value;
        dispatchEvent(new Event("spellCheckingChanged"));
    }

    //-------------------------------------
    //  characterFilter
    //-------------------------------------

    private var _characterFilter: String;
    [Bindable(event="characterFilterChanged")]
    public function get characterFilter(): String {
        return _characterFilter;
    }
    public function set characterFilter(value: String): void {
        if (value == _characterFilter) return;
        _characterFilter = value;
        dispatchEvent(new Event("characterFilterChanged"));
    }

    //--------------------------------------------------------------------------
    //
    //  Description
    //
    //--------------------------------------------------------------------------

    override public function toString(): String {
        return "[NativeKeyboardTextParams(text=\""+text+"\", isSecureTextEntry=\""+isSecureTextEntry+"\", maxCharactersCount=\""+maxCharactersCount+"\", keyboardType=\""+keyboardType+"\", returnKeyType=\""+returnKeyType+"\", autoCapitalization=\""+autoCapitalization+"\", autoCorrection=\""+autoCorrection+"\", spellChecking=\""+spellChecking+"\")]";
    }
}
}