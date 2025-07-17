package org.docksidestage.dbflute.flex.bs {

// *customization mark by jflute
import mx.collections.ArrayCollection;
import org.docksidestage.dbflute.flex.ex.*;

/**
 * The flex DTO of WHITE_BASE_ONE06_AMBA as TABLE.
 * <pre>
 * [primary-key]
 *     AMBA_ID
 *
 * [column]
 *     AMBA_ID, AMBA_NAME
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
 *     WHITE_BASE
 *
 * [foreign-property]
 *     
 *
 * [referrer-property]
 *     whiteBaseList
 * </pre>
 * @author DBFlute(AutoGenerator)
 */
public class BsWhiteBaseOne06Amba {

    // ===================================================================================
    //                                                                           Attribute
    //                                                                           =========
    private var _ambaId:int;

    private var _ambaName:String;


    // ===================================================================================
    //                                                                       Foreign Table
    //                                                                       =============
    // ===================================================================================
    //                                                                      Referrer Table
    //                                                                      ==============
    WhiteBaseDto;
    protected var _whiteBaseList:ArrayCollection; /* of the entity 'WhiteBaseDto'. */

    public function get whiteBaseList():ArrayCollection {
        if (_whiteBaseList == null) { _whiteBaseList = new ArrayCollection(); }
        return _whiteBaseList;
    }

    public function set whiteBaseList(whiteBaseList:ArrayCollection):void {
        this._whiteBaseList = whiteBaseList;
    }


    // ===================================================================================
    //                                                                            Accessor
    //                                                                            ========
    public function get ambaId():int {
        return _ambaId;
    }

    public function set ambaId(ambaId:int):void {
        this._ambaId = ambaId;
    }

    public function get ambaName():String {
        return _ambaName;
    }

    public function set ambaName(ambaName:String):void {
        this._ambaName = ambaName;
    }

}

}