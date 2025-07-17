/**
 * AlsoToConsiderKeywordList_type0.as
 * This file was auto-generated from WSDL by the Apache Axis2 generator modified by Adobe
 * Any change made to this file will be overwritten when the code is re-generated.
 */
package com.macys.marketing.sema{
    import mx.utils.ObjectProxy;
    import mx.collections.ArrayCollection;
    import mx.collections.IList;
    import mx.collections.ICollectionView;
    import mx.rpc.soap.types.*;
    /**
     * Typed array collection
     */

    public class AlsoToConsiderKeywordList_type0 extends ArrayCollection
    {
        /**
         * Constructor - initializes the array collection based on a source array
         */
        
        public function AlsoToConsiderKeywordList_type0(source:Array = null)
        {
            super(source);
        }
        
        
        public function addKeywordVariationAt(item:KeywordVariation,index:int):void {
            addItemAt(item,index);
        }
            
        public function addKeywordVariation(item:KeywordVariation):void {
            addItem(item);
        } 

        public function getKeywordVariationAt(index:int):KeywordVariation {
            return getItemAt(index) as KeywordVariation;
        }
                
        public function getKeywordVariationIndex(item:KeywordVariation):int {
            return getItemIndex(item);
        }
                            
        public function setKeywordVariationAt(item:KeywordVariation,index:int):void {
            setItemAt(item,index);
        }

        public function asIList():IList {
            return this as IList;
        }
        
        public function asICollectionView():ICollectionView {
            return this as ICollectionView;
        }
    }
}