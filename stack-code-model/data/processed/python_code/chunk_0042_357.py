package org.docksidestage.dbflute.flex.bs {

// *customization mark by jflute
import mx.collections.ArrayCollection;
import org.docksidestage.dbflute.flex.ex.*;

/**
 * The flex DTO of WHITE_ON_PARADE_NULLABLE_TO_MANY as TABLE.
 * <pre>
 * [primary-key]
 *     MANY_ID
 *
 * [column]
 *     MANY_ID, MANY_NAME
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
 *     WHITE_ON_PARADE_REF
 *
 * [foreign-property]
 *     
 *
 * [referrer-property]
 *     whiteOnParadeRefList
 * </pre>
 * @author DBFlute(AutoGenerator)
 */
public class BsWhiteOnParadeNullableToMany {

    // ===================================================================================
    //                                                                           Attribute
    //                                                                           =========
    private var _manyId:Number;

    private var _manyName:String;


    // ===================================================================================
    //                                                                       Foreign Table
    //                                                                       =============
    // ===================================================================================
    //                                                                      Referrer Table
    //                                                                      ==============
    WhiteOnParadeRefDto;
    protected var _whiteOnParadeRefList:ArrayCollection; /* of the entity 'WhiteOnParadeRefDto'. */

    public function get whiteOnParadeRefList():ArrayCollection {
        if (_whiteOnParadeRefList == null) { _whiteOnParadeRefList = new ArrayCollection(); }
        return _whiteOnParadeRefList;
    }

    public function set whiteOnParadeRefList(whiteOnParadeRefList:ArrayCollection):void {
        this._whiteOnParadeRefList = whiteOnParadeRefList;
    }


    // ===================================================================================
    //                                                                            Accessor
    //                                                                            ========
    public function get manyId():Number {
        return _manyId;
    }

    public function set manyId(manyId:Number):void {
        this._manyId = manyId;
    }

    public function get manyName():String {
        return _manyName;
    }

    public function set manyName(manyName:String):void {
        this._manyName = manyName;
    }

}

}