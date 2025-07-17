package org.docksidestage.dbflute.flex.bs {

// *customization mark by jflute
import mx.collections.ArrayCollection;
import org.docksidestage.dbflute.flex.ex.*;

/**
 * The flex DTO of WHITE_BASE_ONE04_BONVO_PARKSIDE as TABLE.
 * <pre>
 * [primary-key]
 *     PARKSIDE_ID
 *
 * [column]
 *     PARKSIDE_ID, PARKSIDE_NAME
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
 *     WHITE_BASE_ONE04_BONVO
 *
 * [foreign-property]
 *     
 *
 * [referrer-property]
 *     whiteBaseOne04BonvoList
 * </pre>
 * @author DBFlute(AutoGenerator)
 */
public class BsWhiteBaseOne04BonvoParkside {

    // ===================================================================================
    //                                                                           Attribute
    //                                                                           =========
    private var _parksideId:int;

    private var _parksideName:String;


    // ===================================================================================
    //                                                                       Foreign Table
    //                                                                       =============
    // ===================================================================================
    //                                                                      Referrer Table
    //                                                                      ==============
    WhiteBaseOne04BonvoDto;
    protected var _whiteBaseOne04BonvoList:ArrayCollection; /* of the entity 'WhiteBaseOne04BonvoDto'. */

    public function get whiteBaseOne04BonvoList():ArrayCollection {
        if (_whiteBaseOne04BonvoList == null) { _whiteBaseOne04BonvoList = new ArrayCollection(); }
        return _whiteBaseOne04BonvoList;
    }

    public function set whiteBaseOne04BonvoList(whiteBaseOne04BonvoList:ArrayCollection):void {
        this._whiteBaseOne04BonvoList = whiteBaseOne04BonvoList;
    }


    // ===================================================================================
    //                                                                            Accessor
    //                                                                            ========
    public function get parksideId():int {
        return _parksideId;
    }

    public function set parksideId(parksideId:int):void {
        this._parksideId = parksideId;
    }

    public function get parksideName():String {
        return _parksideName;
    }

    public function set parksideName(parksideName:String):void {
        this._parksideName = parksideName;
    }

}

}