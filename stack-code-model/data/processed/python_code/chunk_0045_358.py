/**
 * PutPortfolioGroups.as
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

    public class PutPortfolioGroups extends ArrayCollection
    {
        /**
         * Constructor - initializes the array collection based on a source array
         */
        
        public function PutPortfolioGroups(source:Array = null)
        {
            super(source);
        }
        
        
        public function addPortfolioGroupAt(item:PortfolioGroup,index:int):void {
            addItemAt(item,index);
        }
            
        public function addPortfolioGroup(item:PortfolioGroup):void {
            addItem(item);
        } 

        public function getPortfolioGroupAt(index:int):PortfolioGroup {
            return getItemAt(index) as PortfolioGroup;
        }
                
        public function getPortfolioGroupIndex(item:PortfolioGroup):int {
            return getItemIndex(item);
        }
                            
        public function setPortfolioGroupAt(item:PortfolioGroup,index:int):void {
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