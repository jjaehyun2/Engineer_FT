package org.docksidestage.dbflute.flex.bs {

// *customization mark by jflute
import mx.collections.ArrayCollection;
import org.docksidestage.dbflute.flex.ex.*;

/**
 * The flex DTO of (会員退会情報)MEMBER_WITHDRAWAL as TABLE.
 * <pre>
 * [primary-key]
 *     MEMBER_ID
 *
 * [column]
 *     MEMBER_ID, WITHDRAWAL_REASON_CODE, WITHDRAWAL_REASON_INPUT_TEXT, WITHDRAWAL_DATETIME, REGISTER_DATETIME, REGISTER_USER, UPDATE_DATETIME, UPDATE_USER
 *
 * [sequence]
 *     
 *
 * [identity]
 *     
 *
 * [version-no]
 *     
 *
 * [foreign-table]
 *     MEMBER, WITHDRAWAL_REASON
 *
 * [referrer-table]
 *     
 *
 * [foreign-property]
 *     member, withdrawalReason
 *
 * [referrer-property]
 *     
 * </pre>
 * @author DBFlute(AutoGenerator)
 */
public class BsMemberWithdrawal {

    // ===================================================================================
    //                                                                           Attribute
    //                                                                           =========
    private var _memberId:int;

    private var _withdrawalReasonCode:String;

    private var _withdrawalReasonInputText:String;

    private var _withdrawalDatetime:Date;

    private var _registerDatetime:Date;

    private var _registerUser:String;

    private var _updateDatetime:Date;

    private var _updateUser:String;


    // ===================================================================================
    //                                                                       Foreign Table
    //                                                                       =============
    private var _member:MemberDto;

    public function get member():MemberDto {
        return _member;
    }

    public function set member(member:MemberDto):void {
        this._member = member;
    }

    private var _withdrawalReason:WithdrawalReasonDto;

    public function get withdrawalReason():WithdrawalReasonDto {
        return _withdrawalReason;
    }

    public function set withdrawalReason(withdrawalReason:WithdrawalReasonDto):void {
        this._withdrawalReason = withdrawalReason;
    }

    // ===================================================================================
    //                                                                      Referrer Table
    //                                                                      ==============

    // ===================================================================================
    //                                                                            Accessor
    //                                                                            ========
    public function get memberId():int {
        return _memberId;
    }

    public function set memberId(memberId:int):void {
        this._memberId = memberId;
    }

    public function get withdrawalReasonCode():String {
        return _withdrawalReasonCode;
    }

    public function set withdrawalReasonCode(withdrawalReasonCode:String):void {
        this._withdrawalReasonCode = withdrawalReasonCode;
    }

    public function get withdrawalReasonInputText():String {
        return _withdrawalReasonInputText;
    }

    public function set withdrawalReasonInputText(withdrawalReasonInputText:String):void {
        this._withdrawalReasonInputText = withdrawalReasonInputText;
    }

    public function get withdrawalDatetime():Date {
        return _withdrawalDatetime;
    }

    public function set withdrawalDatetime(withdrawalDatetime:Date):void {
        this._withdrawalDatetime = withdrawalDatetime;
    }

    public function get registerDatetime():Date {
        return _registerDatetime;
    }

    public function set registerDatetime(registerDatetime:Date):void {
        this._registerDatetime = registerDatetime;
    }

    public function get registerUser():String {
        return _registerUser;
    }

    public function set registerUser(registerUser:String):void {
        this._registerUser = registerUser;
    }

    public function get updateDatetime():Date {
        return _updateDatetime;
    }

    public function set updateDatetime(updateDatetime:Date):void {
        this._updateDatetime = updateDatetime;
    }

    public function get updateUser():String {
        return _updateUser;
    }

    public function set updateUser(updateUser:String):void {
        this._updateUser = updateUser;
    }

}

}