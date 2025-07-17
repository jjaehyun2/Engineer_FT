package org.docksidestage.dbflute.flex.bs {

// *customization mark by jflute
import mx.collections.ArrayCollection;
import org.docksidestage.dbflute.flex.ex.*;

/**
 * The flex DTO of WHITE_BASE_ONE02_LAND as TABLE.
 * <pre>
 * [primary-key]
 *     LAND_ID
 *
 * [column]
 *     LAND_ID, LAND_NAME
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
public class BsWhiteBaseOne02Land {

    // ===================================================================================
    //                                                                           Attribute
    //                                                                           =========
    private var _landId:int;

    private var _landName:String;


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
    public function get landId():int {
        return _landId;
    }

    public function set landId(landId:int):void {
        this._landId = landId;
    }

    public function get landName():String {
        return _landName;
    }

    public function set landName(landName:String):void {
        this._landName = landName;
    }

}

}