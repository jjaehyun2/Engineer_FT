package org.docksidestage.dbflute.flex.bs {

// *customization mark by jflute
import mx.collections.ArrayCollection;
import org.docksidestage.dbflute.flex.ex.*;

/**
 * The flex DTO of (会員サービス)MEMBER_SERVICE as TABLE.
 * <pre>
 * [primary-key]
 *     MEMBER_SERVICE_ID
 *
 * [column]
 *     MEMBER_SERVICE_ID, MEMBER_ID, SERVICE_POINT_COUNT, SERVICE_RANK_CODE, REGISTER_DATETIME, REGISTER_USER, UPDATE_DATETIME, UPDATE_USER, VERSION_NO
 *
 * [sequence]
 *     
 *
 * [identity]
 *     MEMBER_SERVICE_ID
 *
 * [version-no]
 *     VERSION_NO
 *
 * [foreign-table]
 *     MEMBER, SERVICE_RANK
 *
 * [referrer-table]
 *     
 *
 * [foreign-property]
 *     member, serviceRank
 *
 * [referrer-property]
 *     
 * </pre>
 * @author DBFlute(AutoGenerator)
 */
public class BsMemberService {

    // ===================================================================================
    //                                                                           Attribute
    //                                                                           =========
    private var _memberServiceId:int;

    private var _memberId:int;

    private var _servicePointCount:int;

    private var _serviceRankCode:String;

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

    private var _serviceRank:ServiceRankDto;

    public function get serviceRank():ServiceRankDto {
        return _serviceRank;
    }

    public function set serviceRank(serviceRank:ServiceRankDto):void {
        this._serviceRank = serviceRank;
    }

    // ===================================================================================
    //                                                                      Referrer Table
    //                                                                      ==============

    // ===================================================================================
    //                                                                            Accessor
    //                                                                            ========
    public function get memberServiceId():int {
        return _memberServiceId;
    }

    public function set memberServiceId(memberServiceId:int):void {
        this._memberServiceId = memberServiceId;
    }

    public function get memberId():int {
        return _memberId;
    }

    public function set memberId(memberId:int):void {
        this._memberId = memberId;
    }

    public function get servicePointCount():int {
        return _servicePointCount;
    }

    public function set servicePointCount(servicePointCount:int):void {
        this._servicePointCount = servicePointCount;
    }

    public function get serviceRankCode():String {
        return _serviceRankCode;
    }

    public function set serviceRankCode(serviceRankCode:String):void {
        this._serviceRankCode = serviceRankCode;
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