package org.docksidestage.dbflute.flex.bs {

// *customization mark by jflute
import mx.collections.ArrayCollection;
import org.docksidestage.dbflute.flex.ex.*;

/**
 * The flex DTO of (商品ステータス)PRODUCT_STATUS as TABLE.
 * <pre>
 * [primary-key]
 *     PRODUCT_STATUS_CODE
 *
 * [column]
 *     PRODUCT_STATUS_CODE, PRODUCT_STATUS_NAME, DISPLAY_ORDER
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
 *     PRODUCT, SUMMARY_PRODUCT
 *
 * [foreign-property]
 *     
 *
 * [referrer-property]
 *     productList, summaryProductList
 * </pre>
 * @author DBFlute(AutoGenerator)
 */
public class BsProductStatus {

    // ===================================================================================
    //                                                                           Attribute
    //                                                                           =========
    private var _productStatusCode:String;

    private var _productStatusName:String;

    private var _displayOrder:int;


    // ===================================================================================
    //                                                                       Foreign Table
    //                                                                       =============
    // ===================================================================================
    //                                                                      Referrer Table
    //                                                                      ==============
    ProductDto;
    protected var _productList:ArrayCollection; /* of the entity 'ProductDto'. */

    public function get productList():ArrayCollection {
        if (_productList == null) { _productList = new ArrayCollection(); }
        return _productList;
    }

    public function set productList(productList:ArrayCollection):void {
        this._productList = productList;
    }

    SummaryProductDto;
    protected var _summaryProductList:ArrayCollection; /* of the entity 'SummaryProductDto'. */

    public function get summaryProductList():ArrayCollection {
        if (_summaryProductList == null) { _summaryProductList = new ArrayCollection(); }
        return _summaryProductList;
    }

    public function set summaryProductList(summaryProductList:ArrayCollection):void {
        this._summaryProductList = summaryProductList;
    }


    // ===================================================================================
    //                                                                            Accessor
    //                                                                            ========
    public function get productStatusCode():String {
        return _productStatusCode;
    }

    public function set productStatusCode(productStatusCode:String):void {
        this._productStatusCode = productStatusCode;
    }

    public function get productStatusName():String {
        return _productStatusName;
    }

    public function set productStatusName(productStatusName:String):void {
        this._productStatusName = productStatusName;
    }

    public function get displayOrder():int {
        return _displayOrder;
    }

    public function set displayOrder(displayOrder:int):void {
        this._displayOrder = displayOrder;
    }

}

}