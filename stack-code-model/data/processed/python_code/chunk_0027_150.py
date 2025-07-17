/**
 * PutPortfolios.as
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

    public class PutPortfolios extends ArrayCollection
    {
        /**
         * Constructor - initializes the array collection based on a source array
         */
        
        public function PutPortfolios(source:Array = null)
        {
            super(source);
        }
        
        
        public function addPortfolioAt(item:Portfolio,index:int):void {
            addItemAt(item,index);
        }
            
        public function addPortfolio(item:Portfolio):void {
            addItem(item);
        } 

        public function getPortfolioAt(index:int):Portfolio {
            return getItemAt(index) as Portfolio;
        }
                
        public function getPortfolioIndex(item:Portfolio):int {
            return getItemIndex(item);
        }
                            
        public function setPortfolioAt(item:Portfolio,index:int):void {
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