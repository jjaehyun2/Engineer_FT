package org.docksidestage.dbflute.flex.bs {

// *customization mark by jflute
import mx.collections.ArrayCollection;
import org.docksidestage.dbflute.flex.ex.*;

/**
 * The flex DTO of (会員ログイン)MEMBER_LOGIN as TABLE.
 * <pre>
 * [primary-key]
 *     MEMBER_LOGIN_ID
 *
 * [column]
 *     MEMBER_LOGIN_ID, MEMBER_ID, LOGIN_DATETIME, MOBILE_LOGIN_FLG, LOGIN_MEMBER_STATUS_CODE
 *
 * [sequence]
 *     MAIHAMADB.PUBLIC.SEQ_MEMBER_LOGIN
 *
 * [identity]
 *     MEMBER_LOGIN_ID
 *
 * [version-no]
 *     
 *
 * [foreign-table]
 *     MEMBER_STATUS, MEMBER
 *
 * [referrer-table]
 *     
 *
 * [foreign-property]
 *     memberStatus, member
 *
 * [referrer-property]
 *     
 * </pre>
 * @author DBFlute(AutoGenerator)
 */
public class BsMemberLogin {

    // ===================================================================================
    //                                                                           Attribute
    //                                                                           =========
    private var _memberLoginId:Number;

    private var _memberId:int;

    private var _loginDatetime:Date;

    private var _mobileLoginFlg:int;

    private var _loginMemberStatusCode:String;


    // ===================================================================================
    //                                                                       Foreign Table
    //                                                                       =============
    private var _memberStatus:MemberStatusDto;

    public function get memberStatus():MemberStatusDto {
        return _memberStatus;
    }

    public function set memberStatus(memberStatus:MemberStatusDto):void {
        this._memberStatus = memberStatus;
    }

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
    public function get memberLoginId():Number {
        return _memberLoginId;
    }

    public function set memberLoginId(memberLoginId:Number):void {
        this._memberLoginId = memberLoginId;
    }

    public function get memberId():int {
        return _memberId;
    }

    public function set memberId(memberId:int):void {
        this._memberId = memberId;
    }

    public function get loginDatetime():Date {
        return _loginDatetime;
    }

    public function set loginDatetime(loginDatetime:Date):void {
        this._loginDatetime = loginDatetime;
    }

    public function get mobileLoginFlg():int {
        return _mobileLoginFlg;
    }

    public function set mobileLoginFlg(mobileLoginFlg:int):void {
        this._mobileLoginFlg = mobileLoginFlg;
    }

    public function get loginMemberStatusCode():String {
        return _loginMemberStatusCode;
    }

    public function set loginMemberStatusCode(loginMemberStatusCode:String):void {
        this._loginMemberStatusCode = loginMemberStatusCode;
    }

}

}