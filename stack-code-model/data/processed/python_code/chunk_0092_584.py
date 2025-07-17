/**
 * GetAllAdKeywordsResponse.as
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

    public class GetAllAdKeywordsResponse extends ArrayCollection
    {
        /**
         * Constructor - initializes the array collection based on a source array
         */
        
        public function GetAllAdKeywordsResponse(source:Array = null)
        {
            super(source);
        }
        
        
        public function addAdKeyWordAt(item:AdKeyWord,index:int):void {
            addItemAt(item,index);
        }
            
        public function addAdKeyWord(item:AdKeyWord):void {
            addItem(item);
        } 

        public function getAdKeyWordAt(index:int):AdKeyWord {
            return getItemAt(index) as AdKeyWord;
        }
                
        public function getAdKeyWordIndex(item:AdKeyWord):int {
            return getItemIndex(item);
        }
                            
        public function setAdKeyWordAt(item:AdKeyWord,index:int):void {
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