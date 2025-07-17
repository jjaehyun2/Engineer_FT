package org.docksidestage.dbflute.flex.bs {

// *customization mark by jflute
import mx.collections.ArrayCollection;
import org.docksidestage.dbflute.flex.ex.*;

/**
 * The flex DTO of WHITE_BASE_ONE01_SEA_HANGAR as TABLE.
 * <pre>
 * [primary-key]
 *     HANGAR_ID
 *
 * [column]
 *     HANGAR_ID, HANGAR_NAME, SEA_ID
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
 *     WHITE_BASE_ONE01_SEA
 *
 * [referrer-table]
 *     
 *
 * [foreign-property]
 *     whiteBaseOne01Sea
 *
 * [referrer-property]
 *     
 * </pre>
 * @author DBFlute(AutoGenerator)
 */
public class BsWhiteBaseOne01SeaHangar {

    // ===================================================================================
    //                                                                           Attribute
    //                                                                           =========
    private var _hangarId:int;

    private var _hangarName:String;

    private var _seaId:int;


    // ===================================================================================
    //                                                                       Foreign Table
    //                                                                       =============
    private var _whiteBaseOne01Sea:WhiteBaseOne01SeaDto;

    public function get whiteBaseOne01Sea():WhiteBaseOne01SeaDto {
        return _whiteBaseOne01Sea;
    }

    public function set whiteBaseOne01Sea(whiteBaseOne01Sea:WhiteBaseOne01SeaDto):void {
        this._whiteBaseOne01Sea = whiteBaseOne01Sea;
    }

    // ===================================================================================
    //                                                                      Referrer Table
    //                                                                      ==============

    // ===================================================================================
    //                                                                            Accessor
    //                                                                            ========
    public function get hangarId():int {
        return _hangarId;
    }

    public function set hangarId(hangarId:int):void {
        this._hangarId = hangarId;
    }

    public function get hangarName():String {
        return _hangarName;
    }

    public function set hangarName(hangarName:String):void {
        this._hangarName = hangarName;
    }

    public function get seaId():int {
        return _seaId;
    }

    public function set seaId(seaId:int):void {
        this._seaId = seaId;
    }

}

}