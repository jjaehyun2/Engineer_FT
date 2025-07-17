package org.docksidestage.dbflute.flex.bs {

// *customization mark by jflute
import mx.collections.ArrayCollection;
import org.docksidestage.dbflute.flex.ex.*;

/**
 * The flex DTO of (会員セキュリティ情報)MEMBER_SECURITY as TABLE.
 * <pre>
 * [primary-key]
 *     MEMBER_ID
 *
 * [column]
 *     MEMBER_ID, LOGIN_PASSWORD, REMINDER_QUESTION, REMINDER_ANSWER, REMINDER_USE_COUNT, REGISTER_DATETIME, REGISTER_USER, UPDATE_DATETIME, UPDATE_USER, VERSION_NO
 *
 * [sequence]
 *     
 *
 * [identity]
 *     
 *
 * [version-no]
 *     VERSION_NO
 *
 * [foreign-table]
 *     MEMBER
 *
 * [referrer-table]
 *     
 *
 * [foreign-property]
 *     member
 *
 * [referrer-property]
 *     
 * </pre>
 * @author DBFlute(AutoGenerator)
 */
public class BsMemberSecurity {

    // ===================================================================================
    //                                                                           Attribute
    //                                                                           =========
    private var _memberId:int;

    private var _loginPassword:String;

    private var _reminderQuestion:String;

    private var _reminderAnswer:String;

    private var _reminderUseCount:int;

    private var _registerDatetime:Date;

    private var _registerUser:String;

    private var _updateDatetime:Date;

    private var _updateUser:String;

    private var _versionNo:Number;


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

    public function get loginPassword():String {
        return _loginPassword;
    }

    public function set loginPassword(loginPassword:String):void {
        this._loginPassword = loginPassword;
    }

    public function get reminderQuestion():String {
        return _reminderQuestion;
    }

    public function set reminderQuestion(reminderQuestion:String):void {
        this._reminderQuestion = reminderQuestion;
    }

    public function get reminderAnswer():String {
        return _reminderAnswer;
    }

    public function set reminderAnswer(reminderAnswer:String):void {
        this._reminderAnswer = reminderAnswer;
    }

    public function get reminderUseCount():int {
        return _reminderUseCount;
    }

    public function set reminderUseCount(reminderUseCount:int):void {
        this._reminderUseCount = reminderUseCount;
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

    public function get versionNo():Number {
        return _versionNo;
    }

    public function set versionNo(versionNo:Number):void {
        this._versionNo = versionNo;
    }

}

}