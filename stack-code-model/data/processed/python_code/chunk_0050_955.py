package org.docksidestage.dbflute.flex.bs {

// *customization mark by jflute
import mx.collections.ArrayCollection;
import org.docksidestage.dbflute.flex.ex.*;

/**
 * The flex DTO of SUMMARY_WITHDRAWAL as VIEW.
 * <pre>
 * [primary-key]
 *     
 *
 * [column]
 *     MEMBER_ID, MEMBER_NAME, WITHDRAWAL_REASON_CODE, WITHDRAWAL_REASON_TEXT, WITHDRAWAL_REASON_INPUT_TEXT, WITHDRAWAL_DATETIME, MEMBER_STATUS_CODE, MEMBER_STATUS_NAME, MAX_PURCHASE_PRICE
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
 *     
 *
 * [referrer-table]
 *     
 *
 * [foreign-property]
 *     
 *
 * [referrer-property]
 *     
 * </pre>
 * @author DBFlute(AutoGenerator)
 */
public class BsSummaryWithdrawal {

    // ===================================================================================
    //                                                                           Attribute
    //                                                                           =========
    private var _memberId:int;

    private var _memberName:String;

    private var _withdrawalReasonCode:String;

    private var _withdrawalReasonText:String;

    private var _withdrawalReasonInputText:String;

    private var _withdrawalDatetime:Date;

    private var _memberStatusCode:String;

    private var _memberStatusName:String;

    private var _maxPurchasePrice:int;


    // ===================================================================================
    //                                                                       Foreign Table
    //                                                                       =============
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

    public function get memberName():String {
        return _memberName;
    }

    public function set memberName(memberName:String):void {
        this._memberName = memberName;
    }

    public function get withdrawalReasonCode():String {
        return _withdrawalReasonCode;
    }

    public function set withdrawalReasonCode(withdrawalReasonCode:String):void {
        this._withdrawalReasonCode = withdrawalReasonCode;
    }

    public function get withdrawalReasonText():String {
        return _withdrawalReasonText;
    }

    public function set withdrawalReasonText(withdrawalReasonText:String):void {
        this._withdrawalReasonText = withdrawalReasonText;
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

    public function get memberStatusCode():String {
        return _memberStatusCode;
    }

    public function set memberStatusCode(memberStatusCode:String):void {
        this._memberStatusCode = memberStatusCode;
    }

    public function get memberStatusName():String {
        return _memberStatusName;
    }

    public function set memberStatusName(memberStatusName:String):void {
        this._memberStatusName = memberStatusName;
    }

    public function get maxPurchasePrice():int {
        return _maxPurchasePrice;
    }

    public function set maxPurchasePrice(maxPurchasePrice:int):void {
        this._maxPurchasePrice = maxPurchasePrice;
    }

}

}