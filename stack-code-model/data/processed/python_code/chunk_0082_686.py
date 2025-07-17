package org.docksidestage.dbflute.flex.bs.customize {

// *customization mark by jflute
import mx.collections.ArrayCollection;
import org.docksidestage.dbflute.flex.ex.customize.*;

/**
 * The flex DTO of VendorCheckDecimalSum.
 * <pre>
 * [primary-key]
 *     
 *
 * [column]
 *     DECIMAL_DIGIT_SUM
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
public class BsVendorCheckDecimalSum {

    // ===================================================================================
    //                                                                           Attribute
    //                                                                           =========
    private var _decimalDigitSum:Number;


    // ===================================================================================
    //                                                                       Foreign Table
    //                                                                       =============
    // ===================================================================================
    //                                                                      Referrer Table
    //                                                                      ==============

    // ===================================================================================
    //                                                                            Accessor
    //                                                                            ========
    public function get decimalDigitSum():Number {
        return _decimalDigitSum;
    }

    public function set decimalDigitSum(decimalDigitSum:Number):void {
        this._decimalDigitSum = decimalDigitSum;
    }

}

}