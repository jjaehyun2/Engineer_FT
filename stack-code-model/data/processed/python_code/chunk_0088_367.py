package org.docksidestage.dbflute.flex.bs {

// *customization mark by jflute
import mx.collections.ArrayCollection;
import org.docksidestage.dbflute.flex.ex.*;

/**
 * The flex DTO of (会員住所情報)MEMBER_ADDRESS as TABLE.
 * <pre>
 * [primary-key]
 *     MEMBER_ADDRESS_ID
 *
 * [column]
 *     MEMBER_ADDRESS_ID, MEMBER_ID, VALID_BEGIN_DATE, VALID_END_DATE, ADDRESS, REGION_ID, REGISTER_DATETIME, REGISTER_USER, UPDATE_DATETIME, UPDATE_USER, VERSION_NO
 *
 * [sequence]
 *     
 *
 * [identity]
 *     MEMBER_ADDRESS_ID
 *
 * [version-no]
 *     VERSION_NO
 *
 * [foreign-table]
 *     MEMBER, REGION
 *
 * [referrer-table]
 *     
 *
 * [foreign-property]
 *     member, region
 *
 * [referrer-property]
 *     
 * </pre>
 * @author DBFlute(AutoGenerator)
 */
public class BsMemberAddress {

    // ===================================================================================
    //                                                                           Attribute
    //                                                                           =========
    private var _memberAddressId:int;

    private var _memberId:int;

    private var _validBeginDate:Date;

    private var _validEndDate:Date;

    private var _address:String;

    private var _regionId:int;

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

    private var _region:RegionDto;

    public function get region():RegionDto {
        return _region;
    }

    public function set region(region:RegionDto):void {
        this._region = region;
    }

    // ===================================================================================
    //                                                                      Referrer Table
    //                                                                      ==============

    // ===================================================================================
    //                                                                            Accessor
    //                                                                            ========
    public function get memberAddressId():int {
        return _memberAddressId;
    }

    public function set memberAddressId(memberAddressId:int):void {
        this._memberAddressId = memberAddressId;
    }

    public function get memberId():int {
        return _memberId;
    }

    public function set memberId(memberId:int):void {
        this._memberId = memberId;
    }

    public function get validBeginDate():Date {
        return _validBeginDate;
    }

    public function set validBeginDate(validBeginDate:Date):void {
        this._validBeginDate = validBeginDate;
    }

    public function get validEndDate():Date {
        return _validEndDate;
    }

    public function set validEndDate(validEndDate:Date):void {
        this._validEndDate = validEndDate;
    }

    public function get address():String {
        return _address;
    }

    public function set address(address:String):void {
        this._address = address;
    }

    public function get regionId():int {
        return _regionId;
    }

    public function set regionId(regionId:int):void {
        this._regionId = regionId;
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