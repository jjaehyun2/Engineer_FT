package org.docksidestage.dbflute.flex.bs {

// *customization mark by jflute
import mx.collections.ArrayCollection;
import org.docksidestage.dbflute.flex.ex.*;

/**
 * The flex DTO of (購入支払)PURCHASE_PAYMENT as TABLE.
 * <pre>
 * [primary-key]
 *     PURCHASE_PAYMENT_ID
 *
 * [column]
 *     PURCHASE_PAYMENT_ID, PURCHASE_ID, PAYMENT_AMOUNT, PAYMENT_DATETIME, PAYMENT_METHOD_CODE, REGISTER_DATETIME, REGISTER_USER, UPDATE_DATETIME, UPDATE_USER
 *
 * [sequence]
 *     
 *
 * [identity]
 *     PURCHASE_PAYMENT_ID
 *
 * [version-no]
 *     
 *
 * [foreign-table]
 *     PURCHASE
 *
 * [referrer-table]
 *     
 *
 * [foreign-property]
 *     purchase
 *
 * [referrer-property]
 *     
 * </pre>
 * @author DBFlute(AutoGenerator)
 */
public class BsPurchasePayment {

    // ===================================================================================
    //                                                                           Attribute
    //                                                                           =========
    private var _purchasePaymentId:Number;

    private var _purchaseId:Number;

    private var _paymentAmount:Number;

    private var _paymentDatetime:Date;

    private var _paymentMethodCode:String;

    private var _registerDatetime:Date;

    private var _registerUser:String;

    private var _updateDatetime:Date;

    private var _updateUser:String;


    // ===================================================================================
    //                                                                       Foreign Table
    //                                                                       =============
    private var _purchase:PurchaseDto;

    public function get purchase():PurchaseDto {
        return _purchase;
    }

    public function set purchase(purchase:PurchaseDto):void {
        this._purchase = purchase;
    }

    // ===================================================================================
    //                                                                      Referrer Table
    //                                                                      ==============

    // ===================================================================================
    //                                                                            Accessor
    //                                                                            ========
    public function get purchasePaymentId():Number {
        return _purchasePaymentId;
    }

    public function set purchasePaymentId(purchasePaymentId:Number):void {
        this._purchasePaymentId = purchasePaymentId;
    }

    public function get purchaseId():Number {
        return _purchaseId;
    }

    public function set purchaseId(purchaseId:Number):void {
        this._purchaseId = purchaseId;
    }

    public function get paymentAmount():Number {
        return _paymentAmount;
    }

    public function set paymentAmount(paymentAmount:Number):void {
        this._paymentAmount = paymentAmount;
    }

    public function get paymentDatetime():Date {
        return _paymentDatetime;
    }

    public function set paymentDatetime(paymentDatetime:Date):void {
        this._paymentDatetime = paymentDatetime;
    }

    public function get paymentMethodCode():String {
        return _paymentMethodCode;
    }

    public function set paymentMethodCode(paymentMethodCode:String):void {
        this._paymentMethodCode = paymentMethodCode;
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